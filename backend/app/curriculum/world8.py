"""
Curriculum module: WORLD_8
Upgraded with pedagogical question scenarios and scaffolded starter code.
"""

WORLD_8 = {'description': 'Master try/except/finally, raising exceptions, file I/O with context managers, and JSON '
                'data serialization.',
 'final_project_desc': 'Build a robust CLI note-taking and task persistence system with JSON storage, error '
                       'recovery, and search.',
 'final_project_title': 'File-Based Notes Application',
 'goal': 'Build fault-tolerant applications that handle runtime exceptions and persist data across sessions.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Print these three error names, one per line: SyntaxError, ZeroDivisionError, and IndexError.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["e1 = 'SyntaxError'\n"
                                       "e2 = 'ZeroDivisionError'\n"
                                       "e3 = 'IndexError'\n"
                                       'print(e1)\n'
                                       'print(e2)\n'
                                       'print(e3)'],
                             'initial_code': '# Error Classification: Syntax vs Exceptions\n'
                                             '# Step 1: Assign e1, e2, e3:\n'
                                             "e1 = 'SyntaxError'\n"
                                             "e2 = 'ZeroDivisionError'\n"
                                             "e3 = 'IndexError'\n"
                                             '\n'
                                             '# Step 2: Print all three below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "print('SyntaxError')\n"
                                              "print('ZeroDivisionError')\n"
                                              "print('IndexError')",
                             'test_cases': [{'expected_output': 'SyntaxError\nZeroDivisionError\nIndexError',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Exception Type Classifier',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read a word describing the problem.\n2. Print ZeroDivisionError for zero, IndexError for index, KeyError for key, and StandardError for any other word.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['err = input().strip()\n'
                                       "if err == 'zero':\n"
                                       "    print('ZeroDivisionError')\n"
                                       "elif err == 'index':\n"
                                       "    print('IndexError')\n"
                                       "elif err == 'key':\n"
                                       "    print('KeyError')\n"
                                       'else:\n'
                                       "    print('StandardError')"],
                             'initial_code': '# ⚔️ Boss Challenge: Crash Predictor Engine\n'
                                             '# Step 1: Read err code:\n'
                                             'err = input().strip()\n'
                                             '\n'
                                             '# Step 2: Map error code using if/elif/else below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'scenario = input().strip()\n'
                                              "if scenario == 'zero':\n"
                                              "    print('ZeroDivisionError')\n"
                                              "elif scenario == 'index':\n"
                                              "    print('IndexError')\n"
                                              "elif scenario == 'key':\n"
                                              "    print('KeyError')\n"
                                              'else:\n'
                                              "    print('StandardError')",
                             'test_cases': [{'expected_output': 'ZeroDivisionError',
                                             'input_data': 'zero\n',
                                             'is_hidden': False},
                                            {'expected_output': 'IndexError',
                                             'input_data': 'index\n',
                                             'is_hidden': False},
                                            {'expected_output': 'KeyError',
                                             'input_data': 'key\n',
                                             'is_hidden': False},
                                            {'expected_output': 'StandardError',
                                             'input_data': 'clean\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Crash Predictor Engine',
                             'xp_reward': 150}],
             'description': 'Understand compile-time grammatical flaws versus runtime execution crashes.',
             'lesson': {'common_mistakes': [{'fix': 'First ask whether Python could parse the code; then '
                                                    'read the traceback for runtime failures.',
                                             'mistake': 'SyntaxError is not the same as NameError, '
                                                        'TypeError, or IndexError',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Different failures need different '
                                                'fixes, and the stage of failure matters. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: A syntax error stops python from '
                                                'understanding the program; an exception occurs while valid '
                                                'syntax runs. Python uses this idea to python parses source '
                                                'before execution; a traceback then points to the runtime '
                                                'line and call path\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Syntaxerror is not the same as nameerror, '
                                                'typeerror, or indexerror. If you change the example’s input '
                                                'or value, check this rule again because it can change the '
                                                'result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Python could not parse the source',
                        'id': 75,
                        'introduction': 'Why learn this? Different failures need different fixes, and the '
                                        'stage of failure matters. In this lesson, we will see a syntax '
                                        'error stops Python from understanding the program; an exception '
                                        'occurs while valid syntax runs, follow how Python handles it, and '
                                        'practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a syntax error stops Python from understanding the '
                                                'program; an exception occurs while valid syntax runs in '
                                                'your own words.',
                                                'Trace a small Syntax Errors vs Exceptions example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'SyntaxError is not the same as NameError, TypeError, or '
                                                'IndexError.'],
                        'level_id': 75,
                        'line_by_line': [{'code': 'bad_source = \'if True print("Hi")\'',
                                          'explanation': 'Store \'if True print("Hi")\' in bad_source so '
                                                         'later instructions can use it.',
                                          'line': '1'},
                                         {'code': 'try:',
                                          'explanation': 'Start the block that may fail. If a matching '
                                                         'exception happens, Python jumps to an except '
                                                         'block.',
                                          'line': '2'},
                                         {'code': "    compile(bad_source, '<lesson>', 'exec')",
                                          'explanation': 'Call compile now. Python runs its body, and any '
                                                         'returned result is available to the caller.',
                                          'line': '3'},
                                         {'code': 'except SyntaxError:',
                                          'explanation': 'Handle only a SyntaxError exception here.',
                                          'line': '4'},
                                         {'code': "    print('Python could not parse the source')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '5'}],
                        'practical_examples': [{'code': 'bad_source = \'if True print("Hi")\'\n'
                                                        'try:\n'
                                                        "    compile(bad_source, '<lesson>', 'exec')\n"
                                                        'except SyntaxError:\n'
                                                        "    print('Python could not parse the source')",
                                                'explanation': 'Purpose: A syntax error happens before '
                                                               'normal execution shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: bad_source = 'if True "
                                                               'print("Hi")\'\n'
                                                               'Store \'if True print("Hi")\' in bad_source '
                                                               'so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 2: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 3: compile(bad_source, '<lesson>', "
                                                               "'exec')\n"
                                                               'Call compile now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Line 4: except SyntaxError:\n'
                                                               'Handle only a SyntaxError exception here.\n'
                                                               '\n'
                                                               "Line 5: print('Python could not parse the "
                                                               "source')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Python could not parse the '
                                                               'source',
                                                'output': 'Python could not parse the source',
                                                'title': 'A syntax error happens before normal execution'},
                                               {'code': 'try:\n'
                                                        '    print(missing_name)\n'
                                                        'except NameError as error:\n'
                                                        '    print(type(error).__name__)',
                                                'explanation': 'Purpose: A NameError happens while valid '
                                                               'syntax runs shows the current lesson idea in '
                                                               'a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 2: print(missing_name)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: except NameError as error:\n'
                                                               'Handle only a NameError exception here. The '
                                                               'exception details are stored in error.\n'
                                                               '\n'
                                                               'Line 4: print(type(error).__name__)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: NameError',
                                                'output': 'NameError',
                                                'title': 'A NameError happens while valid syntax runs'},
                                               {'code': 'try:\n'
                                                        "    print('Age: ' + 12)\n"
                                                        'except TypeError as error:\n'
                                                        '    print(type(error).__name__)',
                                                'explanation': 'Purpose: A TypeError is a runtime exception '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 2: print('Age: ' + 12)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: except TypeError as error:\n'
                                                               'Handle only a TypeError exception here. The '
                                                               'exception details are stored in error.\n'
                                                               '\n'
                                                               'Line 4: print(type(error).__name__)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: TypeError',
                                                'output': 'TypeError',
                                                'title': 'A TypeError is a runtime exception'}],
                        'practice_questions': [{'answer': 'A syntax error stops python from understanding '
                                                          'the program; an exception occurs while valid '
                                                          'syntax runs.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Different failures need different fixes, and the '
                                                          'stage of failure matters.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Syntaxerror is not the same as nameerror, '
                                                          'typeerror, or indexerror.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is finding a missing colon '
                                           'versus a misspelled variable. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: First ask whether Python could parse the code; then read the '
                                   'traceback for runtime failures. Syntaxerror is not the same as '
                                   'nameerror, typeerror, or indexerror The practical example and its '
                                   'line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': 'bad_source = \'if True print("Hi")\'\n'
                                            'try:\n'
                                            "    compile(bad_source, '<lesson>', 'exec')\n"
                                            'except SyntaxError:\n'
                                            "    print('Python could not parse the source')",
                        'terminology': [{'definition': 'Python could not parse the source code.',
                                         'term': 'SyntaxError'},
                                        {'definition': 'A runtime problem that interrupts normal execution.',
                                         'term': 'Exception'},
                                        {'definition': 'A report showing the error and the calls that led to '
                                                       'it.',
                                         'term': 'Traceback'}],
                        'title': 'Syntax Errors vs Exceptions'},
             'number': 75,
             'quizzes': [{'explanation': '10 / 0 raises a ZeroDivisionError, which is caught and val is set '
                                         'to -1.',
                          'options': [{'explanation': 'Correct! The exception was caught and handled.',
                                       'is_correct': True,
                                       'text': '-1'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '0'},
                                      {'explanation': 'Incorrect. The exception was caught, so program '
                                                      'execution continued.',
                                       'is_correct': False,
                                       'text': 'ZeroDivisionError'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'}],
                          'question': 'What will be printed when running this try-except block?\n'
                                      '\n'
                                      'try:\n'
                                      '    val = 10 / 0\n'
                                      'except ZeroDivisionError:\n'
                                      '    val = -1\n'
                                      'print(val)'},
                         {'explanation': "No exception occurred in the try block, so the 'else' block "
                                         'executes.',
                          'options': [{'explanation': "Correct! The 'else' block runs only when no exception "
                                                      'occurs.',
                                       'is_correct': True,
                                       'text': 'Success'},
                                      {'explanation': 'Incorrect. 10 / 2 raises no error.',
                                       'is_correct': False,
                                       'text': 'Error'},
                                      {'explanation': "Incorrect. print('Success') was called.",
                                       'is_correct': False,
                                       'text': '5.0'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Success\nError'}],
                          'question': 'What is the output of the try-except-else block?\n'
                                      '\n'
                                      'try:\n'
                                      '    x = 10 / 2\n'
                                      'except ZeroDivisionError:\n'
                                      "    print('Error')\n"
                                      'else:\n'
                                      "    print('Success')"}],
             'title': 'Syntax Errors vs Exceptions'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read one line and try to turn it into a whole number.\n2. If that works, print Converted followed by the number.\n3. If it is not a whole number, print Conversion failed.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['s = input().strip()\n'
                                       'try:\n'
                                       '    val = int(s)\n'
                                       "    print(f'Converted: {val}')\n"
                                       'except ValueError:\n'
                                       "    print('Conversion failed')"],
                             'initial_code': '# Basic Exception Handling with try and except\n'
                                             '# Step 1: Read input:\n'
                                             's = input().strip()\n'
                                             '\n'
                                             '# Step 2: Write try/except block below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'raw = input().strip()\n'
                                              'try:\n'
                                              '    number = int(raw)\n'
                                              "    print(f'Converted: {number}')\n"
                                              'except ValueError:\n'
                                              "    print('Conversion failed')",
                             'test_cases': [{'expected_output': 'Converted: 25',
                                             'input_data': '25\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Conversion failed',
                                             'input_data': 'twenty-five\n',
                                             'is_hidden': False}],
                             'title': 'Bulletproof Number Converter',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. First read how many pairs to process.\n2. For each pair, divide the first whole number by the second using whole-number division.\n3. Print the answer, Cannot divide by zero, or Invalid number as appropriate.\n\nInput for this example: The Input box shows 4 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['n = int(input())\n'
                                       'for _ in range(n):\n'
                                       '    try:\n'
                                       '        a, b = [int(x) for x in input().split()]\n'
                                       '        print(a // b)\n'
                                       '    except ZeroDivisionError:\n'
                                       "        print('Division by zero error')\n"
                                       '    except ValueError:\n'
                                       "        print('Invalid input')"],
                             'initial_code': '# ⚔️ Boss Challenge: Safe Batch Division\n'
                                             '# Step 1: Read count n:\n'
                                             'n = int(input())\n'
                                             '\n'
                                             '# Step 2: Loop n times with try/except handling:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'count = int(input())\n'
                                              'for _ in range(count):\n'
                                              '    try:\n'
                                              '        a_text, b_text = input().split()\n'
                                              '        a = int(a_text)\n'
                                              '        b = int(b_text)\n'
                                              "        print(f'Result: {a // b}')\n"
                                              '    except ZeroDivisionError:\n'
                                              "        print('Cannot divide by zero')\n"
                                              '    except ValueError:\n'
                                              "        print('Invalid number')",
                             'test_cases': [{'expected_output': 'Result: 5\n'
                                                                'Cannot divide by zero\n'
                                                                'Invalid number',
                                             'input_data': '3\n10 2\n5 0\nabc 4\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Result: 25\nResult: 3',
                                             'input_data': '2\n100 4\n9 3\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Safe Batch Division',
                             'xp_reward': 150}],
             'description': 'Intercept runtime errors gracefully and prevent application crashes using try '
                            'and except blocks.',
             'lesson': {'common_mistakes': [{'fix': 'Protect the risky conversion and give a clear response '
                                                    'when it fails.',
                                             'mistake': 'only put statements that may raise the handled '
                                                        'error in the try block',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: External input can be malformed even '
                                                'when the program is written correctly. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: An exception is an event that interrupts '
                                                'normal execution. Python uses this idea to try marks risky '
                                                'statements and except handles a matching exception type\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Only put statements that may raise the '
                                                'handled error in the try block. If you change the example’s '
                                                'input or value, check this rule again because it can change '
                                                'the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Warning: Invalid integer format!',
                        'id': 76,
                        'introduction': 'Why learn this? External input can be malformed even when the '
                                        'program is written correctly. In this lesson, we will see an '
                                        'exception is an event that interrupts normal execution, follow how '
                                        'Python handles it, and practice a small example you can change '
                                        'yourself.',
                        'learning_objectives': ['Explain an exception is an event that interrupts normal '
                                                'execution in your own words.',
                                                'Trace a small Basic Exception Handling (try and except) '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: only '
                                                'put statements that may raise the handled error in the try '
                                                'block.'],
                        'level_id': 76,
                        'line_by_line': [{'code': "raw_input = 'abc'",
                                          'explanation': "Store 'abc' in raw_input so later instructions can "
                                                         'use it.',
                                          'line': '1'},
                                         {'code': 'try:',
                                          'explanation': 'Start the block that may fail. If a matching '
                                                         'exception happens, Python jumps to an except '
                                                         'block.',
                                          'line': '2'},
                                         {'code': '    val = int(raw_input)',
                                          'explanation': 'Store int(raw_input) in val so later instructions '
                                                         'can use it.',
                                          'line': '3'},
                                         {'code': "    print('Number:', val)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '4'},
                                         {'code': 'except ValueError:',
                                          'explanation': 'Handle only a ValueError exception here.',
                                          'line': '5'},
                                         {'code': "    print('Warning: Invalid integer format!')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '6'}],
                        'practical_examples': [{'code': "raw_input = 'abc'\n"
                                                        'try:\n'
                                                        '    val = int(raw_input)\n'
                                                        "    print('Number:', val)\n"
                                                        'except ValueError:\n'
                                                        "    print('Warning: Invalid integer format!')",
                                                'explanation': 'Purpose: Example 1: Safe integer parsing '
                                                               'from user input shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: raw_input = 'abc'\n"
                                                               "Store 'abc' in raw_input so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 2: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 3: val = int(raw_input)\n'
                                                               'Store int(raw_input) in val so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 4: print('Number:', val)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 5: except ValueError:\n'
                                                               'Handle only a ValueError exception here.\n'
                                                               '\n'
                                                               "Line 6: print('Warning: Invalid integer "
                                                               "format!')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Warning: Invalid integer '
                                                               'format!',
                                                'output': 'Warning: Invalid integer format!',
                                                'title': 'Example 1: Safe integer parsing from user input'},
                                               {'code': "config = {'host': 'localhost'}\n"
                                                        'try:\n'
                                                        "    port = config['port']\n"
                                                        'except KeyError:\n'
                                                        '    port = 8080\n'
                                                        "print('Server running on port:', port)",
                                                'explanation': 'Purpose: Example 2: Safe dictionary key '
                                                               'lookup shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: config = {'host': 'localhost'}\n"
                                                               "Store {'host': 'localhost'} in config so "
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               'Line 2: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 3: port = config['port']\n"
                                                               "Store config['port'] in port so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: except KeyError:\n'
                                                               'Handle only a KeyError exception here.\n'
                                                               '\n'
                                                               'Line 5: port = 8080\n'
                                                               'Store 8080 in port so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               "Line 6: print('Server running on port:', "
                                                               'port)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Server running on port: 8080',
                                                'output': 'Server running on port: 8080',
                                                'title': 'Example 2: Safe dictionary key lookup'},
                                               {'code': "queue = ['Alpha', 'Beta']\n"
                                                        'try:\n'
                                                        '    third = queue[2]\n'
                                                        'except IndexError:\n'
                                                        "    third = 'None'\n"
                                                        "print('Third in queue:', third)",
                                                'explanation': 'Purpose: Example 3: Safe list index '
                                                               'retrieval shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: queue = ['Alpha', 'Beta']\n"
                                                               'Create the list shown and store it in queue. '
                                                               'The list keeps items in order and can be '
                                                               'processed one item at a time.\n'
                                                               '\n'
                                                               'Line 2: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 3: third = queue[2]\n'
                                                               'Store queue[2] in third so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: except IndexError:\n'
                                                               'Handle only a IndexError exception here.\n'
                                                               '\n'
                                                               "Line 5: third = 'None'\n"
                                                               "Store 'None' in third so later instructions "
                                                               'can use it.\n'
                                                               '\n'
                                                               "Line 6: print('Third in queue:', third)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Third in queue: None',
                                                'output': 'Third in queue: None',
                                                'title': 'Example 3: Safe list index retrieval'}],
                        'practice_questions': [{'answer': 'An exception is an event that interrupts normal '
                                                          'execution.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'External input can be malformed even when the '
                                                          'program is written correctly.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Only put statements that may raise the handled '
                                                          'error in the try block.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is turning a typed number '
                                           'into int without crashing on letters. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Protect the risky conversion and give a clear response when it '
                                   'fails. Only put statements that may raise the handled error in the try '
                                   'block The practical example and its line-by-line walkthrough show the '
                                   'idea in action.',
                        'syntax_breakdown': "raw_input = 'abc'\n"
                                            'try:\n'
                                            '    val = int(raw_input)\n'
                                            "    print('Number:', val)\n"
                                            'except ValueError:\n'
                                            "    print('Warning: Invalid integer format!')",
                        'terminology': [{'definition': 'The block containing statements that may fail.',
                                         'term': 'try'},
                                        {'definition': 'A block that handles a matching exception.',
                                         'term': 'except'},
                                        {'definition': 'An error often raised when a value has the wrong '
                                                       'form.',
                                         'term': 'ValueError'}],
                        'title': 'Basic Exception Handling (try and except)'},
             'number': 76,
             'quizzes': [{'explanation': "int('invalid') raises ValueError. x becomes 10 in except, then "
                                         'finally adds 5: 10 + 5 = 15.',
                          'options': [{'explanation': 'Correct! finally always runs after try/except: 10 + 5 '
                                                      '= 15.',
                                       'is_correct': True,
                                       'text': '15'},
                                      {'explanation': 'Incorrect. The finally block executes afterwards.',
                                       'is_correct': False,
                                       'text': '10'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '6'},
                                      {'explanation': 'Incorrect. The ValueError was caught.',
                                       'is_correct': False,
                                       'text': 'ValueError'}],
                          'question': 'What will be printed when running this finally block?\n'
                                      '\n'
                                      'x = 1\n'
                                      'try:\n'
                                      "    x = int('invalid')\n"
                                      'except ValueError:\n'
                                      '    x = 10\n'
                                      'finally:\n'
                                      '    x += 5\n'
                                      'print(x)'},
                         {'explanation': 'The finally block runs unconditionally before exiting the '
                                         'try/except construct.',
                          'options': [{'explanation': 'Correct! finally is guaranteed to execute.',
                                       'is_correct': True,
                                       'text': 'Always, whether an exception occurred or not'},
                                      {'explanation': 'Incorrect. That is the except block.',
                                       'is_correct': False,
                                       'text': 'Only when an exception occurs'},
                                      {'explanation': 'Incorrect. That is the else block.',
                                       'is_correct': False,
                                       'text': 'Only when no exception occurs'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Only if sys.exit() is called'}],
                          'question': 'When does code inside a `finally` block execute in Python?'}],
             'title': 'Basic Exception Handling (try and except)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Look up the key the user enters in this dictionary: the key a has the value 10.\n2. Print the value, or print Key not found if the key is missing.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["d = {'a': 10}\n"
                                       'k = input().strip()\n'
                                       'try:\n'
                                       '    print(d[k])\n'
                                       'except KeyError:\n'
                                       "    print('Key not found')"],
                             'initial_code': '# Catching Specific Exceptions\n'
                                             '# Step 1: Dictionary defined:\n'
                                             "d = {'a': 10}\n"
                                             'k = input().strip()\n'
                                             '\n'
                                             '# Step 2: Try d[k] and catch KeyError below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "data = {'a': 10}\n"
                                              'key = input().strip()\n'
                                              'try:\n'
                                              '    print(data[key])\n'
                                              'except KeyError:\n'
                                              "    print('Key not found')",
                             'test_cases': [{'expected_output': '10',
                                             'input_data': 'a\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Key not found',
                                             'input_data': 'z\n',
                                             'is_hidden': False}],
                             'title': 'Safe Dictionary Lookup',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use the list 10, 20, 30.\n2. Read a whole-number position, where counting starts at zero.\n3. Print the item there, or show a different message if the position is outside the list or is not a number.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['arr = [10, 20, 30]\n'
                                       'try:\n'
                                       '    idx = int(input())\n'
                                       '    print(arr[idx])\n'
                                       'except IndexError:\n'
                                       "    print('Index out of bounds')\n"
                                       'except ValueError:\n'
                                       "    print('Not an integer')"],
                             'initial_code': '# ⚔️ Boss Challenge: Array Boundary Guard\n'
                                             'arr = [10, 20, 30]\n'
                                             '# Step 1: Try reading idx and accessing arr[idx]:\n'
                                             '\n'
                                             '# Step 2: Catch IndexError and ValueError below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'arr = [10, 20, 30]\n'
                                              'try:\n'
                                              '    index = int(input())\n'
                                              '    print(arr[index])\n'
                                              'except IndexError:\n'
                                              "    print('Index out of range')\n"
                                              'except ValueError:\n'
                                              "    print('Invalid index')",
                             'test_cases': [{'expected_output': '20',
                                             'input_data': '1\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Index out of range',
                                             'input_data': '5\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Invalid index',
                                             'input_data': 'hello\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Array Boundary Guard',
                             'xp_reward': 150}],
             'description': 'Handle distinct error conditions individually using multiple except blocks and '
                            'exception aliases.',
             'lesson': {'common_mistakes': [{'fix': 'Catch the error you expect and let unrelated '
                                                    'programming mistakes stay visible.',
                                             'mistake': 'catch specific errors before their broader parent '
                                                        'classes; avoid hiding bugs with bare except',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Different failures should produce '
                                                'different useful responses. This is the practical problem '
                                                'the feature solves.\n'
                                                '\n'
                                                'What it means: An exception class identifies a kind of '
                                                'runtime problem. Python uses this idea to python checks '
                                                'except clauses from top to bottom and runs the first '
                                                'matching one\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Catch specific errors before their broader '
                                                'parent classes; avoid hiding bugs with bare except. If you '
                                                'change the example’s input or value, check this rule again '
                                                'because it can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Bad input format\nDivision by zero',
                        'id': 77,
                        'introduction': 'Why learn this? Different failures should produce different useful '
                                        'responses. In this lesson, we will see an exception class '
                                        'identifies a kind of runtime problem, follow how Python handles it, '
                                        'and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain an exception class identifies a kind of runtime '
                                                'problem in your own words.',
                                                'Trace a small Catching Specific Exceptions example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'catch specific errors before their broader parent classes; '
                                                'avoid hiding bugs with bare except.'],
                        'level_id': 77,
                        'line_by_line': [{'code': 'def process(val_str, div):',
                                          'explanation': 'Define a function named process. Its parameters '
                                                         '(val_str, div) are local names that receive values '
                                                         'when the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '1'},
                                         {'code': '    try:',
                                          'explanation': 'Start the block that may fail. If a matching '
                                                         'exception happens, Python jumps to an except '
                                                         'block.',
                                          'line': '2'},
                                         {'code': '        num = float(val_str)',
                                          'explanation': 'Store float(val_str) in num so later instructions '
                                                         'can use it.',
                                          'line': '3'},
                                         {'code': '        return num / div',
                                          'explanation': 'Send num / div back to the caller and end this '
                                                         'function call.',
                                          'line': '4'},
                                         {'code': '    except ValueError:',
                                          'explanation': 'Handle only a ValueError exception here.',
                                          'line': '5'},
                                         {'code': "        return 'Bad input format'",
                                          'explanation': "Send 'Bad input format' back to the caller and end "
                                                         'this function call.',
                                          'line': '6'},
                                         {'code': '    except ZeroDivisionError:',
                                          'explanation': 'Handle only a ZeroDivisionError exception here.',
                                          'line': '7'},
                                         {'code': "        return 'Division by zero'",
                                          'explanation': "Send 'Division by zero' back to the caller and end "
                                                         'this function call.',
                                          'line': '8'},
                                         {'code': "print(process('forty', 2))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '9'},
                                         {'code': "print(process('40', 0))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '10'}],
                        'practical_examples': [{'code': 'def process(val_str, div):\n'
                                                        '    try:\n'
                                                        '        num = float(val_str)\n'
                                                        '        return num / div\n'
                                                        '    except ValueError:\n'
                                                        "        return 'Bad input format'\n"
                                                        '    except ZeroDivisionError:\n'
                                                        "        return 'Division by zero'\n"
                                                        "print(process('forty', 2))\n"
                                                        "print(process('40', 0))",
                                                'explanation': 'Purpose: Example 1: Differentiating '
                                                               'ValueError vs ZeroDivisionError shows the '
                                                               'current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def process(val_str, div):\n'
                                                               'Define a function named process. Its '
                                                               'parameters (val_str, div) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 3: num = float(val_str)\n'
                                                               'Store float(val_str) in num so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: return num / div\n'
                                                               'Send num / div back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 5: except ValueError:\n'
                                                               'Handle only a ValueError exception here.\n'
                                                               '\n'
                                                               "Line 6: return 'Bad input format'\n"
                                                               "Send 'Bad input format' back to the caller "
                                                               'and end this function call.\n'
                                                               '\n'
                                                               'Line 7: except ZeroDivisionError:\n'
                                                               'Handle only a ZeroDivisionError exception '
                                                               'here.\n'
                                                               '\n'
                                                               "Line 8: return 'Division by zero'\n"
                                                               "Send 'Division by zero' back to the caller "
                                                               'and end this function call.\n'
                                                               '\n'
                                                               "Line 9: print(process('forty', 2))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 10: print(process('40', 0))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Bad input format\n'
                                                               'Division by zero',
                                                'output': 'Bad input format\nDivision by zero',
                                                'title': 'Example 1: Differentiating ValueError vs '
                                                         'ZeroDivisionError'},
                                               {'code': 'try:\n'
                                                        "    with open('nonexistent_file.xyz') as f:\n"
                                                        '        content = f.read()\n'
                                                        'except FileNotFoundError as err:\n'
                                                        "    print(f'System reported: {err.strerror}')",
                                                'explanation': 'Purpose: Example 2: Storing exception '
                                                               "details with 'as e' shows the current lesson "
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 2: with open('nonexistent_file.xyz') as "
                                                               'f:\n'
                                                               'Enter a managed block for '
                                                               "open('nonexistent_file.xyz') and call the "
                                                               'open resource f. When the indented block '
                                                               'ends, Python closes the resource '
                                                               'automatically.\n'
                                                               '\n'
                                                               'Line 3: content = f.read()\n'
                                                               'Store f.read() in content so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: except FileNotFoundError as err:\n'
                                                               'Handle only a FileNotFoundError exception '
                                                               'here. The exception details are stored in '
                                                               'err.\n'
                                                               '\n'
                                                               "Line 5: print(f'System reported: "
                                                               "{err.strerror}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: System reported: No such file '
                                                               'or directory',
                                                'output': 'System reported: No such file or directory',
                                                'title': "Example 2: Storing exception details with 'as e'"},
                                               {'code': 'try:\n'
                                                        "    data = int('abc')\n"
                                                        'except (ValueError, TypeError) as e:\n'
                                                        "    print('Caught data conversion error!')",
                                                'explanation': 'Purpose: Example 3: Grouping related '
                                                               'exceptions into a tuple shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 2: data = int('abc')\n"
                                                               "Store int('abc') in data so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 3: except (ValueError, TypeError) as '
                                                               'e:\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 4: print('Caught data conversion "
                                                               "error!')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Caught data conversion error!',
                                                'output': 'Caught data conversion error!',
                                                'title': 'Example 3: Grouping related exceptions into a '
                                                         'tuple'}],
                        'practice_questions': [{'answer': 'An exception class identifies a kind of runtime '
                                                          'problem.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Different failures should produce different '
                                                          'useful responses.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Catch specific errors before their broader parent '
                                                          'classes; avoid hiding bugs with bare except.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is showing separate messages '
                                           'for invalid numbers and missing files. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Catch the error you expect and let unrelated programming '
                                   'mistakes stay visible. Catch specific errors before their broader parent '
                                   'classes; avoid hiding bugs with bare except The practical example and '
                                   'its line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': 'def process(val_str, div):\n'
                                            '    try:\n'
                                            '        num = float(val_str)\n'
                                            '        return num / div\n'
                                            '    except ValueError:\n'
                                            "        return 'Bad input format'\n"
                                            '    except ZeroDivisionError:\n'
                                            "        return 'Division by zero'\n"
                                            "print(process('forty', 2))\n"
                                            "print(process('40', 0))",
                        'terminology': [{'definition': 'A class identifying a category of error.',
                                         'term': 'Exception type'},
                                        {'definition': 'An except block for one expected error type.',
                                         'term': 'Specific handler'},
                                        {'definition': 'Parent and child relationships between error '
                                                       'classes.',
                                         'term': 'Exception hierarchy'}],
                        'title': 'Catching Specific Exceptions'},
             'number': 77,
             'quizzes': [{'explanation': 'Calling set_age(-5) satisfies age < 0, raising a ValueError.',
                          'options': [{'explanation': 'Correct! raise explicitly throws the specified '
                                                      'ValueError.',
                                       'is_correct': True,
                                       'text': 'ValueError: Age cannot be negative'},
                                      {'explanation': 'Incorrect. -5 is a valid int.',
                                       'is_correct': False,
                                       'text': 'TypeError'},
                                      {'explanation': 'Incorrect. An exception is raised before returning.',
                                       'is_correct': False,
                                       'text': '-5'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'AssertionError'}],
                          'question': 'What exception is raised by the following function call?\n'
                                      '\n'
                                      'def set_age(age):\n'
                                      '    if age < 0:\n'
                                      "        raise ValueError('Age cannot be negative')\n"
                                      '    return age\n'
                                      '\n'
                                      'set_age(-5)'},
                         {'explanation': "The 'raise' keyword throws exceptions in Python.",
                          'options': [{'explanation': "Correct! 'raise Exception(...)' throws an exception.",
                                       'is_correct': True,
                                       'text': 'raise'},
                                      {'explanation': "Incorrect. 'throw' is Java/C++/JavaScript syntax.",
                                       'is_correct': False,
                                       'text': 'throw'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'trigger'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'catch'}],
                          'question': 'Which keyword is used to manually trigger an exception in Python '
                                      'code?'}],
             'title': 'Catching Specific Exceptions'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a whole number and try to divide 100 by it.\n2. If it is zero, print Cannot divide by zero.\n3. Otherwise print Division successful.\n4. Always print Cleanup complete at the end.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['try:\n'
                                       '    n = int(input())\n'
                                       '    print(100 // n)\n'
                                       'except ZeroDivisionError:\n'
                                       "    print('Cannot divide by zero')\n"
                                       'else:\n'
                                       "    print('Division successful')\n"
                                       'finally:\n'
                                       "    print('Cleanup complete')"],
                             'initial_code': '# Complete Exception Lifecycle: try/except/else/finally\n'
                                             '# Step 1: Read n:\n'
                                             'n = int(input())\n'
                                             '\n'
                                             '# Step 2: Implement full 4-part block below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'n = int(input())\n'
                                              'try:\n'
                                              '    result = 100 // n\n'
                                              'except ZeroDivisionError:\n'
                                              "    print('Cannot divide by zero')\n"
                                              'else:\n'
                                              "    print('Division successful')\n"
                                              'finally:\n'
                                              "    print('Cleanup complete')",
                             'test_cases': [{'expected_output': 'Division successful\nCleanup complete',
                                             'input_data': '5\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Cannot divide by zero\nCleanup complete',
                                             'input_data': '0\n',
                                             'is_hidden': False}],
                             'title': 'Complete Exception Lifecycle',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read text and try to turn it into a whole number.\n2. Print Parsed with the number if it works, or Failed to parse if it does not.\n3. Always print Audit logged at the end.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['try:\n'
                                       '    s = input().strip()\n'
                                       '    n = int(s)\n'
                                       'except ValueError:\n'
                                       "    print('Failed to parse')\n"
                                       'else:\n'
                                       "    print(f'Parsed: {n}')\n"
                                       'finally:\n'
                                       "    print('Audit logged')"],
                             'initial_code': '# ⚔️ Boss Challenge: Audit Trail Parser\n'
                                             '# Step 1: Read s:\n'
                                             's = input().strip()\n'
                                             '\n'
                                             '# Step 2: Try int(s), except ValueError, else, finally:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'text = input().strip()\n'
                                              'try:\n'
                                              '    number = int(text)\n'
                                              'except ValueError:\n'
                                              "    print('Failed to parse')\n"
                                              'else:\n'
                                              "    print(f'Parsed: {number}')\n"
                                              'finally:\n'
                                              "    print('Audit logged')",
                             'test_cases': [{'expected_output': 'Parsed: 42\nAudit logged',
                                             'input_data': '42\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Failed to parse\nAudit logged',
                                             'input_data': 'not-a-number\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Audit Trail Parser',
                             'xp_reward': 150}],
             'description': 'Execute success-only operations with else and guaranteed cleanup with finally.',
             'lesson': {'common_mistakes': [{'fix': 'else means success; finally means cleanup either way.',
                                             'mistake': 'finally is for cleanup, not a place to hide or '
                                                        'overwrite the original error',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Programs often need a success path '
                                                'and cleanup regardless of success. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: Else runs when try finishes without an '
                                                'exception; finally runs during normal or exceptional flow. '
                                                'Python uses this idea to order is try, then except if '
                                                'needed or else if successful, and finally in either case\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Finally is for cleanup, not a place to hide '
                                                'or overwrite the original error. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Performing query...\nDatabase connection closed safely.',
                        'id': 78,
                        'introduction': 'Why learn this? Programs often need a success path and cleanup '
                                        'regardless of success. In this lesson, we will see else runs when '
                                        'try finishes without an exception; finally runs during normal or '
                                        'exceptional flow, follow how Python handles it, and practice a '
                                        'small example you can change yourself.',
                        'learning_objectives': ['Explain else runs when try finishes without an exception; '
                                                'finally runs during normal or exceptional flow in your own '
                                                'words.',
                                                'Trace a small The else and finally Blocks example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'finally is for cleanup, not a place to hide or overwrite '
                                                'the original error.'],
                        'level_id': 78,
                        'line_by_line': [{'code': 'connection_open = True',
                                          'explanation': 'Store True in connection_open so later '
                                                         'instructions can use it.',
                                          'line': '1'},
                                         {'code': 'try:',
                                          'explanation': 'Start the block that may fail. If a matching '
                                                         'exception happens, Python jumps to an except '
                                                         'block.',
                                          'line': '2'},
                                         {'code': "    print('Performing query...')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'},
                                         {'code': 'finally:',
                                          'explanation': 'This block runs after try/except whether the '
                                                         'protected work succeeded or failed, so it is '
                                                         'useful for cleanup.',
                                          'line': '4'},
                                         {'code': '    connection_open = False',
                                          'explanation': 'Store False in connection_open so later '
                                                         'instructions can use it.',
                                          'line': '5'},
                                         {'code': "    print('Database connection closed safely.')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '6'}],
                        'practical_examples': [{'code': 'connection_open = True\n'
                                                        'try:\n'
                                                        "    print('Performing query...')\n"
                                                        'finally:\n'
                                                        '    connection_open = False\n'
                                                        "    print('Database connection closed safely.')",
                                                'explanation': 'Purpose: Example 1: Safe resource release '
                                                               'with finally shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: connection_open = True\n'
                                                               'Store True in connection_open so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 2: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 3: print('Performing query...')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: finally:\n'
                                                               'This block runs after try/except whether the '
                                                               'protected work succeeded or failed, so it is '
                                                               'useful for cleanup.\n'
                                                               '\n'
                                                               'Line 5: connection_open = False\n'
                                                               'Store False in connection_open so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 6: print('Database connection closed "
                                                               "safely.')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Performing query...\n'
                                                               'Database connection closed safely.',
                                                'output': 'Performing query...\n'
                                                          'Database connection closed safely.',
                                                'title': 'Example 1: Safe resource release with finally'},
                                               {'code': 'try:\n'
                                                        "    count = int('45')\n"
                                                        'except ValueError:\n'
                                                        "    print('Parse failed')\n"
                                                        'else:\n'
                                                        "    print('Data parsed successfully! Value "
                                                        "doubled:', count * 2)",
                                                'explanation': 'Purpose: Example 2: Successful workflow '
                                                               'branch with else shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 2: count = int('45')\n"
                                                               "Store int('45') in count so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 3: except ValueError:\n'
                                                               'Handle only a ValueError exception here.\n'
                                                               '\n'
                                                               "Line 4: print('Parse failed')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 5: else:\n'
                                                               'For try/except, this block runs only when '
                                                               'the try block had no exception.\n'
                                                               '\n'
                                                               "Line 6: print('Data parsed successfully! "
                                                               "Value doubled:', count * 2)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Data parsed successfully! '
                                                               'Value doubled: 90',
                                                'output': 'Data parsed successfully! Value doubled: 90',
                                                'title': 'Example 2: Successful workflow branch with else'},
                                               {'code': 'def transfer(amount):\n'
                                                        '    try:\n'
                                                        "        print(f'Initiating transfer of ${amount}')\n"
                                                        '    except Exception as e:\n'
                                                        "        print('Transfer failed:', e)\n"
                                                        '    else:\n'
                                                        "        print('Transfer authorized.')\n"
                                                        '    finally:\n'
                                                        "        print('Audit trail entry written.')\n"
                                                        'transfer(250)',
                                                'explanation': 'Purpose: Example 3: Full four-part exception '
                                                               'audit trail shows the current lesson idea in '
                                                               'a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def transfer(amount):\n'
                                                               'Define a function named transfer. Its '
                                                               'parameters (amount) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 3: print(f'Initiating transfer of "
                                                               "${amount}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: except Exception as e:\n'
                                                               'Handle only a Exception exception here. The '
                                                               'exception details are stored in e.\n'
                                                               '\n'
                                                               "Line 5: print('Transfer failed:', e)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 6: else:\n'
                                                               'For try/except, this block runs only when '
                                                               'the try block had no exception.\n'
                                                               '\n'
                                                               "Line 7: print('Transfer authorized.')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 8: finally:\n'
                                                               'This block runs after try/except whether the '
                                                               'protected work succeeded or failed, so it is '
                                                               'useful for cleanup.\n'
                                                               '\n'
                                                               "Line 9: print('Audit trail entry written.')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 10: transfer(250)\n'
                                                               'Call transfer now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Initiating transfer of $250\n'
                                                               'Transfer authorized.\n'
                                                               'Audit trail entry written.',
                                                'output': 'Initiating transfer of $250\n'
                                                          'Transfer authorized.\n'
                                                          'Audit trail entry written.',
                                                'title': 'Example 3: Full four-part exception audit trail'}],
                        'practice_questions': [{'answer': 'Else runs when try finishes without an exception; '
                                                          'finally runs during normal or exceptional flow.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Programs often need a success path and cleanup '
                                                          'regardless of success.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Finally is for cleanup, not a place to hide or '
                                                          'overwrite the original error.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is closing a resource or '
                                           'reporting success after parsing. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: else means success; finally means cleanup either way. Finally '
                                   'is for cleanup, not a place to hide or overwrite the original error The '
                                   'practical example and its line-by-line walkthrough show the idea in '
                                   'action.',
                        'syntax_breakdown': 'connection_open = True\n'
                                            'try:\n'
                                            "    print('Performing query...')\n"
                                            'finally:\n'
                                            '    connection_open = False\n'
                                            "    print('Database connection closed safely.')",
                        'terminology': [{'definition': 'Runs after try only when no exception occurred.',
                                         'term': 'else block'},
                                        {'definition': 'Runs after try/except whether work succeeds or '
                                                       'fails.',
                                         'term': 'finally block'},
                                        {'definition': 'Closing or releasing a resource after use.',
                                         'term': 'Cleanup'}],
                        'title': 'The else and finally Blocks'},
             'number': 78,
             'quizzes': [{'explanation': 'The with statement automatically closes the file object upon '
                                         'exiting the block. f.closed is True.',
                          'options': [{'explanation': "Correct! 'with' ensures automatic resource closure.",
                                       'is_correct': True,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect. The context manager closes the file on '
                                                      'exit.',
                                       'is_correct': False,
                                       'text': 'False'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect. closed is a valid file attribute.',
                                       'is_correct': False,
                                       'text': 'AttributeError'}],
                          'question': 'What is the output of the file context manager test?\n'
                                      '\n'
                                      "with open('temp.txt', 'w') as f:\n"
                                      "    f.write('Hello')\n"
                                      'print(f.closed)'},
                         {'explanation': "'w' mode creates a new file or overwrites an existing file.",
                          'options': [{'explanation': "Correct! 'w' truncates existing files or creates new "
                                                      'ones.',
                                       'is_correct': True,
                                       'text': "'w' (write mode)"},
                                      {'explanation': "Incorrect. 'a' preserves existing content and writes "
                                                      'at the end.',
                                       'is_correct': False,
                                       'text': "'a' (append mode)"},
                                      {'explanation': "Incorrect. 'r' is read-only.",
                                       'is_correct': False,
                                       'text': "'r' (read mode)"},
                                      {'explanation': "Incorrect. 'x' fails if the file exists.",
                                       'is_correct': False,
                                       'text': "'x' (exclusive mode)"}],
                          'question': 'Which file open mode overwrites an existing file if it already '
                                      'exists?'}],
             'title': 'The else and finally Blocks'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read an age.\n2. If it is below zero, raise a ValueError with the message Age cannot be negative.\n3. Otherwise print Valid age followed by the age.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['age = int(input())\n'
                                       'if age < 0:\n'
                                       "    raise ValueError('Age cannot be negative')\n"
                                       "print(f'Valid age: {age}')"],
                             'initial_code': '# The raise Keyword: Triggering Errors Intentionally\n'
                                             '# Step 1: Read age:\n'
                                             'age = int(input())\n'
                                             '\n'
                                             '# Step 2: Validate age and raise ValueError if negative:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'age = int(input())\n'
                                              'if age < 0:\n'
                                              "    raise ValueError('Age cannot be negative')\n"
                                              "print(f'Valid age: {age}')",
                             'test_cases': [{'expected_output': 'Valid age: 10',
                                             'input_data': '10\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Valid age: 0',
                                             'input_data': '0\n',
                                             'is_hidden': False}],
                             'title': 'Input Validation Guard',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write set_percentage to accept numbers from 0 through 100, including both ends.\n2. For a number outside that range, raise a ValueError.\n3. Catch the error and print Caught followed by its message for a valid number, print the percentage.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def set_percentage(p):\n'
                                       '    if p < 0 or p > 100:\n'
                                       "        raise ValueError('Invalid percentage')\n"
                                       "    return f'{p}%'\n"
                                       'try:\n'
                                       '    val = int(input())\n'
                                       '    print(set_percentage(val))\n'
                                       'except ValueError as e:\n'
                                       "    print(f'Caught: {e}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Bounded Percentage Validator\n'
                                             '# Step 1: Define set_percentage(p):\n'
                                             '\n'
                                             '# Step 2: Read val and try/except call below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def set_percentage(p):\n'
                                              '    if p < 0 or p > 100:\n'
                                              "        raise ValueError('Invalid percentage')\n"
                                              '    return p\n'
                                              '\n'
                                              'try:\n'
                                              '    value = float(input())\n'
                                              "    print(f'Percentage: {set_percentage(value):g}')\n"
                                              'except ValueError as error:\n'
                                              "    print(f'Caught: {error}')",
                             'test_cases': [{'expected_output': 'Percentage: 50',
                                             'input_data': '50\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Percentage: 0',
                                             'input_data': '0\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Percentage: 100',
                                             'input_data': '100\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Caught: Invalid percentage',
                                             'input_data': '101\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Bounded Percentage Validator',
                             'xp_reward': 150}],
             'description': 'Trigger explicit runtime errors using raise to enforce business logic and '
                            'invariants.',
             'lesson': {'common_mistakes': [{'fix': 'Validate inputs, raise a meaningful error, and handle '
                                                    'it at the right level.',
                                             'mistake': 'raise is different from print; custom exception '
                                                        'classes are useful only for named domain errors',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A function can stop invalid data '
                                                'before it damages later work. This is the practical problem '
                                                'the feature solves.\n'
                                                '\n'
                                                'What it means: Raise deliberately creates an exception and '
                                                'transfers control to the caller. Python uses this idea to '
                                                'choose a fitting exception, include a helpful message, and '
                                                'let a caller handle it\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Raise is different from print; custom '
                                                'exception classes are useful only for named domain errors. '
                                                'If you change the example’s input or value, check this rule '
                                                'again because it can change the result or the path Python '
                                                'takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Validation blocked transaction: Withdrawal amount must be '
                                           'positive!',
                        'id': 79,
                        'introduction': 'Why learn this? A function can stop invalid data before it damages '
                                        'later work. In this lesson, we will see raise deliberately creates '
                                        'an exception and transfers control to the caller, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain raise deliberately creates an exception and '
                                                'transfers control to the caller in your own words.',
                                                'Trace a small Raising Exceptions (The raise Keyword) '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'raise is different from print; custom exception classes are '
                                                'useful only for named domain errors.'],
                        'level_id': 79,
                        'line_by_line': [{'code': 'def withdraw(balance, amount):',
                                          'explanation': 'Define a function named withdraw. Its parameters '
                                                         '(balance, amount) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '1'},
                                         {'code': '    if amount <= 0:',
                                          'explanation': 'Check whether amount <= 0 is true. If it is, run '
                                                         'the indented block; otherwise Python skips that '
                                                         'block.',
                                          'line': '2'},
                                         {'code': "        raise ValueError('Withdrawal amount must be "
                                                  "positive!')",
                                          'explanation': "Stop this path by raising ValueError('Withdrawal "
                                                         "amount must be positive!'). Python passes that "
                                                         'error to the caller unless a matching except block '
                                                         'handles it.',
                                          'line': '3'},
                                         {'code': '    if amount > balance:',
                                          'explanation': 'Check whether amount > balance is true. If it is, '
                                                         'run the indented block; otherwise Python skips '
                                                         'that block.',
                                          'line': '4'},
                                         {'code': "        raise RuntimeError('Insufficient funds!')",
                                          'explanation': 'Stop this path by raising '
                                                         "RuntimeError('Insufficient funds!'). Python passes "
                                                         'that error to the caller unless a matching except '
                                                         'block handles it.',
                                          'line': '5'},
                                         {'code': '    return balance - amount',
                                          'explanation': 'Send balance - amount back to the caller and end '
                                                         'this function call.',
                                          'line': '6'},
                                         {'code': 'try:',
                                          'explanation': 'Start the block that may fail. If a matching '
                                                         'exception happens, Python jumps to an except '
                                                         'block.',
                                          'line': '7'},
                                         {'code': '    withdraw(100, -20)',
                                          'explanation': 'Call withdraw now. Python runs its body, and any '
                                                         'returned result is available to the caller.',
                                          'line': '8'},
                                         {'code': 'except ValueError as e:',
                                          'explanation': 'Handle only a ValueError exception here. The '
                                                         'exception details are stored in e.',
                                          'line': '9'},
                                         {'code': "    print('Validation blocked transaction:', e)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '10'}],
                        'practical_examples': [{'code': 'def withdraw(balance, amount):\n'
                                                        '    if amount <= 0:\n'
                                                        "        raise ValueError('Withdrawal amount must be "
                                                        "positive!')\n"
                                                        '    if amount > balance:\n'
                                                        "        raise RuntimeError('Insufficient funds!')\n"
                                                        '    return balance - amount\n'
                                                        'try:\n'
                                                        '    withdraw(100, -20)\n'
                                                        'except ValueError as e:\n'
                                                        "    print('Validation blocked transaction:', e)",
                                                'explanation': 'Purpose: Example 1: Enforcing positive bank '
                                                               'withdrawal amounts shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def withdraw(balance, amount):\n'
                                                               'Define a function named withdraw. Its '
                                                               'parameters (balance, amount) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: if amount <= 0:\n'
                                                               'Check whether amount <= 0 is true. If it is, '
                                                               'run the indented block; otherwise Python '
                                                               'skips that block.\n'
                                                               '\n'
                                                               "Line 3: raise ValueError('Withdrawal amount "
                                                               "must be positive!')\n"
                                                               'Stop this path by raising '
                                                               "ValueError('Withdrawal amount must be "
                                                               "positive!'). Python passes that error to the "
                                                               'caller unless a matching except block '
                                                               'handles it.\n'
                                                               '\n'
                                                               'Line 4: if amount > balance:\n'
                                                               'Check whether amount > balance is true. If '
                                                               'it is, run the indented block; otherwise '
                                                               'Python skips that block.\n'
                                                               '\n'
                                                               "Line 5: raise RuntimeError('Insufficient "
                                                               "funds!')\n"
                                                               'Stop this path by raising '
                                                               "RuntimeError('Insufficient funds!'). Python "
                                                               'passes that error to the caller unless a '
                                                               'matching except block handles it.\n'
                                                               '\n'
                                                               'Line 6: return balance - amount\n'
                                                               'Send balance - amount back to the caller and '
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 7: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 8: withdraw(100, -20)\n'
                                                               'Call withdraw now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Line 9: except ValueError as e:\n'
                                                               'Handle only a ValueError exception here. The '
                                                               'exception details are stored in e.\n'
                                                               '\n'
                                                               "Line 10: print('Validation blocked "
                                                               "transaction:', e)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Validation blocked '
                                                               'transaction: Withdrawal amount must be '
                                                               'positive!',
                                                'output': 'Validation blocked transaction: Withdrawal amount '
                                                          'must be positive!',
                                                'title': 'Example 1: Enforcing positive bank withdrawal '
                                                         'amounts'},
                                               {'code': 'def register(username):\n'
                                                        '    if len(username) < 3:\n'
                                                        "        raise ValueError('Username must be at least "
                                                        "3 characters long')\n"
                                                        "    return f'User {username} registered.'\n"
                                                        'try:\n'
                                                        "    print(register('ab'))\n"
                                                        'except ValueError as e:\n'
                                                        "    print('Error:', e)",
                                                'explanation': 'Purpose: Example 2: Validating string '
                                                               'lengths shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def register(username):\n'
                                                               'Define a function named register. Its '
                                                               'parameters (username) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: if len(username) < 3:\n'
                                                               'Check whether len(username) < 3 is true. If '
                                                               'it is, run the indented block; otherwise '
                                                               'Python skips that block.\n'
                                                               '\n'
                                                               "Line 3: raise ValueError('Username must be "
                                                               "at least 3 characters long')\n"
                                                               'Stop this path by raising '
                                                               "ValueError('Username must be at least 3 "
                                                               "characters long'). Python passes that error "
                                                               'to the caller unless a matching except block '
                                                               'handles it.\n'
                                                               '\n'
                                                               "Line 4: return f'User {username} "
                                                               "registered.'\n"
                                                               "Send f'User {username} registered.' back to "
                                                               'the caller and end this function call.\n'
                                                               '\n'
                                                               'Line 5: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 6: print(register('ab'))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 7: except ValueError as e:\n'
                                                               'Handle only a ValueError exception here. The '
                                                               'exception details are stored in e.\n'
                                                               '\n'
                                                               "Line 8: print('Error:', e)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Error: Username must be at '
                                                               'least 3 characters long',
                                                'output': 'Error: Username must be at least 3 characters '
                                                          'long',
                                                'title': 'Example 2: Validating string lengths'},
                                               {'code': 'class InventoryDepletedError(Exception):\n'
                                                        '    pass\n'
                                                        'def consume_potion(count):\n'
                                                        '    if count <= 0:\n'
                                                        "        raise InventoryDepletedError('No potions "
                                                        "remaining in pouch!')\n"
                                                        '    return count - 1\n'
                                                        'try:\n'
                                                        '    consume_potion(0)\n'
                                                        'except InventoryDepletedError as e:\n'
                                                        "    print('Alert:', e)",
                                                'explanation': 'Purpose: Example 3: Custom domain exception '
                                                               'class shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class '
                                                               'InventoryDepletedError(Exception):\n'
                                                               'Define the class InventoryDepletedError. '
                                                               'This is the blueprint for instances; the '
                                                               'indented lines below describe its data or '
                                                               'behavior. It inherits from Exception.\n'
                                                               '\n'
                                                               'Line 2: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: def consume_potion(count):\n'
                                                               'Define a function named consume_potion. Its '
                                                               'parameters (count) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 4: if count <= 0:\n'
                                                               'Check whether count <= 0 is true. If it is, '
                                                               'run the indented block; otherwise Python '
                                                               'skips that block.\n'
                                                               '\n'
                                                               "Line 5: raise InventoryDepletedError('No "
                                                               "potions remaining in pouch!')\n"
                                                               'Stop this path by raising '
                                                               "InventoryDepletedError('No potions remaining "
                                                               "in pouch!'). Python passes that error to the "
                                                               'caller unless a matching except block '
                                                               'handles it.\n'
                                                               '\n'
                                                               'Line 6: return count - 1\n'
                                                               'Send count - 1 back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 7: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 8: consume_potion(0)\n'
                                                               'Call consume_potion now. Python runs its '
                                                               'body, and any returned result is available '
                                                               'to the caller.\n'
                                                               '\n'
                                                               'Line 9: except InventoryDepletedError as e:\n'
                                                               'Handle only a InventoryDepletedError '
                                                               'exception here. The exception details are '
                                                               'stored in e.\n'
                                                               '\n'
                                                               "Line 10: print('Alert:', e)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Alert: No potions remaining in '
                                                               'pouch!',
                                                'output': 'Alert: No potions remaining in pouch!',
                                                'title': 'Example 3: Custom domain exception class'}],
                        'practice_questions': [{'answer': 'Raise deliberately creates an exception and '
                                                          'transfers control to the caller.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A function can stop invalid data before it '
                                                          'damages later work.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Raise is different from print; custom exception '
                                                          'classes are useful only for named domain errors.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is rejecting a negative '
                                           'withdrawal before changing an account. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Validate inputs, raise a meaningful error, and handle it at '
                                   'the right level. Raise is different from print; custom exception classes '
                                   'are useful only for named domain errors The practical example and its '
                                   'line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': 'def withdraw(balance, amount):\n'
                                            '    if amount <= 0:\n'
                                            "        raise ValueError('Withdrawal amount must be "
                                            "positive!')\n"
                                            '    if amount > balance:\n'
                                            "        raise RuntimeError('Insufficient funds!')\n"
                                            '    return balance - amount\n'
                                            'try:\n'
                                            '    withdraw(100, -20)\n'
                                            'except ValueError as e:\n'
                                            "    print('Validation blocked transaction:', e)",
                        'terminology': [{'definition': 'The keyword that deliberately signals an exception.',
                                         'term': 'raise'},
                                        {'definition': 'Checking that a value meets the rules before '
                                                       'continuing.',
                                         'term': 'Validation'},
                                        {'definition': 'A named exception class for a meaningful '
                                                       'application-specific failure.',
                                         'term': 'Custom exception'}],
                        'title': 'Raising Exceptions (The raise Keyword)'},
             'number': 79,
             'quizzes': [{'explanation': '.strip() removes trailing whitespace and newline characters from '
                                         'each string.',
                          'options': [{'explanation': 'Correct! .strip() strips \\n from all items.',
                                       'is_correct': True,
                                       'text': "['Hero', 'Mage', 'Rogue']"},
                                      {'explanation': 'Incorrect. strip() removes the newlines.',
                                       'is_correct': False,
                                       'text': "['Hero\\n', 'Mage\\n', 'Rogue\\n']"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "'Hero Mage Rogue'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': "['Hero']"}],
                          'question': 'What is the output of stripping newline characters from lines?\n'
                                      '\n'
                                      "raw_lines = ['Hero\\n', 'Mage\\n', 'Rogue\\n']\n"
                                      'clean = [line.strip() for line in raw_lines]\n'
                                      'print(clean)'},
                         {'explanation': 'read() returns the entire contents as a single string; readlines() '
                                         'returns a list of line strings.',
                          'options': [{'explanation': 'Correct! read() -> str, readlines() -> list[str].',
                                       'is_correct': True,
                                       'text': 'read() returns a string; readlines() returns a list of '
                                               'strings'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Both return identical lists'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'read() returns a list; readlines() returns a string'},
                                      {'explanation': 'Incorrect in text mode.',
                                       'is_correct': False,
                                       'text': 'read() returns bytes; readlines() returns characters'}],
                          'question': 'What does file.read() return versus file.readlines()?'}],
             'title': 'Raising Exceptions (The raise Keyword)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use an in-memory text stream for this browser exercise.\n2. Read each line and print it without its ending newline.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['from io import StringIO\n'
                                       "with StringIO('First note\\nSecond note') as notes:\n"
                                       '    for line in notes:\n'
                                       '        print(line.strip())'],
                             'initial_code': '# Custom Exception Classes\n'
                                             '# Step 1: Define class InsufficientFundsError(Exception): '
                                             'pass\n'
                                             '\n'
                                             '# Step 2: Test withdrawal and catch error below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'from io import StringIO\n'
                                              "with StringIO('First note\\nSecond note') as notes:\n"
                                              '    for line in notes:\n'
                                              '        print(line.strip())',
                             'test_cases': [{'expected_output': 'First note\nSecond note',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Read a Text File Line by Line',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read the three lines from an in-memory text stream.\n2. Print each line and then the number of lines read.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['from io import StringIO\n'
                                       "notes = StringIO('Map the route\\nPack supplies\\nStart the quest')\n"
                                       'lines = [line.strip() for line in notes]\n'
                                       'for line in lines:\n'
                                       '    print(line)\n'
                                       "print('Line count:', len(lines))"],
                             'initial_code': '# ⚔️ Boss Challenge: Game Level Boundary Exception\n'
                                             '# Step 1: Define InvalidLevelError:\n'
                                             '\n'
                                             '# Step 2: Define check_level(lvl) and handle exception:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'from io import StringIO\n'
                                              "notes = StringIO('Map the route\\nPack supplies\\nStart the "
                                              "quest')\n"
                                              'lines = [line.strip() for line in notes]\n'
                                              'for line in lines:\n'
                                              '    print(line)\n'
                                              "print('Line count:', len(lines))",
                             'test_cases': [{'expected_output': 'Map the route\n'
                                                                'Pack supplies\n'
                                                                'Start the quest\n'
                                                                'Line count: 3',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Read and Count Lines',
                             'xp_reward': 150}],
             'description': 'Read external text files into Python memory using open(), read(), and '
                            'readlines().',
             'lesson': {'common_mistakes': [{'fix': 'Read text using a clear path, encoding, and a suitable '
                                                    'way to consume its lines.',
                                             'mistake': 'missing paths raise FileNotFoundError; read() loads '
                                                        'all text and may be costly for large files',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Reading a file lets a program use '
                                                'information saved beyond one run. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: A file handle is python’s connection to an '
                                                'open file. Python uses this idea to open with mode r and '
                                                'UTF-8, then read, readline, or loop over lines\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Missing paths raise filenotfounderror; '
                                                'read() loads all text and may be costly for large files. If '
                                                'you change the example’s input or value, check this rule '
                                                'again because it can change the result or the path Python '
                                                'takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Pack a map\nBring water',
                        'id': 80,
                        'introduction': 'Why learn this? Reading a file lets a program use information saved '
                                        'beyond one run. In this lesson, we will see a file handle is '
                                        'Python’s connection to an open file, follow how Python handles it, '
                                        'and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a file handle is Python’s connection to an open '
                                                'file in your own words.',
                                                'Trace a small Reading Files example and predict what Python '
                                                'does next.',
                                                'Use the concept safely, including this important rule: '
                                                'missing paths raise FileNotFoundError; read() loads all '
                                                'text and may be costly for large files.'],
                        'level_id': 80,
                        'line_by_line': [{'code': "with open('quest_notes.txt', 'w', encoding='utf-8') as "
                                                  'file:',
                                          'explanation': "Enter a managed block for open('quest_notes.txt', "
                                                         "'w', encoding='utf-8') and call the open resource "
                                                         'file. When the indented block ends, Python closes '
                                                         'the resource automatically.',
                                          'line': '1'},
                                         {'code': "    file.write('Pack a map\\nBring water\\n')",
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '2'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '3'},
                                         {'code': "with open('quest_notes.txt', 'r', encoding='utf-8') as "
                                                  'file:',
                                          'explanation': "Enter a managed block for open('quest_notes.txt', "
                                                         "'r', encoding='utf-8') and call the open resource "
                                                         'file. When the indented block ends, Python closes '
                                                         'the resource automatically.',
                                          'line': '4'},
                                         {'code': '    for line in file:',
                                          'explanation': 'Start a loop. Each turn, take the next value from '
                                                         'file and store it in line before running the '
                                                         'indented block.',
                                          'line': '5'},
                                         {'code': '        print(line.strip())',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '6'}],
                        'practical_examples': [{'code': "with open('quest_notes.txt', 'w', encoding='utf-8') "
                                                        'as file:\n'
                                                        "    file.write('Pack a map\\nBring water\\n')\n"
                                                        '\n'
                                                        "with open('quest_notes.txt', 'r', encoding='utf-8') "
                                                        'as file:\n'
                                                        '    for line in file:\n'
                                                        '        print(line.strip())',
                                                'explanation': 'Purpose: Read a text file line by line shows '
                                                               'the current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: with open('quest_notes.txt', 'w', "
                                                               "encoding='utf-8') as file:\n"
                                                               'Enter a managed block for '
                                                               "open('quest_notes.txt', 'w', "
                                                               "encoding='utf-8') and call the open resource "
                                                               'file. When the indented block ends, Python '
                                                               'closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 2: file.write('Pack a map\\nBring "
                                                               "water\\n')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: with open('quest_notes.txt', 'r', "
                                                               "encoding='utf-8') as file:\n"
                                                               'Enter a managed block for '
                                                               "open('quest_notes.txt', 'r', "
                                                               "encoding='utf-8') and call the open resource "
                                                               'file. When the indented block ends, Python '
                                                               'closes the resource automatically.\n'
                                                               '\n'
                                                               'Line 5: for line in file:\n'
                                                               'Start a loop. Each turn, take the next value '
                                                               'from file and store it in line before '
                                                               'running the indented block.\n'
                                                               '\n'
                                                               'Line 6: print(line.strip())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Pack a map\n'
                                                               'Bring water',
                                                'output': 'Pack a map\nBring water',
                                                'title': 'Read a text file line by line'},
                                               {'code': "with open('scores.txt', 'w', encoding='utf-8') as "
                                                        'file:\n'
                                                        "    file.write('Mia,95\\nKai,88\\n')\n"
                                                        '\n'
                                                        "with open('scores.txt', 'r', encoding='utf-8') as "
                                                        'file:\n'
                                                        '    first_line = file.readline().strip()\n'
                                                        '    print(first_line)',
                                                'explanation': 'Purpose: readline reads one line at a time '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: with open('scores.txt', 'w', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('scores.txt', "
                                                               "'w', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 2: file.write('Mia,95\\nKai,88\\n')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: with open('scores.txt', 'r', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('scores.txt', "
                                                               "'r', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               'Line 5: first_line = '
                                                               'file.readline().strip()\n'
                                                               'Store file.readline().strip() in first_line '
                                                               'so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 6: print(first_line)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Mia,95',
                                                'output': 'Mia,95',
                                                'title': 'readline reads one line at a time'},
                                               {'code': 'try:\n'
                                                        "    with open('missing_notes.txt', 'r', "
                                                        "encoding='utf-8') as file:\n"
                                                        '        print(file.read())\n'
                                                        'except FileNotFoundError:\n'
                                                        "    print('Notes file not found yet')",
                                                'explanation': 'Purpose: Handle a file that is not there '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 2: with open('missing_notes.txt', 'r', "
                                                               "encoding='utf-8') as file:\n"
                                                               'Enter a managed block for '
                                                               "open('missing_notes.txt', 'r', "
                                                               "encoding='utf-8') and call the open resource "
                                                               'file. When the indented block ends, Python '
                                                               'closes the resource automatically.\n'
                                                               '\n'
                                                               'Line 3: print(file.read())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: except FileNotFoundError:\n'
                                                               'Handle only a FileNotFoundError exception '
                                                               'here.\n'
                                                               '\n'
                                                               "Line 5: print('Notes file not found yet')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Notes file not found yet',
                                                'output': 'Notes file not found yet',
                                                'title': 'Handle a file that is not there'}],
                        'practice_questions': [{'answer': 'A file handle is python’s connection to an open '
                                                          'file.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Reading a file lets a program use information '
                                                          'saved beyond one run.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Missing paths raise filenotfounderror; read() '
                                                          'loads all text and may be costly for large files.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is loading a saved settings '
                                           'or notes file. The same pattern helps a larger program stay '
                                           'clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Read text using a clear path, encoding, and a suitable way to '
                                   'consume its lines. Missing paths raise filenotfounderror; read() loads '
                                   'all text and may be costly for large files The practical example and its '
                                   'line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': "with open('quest_notes.txt', 'w', encoding='utf-8') as file:\n"
                                            "    file.write('Pack a map\\nBring water\\n')\n"
                                            '\n'
                                            "with open('quest_notes.txt', 'r', encoding='utf-8') as file:\n"
                                            '    for line in file:\n'
                                            '        print(line.strip())',
                        'terminology': [{'definition': 'The object Python uses to work with an open file.',
                                         'term': 'File handle'},
                                        {'definition': 'The rule used to convert stored bytes to text; UTF-8 '
                                                       'supports common writing systems.',
                                         'term': 'Encoding'},
                                        {'definition': 'Read one line from a file.', 'term': 'readline'}],
                        'title': 'Reading Files'},
             'number': 80,
             'quizzes': [{'explanation': 'json.dumps() serializes a Python dictionary into a JSON formatted '
                                         'string.',
                          'options': [{'explanation': 'Correct! json.dumps produces a string.',
                                       'is_correct': True,
                                       'text': "<class 'str'>"},
                                      {'explanation': 'Incorrect. json.loads produces a dict.',
                                       'is_correct': False,
                                       'text': "<class 'dict'>"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "<class 'bytes'>"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'JSON'}],
                          'question': 'What is the output of serialization with json.dumps?\n'
                                      '\n'
                                      'import json\n'
                                      "data = {'level': 10, 'hero': 'Cipher'}\n"
                                      's = json.dumps(data)\n'
                                      'print(type(s))'},
                         {'explanation': "json.loads() parses JSON 'true' into the Python boolean True.",
                          'options': [{'explanation': "Correct! JSON boolean 'true' parses to Python True.",
                                       'is_correct': True,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect. It is deserialized as a boolean.',
                                       'is_correct': False,
                                       'text': "'true'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '1'},
                                      {'explanation': "Incorrect. Key 'active' exists.",
                                       'is_correct': False,
                                       'text': 'KeyError'}],
                          'question': 'What is the output of deserialization with json.loads?\n'
                                      '\n'
                                      'import json\n'
                                      'obj = json.loads(\'{"score": 250, "active": true}\')\n'
                                      "print(obj['active'])"}],
             'title': 'Reading Files'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use StringIO as a safe in-memory file.\n2. Write one line, then append a second line, and print the saved text.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['from io import StringIO\n'
                                       'file = StringIO()\n'
                                       "file.write('First entry\\n')\n"
                                       "file.write('Second entry\\n')\n"
                                       "print(file.getvalue(), end='')"],
                             'initial_code': '# Reading Files Line-by-Line\n'
                                             'import io\n'
                                             '# Step 1: Stream initialized:\n'
                                             "f = io.StringIO('Line 1\\nLine 2\\nLine 3')\n"
                                             '\n'
                                             '# Step 2: Iterate and print line.strip() below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'from io import StringIO\n'
                                              'file = StringIO()\n'
                                              "file.write('First entry\\n')\n"
                                              "file.write('Second entry\\n')\n"
                                              "print(file.getvalue(), end='')",
                             'test_cases': [{'expected_output': 'First entry\nSecond entry',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Write and Append Text',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write three numbered lines to an in-memory stream using a loop, then display all of them.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['from io import StringIO\n'
                                       'log = StringIO()\n'
                                       'for number in range(1, 4):\n'
                                       "    log.write(f'Log {number}\\n')\n"
                                       "print(log.getvalue(), end='')"],
                             'initial_code': '# ⚔️ Boss Challenge: In-Memory File Batch Transform\n'
                                             'import io\n'
                                             "f = io.StringIO('Alpha\\nBeta\\nGamma')\n"
                                             '\n'
                                             "# Step 1: Uppercase lines and join with ', ' below:\n"
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'from io import StringIO\n'
                                              'log = StringIO()\n'
                                              'for number in range(1, 4):\n'
                                              "    log.write(f'Log {number}\\n')\n"
                                              "print(log.getvalue(), end='')",
                             'test_cases': [{'expected_output': 'Log 1\nLog 2\nLog 3',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Build a Log File',
                             'xp_reward': 150}],
             'description': "Create new files and preserve existing records using write ('w') and append "
                            "('a') modes.",
             'lesson': {'common_mistakes': [{'fix': 'Use w to replace and a to add; include newline '
                                                    'characters where needed.',
                                             'mistake': 'w truncates existing content, so use it only when '
                                                        'replacement is intended',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Programs need to save changes and '
                                                'keep earlier records when appropriate. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: W creates or replaces a file; a appends to '
                                                'the end. Python uses this idea to write stores strings and '
                                                'does not add a newline automatically\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: W truncates existing content, so use it '
                                                'only when replacement is intended. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Started\nFinished',
                        'id': 81,
                        'introduction': 'Why learn this? Programs need to save changes and keep earlier '
                                        'records when appropriate. In this lesson, we will see w creates or '
                                        'replaces a file; a appends to the end, follow how Python handles '
                                        'it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain w creates or replaces a file; a appends to the end '
                                                'in your own words.',
                                                'Trace a small Writing and Appending Files example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: w '
                                                'truncates existing content, so use it only when replacement '
                                                'is intended.'],
                        'level_id': 81,
                        'line_by_line': [{'code': "with open('daily_log.txt', 'w', encoding='utf-8') as "
                                                  'file:',
                                          'explanation': "Enter a managed block for open('daily_log.txt', "
                                                         "'w', encoding='utf-8') and call the open resource "
                                                         'file. When the indented block ends, Python closes '
                                                         'the resource automatically.',
                                          'line': '1'},
                                         {'code': "    file.write('Started\\n')",
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '2'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '3'},
                                         {'code': "with open('daily_log.txt', 'a', encoding='utf-8') as "
                                                  'file:',
                                          'explanation': "Enter a managed block for open('daily_log.txt', "
                                                         "'a', encoding='utf-8') and call the open resource "
                                                         'file. When the indented block ends, Python closes '
                                                         'the resource automatically.',
                                          'line': '4'},
                                         {'code': "    file.write('Finished\\n')",
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '5'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '6'},
                                         {'code': "with open('daily_log.txt', 'r', encoding='utf-8') as "
                                                  'file:',
                                          'explanation': "Enter a managed block for open('daily_log.txt', "
                                                         "'r', encoding='utf-8') and call the open resource "
                                                         'file. When the indented block ends, Python closes '
                                                         'the resource automatically.',
                                          'line': '7'},
                                         {'code': "    print(file.read(), end='')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '8'}],
                        'practical_examples': [{'code': "with open('daily_log.txt', 'w', encoding='utf-8') "
                                                        'as file:\n'
                                                        "    file.write('Started\\n')\n"
                                                        '\n'
                                                        "with open('daily_log.txt', 'a', encoding='utf-8') "
                                                        'as file:\n'
                                                        "    file.write('Finished\\n')\n"
                                                        '\n'
                                                        "with open('daily_log.txt', 'r', encoding='utf-8') "
                                                        'as file:\n'
                                                        "    print(file.read(), end='')",
                                                'explanation': 'Purpose: Write then append to a text file '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: with open('daily_log.txt', 'w', "
                                                               "encoding='utf-8') as file:\n"
                                                               'Enter a managed block for '
                                                               "open('daily_log.txt', 'w', encoding='utf-8') "
                                                               'and call the open resource file. When the '
                                                               'indented block ends, Python closes the '
                                                               'resource automatically.\n'
                                                               '\n'
                                                               "Line 2: file.write('Started\\n')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: with open('daily_log.txt', 'a', "
                                                               "encoding='utf-8') as file:\n"
                                                               'Enter a managed block for '
                                                               "open('daily_log.txt', 'a', encoding='utf-8') "
                                                               'and call the open resource file. When the '
                                                               'indented block ends, Python closes the '
                                                               'resource automatically.\n'
                                                               '\n'
                                                               "Line 5: file.write('Finished\\n')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 6: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 7: with open('daily_log.txt', 'r', "
                                                               "encoding='utf-8') as file:\n"
                                                               'Enter a managed block for '
                                                               "open('daily_log.txt', 'r', encoding='utf-8') "
                                                               'and call the open resource file. When the '
                                                               'indented block ends, Python closes the '
                                                               'resource automatically.\n'
                                                               '\n'
                                                               "Line 8: print(file.read(), end='')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Started\n'
                                                               'Finished',
                                                'output': 'Started\nFinished',
                                                'title': 'Write then append to a text file'},
                                               {'code': "with open('report.txt', 'w', encoding='utf-8') as "
                                                        'file:\n'
                                                        "    written = file.write('Ready')\n"
                                                        "    print('Characters written:', written)\n"
                                                        '\n'
                                                        "with open('report.txt', 'a', encoding='utf-8') as "
                                                        'file:\n'
                                                        "    file.write(' now')\n"
                                                        '\n'
                                                        "with open('report.txt', 'r', encoding='utf-8') as "
                                                        'file:\n'
                                                        '    print(file.read())',
                                                'explanation': 'Purpose: write does not add a newline for '
                                                               'you shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: with open('report.txt', 'w', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('report.txt', "
                                                               "'w', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 2: written = file.write('Ready')\n"
                                                               "Store file.write('Ready') in written so "
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               "Line 3: print('Characters written:', "
                                                               'written)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 5: with open('report.txt', 'a', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('report.txt', "
                                                               "'a', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 6: file.write(' now')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 7: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 8: with open('report.txt', 'r', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('report.txt', "
                                                               "'r', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               'Line 9: print(file.read())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Characters written: 5\n'
                                                               'Ready now',
                                                'output': 'Characters written: 5\nReady now',
                                                'title': 'write does not add a newline for you'},
                                               {'code': "with open('events.txt', 'w', encoding='utf-8') as "
                                                        'file:\n'
                                                        "    file.write('First\\n')\n"
                                                        "with open('events.txt', 'a', encoding='utf-8') as "
                                                        'file:\n'
                                                        "    file.write('Second\\n')\n"
                                                        "with open('events.txt', 'r', encoding='utf-8') as "
                                                        'file:\n'
                                                        "    print(file.read(), end='')",
                                                'explanation': 'Purpose: Append preserves earlier lines '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: with open('events.txt', 'w', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('events.txt', "
                                                               "'w', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 2: file.write('First\\n')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 3: with open('events.txt', 'a', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('events.txt', "
                                                               "'a', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 4: file.write('Second\\n')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 5: with open('events.txt', 'r', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('events.txt', "
                                                               "'r', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 6: print(file.read(), end='')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: First\n'
                                                               'Second',
                                                'output': 'First\nSecond',
                                                'title': 'Append preserves earlier lines'}],
                        'practice_questions': [{'answer': 'W creates or replaces a file; a appends to the '
                                                          'end.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Programs need to save changes and keep earlier '
                                                          'records when appropriate.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'W truncates existing content, so use it only when '
                                                          'replacement is intended.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is saving a fresh report or '
                                           'adding an audit entry. The same pattern helps a larger program '
                                           'stay clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Use w to replace and a to add; include newline characters '
                                   'where needed. W truncates existing content, so use it only when '
                                   'replacement is intended The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': "with open('daily_log.txt', 'w', encoding='utf-8') as file:\n"
                                            "    file.write('Started\\n')\n"
                                            '\n'
                                            "with open('daily_log.txt', 'a', encoding='utf-8') as file:\n"
                                            "    file.write('Finished\\n')\n"
                                            '\n'
                                            "with open('daily_log.txt', 'r', encoding='utf-8') as file:\n"
                                            "    print(file.read(), end='')",
                        'terminology': [{'definition': 'Open a file for writing, replacing its previous '
                                                       'contents.',
                                         'term': 'w mode'},
                                        {'definition': 'Open a file to add text at its end.',
                                         'term': 'a mode'},
                                        {'definition': 'The character that starts a new line in a text file.',
                                         'term': 'Newline'}],
                        'title': 'Writing and Appending Files'},
             'number': 81,
             'quizzes': [{'explanation': "split(',') splits at commas into a list: ['Alex', '100', "
                                         "'Warrior'].",
                          'options': [{'explanation': 'Correct! Comma splitting produces a list of 3 '
                                                      'strings.',
                                       'is_correct': True,
                                       'text': "['Alex', '100', 'Warrior']"},
                                      {'explanation': 'Incorrect. split() returns a list of strings.',
                                       'is_correct': False,
                                       'text': "('Alex', 100, 'Warrior')"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "{'name': 'Alex'}"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "'Alex 100 Warrior'"}],
                          'question': "Given a CSV line 'Alex,100,Warrior', what is the output of "
                                      "row.split(',')?"},
                         {'explanation': 'csv.DictReader maps headers to values, yielding dictionaries like '
                                         "{'name': 'Alex', 'score': '100'}.",
                          'options': [{'explanation': 'Correct! DictReader parses each row into a dict.',
                                       'is_correct': True,
                                       'text': 'A dictionary mapping header names to row values'},
                                      {'explanation': 'Incorrect. That is standard csv.reader.',
                                       'is_correct': False,
                                       'text': 'A tuple of raw column values'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'A single formatted string'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'A list of integers'}],
                          'question': 'What does csv.DictReader yield for each line of a CSV with header '
                                      "'name,score'?"}],
             'title': 'Writing and Appending Files'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use a with block to read an in-memory text stream.\n2. The block closes the stream when it ends.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['from io import StringIO\n'
                                       "with StringIO('Safe until the block ends') as stream:\n"
                                       '    print(stream.read())\n'
                                       "print('Closed:', stream.closed)"],
                             'initial_code': '# Writing to Streams with .write()\n'
                                             'import io\n'
                                             'f = io.StringIO()\n'
                                             '\n'
                                             "# Step 1: Write 'Hello ' and 'World!' below:\n"
                                             '\n'
                                             '# Step 2: Print f.getvalue() below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'from io import StringIO\n'
                                              "with StringIO('Safe until the block ends') as stream:\n"
                                              '    print(stream.read())\n'
                                              "print('Closed:', stream.closed)",
                             'test_cases': [{'expected_output': 'Safe until the block ends\nClosed: True',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Close a Resource with with',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Create a context manager with __enter__ and __exit__.\n2. Print a message when it opens, inside the block, and when it closes.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class ManagedResource:\n'
                                       '    def __enter__(self):\n'
                                       "        print('Opened')\n"
                                       '        return self\n'
                                       '    def __exit__(self, exc_type, exc_value, traceback):\n'
                                       "        print('Closed')\n"
                                       'with ManagedResource():\n'
                                       "    print('In the block')"],
                             'initial_code': '# ⚔️ Boss Challenge: Formatted Log Generator\n'
                                             'import io\n'
                                             'f = io.StringIO()\n'
                                             '\n'
                                             '# Step 1: Write 3 log entries using loop:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class ManagedResource:\n'
                                              '    def __enter__(self):\n'
                                              "        print('Opened')\n"
                                              '        return self\n'
                                              '    def __exit__(self, exc_type, exc_value, traceback):\n'
                                              "        print('Closed')\n"
                                              'with ManagedResource():\n'
                                              "    print('In the block')",
                             'test_cases': [{'expected_output': 'Opened\nIn the block\nClosed',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Custom Context Manager',
                             'xp_reward': 150}],
             'description': "Guarantee leak-free file handling using Python's context management protocol.",
             'lesson': {'common_mistakes': [{'fix': 'with gives the file a clear lifetime and closes it '
                                                    'automatically.',
                                             'mistake': 'the indented block belongs to with; manual close is '
                                                        'easy to forget',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Open files should always be closed '
                                                'even if work fails. This is the practical problem the '
                                                'feature solves.\n'
                                                '\n'
                                                'What it means: A context manager manages setup and cleanup '
                                                'around a block. Python uses this idea to with open(...) as '
                                                'file enters the block and closes the handle on exit\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: The indented block belongs to with; manual '
                                                'close is easy to forget. If you change the example’s input '
                                                'or value, check this rule again because it can change the '
                                                'result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Active',
                        'id': 82,
                        'introduction': 'Why learn this? Open files should always be closed even if work '
                                        'fails. In this lesson, we will see a context manager manages setup '
                                        'and cleanup around a block, follow how Python handles it, and '
                                        'practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a context manager manages setup and cleanup around '
                                                'a block in your own words.',
                                                'Trace a small Context Managers (the with statement) example '
                                                'and predict what Python does next.',
                                                'Use the concept safely, including this important rule: the '
                                                'indented block belongs to with; manual close is easy to '
                                                'forget.'],
                        'level_id': 82,
                        'line_by_line': [{'code': "with open('status.txt', 'w', encoding='utf-8') as file:",
                                          'explanation': "Enter a managed block for open('status.txt', 'w', "
                                                         "encoding='utf-8') and call the open resource file. "
                                                         'When the indented block ends, Python closes the '
                                                         'resource automatically.',
                                          'line': '1'},
                                         {'code': "    file.write('Active')",
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '2'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '3'},
                                         {'code': "with open('status.txt', 'r', encoding='utf-8') as file:",
                                          'explanation': "Enter a managed block for open('status.txt', 'r', "
                                                         "encoding='utf-8') and call the open resource file. "
                                                         'When the indented block ends, Python closes the '
                                                         'resource automatically.',
                                          'line': '4'},
                                         {'code': '    print(file.read())',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '5'}],
                        'practical_examples': [{'code': "with open('status.txt', 'w', encoding='utf-8') as "
                                                        'file:\n'
                                                        "    file.write('Active')\n"
                                                        '\n'
                                                        "with open('status.txt', 'r', encoding='utf-8') as "
                                                        'file:\n'
                                                        '    print(file.read())',
                                                'explanation': 'Purpose: with closes a file automatically '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: with open('status.txt', 'w', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('status.txt', "
                                                               "'w', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 2: file.write('Active')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: with open('status.txt', 'r', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('status.txt', "
                                                               "'r', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               'Line 5: print(file.read())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Active',
                                                'output': 'Active',
                                                'title': 'with closes a file automatically'},
                                               {'code': "with open('first.txt', 'w', encoding='utf-8') as "
                                                        "first, open('second.txt', 'w', encoding='utf-8') as "
                                                        'second:\n'
                                                        "    first.write('A')\n"
                                                        "    second.write('B')\n"
                                                        '\n'
                                                        "with open('first.txt', encoding='utf-8') as first, "
                                                        "open('second.txt', encoding='utf-8') as second:\n"
                                                        '    print(first.read() + second.read())',
                                                'explanation': 'Purpose: Two files can be managed in one '
                                                               'with statement shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: with open('first.txt', 'w', "
                                                               "encoding='utf-8') as first, "
                                                               "open('second.txt', 'w', encoding='utf-8') as "
                                                               'second:\n'
                                                               "Enter a managed block for open('first.txt', "
                                                               "'w', encoding='utf-8') as first, "
                                                               "open('second.txt', 'w', encoding='utf-8') "
                                                               'and call the open resource second. When the '
                                                               'indented block ends, Python closes the '
                                                               'resource automatically.\n'
                                                               '\n'
                                                               "Line 2: first.write('A')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 3: second.write('B')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 5: with open('first.txt', "
                                                               "encoding='utf-8') as first, "
                                                               "open('second.txt', encoding='utf-8') as "
                                                               'second:\n'
                                                               "Enter a managed block for open('first.txt', "
                                                               "encoding='utf-8') as first, "
                                                               "open('second.txt', encoding='utf-8') and "
                                                               'call the open resource second. When the '
                                                               'indented block ends, Python closes the '
                                                               'resource automatically.\n'
                                                               '\n'
                                                               'Line 6: print(first.read() + second.read())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: AB',
                                                'output': 'AB',
                                                'title': 'Two files can be managed in one with statement'},
                                               {'code': 'try:\n'
                                                        "    with open('safe.txt', 'w', encoding='utf-8') as "
                                                        'file:\n'
                                                        "        file.write('Saved')\n"
                                                        "        raise ValueError('demo')\n"
                                                        'except ValueError:\n'
                                                        "    print('Handled the problem')\n"
                                                        '\n'
                                                        "print('The with block has ended')",
                                                'explanation': 'Purpose: Cleanup still happens if an error '
                                                               'occurs in the block shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 2: with open('safe.txt', 'w', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for open('safe.txt', "
                                                               "'w', encoding='utf-8') and call the open "
                                                               'resource file. When the indented block ends, '
                                                               'Python closes the resource automatically.\n'
                                                               '\n'
                                                               "Line 3: file.write('Saved')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 4: raise ValueError('demo')\n"
                                                               'Stop this path by raising '
                                                               "ValueError('demo'). Python passes that error "
                                                               'to the caller unless a matching except block '
                                                               'handles it.\n'
                                                               '\n'
                                                               'Line 5: except ValueError:\n'
                                                               'Handle only a ValueError exception here.\n'
                                                               '\n'
                                                               "Line 6: print('Handled the problem')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 7: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 8: print('The with block has ended')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Handled the problem\n'
                                                               'The with block has ended',
                                                'output': 'Handled the problem\nThe with block has ended',
                                                'title': 'Cleanup still happens if an error occurs in the '
                                                         'block'}],
                        'practice_questions': [{'answer': 'A context manager manages setup and cleanup '
                                                          'around a block.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Open files should always be closed even if work '
                                                          'fails.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'The indented block belongs to with; manual close '
                                                          'is easy to forget.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is reading or writing a file '
                                           'safely. The same pattern helps a larger program stay clear when '
                                           'it handles the same kind of task repeatedly.',
                        'summary': 'Remember: with gives the file a clear lifetime and closes it '
                                   'automatically. The indented block belongs to with; manual close is easy '
                                   'to forget The practical example and its line-by-line walkthrough show '
                                   'the idea in action.',
                        'syntax_breakdown': "with open('status.txt', 'w', encoding='utf-8') as file:\n"
                                            "    file.write('Active')\n"
                                            '\n'
                                            "with open('status.txt', 'r', encoding='utf-8') as file:\n"
                                            '    print(file.read())',
                        'terminology': [{'definition': 'An object that manages setup and cleanup around a '
                                                       'block.',
                                         'term': 'Context manager'},
                                        {'definition': 'Start a managed block.', 'term': 'with'},
                                        {'definition': 'Closing a file when its block ends.',
                                         'term': 'Resource cleanup'}],
                        'title': 'Context Managers (the with statement)'},
             'number': 82,
             'quizzes': [{'explanation': "os.path.basename returns the final component of a path: 'hero.py'.",
                          'options': [{'explanation': 'Correct! basename extracts the file name from the '
                                                      'path.',
                                       'is_correct': True,
                                       'text': 'hero.py'},
                                      {'explanation': 'Incorrect. That is os.path.dirname().',
                                       'is_correct': False,
                                       'text': 'quest/data'},
                                      {'explanation': 'Incorrect. That is os.path.splitext().',
                                       'is_correct': False,
                                       'text': '.py'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'quest'}],
                          'question': 'What is the output of: '
                                      "print(os.path.basename('quest/data/hero.py'))?"},
                         {'explanation': 'os.path.exists() checks file existence and returns True if found.',
                          'options': [{'explanation': 'Correct! Returns True if path exists.',
                                       'is_correct': True,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect. It returns a boolean.',
                                       'is_correct': False,
                                       'text': '1'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "'file.txt'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'}],
                          'question': "What does os.path.exists('file.txt') return if the file is present on "
                                      'disk?'}],
             'title': 'Context Managers (the with statement)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use os.path.join to combine three path parts.\n2. Replace backslashes in the displayed result so the sample is easy to read on any computer.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['import os\n'
                                       "path = os.path.join('data', 'reports', 'quest.txt')\n"
                                       "print(path.replace('\\\\', '/'))"],
                             'initial_code': '# The with Statement: Automatic Resource Cleanup\n'
                                             'import io\n'
                                             "# Step 1: with io.StringIO('Safe resource management') as f:\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import os\n'
                                              "path = os.path.join('data', 'reports', 'quest.txt')\n"
                                              "print(path.replace('\\\\', '/'))",
                             'test_cases': [{'expected_output': 'data/reports/quest.txt',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Join File Path Parts',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use os.path to print the file name and containing folder on separate lines.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import os\n'
                                       "path = os.path.join('missions', 'daily', 'plan.txt')\n"
                                       'print(os.path.basename(path))\n'
                                       "print(os.path.dirname(path).replace('\\\\', '/'))"],
                             'initial_code': '# ⚔️ Boss Challenge: Custom Context Manager Protocol\n'
                                             '# Step 1: Define DummyManager with __enter__ and __exit__:\n'
                                             '\n'
                                             "# Step 2: Use with DummyManager(): print('Inside block')\n"
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import os\n'
                                              "path = os.path.join('missions', 'daily', 'plan.txt')\n"
                                              'print(os.path.basename(path))\n'
                                              "print(os.path.dirname(path).replace('\\\\', '/'))",
                             'test_cases': [{'expected_output': 'plan.txt\nmissions/daily',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Split a File Path',
                             'xp_reward': 150}],
             'description': 'Construct cross-platform file paths, navigate directories, and inspect file '
                            'metadata.',
             'lesson': {'common_mistakes': [{'fix': 'Build paths with pathlib and check where a relative '
                                                    'path starts.',
                                             'mistake': 'relative paths start from the process current '
                                                        'working directory, not always the script folder',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: The same file can live in different '
                                                'folders and operating systems. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: A path is an address; it is separate from '
                                                'the file contents. Python uses this idea to path joins '
                                                'folder names with / and offers name, suffix, parent, exists '
                                                'and read/write helpers\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Relative paths start from the process '
                                                'current working directory, not always the script folder. If '
                                                'you change the example’s input or value, check this rule '
                                                'again because it can change the result or the path Python '
                                                'takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Parent folder: workspace\\projects\n'
                                           'File name: main.py\n'
                                           'Extension: .py',
                        'id': 83,
                        'introduction': 'Why learn this? The same file can live in different folders and '
                                        'operating systems. In this lesson, we will see a path is an '
                                        'address; it is separate from the file contents, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a path is an address; it is separate from the file '
                                                'contents in your own words.',
                                                'Trace a small Working with File Paths (os.path and pathlib) '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'relative paths start from the process current working '
                                                'directory, not always the script folder.'],
                        'level_id': 83,
                        'line_by_line': [{'code': 'from pathlib import Path',
                                          'explanation': 'Import the named tool(s) from pathlib; the names '
                                                         'can then be used directly in this file.',
                                          'line': '1'},
                                         {'code': "p = Path('workspace/projects/main.py')",
                                          'explanation': "Store Path('workspace/projects/main.py') in p so "
                                                         'later instructions can use it.',
                                          'line': '2'},
                                         {'code': "print('Parent folder:', p.parent)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'},
                                         {'code': "print('File name:', p.name)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '4'},
                                         {'code': "print('Extension:', p.suffix)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '5'}],
                        'practical_examples': [{'code': 'from pathlib import Path\n'
                                                        "p = Path('workspace/projects/main.py')\n"
                                                        "print('Parent folder:', p.parent)\n"
                                                        "print('File name:', p.name)\n"
                                                        "print('Extension:', p.suffix)",
                                                'explanation': 'Purpose: Example 1: Inspecting path '
                                                               'components with pathlib shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: from pathlib import Path\n'
                                                               'Import the named tool(s) from pathlib; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 2: p = '
                                                               "Path('workspace/projects/main.py')\n"
                                                               "Store Path('workspace/projects/main.py') in "
                                                               'p so later instructions can use it.\n'
                                                               '\n'
                                                               "Line 3: print('Parent folder:', p.parent)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 4: print('File name:', p.name)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 5: print('Extension:', p.suffix)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Parent folder: '
                                                               'workspace\\projects\n'
                                                               'File name: main.py\n'
                                                               'Extension: .py',
                                                'output': 'Parent folder: workspace\\projects\n'
                                                          'File name: main.py\n'
                                                          'Extension: .py',
                                                'title': 'Example 1: Inspecting path components with '
                                                         'pathlib'},
                                               {'code': 'from pathlib import Path\n'
                                                        "config_path = Path('config.json')\n"
                                                        "print('Path object created:', config_path)\n"
                                                        "print('Is absolute:', config_path.is_absolute())",
                                                'explanation': 'Purpose: Example 2: Checking file existence '
                                                               'safely shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: from pathlib import Path\n'
                                                               'Import the named tool(s) from pathlib; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               "Line 2: config_path = Path('config.json')\n"
                                                               "Store Path('config.json') in config_path so "
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               "Line 3: print('Path object created:', "
                                                               'config_path)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 4: print('Is absolute:', "
                                                               'config_path.is_absolute())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Path object created: '
                                                               'config.json\n'
                                                               'Is absolute: False',
                                                'output': 'Path object created: config.json\n'
                                                          'Is absolute: False',
                                                'title': 'Example 2: Checking file existence safely'},
                                               {'code': 'from pathlib import Path\n'
                                                        "base = Path('app')\n"
                                                        "sub = base / 'logs' / 'daily' / '2026.log'\n"
                                                        "print('Combined Path:', sub)",
                                                'explanation': 'Purpose: Example 3: Building nested '
                                                               'directory paths shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: from pathlib import Path\n'
                                                               'Import the named tool(s) from pathlib; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               "Line 2: base = Path('app')\n"
                                                               "Store Path('app') in base so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 3: sub = base / 'logs' / 'daily' / "
                                                               "'2026.log'\n"
                                                               "Calculate or compare base / 'logs' / 'daily' "
                                                               "/ '2026.log', then save the result in sub.\n"
                                                               '\n'
                                                               "Line 4: print('Combined Path:', sub)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Combined Path: '
                                                               'app\\logs\\daily\\2026.log',
                                                'output': 'Combined Path: app\\logs\\daily\\2026.log',
                                                'title': 'Example 3: Building nested directory paths'}],
                        'practice_questions': [{'answer': 'A path is an address; it is separate from the '
                                                          'file contents.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'The same file can live in different folders and '
                                                          'operating systems.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Relative paths start from the process current '
                                                          'working directory, not always the script folder.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is finding a report in a '
                                           'project data folder on Windows or macOS. The same pattern helps '
                                           'a larger program stay clear when it handles the same kind of '
                                           'task repeatedly.',
                        'summary': 'Remember: Build paths with pathlib and check where a relative path '
                                   'starts. Relative paths start from the process current working directory, '
                                   'not always the script folder The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'from pathlib import Path\n'
                                            "p = Path('workspace/projects/main.py')\n"
                                            "print('Parent folder:', p.parent)\n"
                                            "print('File name:', p.name)\n"
                                            "print('Extension:', p.suffix)",
                        'terminology': [{'definition': 'An address that identifies a file or folder.',
                                         'term': 'Path'},
                                        {'definition': 'A path interpreted from the process current working '
                                                       'directory.',
                                         'term': 'Relative path'},
                                        {'definition': 'Python’s object-oriented tools for building and '
                                                       'checking paths.',
                                         'term': 'Pathlib'}],
                        'title': 'Working with File Paths (os.path and pathlib)'},
             'number': 83,
             'quizzes': [{'explanation': "p.name returns the filename component: 'level1.py'.",
                          'options': [{'explanation': 'Correct! .name extracts the filename.',
                                       'is_correct': True,
                                       'text': 'level1.py'},
                                      {'explanation': 'Incorrect. That is .parent.',
                                       'is_correct': False,
                                       'text': 'quest/levels'},
                                      {'explanation': 'Incorrect. That is .suffix.',
                                       'is_correct': False,
                                       'text': '.py'},
                                      {'explanation': 'Incorrect. That is .stem.',
                                       'is_correct': False,
                                       'text': 'level1'}],
                          'question': 'What is the output of pathlib operator syntax?\n'
                                      '\n'
                                      'from pathlib import Path\n'
                                      "p = Path('quest') / 'levels' / 'level1.py'\n"
                                      'print(p.name)'},
                         {'explanation': '.suffix returns the file extension including the leading period: '
                                         "'.csv'.",
                          'options': [{'explanation': 'Correct! .suffix extracts the file extension with the '
                                                      'dot.',
                                       'is_correct': True,
                                       'text': "'.csv'"},
                                      {'explanation': "Incorrect. .suffix includes the period '.'.",
                                       'is_correct': False,
                                       'text': "'csv'"},
                                      {'explanation': 'Incorrect. That is .stem.',
                                       'is_correct': False,
                                       'text': "'report'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'}],
                          'question': "What does Path('report.csv').suffix return?"}],
             'title': 'Working with File Paths (os.path and pathlib)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use json.loads to read a JSON object containing a name and score.\n2. Print both values.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['import json\n'
                                       'record = json.loads(input())\n'
                                       'print(f"{record[\'name\']}: {record[\'score\']}")'],
                             'initial_code': '# Cross-Platform Paths with os.path.join\n'
                                             'import os\n'
                                             "# Step 1: Join 'data', 'reports', 'log.txt':\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import json\n'
                                              'record = json.loads(input())\n'
                                              'print(f"{record[\'name\']}: {record[\'score\']}")',
                             'test_cases': [{'expected_output': 'Mia: 90',
                                             'input_data': '{"name":"Mia","score":90}\n',
                                             'is_hidden': False}],
                             'title': 'Turn JSON Text into Python Data',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Create a Python dictionary and use json.dumps with sorted keys.\n2. Print the JSON text.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import json\n'
                                       "record = {'name': 'Mia', 'score': 90}\n"
                                       'print(json.dumps(record, sort_keys=True))'],
                             'initial_code': '# ⚔️ Boss Challenge: Path Component Deconstructor\n'
                                             'import os\n'
                                             "p = 'folder/subfolder/file.py'\n"
                                             '\n'
                                             '# Step 1: Print basename and dirname below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import json\n'
                                              "record = {'name': 'Mia', 'score': 90}\n"
                                              'print(json.dumps(record, sort_keys=True))',
                             'test_cases': [{'expected_output': '{"name": "Mia", "score": 90}',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Turn Python Data into JSON',
                             'xp_reward': 150}],
             'description': 'Convert Python structures to JSON and back using json.dumps and json.loads.',
             'lesson': {'common_mistakes': [{'fix': 'Serialize Python objects into JSON text and deserialize '
                                                    'JSON back into objects.',
                                             'mistake': 'JSON supports strings, numbers, booleans, null, '
                                                        'lists, and dictionaries with string keys; not every '
                                                        'Python object',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Programs often need to exchange '
                                                'simple structured data as text. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: Json is text; python dictionaries and lists '
                                                'are in-memory objects. Python uses this idea to dumps/loads '
                                                'convert strings; dump/load write/read through file objects\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Json supports strings, numbers, booleans, '
                                                'null, lists, and dictionaries with string keys; not every '
                                                'python object. If you change the example’s input or value, '
                                                'check this rule again because it can change the result or '
                                                'the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'JSON string payload: {"health": 85, "score": 1200, "alive": '
                                           'true}',
                        'id': 84,
                        'introduction': 'Why learn this? Programs often need to exchange simple structured '
                                        'data as text. In this lesson, we will see JSON is text; Python '
                                        'dictionaries and lists are in-memory objects, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain JSON is text; Python dictionaries and lists are '
                                                'in-memory objects in your own words.',
                                                'Trace a small JSON Serialization and Deserialization '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: JSON '
                                                'supports strings, numbers, booleans, null, lists, and '
                                                'dictionaries with string keys; not every Python object.'],
                        'level_id': 84,
                        'line_by_line': [{'code': 'import json',
                                          'explanation': 'Load the module json so this file can use its '
                                                         'tools. An alias, if present, becomes the name used '
                                                         'below.',
                                          'line': '1'},
                                         {'code': "state = {'health': 85, 'score': 1200, 'alive': True}",
                                          'explanation': "Store {'health': 85, 'score': 1200, 'alive': True} "
                                                         'in state so later instructions can use it.',
                                          'line': '2'},
                                         {'code': 'payload = json.dumps(state)',
                                          'explanation': 'Store json.dumps(state) in payload so later '
                                                         'instructions can use it.',
                                          'line': '3'},
                                         {'code': "print('JSON string payload:', payload)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '4'}],
                        'practical_examples': [{'code': 'import json\n'
                                                        "state = {'health': 85, 'score': 1200, 'alive': "
                                                        'True}\n'
                                                        'payload = json.dumps(state)\n'
                                                        "print('JSON string payload:', payload)",
                                                'explanation': 'Purpose: Example 1: Serializing game state '
                                                               'to JSON string shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import json\n'
                                                               'Load the module json so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               "Line 2: state = {'health': 85, 'score': "
                                                               "1200, 'alive': True}\n"
                                                               "Store {'health': 85, 'score': 1200, 'alive': "
                                                               'True} in state so later instructions can use '
                                                               'it.\n'
                                                               '\n'
                                                               'Line 3: payload = json.dumps(state)\n'
                                                               'Store json.dumps(state) in payload so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 4: print('JSON string payload:', "
                                                               'payload)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: JSON string payload: '
                                                               '{"health": 85, "score": 1200, "alive": true}',
                                                'output': 'JSON string payload: {"health": 85, "score": '
                                                          '1200, "alive": true}',
                                                'title': 'Example 1: Serializing game state to JSON string'},
                                               {'code': 'import json\n'
                                                        'raw_json = \'{"user": "Alex", "active": true, '
                                                        '"roles": ["Admin"]}\'\n'
                                                        'user_dict = json.loads(raw_json)\n'
                                                        "print('User:', user_dict['user'], '| First Role:', "
                                                        "user_dict['roles'][0])",
                                                'explanation': 'Purpose: Example 2: Parsing incoming JSON '
                                                               'API response shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import json\n'
                                                               'Load the module json so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               'Line 2: raw_json = \'{"user": "Alex", '
                                                               '"active": true, "roles": ["Admin"]}\'\n'
                                                               'Store \'{"user": "Alex", "active": true, '
                                                               '"roles": ["Admin"]}\' in raw_json so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 3: user_dict = json.loads(raw_json)\n'
                                                               'Store json.loads(raw_json) in user_dict so '
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               "Line 4: print('User:', user_dict['user'], '| "
                                                               "First Role:', user_dict['roles'][0])\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: User: Alex | First Role: Admin',
                                                'output': 'User: Alex | First Role: Admin',
                                                'title': 'Example 2: Parsing incoming JSON API response'},
                                               {'code': 'import json\n'
                                                        "config = {'theme': 'dark', 'volume': 80}\n"
                                                        'print(json.dumps(config, indent=2))',
                                                'explanation': 'Purpose: Example 3: Pretty-printing JSON '
                                                               'with indentation shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import json\n'
                                                               'Load the module json so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               "Line 2: config = {'theme': 'dark', 'volume': "
                                                               '80}\n'
                                                               "Store {'theme': 'dark', 'volume': 80} in "
                                                               'config so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 3: print(json.dumps(config, indent=2))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: {\n'
                                                               '  "theme": "dark",\n'
                                                               '  "volume": 80\n'
                                                               '}',
                                                'output': '{\n  "theme": "dark",\n  "volume": 80\n}',
                                                'title': 'Example 3: Pretty-printing JSON with indentation'}],
                        'practice_questions': [{'answer': 'Json is text; python dictionaries and lists are '
                                                          'in-memory objects.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Programs often need to exchange simple structured '
                                                          'data as text.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Json supports strings, numbers, booleans, null, '
                                                          'lists, and dictionaries with string keys; not '
                                                          'every python object.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is saving settings or sending '
                                           'a small API payload. The same pattern helps a larger program '
                                           'stay clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Serialize Python objects into JSON text and deserialize JSON '
                                   'back into objects. Json supports strings, numbers, booleans, null, '
                                   'lists, and dictionaries with string keys; not every python object The '
                                   'practical example and its line-by-line walkthrough show the idea in '
                                   'action.',
                        'syntax_breakdown': 'import json\n'
                                            "state = {'health': 85, 'score': 1200, 'alive': True}\n"
                                            'payload = json.dumps(state)\n'
                                            "print('JSON string payload:', payload)",
                        'terminology': [{'definition': 'A text format for common structured data.',
                                         'term': 'JSON'},
                                        {'definition': 'Convert a Python object into JSON text.',
                                         'term': 'Serialize'},
                                        {'definition': 'Convert JSON text back into Python values.',
                                         'term': 'Deserialize'}],
                        'title': 'JSON Serialization and Deserialization'},
             'number': 84,
             'quizzes': [{'explanation': "The custom exception GameError carries the message 'Out of Mana', "
                                         'which is caught and printed.',
                          'options': [{'explanation': 'Correct! str(e) outputs the exception message.',
                                       'is_correct': True,
                                       'text': 'Out of Mana'},
                                      {'explanation': 'Incorrect. str(e) yields the message passed during '
                                                      'instantiation.',
                                       'is_correct': False,
                                       'text': 'GameError'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect. Custom exceptions inheriting from '
                                                      'Exception are standard.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What is the output of catching a custom exception?\n'
                                      '\n'
                                      'class GameError(Exception): pass\n'
                                      '\n'
                                      'try:\n'
                                      "    raise GameError('Out of Mana')\n"
                                      'except GameError as e:\n'
                                      '    print(str(e))'},
                         {'explanation': 'Custom exceptions must inherit from Exception (or BaseException).',
                          'options': [{'explanation': 'Correct! Inheriting from Exception enables standard '
                                                      'try/except handling.',
                                       'is_correct': True,
                                       'text': 'Exception'},
                                      {'explanation': 'Incorrect. Inheriting directly from object cannot be '
                                                      'raised.',
                                       'is_correct': False,
                                       'text': 'object'},
                                      {'explanation': "Incorrect. Python uses 'Exception'.",
                                       'is_correct': False,
                                       'text': 'Error'},
                                      {'explanation': 'Incorrect. Removed in Python 3.',
                                       'is_correct': False,
                                       'text': 'StandardError'}],
                          'question': 'What base class should custom exceptions inherit from in Python?'}],
             'title': 'JSON Serialization and Deserialization'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read the lines from the example text stream.\n2. Add the lines that are whole numbers and skip any line that is not a number.\n3. Print the total.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['import io\n'
                                       "with io.StringIO('10\\n20\\nabc\\n30') as f:\n"
                                       '    total = 0\n'
                                       '    for line in f:\n'
                                       '        try:\n'
                                       '            total += int(line.strip())\n'
                                       '        except ValueError:\n'
                                       '            pass\n'
                                       "    print(f'Total: {total}')"],
                             'initial_code': '# World 8 Capstone: Resilient Data Pipeline\n'
                                             'import io\n'
                                             '# Step 1: Stream initialized:\n'
                                             "with io.StringIO('10\\n20\\nabc\\n30') as f:\n"
                                             '    total = 0\n'
                                             '    # Step 2: Iterate lines and accumulate with try/except:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'from io import StringIO\n'
                                              '\n'
                                              "stream = StringIO('10\\n20\\nabc\\n30')\n"
                                              'total = 0\n'
                                              'for line in stream:\n'
                                              '    try:\n'
                                              '        total += int(line.strip())\n'
                                              '    except ValueError:\n'
                                              '        pass\n'
                                              "print(f'Total: {total}')",
                             'test_cases': [{'expected_output': 'Total: 60',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'World 8 Capstone: Fault-Tolerant File Parser',
                             'xp_reward': 50},
                            {'description': 'Your task, step by step:\n1. Count both INFO and ERROR entries in the log list.\n2. Print the heading and both totals.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["logs = ['[INFO] Started', '[ERROR] Disk full', '[INFO] Saved', "
                                       "'[ERROR] Retry']\n"
                                       "info_count = sum('[INFO]' in line for line in logs)\n"
                                       "error_count = sum('[ERROR]' in line for line in logs)\n"
                                       "print('Log Analysis Summary:')\n"
                                       "print('Total INFO Logs:', info_count)\n"
                                       "print('Total ERROR Logs:', error_count)"],
                             'initial_code': '# ⚔️ Boss Challenge: Log Analyzer Summary\n'
                                             '\n'
                                             'logs = [\n'
                                             "    '[INFO] System startup',\n"
                                             "    '[ERROR] Database connection lost',\n"
                                             "    '[INFO] User logged in',\n"
                                             "    '[ERROR] Disk full'\n"
                                             ']\n'
                                             '\n'
                                             "# Step 1: Count how many start with '[INFO]' and how many with "
                                             "'[ERROR]':\n"
                                             'info_count = 0\n'
                                             'error_count = 0\n'
                                             '\n'
                                             '# Step 2: Loop through logs and update counts:\n'
                                             '\n'
                                             '\n'
                                             '# Step 3: Print the summary:\n'
                                             "print('Log Analysis Summary:')\n"
                                             "print(f'Total INFO Logs: {info_count}')\n"
                                             "print(f'Total ERROR Logs: {error_count}')\n",
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "logs = ['[INFO] Started', '[ERROR] Disk full', '[INFO] "
                                              "Saved', '[ERROR] Retry']\n"
                                              "info_count = sum('[INFO]' in line for line in logs)\n"
                                              "error_count = sum('[ERROR]' in line for line in logs)\n"
                                              "print('Log Analysis Summary:')\n"
                                              "print('Total INFO Logs:', info_count)\n"
                                              "print('Total ERROR Logs:', error_count)",
                             'test_cases': [{'expected_output': 'Log Analysis Summary:\n'
                                                                'Total INFO Logs: 2\n'
                                                                'Total ERROR Logs: 2',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Count Log Levels',
                             'xp_reward': 250}],
             'description': 'Synthesize exception handling, file I/O, path management, and JSON '
                            'serialization into a persistent note system.',
             'lesson': {'common_mistakes': [{'fix': 'Load, change, and save the same JSON file so notes '
                                                    'persist between runs.',
                                             'mistake': 'the file is relative to the current working '
                                                        'directory; JSON text can be invalid',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Notes should still exist after the '
                                                'application closes. This is the practical problem the '
                                                'feature solves.\n'
                                                '\n'
                                                'What it means: A notes app loads json from a named file, '
                                                'changes a list, then saves it. Python uses this idea to use '
                                                'a relative notes.json path, UTF-8, with, and JSON '
                                                'load/dump; handle a missing or damaged file\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: The file is relative to the current working '
                                                'directory; json text can be invalid. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Saved one new note to notes.json',
                        'id': 85,
                        'introduction': 'Why learn this? Notes should still exist after the application '
                                        'closes. In this lesson, we will see a notes app loads JSON from a '
                                        'named file, changes a list, then saves it, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a notes app loads JSON from a named file, changes a '
                                                'list, then saves it in your own words.',
                                                'Trace a small World 8 Examination & Capstone: File-Based '
                                                'Notes Application example and predict what Python does '
                                                'next.',
                                                'Use the concept safely, including this important rule: the '
                                                'file is relative to the current working directory; JSON '
                                                'text can be invalid.'],
                        'level_id': 85,
                        'line_by_line': [{'code': 'import json',
                                          'explanation': 'Load the module json so this file can use its '
                                                         'tools. An alias, if present, becomes the name used '
                                                         'below.',
                                          'line': '1'},
                                         {'code': 'from pathlib import Path',
                                          'explanation': 'Import the named tool(s) from pathlib; the names '
                                                         'can then be used directly in this file.',
                                          'line': '2'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '3'},
                                         {'code': "path = Path('notes.json')",
                                          'explanation': "Store Path('notes.json') in path so later "
                                                         'instructions can use it.',
                                          'line': '4'},
                                         {'code': 'try:',
                                          'explanation': 'Start the block that may fail. If a matching '
                                                         'exception happens, Python jumps to an except '
                                                         'block.',
                                          'line': '5'},
                                         {'code': "    with path.open('r', encoding='utf-8') as file:",
                                          'explanation': "Enter a managed block for path.open('r', "
                                                         "encoding='utf-8') and call the open resource file. "
                                                         'When the indented block ends, Python closes the '
                                                         'resource automatically.',
                                          'line': '6'},
                                         {'code': '        notes = json.load(file)',
                                          'explanation': 'Store json.load(file) in notes so later '
                                                         'instructions can use it.',
                                          'line': '7'},
                                         {'code': 'except FileNotFoundError:',
                                          'explanation': 'Handle only a FileNotFoundError exception here.',
                                          'line': '8'},
                                         {'code': '    notes = []',
                                          'explanation': 'Create the list shown and store it in notes. The '
                                                         'list keeps items in order and can be processed one '
                                                         'item at a time.',
                                          'line': '9'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '10'},
                                         {'code': "notes.append({'text': 'Pack a map'})",
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '11'},
                                         {'code': "with path.open('w', encoding='utf-8') as file:",
                                          'explanation': "Enter a managed block for path.open('w', "
                                                         "encoding='utf-8') and call the open resource file. "
                                                         'When the indented block ends, Python closes the '
                                                         'resource automatically.',
                                          'line': '12'},
                                         {'code': '    json.dump(notes, file, indent=2)',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '13'},
                                         {'code': "print('Saved one new note to notes.json')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '14'}],
                        'practical_examples': [{'code': 'import json\n'
                                                        'from pathlib import Path\n'
                                                        '\n'
                                                        "path = Path('notes.json')\n"
                                                        'try:\n'
                                                        "    with path.open('r', encoding='utf-8') as file:\n"
                                                        '        notes = json.load(file)\n'
                                                        'except FileNotFoundError:\n'
                                                        '    notes = []\n'
                                                        '\n'
                                                        "notes.append({'text': 'Pack a map'})\n"
                                                        "with path.open('w', encoding='utf-8') as file:\n"
                                                        '    json.dump(notes, file, indent=2)\n'
                                                        "print('Saved one new note to notes.json')",
                                                'explanation': 'Purpose: A persistent notes file can be '
                                                               'loaded, changed, and saved shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import json\n'
                                                               'Load the module json so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               'Line 2: from pathlib import Path\n'
                                                               'Import the named tool(s) from pathlib; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: path = Path('notes.json')\n"
                                                               "Store Path('notes.json') in path so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 6: with path.open('r', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for path.open('r', "
                                                               "encoding='utf-8') and call the open resource "
                                                               'file. When the indented block ends, Python '
                                                               'closes the resource automatically.\n'
                                                               '\n'
                                                               'Line 7: notes = json.load(file)\n'
                                                               'Store json.load(file) in notes so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 8: except FileNotFoundError:\n'
                                                               'Handle only a FileNotFoundError exception '
                                                               'here.\n'
                                                               '\n'
                                                               'Line 9: notes = []\n'
                                                               'Create the list shown and store it in notes. '
                                                               'The list keeps items in order and can be '
                                                               'processed one item at a time.\n'
                                                               '\n'
                                                               'Line 10: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 11: notes.append({'text': 'Pack a "
                                                               "map'})\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 12: with path.open('w', "
                                                               "encoding='utf-8') as file:\n"
                                                               "Enter a managed block for path.open('w', "
                                                               "encoding='utf-8') and call the open resource "
                                                               'file. When the indented block ends, Python '
                                                               'closes the resource automatically.\n'
                                                               '\n'
                                                               'Line 13: json.dump(notes, file, indent=2)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 14: print('Saved one new note to "
                                                               "notes.json')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Saved one new note to '
                                                               'notes.json',
                                                'output': 'Saved one new note to notes.json',
                                                'title': 'A persistent notes file can be loaded, changed, '
                                                         'and saved'},
                                               {'code': 'import json\n'
                                                        'from pathlib import Path\n'
                                                        '\n'
                                                        "path = Path('broken_notes.json')\n"
                                                        "path.write_text('{not valid JSON', "
                                                        "encoding='utf-8')\n"
                                                        'try:\n'
                                                        '    notes = '
                                                        "json.loads(path.read_text(encoding='utf-8'))\n"
                                                        'except FileNotFoundError:\n'
                                                        '    notes = []\n'
                                                        'except json.JSONDecodeError:\n'
                                                        '    notes = []\n'
                                                        "print('Notes ready:', len(notes))",
                                                'explanation': 'Purpose: Handle damaged JSON with a helpful '
                                                               'fallback shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import json\n'
                                                               'Load the module json so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               'Line 2: from pathlib import Path\n'
                                                               'Import the named tool(s) from pathlib; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: path = Path('broken_notes.json')\n"
                                                               "Store Path('broken_notes.json') in path so "
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               "Line 5: path.write_text('{not valid JSON', "
                                                               "encoding='utf-8')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 6: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 7: notes = '
                                                               "json.loads(path.read_text(encoding='utf-8'))\n"
                                                               'Store '
                                                               "json.loads(path.read_text(encoding='utf-8')) "
                                                               'in notes so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 8: except FileNotFoundError:\n'
                                                               'Handle only a FileNotFoundError exception '
                                                               'here.\n'
                                                               '\n'
                                                               'Line 9: notes = []\n'
                                                               'Create the list shown and store it in notes. '
                                                               'The list keeps items in order and can be '
                                                               'processed one item at a time.\n'
                                                               '\n'
                                                               'Line 10: except json.JSONDecodeError:\n'
                                                               'Handle only a json.JSONDecodeError exception '
                                                               'here.\n'
                                                               '\n'
                                                               'Line 11: notes = []\n'
                                                               'Create the list shown and store it in notes. '
                                                               'The list keeps items in order and can be '
                                                               'processed one item at a time.\n'
                                                               '\n'
                                                               "Line 12: print('Notes ready:', len(notes))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Notes ready: 0',
                                                'output': 'Notes ready: 0',
                                                'title': 'Handle damaged JSON with a helpful fallback'},
                                               {'code': 'import json\n'
                                                        "note = {'text': 'Bring water'}\n"
                                                        'text = json.dumps(note, indent=2)\n'
                                                        'print(text)',
                                                'explanation': 'Purpose: Show the JSON text saved for a note '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import json\n'
                                                               'Load the module json so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               "Line 2: note = {'text': 'Bring water'}\n"
                                                               "Store {'text': 'Bring water'} in note so "
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               'Line 3: text = json.dumps(note, indent=2)\n'
                                                               'Store json.dumps(note, indent=2) in text so '
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: print(text)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: {\n'
                                                               '  "text": "Bring water"\n'
                                                               '}',
                                                'output': '{\n  "text": "Bring water"\n}',
                                                'title': 'Show the JSON text saved for a note'}],
                        'practice_questions': [{'answer': 'A notes app loads json from a named file, changes '
                                                          'a list, then saves it.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Notes should still exist after the application '
                                                          'closes.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'The file is relative to the current working '
                                                          'directory; json text can be invalid.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, variables, conditions, and basic loops from earlier '
                                         'worlds. The lesson briefly explains any new word before relying on '
                                         'it.',
                        'real_world_apps': 'A realistic use of this exact idea is a small personal notes '
                                           'list stored on the learner’s computer. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Load, change, and save the same JSON file so notes persist '
                                   'between runs. The file is relative to the current working directory; '
                                   'json text can be invalid The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'import json\n'
                                            'from pathlib import Path\n'
                                            '\n'
                                            "path = Path('notes.json')\n"
                                            'try:\n'
                                            "    with path.open('r', encoding='utf-8') as file:\n"
                                            '        notes = json.load(file)\n'
                                            'except FileNotFoundError:\n'
                                            '    notes = []\n'
                                            '\n'
                                            "notes.append({'text': 'Pack a map'})\n"
                                            "with path.open('w', encoding='utf-8') as file:\n"
                                            '    json.dump(notes, file, indent=2)\n'
                                            "print('Saved one new note to notes.json')",
                        'terminology': [{'definition': 'Keeping data after a program stops.',
                                         'term': 'Persistence'},
                                        {'definition': 'A text file holding serialized JSON data.',
                                         'term': 'JSON file'},
                                        {'definition': 'The folder from which a process resolves relative '
                                                       'paths.',
                                         'term': 'Working directory'}],
                        'title': 'World 8 Examination & Capstone: File-Based Notes Application'},
             'number': 85,
             'quizzes': [{'explanation': "data['score'] is 100 and data['multiplier'] is 1.5. 100 * 1.5 = "
                                         '150.0.',
                          'options': [{'explanation': 'Correct! 100 * 1.5 = 150.0.',
                                       'is_correct': True,
                                       'text': '150.0'},
                                      {'explanation': 'Incorrect. Multiplying by float yields float.',
                                       'is_correct': False,
                                       'text': '150'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '100'},
                                      {'explanation': 'Incorrect. Both values are numeric.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the combined file-parsing snippet?\n'
                                      '\n'
                                      'import json\n'
                                      'data = json.loads(\'{"score": 100, "multiplier": 1.5}\')\n'
                                      "print(data['score'] * data['multiplier'])"},
                         {'explanation': 'Opening a file that does not exist in read mode raises '
                                         'FileNotFoundError, which is caught and printed.',
                          'options': [{'explanation': 'Correct! FileNotFoundError is caught gracefully.',
                                       'is_correct': True,
                                       'text': 'Handled missing file'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect. The except block catches the error.',
                                       'is_correct': False,
                                       'text': 'Crash with unhandled exception'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'IOError: unhandled'}],
                          'question': 'What will be printed when running:\n'
                                      '\n'
                                      'try:\n'
                                      "    with open('nonexistent_file_xyz.txt') as f:\n"
                                      '        print(f.read())\n'
                                      'except FileNotFoundError:\n'
                                      "    print('Handled missing file')"}],
             'title': 'World 8 Examination & Capstone: File-Based Notes Application'}],
 'number': 8,
 'title': 'Error Handling and File Management'}
