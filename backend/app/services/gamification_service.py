from datetime import date, timedelta
from app.models.user import User
from app.models.progress import XPTransaction, Achievement, UserAchievement, UserProgress, ChallengeSubmission, QuizAttempt
from app.models.curriculum import Level

RANKS = [
    (0, "Beginner"),
    (3000, "Python Apprentice"),
    (9000, "Code Explorer"),
    (18000, "Logic Builder"),
    (28000, "Python Developer"),
    (38000, "Advanced Developer"),
    (46000, "Python Master")
]

DEFAULT_ACHIEVEMENTS = [
    {"code": "FIRST_PROGRAM", "title": "First Program", "description": "Executed your very first Python program.", "icon": "Terminal", "xp_bonus": 50},
    {"code": "FIRST_CHALLENGE", "title": "First Coding Challenge", "description": "Successfully solved your first coding challenge.", "icon": "CheckCircle", "xp_bonus": 50},
    {"code": "PERFECT_EXAM", "title": "Perfect Examination", "description": "Scored 100% on a level MCQ examination.", "icon": "Award", "xp_bonus": 100},
    {"code": "FIVE_LEVELS", "title": "Five Levels Completed", "description": "Mastered and completed 5 curriculum levels.", "icon": "Zap", "xp_bonus": 150},
    {"code": "TEN_LEVELS", "title": "Ten Levels Completed", "description": "Mastered and completed 10 curriculum levels.", "icon": "Star", "xp_bonus": 200},
    {"code": "DEBUGGING_EXPERT", "title": "Debugging Expert", "description": "Passed 10 practical coding exercises.", "icon": "Wrench", "xp_bonus": 100},
    {"code": "LOOP_MASTER", "title": "Loop Master", "description": "Conquered loops and iteration in World 5.", "icon": "Repeat", "xp_bonus": 200},
    {"code": "FUNCTION_SPECIALIST", "title": "Function Specialist", "description": "Mastered modular programming and functions in World 7.", "icon": "Code", "xp_bonus": 250},
    {"code": "OOP_EXPERT", "title": "OOP Expert", "description": "Built object-oriented software architectures in World 10.", "icon": "Layers", "xp_bonus": 300},
    {"code": "PYTHON_GRADUATE", "title": "Python Graduate", "description": "Completed all 12 Worlds of Python Quest.", "icon": "GraduationCap", "xp_bonus": 500}
]

def seed_achievements(db):
    for ach in DEFAULT_ACHIEVEMENTS:
        existing = db.query(Achievement).filter(Achievement.code == ach["code"]).first()
        if not existing:
            db.add(Achievement(**ach))
    db.commit()

def calculate_rank(total_xp: int) -> str:
    current = "Beginner"
    for min_xp, rank_name in RANKS:
        if total_xp >= min_xp:
            current = rank_name
        else:
            break
    return current

def update_user_streak(user: User):
    today = date.today()
    if not user.last_active_date:
        user.streak_days = 1
        user.last_active_date = today
    elif user.last_active_date == today:
        pass  # already active today
    elif user.last_active_date == today - timedelta(days=1):
        user.streak_days += 1
        user.last_active_date = today
    else:
        user.streak_days = 1
        user.last_active_date = today

def award_xp(db, user: User, amount: int, source: str, description: str = "") -> tuple[bool, int]:
    """
    Awards XP ensuring idempotency: rewards each source only once.
    Returns (awarded: bool, new_total_xp: int).
    """
    existing = db.query(XPTransaction).filter(
        XPTransaction.user_id == user.id,
        XPTransaction.source == source
    ).first()

    if existing:
        return False, user.total_xp

    tx = XPTransaction(
        user_id=user.id,
        amount=amount,
        source=source,
        description=description
    )
    db.add(tx)
    user.total_xp += amount
    user.current_rank = calculate_rank(user.total_xp)
    update_user_streak(user)
    db.commit()

    # Check for unlocked achievements
    check_achievements(db, user)

    return True, user.total_xp

def check_achievements(db, user: User):
    """
    Evaluates criteria and unlocks achievements for the user.
    """
    unlocked_codes = {
        ua.achievement.code for ua in db.query(UserAchievement).filter(UserAchievement.user_id == user.id).all()
        if ua.achievement
    }

    achievements_to_unlock = []

    # FIRST_PROGRAM
    if "FIRST_PROGRAM" not in unlocked_codes:
        sub_count = db.query(ChallengeSubmission).filter(ChallengeSubmission.user_id == user.id).count()
        if sub_count >= 1:
            achievements_to_unlock.append("FIRST_PROGRAM")

    # FIRST_CHALLENGE
    if "FIRST_CHALLENGE" not in unlocked_codes:
        passed_count = db.query(ChallengeSubmission).filter(
            ChallengeSubmission.user_id == user.id,
            ChallengeSubmission.passed == True
        ).count()
        if passed_count >= 1:
            achievements_to_unlock.append("FIRST_CHALLENGE")

    # PERFECT_EXAM
    if "PERFECT_EXAM" not in unlocked_codes:
        perfect_exam = db.query(QuizAttempt).filter(
            QuizAttempt.user_id == user.id,
            QuizAttempt.score_percent >= 100.0
        ).first()
        if perfect_exam:
            achievements_to_unlock.append("PERFECT_EXAM")

    # FIVE_LEVELS
    completed_levels_count = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.is_level_completed == True
    ).count()

    if "FIVE_LEVELS" not in unlocked_codes and completed_levels_count >= 5:
        achievements_to_unlock.append("FIVE_LEVELS")

    # TEN_LEVELS
    if "TEN_LEVELS" not in unlocked_codes and completed_levels_count >= 10:
        achievements_to_unlock.append("TEN_LEVELS")

    # DEBUGGING_EXPERT
    if "DEBUGGING_EXPERT" not in unlocked_codes:
        passed_count = db.query(ChallengeSubmission).filter(
            ChallengeSubmission.user_id == user.id,
            ChallengeSubmission.passed == True
        ).count()
        if passed_count >= 10:
            achievements_to_unlock.append("DEBUGGING_EXPERT")

    # Grant achievements
    for code in achievements_to_unlock:
        ach = db.query(Achievement).filter(Achievement.code == code).first()
        if ach:
            ua = UserAchievement(user_id=user.id, achievement_id=ach.id)
            db.add(ua)
            # Award bonus XP for achievement
            tx = XPTransaction(
                user_id=user.id,
                amount=ach.xp_bonus,
                source=f"achievement_{code}",
                description=f"Unlocked Achievement: {ach.title}"
            )
            db.add(tx)
            user.total_xp += ach.xp_bonus
            user.current_rank = calculate_rank(user.total_xp)

    if achievements_to_unlock:
        db.commit()
