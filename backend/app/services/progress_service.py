from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.curriculum import Level, CodingChallenge, QuizQuestion, World
from app.models.progress import UserProgress, ChallengeSubmission, QuizAttempt
from app.services.gamification_service import award_xp

def get_or_create_progress(db: Session, user_id: int, level_id: int) -> UserProgress:
    prog = db.query(UserProgress).filter(
        UserProgress.user_id == user_id,
        UserProgress.level_id == level_id
    ).first()

    if not prog:
        # Count non-boss challenges
        non_boss_count = db.query(CodingChallenge).filter(
            CodingChallenge.level_id == level_id,
            CodingChallenge.is_boss == False
        ).count()

        prog = UserProgress(
            user_id=user_id,
            level_id=level_id,
            lesson_completed=False,
            challenges_passed=0,
            total_challenges=non_boss_count,
            mcq_score=0.0,
            mcq_passed=False,
            boss_completed=False,
            is_level_completed=False
        )
        db.add(prog)
        db.commit()
        db.refresh(prog)

    return prog

def is_level_unlocked(db: Session, user_id: int, level_id: int) -> bool:
    """
    Verifies on the backend whether a level is unlocked for a user.
    Level 1 is unlocked for everyone.
    Level N requires Level N-1 to be completed.
    """
    level = db.query(Level).filter(Level.id == level_id).first()
    if not level:
        return False

    if level.is_unlocked_by_default or (level.world_id == 1 and level.order_index == 1):
        return True

    # Find previous level in order
    prev_level = db.query(Level).filter(
        Level.number == level.number - 1
    ).first()

    if not prev_level:
        # If no explicit number-1, check order_index within same world or previous world
        if level.order_index > 1:
            prev_level = db.query(Level).filter(
                Level.world_id == level.world_id,
                Level.order_index == level.order_index - 1
            ).first()
        else:
            prev_world = db.query(World).filter(World.id == level.world_id - 1).first()
            if prev_world:
                prev_level = db.query(Level).filter(Level.world_id == prev_world.id).order_by(Level.order_index.desc()).first()

    if not prev_level:
        return True

    prev_prog = db.query(UserProgress).filter(
        UserProgress.user_id == user_id,
        UserProgress.level_id == prev_level.id
    ).first()

    return prev_prog is not None and prev_prog.is_level_completed

def verify_and_update_level_completion(db: Session, user: User, level_id: int) -> dict:
    """
    Strict backend verification of completion criteria:
    - Lesson marked completed
    - Coding challenges >= 80% passed
    - MCQ examination >= 80% score
    - Boss challenge passed (if exists)
    """
    prog = get_or_create_progress(db, user.id, level_id)
    level = db.query(Level).filter(Level.id == level_id).first()
    if not level:
        return {"completed": False, "reason": "Level not found"}

    # Recalculate passed non-boss challenges
    non_boss_challenges = db.query(CodingChallenge).filter(
        CodingChallenge.level_id == level_id,
        CodingChallenge.is_boss == False
    ).all()
    total_challenges = len(non_boss_challenges)
    prog.total_challenges = total_challenges

    passed_challenges = 0
    for ch in non_boss_challenges:
        has_passed = db.query(ChallengeSubmission).filter(
            ChallengeSubmission.user_id == user.id,
            ChallengeSubmission.challenge_id == ch.id,
            ChallengeSubmission.passed == True
        ).first() is not None
        if has_passed:
            passed_challenges += 1
    prog.challenges_passed = passed_challenges

    # Check boss challenge
    boss_ch = db.query(CodingChallenge).filter(
        CodingChallenge.level_id == level_id,
        CodingChallenge.is_boss == True
    ).first()
    if boss_ch:
        boss_passed = db.query(ChallengeSubmission).filter(
            ChallengeSubmission.user_id == user.id,
            ChallengeSubmission.challenge_id == boss_ch.id,
            ChallengeSubmission.passed == True
        ).first() is not None
        prog.boss_completed = boss_passed
    else:
        prog.boss_completed = True  # No boss challenge for this level

    # Check quiz questions
    total_questions = db.query(QuizQuestion).filter(QuizQuestion.level_id == level_id).count()
    if total_questions == 0:
        prog.mcq_passed = True
        prog.mcq_score = 100.0

    # Verification checks
    lesson_ok = prog.lesson_completed
    challenges_ok = (total_challenges == 0) or ((passed_challenges / total_challenges) >= 0.8)
    mcq_ok = prog.mcq_passed and (prog.mcq_score >= 80.0)
    boss_ok = prog.boss_completed

    all_satisfied = lesson_ok and challenges_ok and mcq_ok and boss_ok

    was_completed = prog.is_level_completed
    if all_satisfied and not was_completed:
        prog.is_level_completed = True
        prog.completed_at = datetime.utcnow()

        # Check if perfect completion bonus eligible
        is_perfect = (
            (total_challenges == 0 or passed_challenges == total_challenges) and
            prog.mcq_score >= 100.0 and
            boss_ok
        )
        if is_perfect:
            award_xp(db, user, 100, f"perfect_level_{level_id}", f"Perfect completion bonus for Level {level.number}")

        # Advance user current_level_id if this level equals current
        if user.current_level_id == level.number:
            next_level = db.query(Level).filter(Level.number == level.number + 1).first()
            if next_level:
                user.current_level_id = next_level.number
                user.current_world_id = next_level.world_id

    db.commit()

    return {
        "is_level_completed": prog.is_level_completed,
        "criteria": {
            "lesson_completed": lesson_ok,
            "challenges_passed": f"{passed_challenges}/{total_challenges}",
            "challenges_ok": challenges_ok,
            "mcq_score": prog.mcq_score,
            "mcq_ok": mcq_ok,
            "boss_completed": boss_ok
        }
    }
