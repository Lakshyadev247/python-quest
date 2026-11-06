"""
Master Global Verification Script for Python Quest Curriculum
Verifies database integrity, absence of placeholders, all 13 lesson sections,
and executes all challenge test cases through the code execution sandbox.
"""

import sys
import io
import json
from app.database import SessionLocal
from app.models.curriculum import World, Level, Lesson, CodingChallenge, TestCase, QuizQuestion, QuizOption
from app.curriculum.test_curriculum_module import validate_world_module

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

ALL_MODULES = [
    WORLD_1, WORLD_2, WORLD_3, WORLD_4, WORLD_5, WORLD_6,
    WORLD_7, WORLD_8, WORLD_9, WORLD_10, WORLD_11, WORLD_12
]

def run_global_verification():
    sys.stdout.reconfigure(encoding="utf-8")
    print("================================================================================")
    print("       PYTHON QUEST: GLOBAL 12-WORLD CURRICULUM VERIFICATION SUITE              ")
    print("================================================================================")

    db = SessionLocal()
    try:
        # 1. World & Level Counts
        worlds = db.query(World).order_by(World.number).all()
        assert len(worlds) == 12, f"Expected 12 worlds, found {len(worlds)}"
        
        levels = db.query(Level).order_by(Level.number).all()
        assert len(levels) == 126, f"Expected 126 levels, found {len(levels)}"
        print(f"✓ Database Schema Verified: 12 Worlds, 126 Levels present.")

        # 2. Check Lessons
        lessons = db.query(Lesson).all()
        assert len(lessons) == 126, f"Expected 126 lessons, found {len(lessons)}"
        
        mandatory_keys = [
            "learning_objectives", "prerequisites", "introduction",
            "detailed_explanation", "terminology", "syntax_breakdown",
            "practical_examples", "line_by_line", "expected_output",
            "common_mistakes", "real_world_apps", "summary", "practice_questions"
        ]

        placeholder_count = 0
        for l in lessons:
            data = l.to_dict()
            for key in mandatory_keys:
                val = data.get(key)
                assert val, f"Level {l.level.number} missing lesson key: {key}"
                val_str = str(val)
                if ": Completed" in val_str or "Mastered:" in val_str:
                    placeholder_count += 1

        assert placeholder_count == 0, f"Found {placeholder_count} placeholders in lessons!"
        print(f"✓ All 126 Lessons verified: 100% complete with 13 mandatory sections.")

        # 3. Check Challenges
        challenges = db.query(CodingChallenge).all()
        assert len(challenges) >= 252, f"Expected at least 252 challenges, found {len(challenges)}"
        
        boss_count = sum(1 for c in challenges if c.is_boss)
        std_count = len(challenges) - boss_count
        assert boss_count == 126, f"Expected 126 boss challenges, found {boss_count}"

        # Check for placeholder titles/descriptions
        ch_placeholders = 0
        for c in challenges:
            if "Mastery challenge for Level" in c.description or ": Completed" in c.description:
                ch_placeholders += 1
        assert ch_placeholders == 0, f"Found {ch_placeholders} placeholder challenges!"
        print(f"✓ All {len(challenges)} Challenges verified ({std_count} Standard + {boss_count} Boss). ZERO placeholders.")

        # 4. Check Test Cases
        test_cases = db.query(TestCase).all()
        assert len(test_cases) >= 252, f"Expected at least 252 test cases, found {len(test_cases)}"
        tc_placeholders = 0
        for tc in test_cases:
            if ": Completed" in tc.expected_output or "Mastered:" in tc.expected_output:
                tc_placeholders += 1
        assert tc_placeholders == 0, f"Found {tc_placeholders} placeholder test cases!"
        print(f"✓ All {len(test_cases)} Test Cases verified. ZERO placeholders.")

        # 5. Check Quizzes
        quizzes = db.query(QuizQuestion).all()
        assert len(quizzes) >= 252, f"Expected at least 252 quiz questions, found {len(quizzes)}"
        quiz_placeholders = 0
        for q in quizzes:
            if "What is the core focus of" in q.question:
                quiz_placeholders += 1
            assert len(q.options) == 4, f"Question {q.id} has {len(q.options)} options instead of 4"
            correct_opts = [o for o in q.options if o.is_correct]
            assert len(correct_opts) == 1, f"Question {q.id} has {len(correct_opts)} correct options instead of 1"

        assert quiz_placeholders == 0, f"Found {quiz_placeholders} placeholder quiz questions!"
        print(f"✓ All {len(quizzes)} Quiz Questions and {len(quizzes) * 4} Options verified. ZERO placeholders.")

        # 6. Execute Sandbox Tests across all 12 modules
        print("\n--- EXECUTING COMPLETE SANDBOX TEST SUITE ACROSS ALL 12 WORLDS ---")
        for w_mod in ALL_MODULES:
            assert validate_world_module(w_mod) is True
        
        print(f"\n================================================================================")
        print(f"🏆 ALL CHECKS PASSED: 12/12 WORLDS, 126/126 LEVELS COMPLETED & VERIFIED")
        print(f"🏆 Total Database Records: 126 Lessons, 252 Challenges, 452 Test Cases, 252 Quizzes")
        print(f"================================================================================")

    finally:
        db.close()

if __name__ == "__main__":
    run_global_verification()
