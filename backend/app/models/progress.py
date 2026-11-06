from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    level_id = Column(Integer, ForeignKey("levels.id", ondelete="CASCADE"), nullable=False, index=True)
    
    lesson_completed = Column(Boolean, default=False)
    challenges_passed = Column(Integer, default=0)
    total_challenges = Column(Integer, default=0)
    mcq_score = Column(Float, default=0.0)  # Percentage (e.g. 80.0)
    mcq_passed = Column(Boolean, default=False)
    boss_completed = Column(Boolean, default=False)
    is_level_completed = Column(Boolean, default=False)
    
    completed_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="progress")
    level = relationship("Level", back_populates="progress_records")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "level_id": self.level_id,
            "lesson_completed": self.lesson_completed,
            "challenges_passed": self.challenges_passed,
            "total_challenges": self.total_challenges,
            "mcq_score": self.mcq_score,
            "mcq_passed": self.mcq_passed,
            "boss_completed": self.boss_completed,
            "is_level_completed": self.is_level_completed,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class ChallengeSubmission(Base):
    __tablename__ = "challenge_submissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    challenge_id = Column(Integer, ForeignKey("coding_challenges.id", ondelete="CASCADE"), nullable=False, index=True)
    submitted_code = Column(Text, nullable=False)
    passed = Column(Boolean, default=False)
    stdout = Column(Text, nullable=True)
    stderr = Column(Text, nullable=True)
    tests_passed = Column(Integer, default=0)
    total_tests = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="submissions")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "challenge_id": self.challenge_id,
            "submitted_code": self.submitted_code,
            "passed": self.passed,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "tests_passed": self.tests_passed,
            "total_tests": self.total_tests,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    level_id = Column(Integer, ForeignKey("levels.id", ondelete="CASCADE"), nullable=False, index=True)
    score_percent = Column(Float, nullable=False)
    total_questions = Column(Integer, nullable=False)
    correct_count = Column(Integer, nullable=False)
    passed = Column(Boolean, default=False)
    answers_json = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="quiz_attempts")

    def to_dict(self):
        import json
        return {
            "id": self.id,
            "user_id": self.user_id,
            "level_id": self.level_id,
            "score_percent": self.score_percent,
            "total_questions": self.total_questions,
            "correct_count": self.correct_count,
            "passed": self.passed,
            "answers": json.loads(self.answers_json) if self.answers_json else {},
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class XPTransaction(Base):
    __tablename__ = "xp_transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    source = Column(String(100), nullable=False)  # e.g. "lesson_1", "challenge_2", "boss_1", "perfect_bonus_1"
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="xp_transactions")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "amount": self.amount,
            "source": self.source,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    icon = Column(String(50), default="Award")
    xp_bonus = Column(Integer, default=100)

    user_achievements = relationship("UserAchievement", back_populates="achievement", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "icon": self.icon,
            "xp_bonus": self.xp_bonus
        }


class UserAchievement(Base):
    __tablename__ = "user_achievements"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    achievement_id = Column(Integer, ForeignKey("achievements.id", ondelete="CASCADE"), nullable=False, index=True)
    unlocked_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="achievements")
    achievement = relationship("Achievement", back_populates="user_achievements")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "achievement_id": self.achievement_id,
            "achievement": self.achievement.to_dict() if self.achievement else None,
            "unlocked_at": self.unlocked_at.isoformat() if self.unlocked_at else None
        }
