from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class World(Base):
    __tablename__ = "worlds"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, nullable=False)
    title = Column(String(150), nullable=False)
    goal = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    final_project_title = Column(String(150), nullable=True)
    final_project_desc = Column(Text, nullable=True)
    is_unlocked_by_default = Column(Boolean, default=False)

    levels = relationship("Level", back_populates="world", order_by="Level.order_index", cascade="all, delete-orphan")

    def to_dict(self, include_levels=False):
        data = {
            "id": self.id,
            "number": self.number,
            "title": self.title,
            "goal": self.goal,
            "description": self.description,
            "final_project_title": self.final_project_title,
            "final_project_desc": self.final_project_desc,
            "is_unlocked_by_default": self.is_unlocked_by_default,
            "total_levels": len(self.levels) if self.levels else 0
        }
        if include_levels:
            data["levels"] = [lvl.to_dict() for lvl in self.levels]
        return data


class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey("worlds.id", ondelete="CASCADE"), nullable=False, index=True)
    number = Column(Integer, nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    order_index = Column(Integer, nullable=False)
    is_unlocked_by_default = Column(Boolean, default=False)

    world = relationship("World", back_populates="levels")
    lesson = relationship("Lesson", back_populates="level", uselist=False, cascade="all, delete-orphan")
    challenges = relationship("CodingChallenge", back_populates="level", order_by="CodingChallenge.order_index", cascade="all, delete-orphan")
    quiz_questions = relationship("QuizQuestion", back_populates="level", order_by="QuizQuestion.order_index", cascade="all, delete-orphan")
    progress_records = relationship("UserProgress", back_populates="level", cascade="all, delete-orphan")

    def to_dict(self, include_details=False):
        data = {
            "id": self.id,
            "world_id": self.world_id,
            "number": self.number,
            "title": self.title,
            "description": self.description,
            "order_index": self.order_index,
            "is_unlocked_by_default": self.is_unlocked_by_default,
            "total_challenges": len(self.challenges) if self.challenges else 0,
            "total_questions": len(self.quiz_questions) if self.quiz_questions else 0,
            "has_lesson": self.lesson is not None
        }
        if include_details:
            if self.lesson:
                data["lesson"] = self.lesson.to_dict()
            data["challenges"] = [c.to_dict(include_solution=True) for c in self.challenges]
            data["quiz_questions"] = [q.to_dict() for q in self.quiz_questions]
        return data


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    level_id = Column(Integer, ForeignKey("levels.id", ondelete="CASCADE"), unique=True, nullable=False)
    title = Column(String(150), nullable=False)
    
    # 13 structured sections (Section 6 of Master Spec)
    learning_objectives = Column(Text, nullable=False)  # JSON or text
    prerequisites = Column(Text, nullable=False)
    introduction = Column(Text, nullable=False)
    detailed_explanation = Column(Text, nullable=False)
    terminology = Column(Text, nullable=False)          # JSON list of {term, definition}
    syntax_breakdown = Column(Text, nullable=False)
    practical_examples = Column(Text, nullable=False)    # JSON list of {title, code, explanation, output}
    line_by_line = Column(Text, nullable=False)          # JSON list of {line, code, explanation}
    expected_output = Column(Text, nullable=False)
    common_mistakes = Column(Text, nullable=False)      # JSON list of {mistake, why, fix}
    real_world_apps = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    practice_questions = Column(Text, nullable=False)   # JSON list of practice questions

    level = relationship("Level", back_populates="lesson")

    def to_dict(self):
        import json
        def safe_json(val):
            if not val:
                return []
            try:
                return json.loads(val)
            except Exception:
                return val

        return {
            "id": self.id,
            "level_id": self.level_id,
            "title": self.title,
            "learning_objectives": safe_json(self.learning_objectives),
            "prerequisites": self.prerequisites,
            "introduction": self.introduction,
            "detailed_explanation": self.detailed_explanation,
            "terminology": safe_json(self.terminology),
            "syntax_breakdown": self.syntax_breakdown,
            "practical_examples": safe_json(self.practical_examples),
            "line_by_line": safe_json(self.line_by_line),
            "expected_output": self.expected_output,
            "common_mistakes": safe_json(self.common_mistakes),
            "real_world_apps": self.real_world_apps,
            "summary": self.summary,
            "practice_questions": safe_json(self.practice_questions)
        }


class CodingChallenge(Base):
    __tablename__ = "coding_challenges"

    id = Column(Integer, primary_key=True, index=True)
    level_id = Column(Integer, ForeignKey("levels.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(150), nullable=False)
    difficulty = Column(String(20), default="easy") # easy, medium, hard, boss
    is_boss = Column(Boolean, default=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=True)
    initial_code = Column(Text, default="# Write your solution here\n")
    solution_code = Column(Text, nullable=True)
    hints = Column(Text, nullable=True) # JSON list
    xp_reward = Column(Integer, default=30)
    order_index = Column(Integer, default=1)

    level = relationship("Level", back_populates="challenges")
    test_cases = relationship("TestCase", back_populates="challenge", cascade="all, delete-orphan")

    def to_dict(self, include_solution=False):
        import json
        def safe_json(val):
            if not val:
                return []
            try:
                return json.loads(val)
            except Exception:
                return [val]

        data = {
            "id": self.id,
            "level_id": self.level_id,
            "title": self.title,
            "difficulty": self.difficulty,
            "is_boss": self.is_boss,
            "description": self.description,
            "requirements": self.requirements,
            "initial_code": self.initial_code,
            "hints": safe_json(self.hints),
            "xp_reward": self.xp_reward,
            "order_index": self.order_index,
            "test_cases": [tc.to_dict() for tc in self.test_cases if not tc.is_hidden]
        }
        if include_solution:
            data["solution_code"] = self.solution_code
        return data


class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)
    challenge_id = Column(Integer, ForeignKey("coding_challenges.id", ondelete="CASCADE"), nullable=False, index=True)
    input_data = Column(Text, default="")
    expected_output = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=False)
    explanation = Column(Text, nullable=True)

    challenge = relationship("CodingChallenge", back_populates="test_cases")

    def to_dict(self):
        return {
            "id": self.id,
            "input_data": self.input_data,
            "expected_output": self.expected_output,
            "is_hidden": self.is_hidden,
            "explanation": self.explanation
        }


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, index=True)
    level_id = Column(Integer, ForeignKey("levels.id", ondelete="CASCADE"), nullable=False, index=True)
    question = Column(Text, nullable=False)
    question_type = Column(String(20), default="single") # single or multiple
    code_snippet = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)
    order_index = Column(Integer, default=1)

    level = relationship("Level", back_populates="quiz_questions")
    options = relationship("QuizOption", back_populates="question", cascade="all, delete-orphan")

    def to_dict(self, include_answers=False):
        return {
            "id": self.id,
            "level_id": self.level_id,
            "question": self.question,
            "question_type": self.question_type,
            "code_snippet": self.code_snippet,
            "explanation": self.explanation if include_answers else None,
            "order_index": self.order_index,
            "options": [opt.to_dict(include_answers=include_answers) for opt in self.options]
        }


class QuizOption(Base):
    __tablename__ = "quiz_options"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("quiz_questions.id", ondelete="CASCADE"), nullable=False, index=True)
    option_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)
    explanation = Column(Text, nullable=True)

    question = relationship("QuizQuestion", back_populates="options")

    def to_dict(self, include_answers=False):
        data = {
            "id": self.id,
            "option_text": self.option_text,
        }
        if include_answers:
            data["is_correct"] = self.is_correct
            data["explanation"] = self.explanation
        return data
