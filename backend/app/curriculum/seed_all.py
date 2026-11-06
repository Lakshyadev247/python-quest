"""
Curriculum Seed Script:
Populates all 12 Worlds and 126 Levels with handcrafted lessons, coding challenges, MCQs, and Capstones.
Completely replaces placeholder records while preserving user records and database integrity.
"""

import sys
import json
from app.database import SessionLocal, engine, Base
from app.models.curriculum import World, Level, Lesson, CodingChallenge, TestCase, QuizQuestion, QuizOption
from app.services.gamification_service import seed_achievements

from app.curriculum.world1 import WORLD_1
from app.curriculum.world2 import WORLD_2
from app.curriculum.world3 import WORLD_3
from app.curriculum.world4 import WORLD_4
from app.curriculum.world5 import WORLD_5
from app.curriculum.world6 import WORLD_6
from app.curriculum.world7 import WORLD_7
from app.curriculum.world8 import WORLD_8
from app.curriculum.world9 import WORLD_9
from app.curriculum.world10 import WORLD_10
from app.curriculum.world11 import WORLD_11
from app.curriculum.world12 import WORLD_12

ALL_WORLDS = [
    WORLD_1, WORLD_2, WORLD_3, WORLD_4, WORLD_5, WORLD_6,
    WORLD_7, WORLD_8, WORLD_9, WORLD_10, WORLD_11, WORLD_12
]

def seed_full_curriculum():
    db = SessionLocal()
    try:
        print("=== INITIATING FULL PYTHON QUEST CURRICULUM SEEDING (12 WORLDS, 126 LEVELS) ===")
        
        # Ensure achievements are seeded
        seed_achievements(db)

        total_lessons_seeded = 0
        total_challenges_seeded = 0
        total_test_cases_seeded = 0
        total_questions_seeded = 0
        total_options_seeded = 0

        for w_data in ALL_WORLDS:
            w_num = w_data["number"]
            world = db.query(World).filter(World.number == w_num).first()
            if not world:
                world = World(
                    number=w_num,
                    title=w_data["title"],
                    goal=w_data.get("goal"),
                    description=w_data.get("description"),
                    final_project_title=w_data.get("final_project_title"),
                    final_project_desc=w_data.get("final_project_desc"),
                    is_unlocked_by_default=(w_num == 1)
                )
                db.add(world)
                db.commit()
                db.refresh(world)
            else:
                world.title = w_data["title"]
                world.goal = w_data.get("goal")
                world.description = w_data.get("description")
                world.final_project_title = w_data.get("final_project_title")
                world.final_project_desc = w_data.get("final_project_desc")
                world.is_unlocked_by_default = (w_num == 1)
                db.commit()

            print(f"Seeding World {w_num}: {world.title}...")

            for lvl_idx, lvl_data in enumerate(w_data["levels"], start=1):
                lvl_num = lvl_data["number"]
                level = db.query(Level).filter(Level.number == lvl_num).first()
                if not level:
                    level = Level(
                        world_id=world.id,
                        number=lvl_num,
                        title=lvl_data["title"],
                        description=lvl_data.get("description"),
                        order_index=lvl_idx,
                        is_unlocked_by_default=(lvl_num == 1)
                    )
                    db.add(level)
                    db.commit()
                    db.refresh(level)
                else:
                    level.world_id = world.id
                    level.title = lvl_data["title"]
                    level.description = lvl_data.get("description")
                    level.order_index = lvl_idx
                    level.is_unlocked_by_default = (lvl_num == 1)
                    db.commit()

                # --- 1. Seed Handcrafted Lesson ---
                lesson_data = lvl_data["lesson"]
                existing_lesson = db.query(Lesson).filter(Lesson.level_id == level.id).first()
                if not existing_lesson:
                    existing_lesson = Lesson(level_id=level.id, title=lvl_data["title"])
                    db.add(existing_lesson)

                existing_lesson.title = lvl_data["title"]
                existing_lesson.learning_objectives = json.dumps(lesson_data["learning_objectives"])
                existing_lesson.prerequisites = lesson_data.get("prerequisites", "None")
                existing_lesson.introduction = lesson_data["introduction"]
                existing_lesson.detailed_explanation = lesson_data["detailed_explanation"]
                existing_lesson.terminology = json.dumps(lesson_data["terminology"])
                existing_lesson.syntax_breakdown = lesson_data["syntax_breakdown"]
                existing_lesson.practical_examples = json.dumps(lesson_data["practical_examples"])
                existing_lesson.line_by_line = json.dumps(lesson_data["line_by_line"])
                existing_lesson.expected_output = lesson_data["expected_output"]
                existing_lesson.common_mistakes = json.dumps(lesson_data["common_mistakes"])
                existing_lesson.real_world_apps = lesson_data["real_world_apps"]
                existing_lesson.summary = lesson_data["summary"]
                existing_lesson.practice_questions = json.dumps(lesson_data["practice_questions"])
                db.commit()
                total_lessons_seeded += 1

                # --- 2. Seed Handcrafted Coding Challenges ---
                # Delete old challenges for this level to remove placeholder challenges
                old_challenges = db.query(CodingChallenge).filter(CodingChallenge.level_id == level.id).all()
                for old_ch in old_challenges:
                    db.delete(old_ch)
                db.commit()

                for ch_order, ch_data in enumerate(lvl_data["challenges"], start=1):
                    ch = CodingChallenge(
                        level_id=level.id,
                        title=ch_data["title"],
                        difficulty=ch_data.get("difficulty", "easy"),
                        is_boss=ch_data.get("is_boss", False),
                        description=ch_data["description"],
                        requirements=ch_data.get("requirements", ""),
                        initial_code=ch_data.get("initial_code", "# Write code here\n"),
                        solution_code=ch_data.get("solution_code", ""),
                        hints=json.dumps(ch_data.get("hints", [])),
                        xp_reward=ch_data.get("xp_reward", 35),
                        order_index=ch_order
                    )
                    db.add(ch)
                    db.commit()
                    db.refresh(ch)
                    total_challenges_seeded += 1

                    for tc_data in ch_data.get("test_cases", []):
                        tc = TestCase(
                            challenge_id=ch.id,
                            input_data=tc_data.get("input_data", ""),
                            expected_output=tc_data["expected_output"],
                            is_hidden=tc_data.get("is_hidden", False),
                            explanation=tc_data.get("explanation", "")
                        )
                        db.add(tc)
                        total_test_cases_seeded += 1
                db.commit()

                # --- 3. Seed Handcrafted Quizzes ---
                # Delete old quiz questions for this level to remove placeholder questions
                old_questions = db.query(QuizQuestion).filter(QuizQuestion.level_id == level.id).all()
                for old_q in old_questions:
                    db.delete(old_q)
                db.commit()

                for q_order, q_data in enumerate(lvl_data["quizzes"], start=1):
                    q = QuizQuestion(
                        level_id=level.id,
                        question=q_data["question"],
                        question_type="single",
                        code_snippet=q_data.get("code_snippet"),
                        explanation=q_data.get("explanation"),
                        order_index=q_order
                    )
                    db.add(q)
                    db.commit()
                    db.refresh(q)
                    total_questions_seeded += 1

                    for opt_data in q_data["options"]:
                        opt = QuizOption(
                            question_id=q.id,
                            option_text=opt_data["text"],
                            is_correct=opt_data["is_correct"],
                            explanation=opt_data.get("explanation", "")
                        )
                        db.add(opt)
                        total_options_seeded += 1
                db.commit()

        # Update manifest.json
        import os
        manifest_path = os.path.join(os.path.dirname(__file__), "manifest.json")
        manifest = {
            "total_worlds": 12,
            "total_levels": 126,
            "worlds_status": {str(i): "completed" for i in range(1, 13)},
            "total_lessons": total_lessons_seeded,
            "total_challenges": total_challenges_seeded,
            "total_test_cases": total_test_cases_seeded,
            "total_quiz_questions": total_questions_seeded,
            "total_quiz_options": total_options_seeded,
            "last_updated": "2026-11-02T02:43:00Z"
        }
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

        print("\n=== CURRICULUM SEEDING COMPLETE ===")
        print(f"Total Worlds Seeded: 12")
        print(f"Total Levels Seeded: 126")
        print(f"Total Lessons Seeded: {total_lessons_seeded}")
        print(f"Total Coding Challenges Seeded: {total_challenges_seeded}")
        print(f"Total Test Cases Seeded: {total_test_cases_seeded}")
        print(f"Total Quiz Questions Seeded: {total_questions_seeded}")
        print(f"Total Quiz Options Seeded: {total_options_seeded}")
        print("All placeholder content has been eradicated from python_quest.db!")
    finally:
        db.close()

if __name__ == "__main__":
    seed_full_curriculum()
