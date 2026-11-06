import sys
import io
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from app.services.executor_service import execute_python_code

def validate_world_module(world_data):
    """
    Validates a world dictionary:
    - Verifies 13-section lesson structure
    - Executes every challenge solution code against its test cases
    - Validates quizzes
    """
    w_num = world_data["number"]
    w_title = world_data["title"]
    levels = world_data["levels"]

    print(f"\n--- VALIDATING WORLD {w_num}: {w_title} ({len(levels)} Levels) ---")
    
    total_tests_executed = 0
    passed_tests = 0
    failed_tests = []

    for lvl in levels:
        l_num = lvl["number"]
        l_title = lvl["title"]
        
        # 1. Validate lesson 13 sections
        lesson = lvl.get("lesson")
        assert lesson is not None, f"Level {l_num} is missing lesson"
        required_keys = [
            "learning_objectives", "prerequisites", "introduction",
            "detailed_explanation", "terminology", "syntax_breakdown",
            "practical_examples", "line_by_line", "expected_output",
            "common_mistakes", "real_world_apps", "summary", "practice_questions"
        ]
        for key in required_keys:
            val = lesson.get(key)
            assert val is not None and len(val) > 0, f"Level {l_num} lesson missing {key}"
        
        # Ensure no placeholder markers
        assert "Programmers use this concept to build reliable" not in lesson["detailed_explanation"], f"Level {l_num} has placeholder detailed_explanation"

        # 2. Validate challenges and execute tests
        challenges = lvl.get("challenges", [])
        assert len(challenges) >= 2, f"Level {l_num} must have at least 2 challenges (1 standard, 1 boss), found {len(challenges)}"
        has_boss = any(c.get("is_boss") for c in challenges)
        assert has_boss, f"Level {l_num} must have a boss challenge"

        for ch in challenges:
            ch_title = ch["title"]
            solution = ch.get("solution_code", "")
            test_cases = ch.get("test_cases", [])
            assert len(solution.strip()) > 0, f"Challenge '{ch_title}' in Level {l_num} missing solution code"
            assert len(test_cases) > 0, f"Challenge '{ch_title}' in Level {l_num} missing test cases"

            # Execute solution against each test case in sandbox
            for tc_idx, tc in enumerate(test_cases):
                total_tests_executed += 1
                inp = tc.get("input_data", "")
                exp = tc["expected_output"].rstrip()

                res = execute_python_code(solution, input_data=inp)
                actual = res["stdout"].rstrip()

                if res["success"] and actual == exp:
                    passed_tests += 1
                else:
                    failed_tests.append({
                        "level": l_num,
                        "challenge": ch_title,
                        "test_idx": tc_idx + 1,
                        "error": res["stderr"] if not res["success"] else f"Output mismatch: expected '{exp}', got '{actual}'"
                    })

        # 3. Validate quizzes
        quizzes = lvl.get("quizzes", [])
        assert len(quizzes) >= 2, f"Level {l_num} must have at least 2 quiz questions"
        for q in quizzes:
            assert len(q.get("question", "")) > 10, f"Level {l_num} has invalid quiz question"
            opts = q.get("options", [])
            assert len(opts) == 4, f"Level {l_num} quiz question must have 4 options, found {len(opts)}"
            correct_opts = [o for o in opts if o.get("is_correct")]
            assert len(correct_opts) == 1, f"Level {l_num} quiz question must have exactly 1 correct option"
            for o in opts:
                assert len(o.get("text", "")) > 0, f"Option missing text in Level {l_num}"

    print(f"✓ World {w_num} structural checks PASSED for all {len(levels)} levels.")
    print(f"✓ Executed {total_tests_executed} challenge test cases: {passed_tests} PASSED, {len(failed_tests)} FAILED.")
    
    if failed_tests:
        print("FAILED TESTS DETAIL:")
        for ft in failed_tests:
            print(f"  Level {ft['level']} - {ft['challenge']} (Test #{ft['test_idx']}): {ft['error']}")
        raise AssertionError(f"World {w_num} failed {len(failed_tests)} test cases!")

    return True
