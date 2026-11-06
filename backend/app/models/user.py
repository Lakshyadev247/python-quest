from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    
    current_rank = Column(String(50), default="Beginner")
    total_xp = Column(Integer, default=0)
    current_world_id = Column(Integer, default=1)
    current_level_id = Column(Integer, default=1)
    streak_days = Column(Integer, default=1)
    last_active_date = Column(Date, default=date.today)
    avatar = Column(String(100), default="snake_novice")
    theme = Column(String(20), default="dark")
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    progress = relationship("UserProgress", back_populates="user", cascade="all, delete-orphan")
    submissions = relationship("ChallengeSubmission", back_populates="user", cascade="all, delete-orphan")
    quiz_attempts = relationship("QuizAttempt", back_populates="user", cascade="all, delete-orphan")
    xp_transactions = relationship("XPTransaction", back_populates="user", cascade="all, delete-orphan")
    achievements = relationship("UserAchievement", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin,
            "current_rank": self.current_rank,
            "total_xp": self.total_xp,
            "current_world_id": self.current_world_id,
            "current_level_id": self.current_level_id,
            "streak_days": self.streak_days,
            "last_active_date": self.last_active_date.isoformat() if self.last_active_date else None,
            "avatar": self.avatar,
            "theme": self.theme,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
