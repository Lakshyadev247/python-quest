import os
import tempfile
import pytest
from app import create_app
from app.config import Config
from app.database import engine, Base, SessionLocal
from app.seed_curriculum import seed_curriculum

@pytest.fixture(scope="module")
def client():
    app = create_app()

    db = SessionLocal()
    from app.models.user import User
    test_user = db.query(User).filter(User.username == "quest_hero").first()
    if test_user:
        db.delete(test_user)
        db.commit()
    db.close()

    with app.test_client() as c:
        yield c

def test_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "healthy"

def test_auth_workflow(client):
    reg_res = client.post("/api/auth/register", json={
        "username": "quest_hero",
        "email": "hero@quest.dev",
        "password": "Password123!"
    })
    assert reg_res.status_code == 201
    reg_data = reg_res.get_json()
    assert "token" in reg_data
    assert reg_data["user"]["username"] == "quest_hero"
    assert reg_data["user"]["is_admin"] is False
    token = reg_data["token"]

    me_res = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me_res.status_code == 200
    me_data = me_res.get_json()
    assert me_data["user"]["username"] == "quest_hero"
    assert me_data["user"]["current_rank"] == "Beginner"

def test_curriculum_and_locking(client):
    login_res = client.post("/api/auth/login", json={
        "username": "quest_hero",
        "password": "Password123!"
    })
    token = login_res.get_json()["token"]

    worlds_res = client.get("/api/worlds", headers={"Authorization": f"Bearer {token}"})
    assert worlds_res.status_code == 200
    worlds = worlds_res.get_json()["worlds"]
    assert len(worlds) == 12
    assert worlds[0]["title"] == "Python Beginner"
    assert worlds[0]["is_unlocked"] is True

    # Level 1 should be unlocked
    lvl1_res = client.get("/api/levels/1", headers={"Authorization": f"Bearer {token}"})
    assert lvl1_res.status_code == 200
    lvl1 = lvl1_res.get_json()["level"]
    assert lvl1["is_unlocked"] is True

    # Level 2 must be locked
    lvl2_res = client.get("/api/levels/2", headers={"Authorization": f"Bearer {token}"})
    assert lvl2_res.status_code == 200
    lvl2 = lvl2_res.get_json()["level"]
    assert lvl2["is_unlocked"] is False, "Level 2 must be locked until Level 1 requirements are satisfied!"

def test_code_execution_security(client):
    login_res = client.post("/api/auth/login", json={
        "username": "quest_hero",
        "password": "Password123!"
    })
    headers = {"Authorization": f"Bearer {login_res.get_json()['token']}"}

    anonymous_res = client.post("/api/code/execute", json={"code": "print(1)"})
    assert anonymous_res.status_code == 200
    assert anonymous_res.get_json()["stdout"].strip() == "1"

    safe_res = client.post("/api/code/execute", json={
        "code": "print('Python' + ' ' + 'Quest')"
    }, headers=headers)
    assert safe_res.status_code == 200
    assert safe_res.get_json()["stdout"].strip() == "Python Quest"
    assert safe_res.get_json()["success"] is True

    unsafe_res = client.post("/api/code/execute", json={
        "code": "import subprocess\nsubprocess.run(['dir'])"
    }, headers=headers)
    assert unsafe_res.status_code == 200
    assert "Security restriction" in unsafe_res.get_json()["stderr"]
    assert unsafe_res.get_json()["success"] is False

    popen_res = client.post("/api/code/execute", json={
        "code": "import os\nprint(os.popen('whoami').read())"
    }, headers=headers)
    assert popen_res.status_code == 200
    assert popen_res.get_json()["success"] is False
    assert "Security restriction" in popen_res.get_json()["stderr"]

    timeout_res = client.post("/api/code/execute", json={
        "code": "while True:\n    pass"
    }, headers=headers)
    assert timeout_res.status_code == 200
    assert timeout_res.get_json()["timed_out"] is True

def test_level_progression_and_completion(client):
    login_res = client.post("/api/auth/login", json={
        "username": "quest_hero",
        "password": "Password123!"
    })
    token = login_res.get_json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 1. Complete Lesson for Level 1
    lesson_res = client.post("/api/progress/lesson", json={"level_id": 1}, headers=headers)
    assert lesson_res.status_code == 200
    assert lesson_res.get_json()["xp_awarded"] == 50

    # 2. Submit coding challenge for Level 1
    lvl1_data = client.get("/api/levels/1", headers=headers).get_json()["level"]
    challenges = lvl1_data["challenges"]
    normal_ch = next(c for c in challenges if not c["is_boss"])
    boss_ch = next(c for c in challenges if c["is_boss"])

    sub1_res = client.post("/api/code/submit", json={
        "challenge_id": normal_ch["id"],
        "code": "print('System Boot')\nprint('Ready for Quest')"
    }, headers=headers)
    assert sub1_res.status_code == 200
    assert sub1_res.get_json()["passed"] is True

    # 3. Pass MCQ quiz for Level 1 with 100%
    quiz_data = client.get("/api/quizzes/1").get_json()
    questions = quiz_data["questions"]
    answers = {}
    db = SessionLocal()
    from app.models.curriculum import QuizOption
    for q in questions:
        correct_opt = db.query(QuizOption).filter(QuizOption.question_id == q["id"], QuizOption.is_correct == True).first()
        answers[str(q["id"])] = correct_opt.id
    db.close()

    quiz_submit_res = client.post("/api/quizzes/1/submit", json={"answers": answers}, headers=headers)
    assert quiz_submit_res.status_code == 200
    assert quiz_submit_res.get_json()["score_percent"] == 100.0

    # Level 2 should STILL be locked because Boss Challenge is not yet completed!
    lvl2_check1 = client.get("/api/levels/2", headers=headers).get_json()["level"]
    assert lvl2_check1["is_unlocked"] is False

    # 4. Pass Boss Challenge for Level 1
    boss_sub_res = client.post("/api/code/submit", json={
        "challenge_id": boss_ch["id"],
        "code": "print('Countdown: 3')\nprint('Countdown: 2')\nprint('Countdown: 1')\nprint('Launch Python Quest!')"
    }, headers=headers)
    assert boss_sub_res.status_code == 200
    assert boss_sub_res.get_json()["passed"] is True

    # NOW all 4 criteria are met: Level 1 completed, Level 2 must unlock!
    lvl2_check2 = client.get("/api/levels/2", headers=headers).get_json()["level"]
    assert lvl2_check2["is_unlocked"] is True, "Level 2 must be unlocked once Level 1 is fully completed!"

def test_achievements_and_profile(client):
    login_res = client.post("/api/auth/login", json={
        "username": "quest_hero",
        "password": "Password123!"
    })
    token = login_res.get_json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    ach_res = client.get("/api/achievements", headers=headers)
    assert ach_res.status_code == 200
    achs = ach_res.get_json()["achievements"]
    unlocked_codes = [a["code"] for a in achs if a["unlocked"]]
    assert "FIRST_PROGRAM" in unlocked_codes
    assert "FIRST_CHALLENGE" in unlocked_codes
    assert "PERFECT_EXAM" in unlocked_codes

    prof_res = client.get("/api/profile", headers=headers)
    assert prof_res.status_code == 200
    prof = prof_res.get_json()
    assert prof["user"]["total_xp"] > 0
    assert prof["stats"]["completed_levels"] >= 1
