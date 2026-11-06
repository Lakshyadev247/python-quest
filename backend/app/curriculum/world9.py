"""
Curriculum module: WORLD_9
Upgraded with pedagogical question scenarios and scaffolded starter code.
"""

WORLD_9 = {'description': 'Deep dive into imports, standard libraries, creating modules, __name__ guards, pip, and '
                'venv.',
 'final_project_desc': 'Build a modular multi-tool CLI utility package featuring math, text formatting, date '
                       'utilities, and statistical calculations.',
 'final_project_title': 'Utility Toolkit',
 'goal': "Master Python's module architecture, standard library, pip, virtual environments, and professional "
         'packaging.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Import Python’s math toolbox.\n2. Read a number and use its square-root tool.\n3. Print the answer with two digits after the decimal point.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["import math\nx = float(input())\nprint(f'{math.sqrt(x):.2f}')"],
                             'initial_code': '# Importing Standard Modules: math\n'
                                             'import math\n'
                                             '# Step 1: Read float x:\n'
                                             'x = float(input())\n'
                                             '\n'
                                             "# Step 2: Print f'{math.sqrt(x):.2f}' below:\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import math\n'
                                              '\n'
                                              'number = float(input())\n'
                                              "print(f'Square root: {math.sqrt(number):.2f}')",
                             'test_cases': [{'expected_output': 'Square root: 4.00',
                                             'input_data': '16\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Square root: 1.41',
                                             'input_data': '2\n',
                                             'is_hidden': False}],
                             'title': 'Math Module Explorer',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read an operation.\n2. For circle, read a radius and print the circle’s area.\n3. For hypot, read two side lengths and print the triangle’s longest side.\n4. Show both answers with two digits after the decimal point.\n5. For another operation, print UNKNOWN OPERATION.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import math\n'
                                       'op = input().strip()\n'
                                       "if op == 'circle':\n"
                                       '    r = float(input())\n'
                                       "    print(f'{math.pi * r * r:.2f}')\n"
                                       "elif op == 'hypot':\n"
                                       '    a = float(input())\n'
                                       '    b = float(input())\n'
                                       "    print(f'{math.hypot(a, b):.2f}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Geometry Toolkit Dispatcher\n'
                                             'import math\n'
                                             'op = input().strip()\n'
                                             '\n'
                                             '# Step 1: Handle circle (math.pi * r * r) and hypot '
                                             '(math.hypot(a, b)):\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import math\n'
                                              '\n'
                                              'operation = input().strip()\n'
                                              "if operation == 'circle':\n"
                                              '    radius = float(input())\n'
                                              "    print(f'Circle Area: {math.pi * radius ** 2:.2f}')\n"
                                              "elif operation == 'hypot':\n"
                                              '    x, y = map(float, input().split())\n'
                                              "    print(f'Hypotenuse: {math.hypot(x, y):.2f}')\n"
                                              'else:\n'
                                              "    print('UNKNOWN OPERATION')",
                             'test_cases': [{'expected_output': 'Circle Area: 78.54',
                                             'input_data': 'circle\n5\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Hypotenuse: 5.00',
                                             'input_data': 'hypot\n3 4\n',
                                             'is_hidden': False},
                                            {'expected_output': 'UNKNOWN OPERATION',
                                             'input_data': 'other\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Geometry Toolkit Dispatcher',
                             'xp_reward': 150}],
             'description': "Organize large software into manageable, reusable files using Python's module "
                            'system.',
             'lesson': {'common_mistakes': [{'fix': 'Import a module and use its qualified names to avoid '
                                                    'name collisions.',
                                             'mistake': 'standard-library modules ship with Python; '
                                                        'third-party packages must be installed',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Common tools should not need to be '
                                                'rewritten for every project. This is the practical problem '
                                                'the feature solves.\n'
                                                '\n'
                                                'What it means: A module is usually a python .py file that '
                                                'has its own namespace. Python uses this idea to import '
                                                'module makes its names available with a module prefix\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Standard-library modules ship with python; '
                                                'third-party packages must be installed. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': '3.14\n9.0',
                        'id': 86,
                        'introduction': 'Why learn this? Common tools should not need to be rewritten for '
                                        'every project. In this lesson, we will see a module is usually a '
                                        'Python .py file that has its own namespace, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a module is usually a Python .py file that has its '
                                                'own namespace in your own words.',
                                                'Trace a small What Are Modules? example and predict what '
                                                'Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'standard-library modules ship with Python; third-party '
                                                'packages must be installed.'],
                        'level_id': 86,
                        'line_by_line': [{'code': 'import math',
                                          'explanation': 'Load the module math so this file can use its '
                                                         'tools. An alias, if present, becomes the name used '
                                                         'below.',
                                          'line': '1'},
                                         {'code': 'print(round(math.pi, 2))',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': 'print(math.sqrt(81))',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'}],
                        'practical_examples': [{'code': 'import math\n'
                                                        'print(round(math.pi, 2))\n'
                                                        'print(math.sqrt(81))',
                                                'explanation': 'Purpose: Use a module namespace shows the '
                                                               'current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import math\n'
                                                               'Load the module math so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               'Line 2: print(round(math.pi, 2))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: print(math.sqrt(81))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 3.14\n'
                                                               '9.0',
                                                'output': '3.14\n9.0',
                                                'title': 'Use a module namespace'},
                                               {'code': 'import random\n'
                                                        'rng = random.Random(4)\n'
                                                        "print('Dice roll result:', rng.randint(1, 6))",
                                                'explanation': 'Purpose: Use a seeded random example for '
                                                               'repeatable practice shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import random\n'
                                                               'Load the module random so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               'Line 2: rng = random.Random(4)\n'
                                                               'Store random.Random(4) in rng so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 3: print('Dice roll result:', "
                                                               'rng.randint(1, 6))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Dice roll result: 2',
                                                'output': 'Dice roll result: 2',
                                                'title': 'Use a seeded random example for repeatable '
                                                         'practice'},
                                               {'code': 'from collections import Counter\n'
                                                        "colors = ['blue', 'red', 'blue']\n"
                                                        'counts = Counter(colors)\n'
                                                        "print(counts['blue'])",
                                                'explanation': 'Purpose: Use a standard-library collection '
                                                               'helper shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: from collections import Counter\n'
                                                               'Import the named tool(s) from collections; '
                                                               'the names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               "Line 2: colors = ['blue', 'red', 'blue']\n"
                                                               'Create the list shown and store it in '
                                                               'colors. The list keeps items in order and '
                                                               'can be processed one item at a time.\n'
                                                               '\n'
                                                               'Line 3: counts = Counter(colors)\n'
                                                               'Store Counter(colors) in counts so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 4: print(counts['blue'])\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 2',
                                                'output': '2',
                                                'title': 'Use a standard-library collection helper'}],
                        'practice_questions': [{'answer': 'A module is usually a python .py file that has '
                                                          'its own namespace.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Common tools should not need to be rewritten for '
                                                          'every project.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Standard-library modules ship with python; '
                                                          'third-party packages must be installed.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is using math, datetime, or '
                                           'collections tools. The same pattern helps a larger program stay '
                                           'clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Import a module and use its qualified names to avoid name '
                                   'collisions. Standard-library modules ship with python; third-party '
                                   'packages must be installed The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'import math\nprint(round(math.pi, 2))\nprint(math.sqrt(81))',
                        'terminology': [{'definition': 'A Python file that can provide names to other code.',
                                         'term': 'Module'},
                                        {'definition': 'The set of names available under a module or scope.',
                                         'term': 'Namespace'},
                                        {'definition': 'Modules included with a Python installation.',
                                         'term': 'Standard library'}],
                        'title': 'What Are Modules?'},
             'number': 86,
             'quizzes': [{'explanation': 'math.sqrt(16) is 4.0 (float) and math.floor(3.9) is 3 (integer).',
                          'options': [{'explanation': 'Correct! math.sqrt returns float; floor rounds down '
                                                      'to integer.',
                                       'is_correct': True,
                                       'text': '4.0 3'},
                                      {'explanation': 'Incorrect. sqrt returns float and floor rounds down.',
                                       'is_correct': False,
                                       'text': '4 4'},
                                      {'explanation': 'Incorrect. sqrt(16) produces 4.0.',
                                       'is_correct': False,
                                       'text': '4 3'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '4.0 4'}],
                          'question': 'What is the output of: print(math.sqrt(16), math.floor(3.9))?'},
                         {'explanation': 'math.ceil() rounds upwards to the nearest integer: 5.',
                          'options': [{'explanation': 'Correct! ceil(4.1) rounds up to 5.',
                                       'is_correct': True,
                                       'text': '5'},
                                      {'explanation': 'Incorrect. That is floor().',
                                       'is_correct': False,
                                       'text': '4'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '4.1'},
                                      {'explanation': 'Incorrect. ceil returns int in Python 3.',
                                       'is_correct': False,
                                       'text': '5.0'}],
                          'question': 'What is the output of: print(math.ceil(4.1))?'}],
             'title': 'What Are Modules?'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read several whole numbers on one line.\n2. Use Python’s statistics tools to print their average to one decimal place, then print the number that appears most often.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['from statistics import mean, mode\n'
                                       'nums = [int(x) for x in input().split()]\n'
                                       "print(f'Mean: {mean(nums):.1f}')\n"
                                       "print(f'Mode: {mode(nums)}')"],
                             'initial_code': '# Selective Imports: from ... import\n'
                                             'from statistics import mean, mode\n'
                                             '# Step 1: Read numbers:\n'
                                             'nums = [int(x) for x in input().split()]\n'
                                             '\n'
                                             '# Step 2: Print Mean and Mode below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'from statistics import mean, mode\n'
                                              '\n'
                                              'values = [int(value) for value in input().split()]\n'
                                              "print(f'Mean: {mean(values):.1f}')\n"
                                              "print(f'Mode: {mode(values)}')",
                             'test_cases': [{'expected_output': 'Mean: 20.0\nMode: 20',
                                             'input_data': '10 20 20 30\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Mean: 8.0\nMode: 5',
                                             'input_data': '5 5 8 14\n',
                                             'is_hidden': False}],
                             'title': 'Selective Stats Calculator',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read two whole numbers.\n2. Use the math tools imported under their new, descriptive names to print their greatest common divisor and least common multiple, as shown.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['from math import gcd as greatest_common_divisor, lcm as '
                                       'least_common_multiple\n'
                                       'a = int(input())\n'
                                       'b = int(input())\n'
                                       "print(f'GCD: {greatest_common_divisor(a, b)}')\n"
                                       "print(f'LCM: {least_common_multiple(a, b)}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Aliased GCD and LCM Engine\n'
                                             'from math import gcd as greatest_common_divisor, lcm as '
                                             'least_common_multiple\n'
                                             'a = int(input())\n'
                                             'b = int(input())\n'
                                             '\n'
                                             '# Step 1: Print GCD and LCM using aliased names below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'from math import gcd as greatest_common_divisor, lcm as '
                                              'least_common_multiple\n'
                                              '\n'
                                              'a, b = map(int, input().split())\n'
                                              "print(f'GCD({a}, {b}): {greatest_common_divisor(a, b)}')\n"
                                              "print(f'LCM({a}, {b}): {least_common_multiple(a, b)}')",
                             'test_cases': [{'expected_output': 'GCD(12, 18): 6\nLCM(12, 18): 36',
                                             'input_data': '12 18\n',
                                             'is_hidden': False},
                                            {'expected_output': 'GCD(15, 25): 5\nLCM(15, 25): 75',
                                             'input_data': '15 25\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Aliased GCD and LCM Engine',
                             'xp_reward': 150}],
             'description': 'Master all import patterns: full imports, selective imports, renaming with as, '
                            'and avoiding wildcard imports.',
             'lesson': {'common_mistakes': [{'fix': 'Prefer explicit imports and aliases that make each '
                                                    'name’s source clear.',
                                             'mistake': 'wildcard imports are allowed but can hide where '
                                                        'names came from',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Different import styles trade clarity '
                                                'for brevity. This is the practical problem the feature '
                                                'solves.\n'
                                                '\n'
                                                'What it means: An alias is another local name for an '
                                                'imported module or object. Python uses this idea to import '
                                                'math as m keeps a module prefix; from math import sqrt '
                                                'imports sqrt directly\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Wildcard imports are allowed but can hide '
                                                'where names came from. If you change the example’s input or '
                                                'value, check this rule again because it can change the '
                                                'result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Floor 7.8: 7\nCeil 7.2: 8',
                        'id': 87,
                        'introduction': 'Why learn this? Different import styles trade clarity for brevity. '
                                        'In this lesson, we will see an alias is another local name for an '
                                        'imported module or object, follow how Python handles it, and '
                                        'practice a small example you can change yourself.',
                        'learning_objectives': ['Explain an alias is another local name for an imported '
                                                'module or object in your own words.',
                                                'Trace a small Import Variations (from ... import & Aliases) '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'wildcard imports are allowed but can hide where names came '
                                                'from.'],
                        'level_id': 87,
                        'line_by_line': [{'code': 'from math import floor, ceil',
                                          'explanation': 'Import the named tool(s) from math; the names can '
                                                         'then be used directly in this file.',
                                          'line': '1'},
                                         {'code': "print('Floor 7.8:', floor(7.8))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': "print('Ceil 7.2:', ceil(7.2))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'}],
                        'practical_examples': [{'code': 'from math import floor, ceil\n'
                                                        "print('Floor 7.8:', floor(7.8))\n"
                                                        "print('Ceil 7.2:', ceil(7.2))",
                                                'explanation': 'Purpose: Example 1: Clean mathematical '
                                                               'imports shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: from math import floor, ceil\n'
                                                               'Import the named tool(s) from math; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               "Line 2: print('Floor 7.8:', floor(7.8))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 3: print('Ceil 7.2:', ceil(7.2))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Floor 7.8: 7\n'
                                                               'Ceil 7.2: 8',
                                                'output': 'Floor 7.8: 7\nCeil 7.2: 8',
                                                'title': 'Example 1: Clean mathematical imports'},
                                               {'code': 'import datetime as dt\n'
                                                        'now = dt.date(2026, 11, 3)\n'
                                                        "print('Year:', now.year, 'Month:', now.month)",
                                                'explanation': 'Purpose: Example 2: Abbreviating module '
                                                               "names with 'as' shows the current lesson "
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import datetime as dt\n'
                                                               'Load the module datetime so this file can '
                                                               'use its tools. An alias, if present, becomes '
                                                               'the name used below.\n'
                                                               '\n'
                                                               'Line 2: now = dt.date(2026, 11, 3)\n'
                                                               'Store dt.date(2026, 11, 3) in now so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 3: print('Year:', now.year, 'Month:', "
                                                               'now.month)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Year: 2026 Month: 11',
                                                'output': 'Year: 2026 Month: 11',
                                                'title': "Example 2: Abbreviating module names with 'as'"},
                                               {'code': 'from math import sin as math_sin\n'
                                                        '# Prevents conflict if your code already defines a '
                                                        'sin function\n'
                                                        "print('Sine of 0:', math_sin(0))",
                                                'explanation': 'Purpose: Example 3: Avoiding naming '
                                                               'collisions with aliases shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: from math import sin as math_sin\n'
                                                               'Import the named tool(s) from math; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 2: # Prevents conflict if your code '
                                                               'already defines a sin function\n'
                                                               'This comment is a note for the reader. '
                                                               'Python skips it; it does not run.\n'
                                                               '\n'
                                                               "Line 3: print('Sine of 0:', math_sin(0))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Sine of 0: 0.0',
                                                'output': 'Sine of 0: 0.0',
                                                'title': 'Example 3: Avoiding naming collisions with '
                                                         'aliases'}],
                        'practice_questions': [{'answer': 'An alias is another local name for an imported '
                                                          'module or object.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Different import styles trade clarity for '
                                                          'brevity.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Wildcard imports are allowed but can hide where '
                                                          'names came from.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is using datetime as dt in a '
                                           'date-focused program. The same pattern helps a larger program '
                                           'stay clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Prefer explicit imports and aliases that make each name’s '
                                   'source clear. Wildcard imports are allowed but can hide where names came '
                                   'from The practical example and its line-by-line walkthrough show the '
                                   'idea in action.',
                        'syntax_breakdown': 'from math import floor, ceil\n'
                                            "print('Floor 7.8:', floor(7.8))\n"
                                            "print('Ceil 7.2:', ceil(7.2))",
                        'terminology': [{'definition': 'An alternate local name for an imported module or '
                                                       'item.',
                                         'term': 'Alias'},
                                        {'definition': 'An import naming only the tools the file needs.',
                                         'term': 'Explicit import'},
                                        {'definition': 'An import using * that can hide where names came '
                                                       'from.',
                                         'term': 'Wildcard import'}],
                        'title': 'Import Variations (from ... import & Aliases)'},
             'number': 87,
             'quizzes': [{'explanation': 'random.choice() selects and returns one random element from the '
                                         'non-empty sequence.',
                          'options': [{'explanation': 'Correct! choice() returns one item from the sequence.',
                                       'is_correct': True,
                                       'text': 'A single element randomly selected from the list'},
                                      {'explanation': 'Incorrect. That is random.shuffle().',
                                       'is_correct': False,
                                       'text': 'A shuffled list of all 3 elements'},
                                      {'explanation': 'Incorrect. That is random.sample().',
                                       'is_correct': False,
                                       'text': 'A list of 2 random elements'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'An integer index'}],
                          'question': "What is the output of random.choice(['Warrior', 'Mage', 'Rogue'])?"},
                         {'explanation': 'random.randint(a, b) includes both endpoints: 1, 2, or 3.',
                          'options': [{'explanation': 'Correct! randint is inclusive on both ends.',
                                       'is_correct': True,
                                       'text': '1, 2, or 3 (both 1 and 3 are inclusive)'},
                                      {'explanation': 'Incorrect. That is randrange(1, 3).',
                                       'is_correct': False,
                                       'text': '1 or 2 (3 is exclusive)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '0, 1, or 2'},
                                      {'explanation': 'Incorrect. randint returns integers.',
                                       'is_correct': False,
                                       'text': 'A float between 1.0 and 3.0'}],
                          'question': 'What are the possible return values of random.randint(1, 3)?'}],
             'title': 'Import Variations (from ... import & Aliases)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a decimal number.\n2. Print its floor, the whole number at or below it, and its ceiling, the whole number at or above it.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['import math\n'
                                       'val = float(input())\n'
                                       "print(f'Floor: {math.floor(val)}')\n"
                                       "print(f'Ceil: {math.ceil(val)}')"],
                             'initial_code': '# math.floor() and math.ceil()\n'
                                             'import math\n'
                                             '# Step 1: Read float val:\n'
                                             'val = float(input())\n'
                                             '\n'
                                             '# Step 2: Print Floor and Ceil below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import math\n'
                                              '\n'
                                              'number = float(input())\n'
                                              "print(f'Floor: {math.floor(number)}')\n"
                                              "print(f'Ceil: {math.ceil(number)}')",
                             'test_cases': [{'expected_output': 'Floor: 16\nCeil: 17',
                                             'input_data': '16.4\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Floor: 9\nCeil: 9',
                                             'input_data': '9.0\n',
                                             'is_hidden': False}],
                             'title': 'Rounding Boundaries: floor and ceil',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Set the random seed to 42, read an upper limit, and print one repeatable random integer from 1 through that limit.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import random\n'
                                       'random.seed(42)\n'
                                       'upper_bound = int(input())\n'
                                       'print(random.randint(1, upper_bound))'],
                             'initial_code': '# ⚔️ Boss Challenge: Seeded Pseudo-Random Generator\n'
                                             'import random\n'
                                             '# Step 1: Seed generator:\n'
                                             'random.seed(42)\n'
                                             'n = int(input())\n'
                                             '\n'
                                             '# Step 2: Print random.randint(1, n) below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import random\n'
                                              'random.seed(42)\n'
                                              'upper_bound = int(input())\n'
                                              'print(random.randint(1, upper_bound))',
                             'test_cases': [{'expected_output': '6', 'input_data': '6\n', 'is_hidden': False},
                                            {'expected_output': '1',
                                             'input_data': '4\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Seeded Pseudo-Random Number',
                             'xp_reward': 150}],
             'description': "Explore Python's 'batteries included' philosophy: random, datetime, and "
                            'collections.',
             'lesson': {'common_mistakes': [{'fix': 'Use a standard-library tool suited to the task and its '
                                                    'risk.',
                                             'mistake': 'random is suitable for ordinary games, not '
                                                        'passwords or security tokens; use secrets for '
                                                        'security',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Python ships useful tested tools for '
                                                'common tasks. This is the practical problem the feature '
                                                'solves.\n'
                                                '\n'
                                                'What it means: The standard library is the set of modules '
                                                'distributed with python. Python uses this idea to random, '
                                                'datetime, and collections provide different ready-made '
                                                'tools\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Random is suitable for ordinary games, not '
                                                'passwords or security tokens; use secrets for security. If '
                                                'you change the example’s input or value, check this rule '
                                                'again because it can change the result or the path Python '
                                                'takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Platform identifier: win32\nPython version major: 3',
                        'id': 88,
                        'introduction': 'Why learn this? Python ships useful tested tools for common tasks. '
                                        'In this lesson, we will see the standard library is the set of '
                                        'modules distributed with Python, follow how Python handles it, and '
                                        'practice a small example you can change yourself.',
                        'learning_objectives': ['Explain the standard library is the set of modules '
                                                'distributed with Python in your own words.',
                                                'Trace a small The Python Standard Library example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'random is suitable for ordinary games, not passwords or '
                                                'security tokens; use secrets for security.'],
                        'level_id': 88,
                        'line_by_line': [{'code': 'import sys',
                                          'explanation': 'Load the module sys so this file can use its '
                                                         'tools. An alias, if present, becomes the name used '
                                                         'below.',
                                          'line': '1'},
                                         {'code': "print('Platform identifier:', sys.platform)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': "print('Python version major:', sys.version_info.major)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'}],
                        'practical_examples': [{'code': 'import sys\n'
                                                        "print('Platform identifier:', sys.platform)\n"
                                                        "print('Python version major:', "
                                                        'sys.version_info.major)',
                                                'explanation': 'Purpose: Example 1: Operating system '
                                                               'platform detection shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import sys\n'
                                                               'Load the module sys so this file can use its '
                                                               'tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               "Line 2: print('Platform identifier:', "
                                                               'sys.platform)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 3: print('Python version major:', "
                                                               'sys.version_info.major)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Platform identifier: win32\n'
                                                               'Python version major: 3\n'
                                                               '\n'
                                                               'The platform text differs across operating '
                                                               'systems; win32 is the value shown on '
                                                               'Windows.',
                                                'output': 'Platform identifier: win32\n'
                                                          'Python version major: 3',
                                                'title': 'Example 1: Operating system platform detection'},
                                               {'code': 'import time\n'
                                                        'start = time.time()\n'
                                                        'time.sleep(0.01)  # Brief pause\n'
                                                        'elapsed = time.time() - start\n'
                                                        "print('Operation completed in under 1 second:', "
                                                        'elapsed < 1.0)',
                                                'explanation': 'Purpose: Example 2: Measuring elapsed '
                                                               'execution time shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import time\n'
                                                               'Load the module time so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               'Line 2: start = time.time()\n'
                                                               'Store time.time() in start so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 3: time.sleep(0.01)  # Brief pause\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 4: elapsed = time.time() - start\n'
                                                               'Calculate or compare time.time() - start, '
                                                               'then save the result in elapsed.\n'
                                                               '\n'
                                                               "Line 5: print('Operation completed in under "
                                                               "1 second:', elapsed < 1.0)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Operation completed in under 1 '
                                                               'second: True',
                                                'output': 'Operation completed in under 1 second: True',
                                                'title': 'Example 2: Measuring elapsed execution time'},
                                               {'code': 'import random\n'
                                                        "deck = ['A', 'K', 'Q', 'J']\n"
                                                        'random.shuffle(deck)\n'
                                                        "print('Deck count:', len(deck))",
                                                'explanation': 'Purpose: Example 3: Shuffling collections '
                                                               'with random.shuffle shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import random\n'
                                                               'Load the module random so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               "Line 2: deck = ['A', 'K', 'Q', 'J']\n"
                                                               'Create the list shown and store it in deck. '
                                                               'The list keeps items in order and can be '
                                                               'processed one item at a time.\n'
                                                               '\n'
                                                               'Line 3: random.shuffle(deck)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 4: print('Deck count:', len(deck))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Deck count: 4',
                                                'output': 'Deck count: 4',
                                                'title': 'Example 3: Shuffling collections with '
                                                         'random.shuffle'}],
                        'practice_questions': [{'answer': 'The standard library is the set of modules '
                                                          'distributed with python.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Python ships useful tested tools for common '
                                                          'tasks.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Random is suitable for ordinary games, not '
                                                          'passwords or security tokens; use secrets for '
                                                          'security.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is counting words with '
                                           'Counter or selecting a game event. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Use a standard-library tool suited to the task and its risk. '
                                   'Random is suitable for ordinary games, not passwords or security tokens; '
                                   'use secrets for security The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'import sys\n'
                                            "print('Platform identifier:', sys.platform)\n"
                                            "print('Python version major:', sys.version_info.major)",
                        'terminology': [{'definition': 'Tools shipped with Python.',
                                         'term': 'Standard library'},
                                        {'definition': 'A separately installed tool that does not ship with '
                                                       'Python.',
                                         'term': 'Third-party package'},
                                        {'definition': 'A standard-library module for security-sensitive '
                                                       'random values.',
                                         'term': 'secrets'}],
                        'title': 'The Python Standard Library'},
             'number': 88,
             'quizzes': [{'explanation': 'd.year is 2026, d.month is 11, and d.day is 2.',
                          'options': [{'explanation': 'Correct! Extracts year, month, and day components.',
                                       'is_correct': True,
                                       'text': '2026 11 2'},
                                      {'explanation': 'Incorrect. Passing separate arguments prints them '
                                                      'space-separated.',
                                       'is_correct': False,
                                       'text': '2026-11-02'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '11 2 2026'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of datetime attribute access?\n'
                                      '\n'
                                      'from datetime import datetime\n'
                                      'd = datetime(2026, 11, 2, 10, 30)\n'
                                      'print(d.year, d.month, d.day)'},
                         {'explanation': '%Y is 4-digit year, %m is 2-digit month, %d is 2-digit day (e.g. '
                                         "'2026-11-02').",
                          'options': [{'explanation': 'Correct! strftime formats datetime objects into '
                                                      'strings.',
                                       'is_correct': True,
                                       'text': "A string formatted like '2026-11-02'"},
                                      {'explanation': 'Incorrect. strftime returns a string.',
                                       'is_correct': False,
                                       'text': 'A datetime object'},
                                      {'explanation': 'Incorrect. That is .timestamp().',
                                       'is_correct': False,
                                       'text': 'A Unix timestamp float'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'A tuple of integers'}],
                          'question': "What does datetime.now().strftime('%Y-%m-%d') produce?"}],
             'title': 'The Python Standard Library'},
            {'challenges': [{'description': 'Your task, step by step:\n1. A Python module can hold reusable functions.\n2. Define format_name in this file and call it only inside the main guard.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def format_name(name):\n'
                                       '    return name.title()\n'
                                       "if __name__ == '__main__':\n"
                                       "    print(format_name('python quest'))"],
                             'initial_code': '# The datetime Module: Date Formatting\n'
                                             'from datetime import date\n'
                                             '# Step 1: Read year, month, day:\n'
                                             'y = int(input())\n'
                                             'm = int(input())\n'
                                             'd = int(input())\n'
                                             '\n'
                                             '# Step 2: Create date and print strftime below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def format_name(name):\n'
                                              '    return name.title()\n'
                                              "if __name__ == '__main__':\n"
                                              "    print(format_name('python quest'))",
                             'test_cases': [{'expected_output': 'Python Quest',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Create and Call a Module Function',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Define a reusable add function.\n2. Use the __main__ guard to run the example only when this file is started directly.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def add(a, b):\n'
                                       '    return a + b\n'
                                       "if __name__ == '__main__':\n"
                                       '    print(add(12, 8))'],
                             'initial_code': '# ⚔️ Boss Challenge: Calendar Day Span Calculator\n'
                                             'from datetime import datetime\n'
                                             "fmt = '%Y-%m-%d'\n"
                                             '\n'
                                             '# Step 1: Parse d1 and d2 with strptime:\n'
                                             '\n'
                                             '# Step 2: Compute diff = abs((d2 - d1).days) and print:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def add(a, b):\n'
                                              '    return a + b\n'
                                              "if __name__ == '__main__':\n"
                                              '    print(add(12, 8))',
                             'test_cases': [{'expected_output': '20', 'input_data': '', 'is_hidden': False}],
                             'title': 'Boss Challenge: Protect the Module Entry Point',
                             'xp_reward': 150}],
             'description': 'Build reusable custom modules and protect executable entrypoints using if '
                            "__name__ == '__main__':.",
             'lesson': {'common_mistakes': [{'fix': 'Put reusable definitions at module level and direct-run '
                                                    'work under the __main__ guard.',
                                             'mistake': 'a guard does not prevent top-level code above it '
                                                        'from running on import',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A project can keep reusable code '
                                                'separate from its run-on-start behavior. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: A module is a .py file; __name__ is __main__ '
                                                'when that file is run directly. Python uses this idea to '
                                                'when imported, the module name is its import name; an if '
                                                'guard runs only in direct execution\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: A guard does not prevent top-level code '
                                                'above it from running on import. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Hello from greeter',
                        'id': 89,
                        'introduction': 'Why learn this? A project can keep reusable code separate from its '
                                        'run-on-start behavior. In this lesson, we will see a module is a '
                                        '.py file; __name__ is __main__ when that file is run directly, '
                                        'follow how Python handles it, and practice a small example you can '
                                        'change yourself.',
                        'learning_objectives': ['Explain a module is a .py file; __name__ is __main__ when '
                                                'that file is run directly in your own words.',
                                                'Trace a small Creating Your Own Modules and __main__ '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: a '
                                                'guard does not prevent top-level code above it from running '
                                                'on import.'],
                        'level_id': 89,
                        'line_by_line': [{'code': '# File: greeter.py',
                                          'explanation': 'This label says the following code belongs in the '
                                                         'separate file greeter.py; it is not a Python '
                                                         'instruction.',
                                          'line': '1'},
                                         {'code': 'def greet():',
                                          'explanation': 'Define a function named greet. Its parameters '
                                                         '(none) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '2'},
                                         {'code': "    print('Hello from greeter')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '4'},
                                         {'code': "if __name__ == '__main__':",
                                          'explanation': "Check whether __name__ == '__main__' is true. If "
                                                         'it is, run the indented block; otherwise Python '
                                                         'skips that block.',
                                          'line': '5'},
                                         {'code': '    greet()',
                                          'explanation': 'Call greet now. Python runs its body, and any '
                                                         'returned result is available to the caller.',
                                          'line': '6'}],
                        'practical_examples': [{'code': '# File: greeter.py\n'
                                                        'def greet():\n'
                                                        "    print('Hello from greeter')\n"
                                                        '\n'
                                                        "if __name__ == '__main__':\n"
                                                        '    greet()',
                                                'explanation': 'Purpose: A guarded module can run directly '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'These labels divide the example into '
                                                               'separate project files. Create each named '
                                                               'file, then run app.py to get the output '
                                                               'shown here.\n'
                                                               '\n'
                                                               'Line 1: # File: greeter.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file greeter.py; it is not a '
                                                               'Python instruction.\n'
                                                               '\n'
                                                               'Line 2: def greet():\n'
                                                               'Define a function named greet. Its '
                                                               'parameters (none) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 3: print('Hello from greeter')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 5: if __name__ == '__main__':\n"
                                                               "Check whether __name__ == '__main__' is "
                                                               'true. If it is, run the indented block; '
                                                               'otherwise Python skips that block.\n'
                                                               '\n'
                                                               'Line 6: greet()\n'
                                                               'Call greet now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Hello from greeter',
                                                'output': 'Hello from greeter',
                                                'title': 'A guarded module can run directly'},
                                               {'code': '# Save greet() in greeter.py, with its __main__ '
                                                        'guard.\n'
                                                        'import greeter\n'
                                                        "print('Importer is running')",
                                                'explanation': 'Purpose: Importing skips the guarded demo '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: # Save greet() in greeter.py, with '
                                                               'its __main__ guard.\n'
                                                               'This comment is a note for the reader. '
                                                               'Python skips it; it does not run.\n'
                                                               '\n'
                                                               'Line 2: import greeter\n'
                                                               'Load the module greeter so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               "Line 3: print('Importer is running')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Importer is running',
                                                'output': 'Importer is running',
                                                'title': 'Importing skips the guarded demo'},
                                               {'code': '# File: tools.py\n'
                                                        'def square(number):\n'
                                                        '    return number * number\n'
                                                        '\n'
                                                        "if __name__ == '__main__':\n"
                                                        '    print(square(4))',
                                                'explanation': 'Purpose: Keep reusable functions outside the '
                                                               'guard shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'These labels divide the example into '
                                                               'separate project files. Create each named '
                                                               'file, then run app.py to get the output '
                                                               'shown here.\n'
                                                               '\n'
                                                               'Line 1: # File: tools.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file tools.py; it is not a '
                                                               'Python instruction.\n'
                                                               '\n'
                                                               'Line 2: def square(number):\n'
                                                               'Define a function named square. Its '
                                                               'parameters (number) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: return number * number\n'
                                                               'Send number * number back to the caller and '
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 5: if __name__ == '__main__':\n"
                                                               "Check whether __name__ == '__main__' is "
                                                               'true. If it is, run the indented block; '
                                                               'otherwise Python skips that block.\n'
                                                               '\n'
                                                               'Line 6: print(square(4))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 16',
                                                'output': '16',
                                                'title': 'Keep reusable functions outside the guard'}],
                        'practice_questions': [{'answer': 'A module is a .py file; __name__ is __main__ when '
                                                          'that file is run directly.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A project can keep reusable code separate from '
                                                          'its run-on-start behavior.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'A guard does not prevent top-level code above it '
                                                          'from running on import.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a helper file used both as '
                                           'a script and as an import. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Put reusable definitions at module level and direct-run work '
                                   'under the __main__ guard. A guard does not prevent top-level code above '
                                   'it from running on import The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': '# File: greeter.py\n'
                                            'def greet():\n'
                                            "    print('Hello from greeter')\n"
                                            '\n'
                                            "if __name__ == '__main__':\n"
                                            '    greet()',
                        'terminology': [{'definition': 'A module variable; it is __main__ when its file is '
                                                       'run directly.',
                                         'term': '__name__'},
                                        {'definition': 'Load a module so its names can be used.',
                                         'term': 'Import'},
                                        {'definition': 'An if statement that runs code only when the file is '
                                                       'executed directly.',
                                         'term': 'Main guard'}],
                        'title': 'Creating Your Own Modules and __main__'},
             'number': 89,
             'quizzes': [{'explanation': 'When executed directly as the entry point script, Python assigns '
                                         "'__main__' to `__name__`.",
                          'options': [{'explanation': "Correct! The entry file has __name__ == '__main__' .",
                                       'is_correct': True,
                                       'text': "'__main__'"},
                                      {'explanation': 'Incorrect. That is the module name only when '
                                                      'imported.',
                                       'is_correct': False,
                                       'text': "'app'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': "'__app__'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': "'root'"}],
                          'question': 'What is the value of `__name__` when a Python file is run directly '
                                      'from the terminal with `python app.py`?'},
                         {'explanation': 'It prevents script execution code from running when the file is '
                                         'imported as a module by another file.',
                          'options': [{'explanation': 'Correct! It isolates executable CLI logic from '
                                                      'reusable declarations.',
                                       'is_correct': True,
                                       'text': 'To allow the file to be imported as a library without '
                                               'auto-executing script code'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To make the file run in multithreaded mode'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To hide functions from external users'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To satisfy the Python syntax compiler'}],
                          'question': "Why do Python developers write `if __name__ == '__main__':` in "
                                      'scripts?'}],
             'title': 'Creating Your Own Modules and __main__'},
            {'challenges': [{'description': 'Your task, step by step:\n1. A package is a folder of Python modules.\n2. Print the two files in this example package, including its __init__.py file.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["package_files = ['quest_tools/__init__.py', 'quest_tools/text.py']\n"
                                       'for path in package_files:\n'
                                       '    print(path)'],
                             'initial_code': '# Inspecting Python Runtime with sys\n'
                                             'import sys\n'
                                             '# Step 1: Print major and minor version below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "package_files = ['quest_tools/__init__.py', "
                                              "'quest_tools/text.py']\n"
                                              'for path in package_files:\n'
                                              '    print(path)',
                             'test_cases': [{'expected_output': 'quest_tools/__init__.py\n'
                                                                'quest_tools/text.py',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Recognize a Python Package',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Show how a function inside a package module is imported and called.\n2. Print the example import and result.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["module_path = 'from quest_tools.text import shout'\n"
                                       'print(module_path)\n'
                                       "print('QUEST!')"],
                             'initial_code': '# ⚔️ Boss Challenge: File Path Existence Verifier\n'
                                             'import os\n'
                                             'path = input().strip()\n'
                                             '\n'
                                             '# Step 1: Print os.path.exists(path) below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "module_path = 'from quest_tools.text import shout'\n"
                                              'print(module_path)\n'
                                              "print('QUEST!')",
                             'test_cases': [{'expected_output': 'from quest_tools.text import shout\nQUEST!',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Package Import Path',
                             'xp_reward': 150}],
             'description': 'Structure multi-file directories into cohesive packages with sub-modules and '
                            '__init__.py.',
             'lesson': {'common_mistakes': [{'fix': 'A package is a folder of modules; __init__.py is '
                                                    'conventional, not universally required.',
                                             'mistake': 'regular packages commonly include __init__.py, but '
                                                        'namespace packages may omit it',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Larger projects need folders that '
                                                'group related modules. This is the practical problem the '
                                                'feature solves.\n'
                                                '\n'
                                                'What it means: A package organizes modules in a directory; '
                                                'a module is one file. Python uses this idea to __init__.py '
                                                'can run package setup and expose selected names; import '
                                                'through the package path\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Regular packages commonly include '
                                                '__init__.py, but namespace packages may omit it. If you '
                                                'change the example’s input or value, check this rule again '
                                                'because it can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'HELLO',
                        'id': 90,
                        'introduction': 'Why learn this? Larger projects need folders that group related '
                                        'modules. In this lesson, we will see a package organizes modules in '
                                        'a directory; a module is one file, follow how Python handles it, '
                                        'and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a package organizes modules in a directory; a '
                                                'module is one file in your own words.',
                                                'Trace a small Python Packages and __init__.py example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'regular packages commonly include __init__.py, but '
                                                'namespace packages may omit it.'],
                        'level_id': 90,
                        'line_by_line': [{'code': '# Folder: mytools/',
                                          'explanation': 'This label names the folder for the files shown '
                                                         'next: mytools/. Create that folder in the project.',
                                          'line': '1'},
                                         {'code': '# File: mytools/__init__.py',
                                          'explanation': 'This label says the following code belongs in the '
                                                         'separate file mytools/__init__.py; it is not a '
                                                         'Python instruction.',
                                          'line': '2'},
                                         {'code': 'from .text import shout',
                                          'explanation': 'Import the named tool(s) from .text; the names can '
                                                         'then be used directly in this file.',
                                          'line': '3'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '4'},
                                         {'code': '# File: mytools/text.py',
                                          'explanation': 'This label says the following code belongs in the '
                                                         'separate file mytools/text.py; it is not a Python '
                                                         'instruction.',
                                          'line': '5'},
                                         {'code': 'def shout(message):',
                                          'explanation': 'Define a function named shout. Its parameters '
                                                         '(message) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '6'},
                                         {'code': '    return message.upper()',
                                          'explanation': 'Send message.upper() back to the caller and end '
                                                         'this function call.',
                                          'line': '7'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '8'},
                                         {'code': '# File: app.py',
                                          'explanation': 'This label says the following code belongs in the '
                                                         'separate file app.py; it is not a Python '
                                                         'instruction.',
                                          'line': '9'},
                                         {'code': 'from mytools import shout',
                                          'explanation': 'Import the named tool(s) from mytools; the names '
                                                         'can then be used directly in this file.',
                                          'line': '10'},
                                         {'code': "print(shout('hello'))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '11'}],
                        'practical_examples': [{'code': '# Folder: mytools/\n'
                                                        '# File: mytools/__init__.py\n'
                                                        'from .text import shout\n'
                                                        '\n'
                                                        '# File: mytools/text.py\n'
                                                        'def shout(message):\n'
                                                        '    return message.upper()\n'
                                                        '\n'
                                                        '# File: app.py\n'
                                                        'from mytools import shout\n'
                                                        "print(shout('hello'))",
                                                'explanation': 'Purpose: A package groups related modules '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'These labels divide the example into '
                                                               'separate project files. Create each named '
                                                               'file, then run app.py to get the output '
                                                               'shown here.\n'
                                                               '\n'
                                                               'Line 1: # Folder: mytools/\n'
                                                               'This label names the folder for the files '
                                                               'shown next: mytools/. Create that folder in '
                                                               'the project.\n'
                                                               '\n'
                                                               'Line 2: # File: mytools/__init__.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file mytools/__init__.py; it '
                                                               'is not a Python instruction.\n'
                                                               '\n'
                                                               'Line 3: from .text import shout\n'
                                                               'Import the named tool(s) from .text; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 5: # File: mytools/text.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file mytools/text.py; it is '
                                                               'not a Python instruction.\n'
                                                               '\n'
                                                               'Line 6: def shout(message):\n'
                                                               'Define a function named shout. Its '
                                                               'parameters (message) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 7: return message.upper()\n'
                                                               'Send message.upper() back to the caller and '
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 8: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 9: # File: app.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file app.py; it is not a '
                                                               'Python instruction.\n'
                                                               '\n'
                                                               'Line 10: from mytools import shout\n'
                                                               'Import the named tool(s) from mytools; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               "Line 11: print(shout('hello'))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: HELLO',
                                                'output': 'HELLO',
                                                'title': 'A package groups related modules'},
                                               {'code': '# File: games/dice.py\n'
                                                        'def roll_label(number):\n'
                                                        "    return f'Roll: {number}'\n"
                                                        '\n'
                                                        '# File: app.py\n'
                                                        'from games.dice import roll_label\n'
                                                        'print(roll_label(5))',
                                                'explanation': 'Purpose: Import through a package path shows '
                                                               'the current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'These labels divide the example into '
                                                               'separate project files. Create each named '
                                                               'file, then run app.py to get the output '
                                                               'shown here.\n'
                                                               '\n'
                                                               'Line 1: # File: games/dice.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file games/dice.py; it is '
                                                               'not a Python instruction.\n'
                                                               '\n'
                                                               'Line 2: def roll_label(number):\n'
                                                               'Define a function named roll_label. Its '
                                                               'parameters (number) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 3: return f'Roll: {number}'\n"
                                                               "Send f'Roll: {number}' back to the caller "
                                                               'and end this function call.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 5: # File: app.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file app.py; it is not a '
                                                               'Python instruction.\n'
                                                               '\n'
                                                               'Line 6: from games.dice import roll_label\n'
                                                               'Import the named tool(s) from games.dice; '
                                                               'the names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 7: print(roll_label(5))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Roll: 5',
                                                'output': 'Roll: 5',
                                                'title': 'Import through a package path'},
                                               {'code': '# File: tools/__init__.py\n'
                                                        'from .math_tools import double\n'
                                                        '\n'
                                                        '# File: tools/math_tools.py\n'
                                                        'def double(number):\n'
                                                        '    return number * 2\n'
                                                        '\n'
                                                        '# File: app.py\n'
                                                        'from tools import double\n'
                                                        'print(double(6))',
                                                'explanation': 'Purpose: __init__.py can expose a simple '
                                                               'public name shows the current lesson idea in '
                                                               'a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'These labels divide the example into '
                                                               'separate project files. Create each named '
                                                               'file, then run app.py to get the output '
                                                               'shown here.\n'
                                                               '\n'
                                                               'Line 1: # File: tools/__init__.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file tools/__init__.py; it '
                                                               'is not a Python instruction.\n'
                                                               '\n'
                                                               'Line 2: from .math_tools import double\n'
                                                               'Import the named tool(s) from .math_tools; '
                                                               'the names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 4: # File: tools/math_tools.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file tools/math_tools.py; it '
                                                               'is not a Python instruction.\n'
                                                               '\n'
                                                               'Line 5: def double(number):\n'
                                                               'Define a function named double. Its '
                                                               'parameters (number) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 6: return number * 2\n'
                                                               'Send number * 2 back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 7: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 8: # File: app.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file app.py; it is not a '
                                                               'Python instruction.\n'
                                                               '\n'
                                                               'Line 9: from tools import double\n'
                                                               'Import the named tool(s) from tools; the '
                                                               'names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 10: print(double(6))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 12',
                                                'output': '12',
                                                'title': '__init__.py can expose a simple public name'}],
                        'practice_questions': [{'answer': 'A package organizes modules in a directory; a '
                                                          'module is one file.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Larger projects need folders that group related '
                                                          'modules.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Regular packages commonly include __init__.py, '
                                                          'but namespace packages may omit it.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is grouping account, report, '
                                           'and formatting tools in one package. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: A package is a folder of modules; __init__.py is conventional, '
                                   'not universally required. Regular packages commonly include __init__.py, '
                                   'but namespace packages may omit it The practical example and its '
                                   'line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': '# Folder: mytools/\n'
                                            '# File: mytools/__init__.py\n'
                                            'from .text import shout\n'
                                            '\n'
                                            '# File: mytools/text.py\n'
                                            'def shout(message):\n'
                                            '    return message.upper()\n'
                                            '\n'
                                            '# File: app.py\n'
                                            'from mytools import shout\n'
                                            "print(shout('hello'))",
                        'terminology': [{'definition': 'A directory that organizes importable Python '
                                                       'modules.',
                                         'term': 'Package'},
                                        {'definition': 'A conventional file for package initialization and '
                                                       'public exports.',
                                         'term': '__init__.py'},
                                        {'definition': 'A package that can be importable without '
                                                       '__init__.py.',
                                         'term': 'Namespace package'}],
                        'title': 'Python Packages and __init__.py'},
             'number': 90,
             'quizzes': [{'explanation': 'Directories containing `__init__.py` are treated as packages.',
                          'options': [{'explanation': 'Correct! __init__.py marks a package directory.',
                                       'is_correct': True,
                                       'text': '__init__.py'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '__package__.py'},
                                      {'explanation': 'Incorrect. That is Node.js/JavaScript.',
                                       'is_correct': False,
                                       'text': 'package.json'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'main.py'}],
                          'question': 'What file marks a directory as a Python package in standard Python?'},
                         {'explanation': 'Circular imports at module load time cause an ImportError: cannot '
                                         'import name ... from partially initialized module.',
                          'options': [{'explanation': 'Correct! Mutual top-level imports create a circular '
                                                      'dependency error.',
                                       'is_correct': True,
                                       'text': 'ImportError: cannot import name (circular import)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Python merges both files into a single scope'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Both modules run in an infinite loop'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Execution succeeds silently'}],
                          'question': 'What happens when module A imports module B, and module B imports '
                                      'module A simultaneously at the top level?'}],
             'title': 'Python Packages and __init__.py'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Print the pip command that installs the requests package from PyPI.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["print('python -m pip install requests')"],
                             'initial_code': '# Deserializing JSON Data\n'
                                             'import json\n'
                                             '# Step 1: Read JSON string:\n'
                                             'raw = input().strip()\n'
                                             '\n'
                                             '# Step 2: Parse and print name and score below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "print('python -m pip install requests')",
                             'test_cases': [{'expected_output': 'python -m pip install requests',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Choose a Package Install Command',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Print three package requirements on separate lines so a project can store them in requirements.txt.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["print('requests>=2.28.0')\n"
                                       "print('flask>=2.2.0')\n"
                                       "print('pytest>=7.0.0')"],
                             'initial_code': '# ⚔️ Boss Challenge: Deterministic JSON Serializer\n'
                                             'import json\n'
                                             '# Step 1: Build dictionary:\n'
                                             "profile = {'player': input().strip(), 'level': int(input()), "
                                             "'inventory': ['sword', 'shield']}\n"
                                             '\n'
                                             '# Step 2: Print json.dumps with sort_keys=True below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "print('requests>=2.28.0')\n"
                                              "print('flask>=2.2.0')\n"
                                              "print('pytest>=7.0.0')",
                             'test_cases': [{'expected_output': 'requests>=2.28.0\n'
                                                                'flask>=2.2.0\n'
                                                                'pytest>=7.0.0',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: List Project Dependencies',
                             'xp_reward': 150}],
             'description': 'Leverage thousands of open-source libraries from the Python Package Index using '
                            'pip.',
             'lesson': {'common_mistakes': [{'fix': 'Use pip from the intended Python environment and record '
                                                    'dependencies.',
                                             'mistake': 'terminal commands are not Python statements; '
                                                        'distribution and import names can differ',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Third-party tools should be installed '
                                                'consistently for a project. This is the practical problem '
                                                'the feature solves.\n'
                                                '\n'
                                                'What it means: Pypi is a package index; pip is a '
                                                'command-line installer. Python uses this idea to run python '
                                                '-m pip in a terminal to install, inspect, upgrade, or '
                                                'uninstall a distribution\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Terminal commands are not python '
                                                'statements; distribution and import names can differ. If '
                                                'you change the example’s input or value, check this rule '
                                                'again because it can change the result or the path Python '
                                                'takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'No fixed output: pip details depend on the installed package '
                                           'version and environment.',
                        'id': 91,
                        'introduction': 'Why learn this? Third-party tools should be installed consistently '
                                        'for a project. In this lesson, we will see PyPI is a package index; '
                                        'pip is a command-line installer, follow how Python handles it, and '
                                        'practice a small example you can change yourself.',
                        'learning_objectives': ['Explain PyPI is a package index; pip is a command-line '
                                                'installer in your own words.',
                                                'Trace a small Package Management with pip and PyPI example '
                                                'and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'terminal commands are not Python statements; distribution '
                                                'and import names can differ.'],
                        'level_id': 91,
                        'line_by_line': [{'code': 'python -m pip install requests',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '1'},
                                         {'code': 'python -m pip show requests',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '2'}],
                        'practical_examples': [{'code': 'python -m pip install requests\n'
                                                        'python -m pip show requests',
                                                'explanation': 'Purpose: Run pip in a terminal using the '
                                                               'active Python shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Terminal command 1: python -m pip install '
                                                               'requests\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Terminal command 2: python -m pip show '
                                                               'requests\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Output trace: These are terminal commands, '
                                                               'not Python statements. Installation and '
                                                               'activation commands do not have one fixed '
                                                               'output.',
                                                'output': 'No fixed output: pip details depend on the '
                                                          'installed package version and environment.',
                                                'title': 'Run pip in a terminal using the active Python'},
                                               {'code': '# requirements.txt\n'
                                                        'requests>=2.28,<3\n'
                                                        '\n'
                                                        '# Terminal command\n'
                                                        'python -m pip install -r requirements.txt',
                                                'explanation': 'Purpose: Record a dependency and version '
                                                               'range shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Terminal command 2: requests>=2.28,<3\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Terminal command 5: python -m pip install -r '
                                                               'requirements.txt\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Output trace: These are terminal commands, '
                                                               'not Python statements. Installation and '
                                                               'activation commands do not have one fixed '
                                                               'output.',
                                                'output': 'No fixed output: pip reports whether it installed '
                                                          'or already had a compatible version.',
                                                'title': 'Record a dependency and version range'},
                                               {'code': 'python -m pip install --upgrade requests\n'
                                                        'python -m pip uninstall requests',
                                                'explanation': 'Purpose: Upgrade or remove a distribution '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Terminal command 1: python -m pip install '
                                                               '--upgrade requests\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Terminal command 2: python -m pip uninstall '
                                                               'requests\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Output trace: These are terminal commands, '
                                                               'not Python statements. Installation and '
                                                               'activation commands do not have one fixed '
                                                               'output.',
                                                'output': 'No fixed output: pip shows the version and asks '
                                                          'for confirmation before uninstalling.',
                                                'title': 'Upgrade or remove a distribution'}],
                        'practice_questions': [{'answer': 'Pypi is a package index; pip is a command-line '
                                                          'installer.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Third-party tools should be installed '
                                                          'consistently for a project.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Terminal commands are not python statements; '
                                                          'distribution and import names can differ.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is adding requests to a '
                                           'project with a pinned dependency list. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Use pip from the intended Python environment and record '
                                   'dependencies. Terminal commands are not python statements; distribution '
                                   'and import names can differ The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'python -m pip install requests\npython -m pip show requests',
                        'terminology': [{'definition': 'A public index that hosts Python distribution '
                                                       'packages.',
                                         'term': 'PyPI'},
                                        {'definition': 'A command-line tool for installing Python '
                                                       'distributions.',
                                         'term': 'pip'},
                                        {'definition': 'A dependency rule limiting which package versions '
                                                       'are acceptable.',
                                         'term': 'Version pin'}],
                        'title': 'Package Management with pip and PyPI'},
             'number': 91,
             'quizzes': [{'explanation': '`pip freeze > requirements.txt` dumps exact installed package '
                                         'versions.',
                          'options': [{'explanation': 'Correct! pip freeze captures current dependencies.',
                                       'is_correct': True,
                                       'text': 'pip freeze > requirements.txt'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'pip list --export'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'pip save requirements.txt'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'python -m requirements'}],
                          'question': 'What shell command exports all currently installed pip packages to a '
                                      'requirements file?'},
                         {'explanation': '`pip install -r requirements.txt` installs packages specified in '
                                         'the file.',
                          'options': [{'explanation': 'Correct! -r specifies a requirements file.',
                                       'is_correct': True,
                                       'text': 'pip install -r requirements.txt'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'pip load requirements.txt'},
                                      {'explanation': 'Incorrect. Without -r pip searches for a package '
                                                      "named 'requirements.txt'.",
                                       'is_correct': False,
                                       'text': 'pip install requirements.txt'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'python install requirements'}],
                          'question': 'What command installs all dependencies listed inside a '
                                      '`requirements.txt` file?'}],
             'title': 'Package Management with pip and PyPI'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Print the command that creates an isolated environment named .venv.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["print('python -m venv .venv')"],
                             'initial_code': '# Python Package Manager (pip)\n'
                                             "tool = 'pip'\n"
                                             "cmd = 'install'\n"
                                             "pkg = 'requests'\n"
                                             '\n'
                                             '# Step 1: Print formatted command below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "print('python -m venv .venv')",
                             'test_cases': [{'expected_output': 'python -m venv .venv',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Create a Virtual Environment',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Print the PowerShell command that activates the .venv environment.\n2. Include .\\ at the start so PowerShell runs the activation script from this folder.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["print('.\\\\.venv\\\\Scripts\\\\Activate.ps1')"],
                             'initial_code': '# ⚔️ Boss Challenge: requirements.txt Generator\n'
                                             "reqs = ['requests>=2.28.0', 'flask>=2.2.0', 'pytest>=7.0.0']\n"
                                             '\n'
                                             '# Step 1: Print each requirement line below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "print('.\\\\.venv\\\\Scripts\\\\Activate.ps1')",
                             'test_cases': [{'expected_output': '.\\.venv\\Scripts\\Activate.ps1',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Activate the Project Environment',
                             'xp_reward': 150}],
             'description': "Isolate project dependencies and eliminate 'dependency hell' using Python's "
                            'built-in venv module.',
             'lesson': {'common_mistakes': [{'fix': 'Create and activate .venv before installing project '
                                                    'packages.',
                                             'mistake': 'activation differs by shell; venv does not install '
                                                        'Python itself',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Projects can need different versions '
                                                'of the same third-party library. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: A virtual environment is an isolated project '
                                                'environment using an existing python installation. Python '
                                                'uses this idea to create with python -m venv .venv, '
                                                'activate it, then install with python -m pip\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Activation differs by shell; venv does not '
                                                'install python itself. If you change the example’s input or '
                                                'value, check this rule again because it can change the '
                                                'result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'No printed output on success; Python creates a .venv folder for '
                                           'the project.',
                        'id': 92,
                        'introduction': 'Why learn this? Projects can need different versions of the same '
                                        'third-party library. In this lesson, we will see a virtual '
                                        'environment is an isolated project environment using an existing '
                                        'Python installation, follow how Python handles it, and practice a '
                                        'small example you can change yourself.',
                        'learning_objectives': ['Explain a virtual environment is an isolated project '
                                                'environment using an existing Python installation in your '
                                                'own words.',
                                                'Trace a small Python Virtual Environments (venv) example '
                                                'and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'activation differs by shell; venv does not install Python '
                                                'itself.'],
                        'level_id': 92,
                        'line_by_line': [{'code': 'python -m venv .venv',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '1'}],
                        'practical_examples': [{'code': 'python -m venv .venv',
                                                'explanation': 'Purpose: Create a virtual environment shows '
                                                               'the current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Terminal command 1: python -m venv .venv\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Output trace: These are terminal commands, '
                                                               'not Python statements. Installation and '
                                                               'activation commands do not have one fixed '
                                                               'output.',
                                                'output': 'No printed output on success; Python creates a '
                                                          '.venv folder for the project.',
                                                'title': 'Create a virtual environment'},
                                               {'code': '.venv\\Scripts\\Activate.ps1  (PowerShell)\n'
                                                        '.venv\\Scripts\\activate.bat  (Windows CMD)\n'
                                                        'source .venv/bin/activate  (macOS or Linux)',
                                                'explanation': 'Purpose: Activate it in common shells shows '
                                                               'the current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Terminal command 1: '
                                                               '.venv\\Scripts\\Activate.ps1  (PowerShell)\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Terminal command 2: '
                                                               '.venv\\Scripts\\activate.bat  (Windows CMD)\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Terminal command 3: source '
                                                               '.venv/bin/activate  (macOS or Linux)\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Output trace: These are terminal commands, '
                                                               'not Python statements. Installation and '
                                                               'activation commands do not have one fixed '
                                                               'output.',
                                                'output': 'The current terminal switches to the environment; '
                                                          'its prompt may show (.venv).',
                                                'title': 'Activate it in common shells'},
                                               {'code': 'python -m pip install requests\n'
                                                        'python -m pip freeze > requirements.txt',
                                                'explanation': 'Purpose: Install inside the active '
                                                               'environment shows the current lesson idea in '
                                                               'a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Terminal command 1: python -m pip install '
                                                               'requests\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Terminal command 2: python -m pip freeze > '
                                                               'requirements.txt\n'
                                                               'Run this command in a terminal, not in the '
                                                               'Python editor. It uses the active Python '
                                                               'environment.\n'
                                                               '\n'
                                                               'Output trace: These are terminal commands, '
                                                               'not Python statements. Installation and '
                                                               'activation commands do not have one fixed '
                                                               'output.',
                                                'output': 'No fixed output: pip status depends on the active '
                                                          'environment; freeze writes the installed '
                                                          'dependency list to requirements.txt.',
                                                'title': 'Install inside the active environment'}],
                        'practice_questions': [{'answer': 'A virtual environment is an isolated project '
                                                          'environment using an existing python '
                                                          'installation.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Projects can need different versions of the same '
                                                          'third-party library.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Activation differs by shell; venv does not '
                                                          'install python itself.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is keeping a web project’s '
                                           'dependencies separate from another project. The same pattern '
                                           'helps a larger program stay clear when it handles the same kind '
                                           'of task repeatedly.',
                        'summary': 'Remember: Create and activate .venv before installing project packages. '
                                   'Activation differs by shell; venv does not install python itself The '
                                   'practical example and its line-by-line walkthrough show the idea in '
                                   'action.',
                        'syntax_breakdown': 'python -m venv .venv',
                        'terminology': [{'definition': 'An isolated set of project packages using an '
                                                       'existing Python installation.',
                                         'term': 'Virtual environment'},
                                        {'definition': 'Adjust the current shell so its Python commands use '
                                                       'the environment.',
                                         'term': 'Activate'},
                                        {'definition': 'A text list of project dependencies and version '
                                                       'rules.',
                                         'term': 'requirements file'}],
                        'title': 'Python Virtual Environments (venv)'},
             'number': 92,
             'quizzes': [{'explanation': '`python -m venv .venv` uses the built-in venv module to create an '
                                         'isolated environment.',
                          'options': [{'explanation': 'Correct! python -m venv creates the virtual '
                                                      'environment directory.',
                                       'is_correct': True,
                                       'text': 'python -m venv .venv'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'pip create venv'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'virtualenv --new'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'python venv create .venv'}],
                          'question': 'What is the standard command to create a virtual environment named '
                                      '`.venv` in Python 3?'},
                         {'explanation': 'Virtual environments contain machine-specific compiled binaries '
                                         'and large libraries; dependencies should be tracked via '
                                         'requirements.txt instead.',
                          'options': [{'explanation': 'Correct! Environments are rebuilt locally, not '
                                                      'tracked in version control.',
                                       'is_correct': True,
                                       'text': 'It contains platform-specific binaries and large libraries '
                                               'that can be reinstalled via requirements.txt'},
                                      {'explanation': 'Incorrect. Git tracks dot-files unless gitignored.',
                                       'is_correct': False,
                                       'text': 'Git refuses to track directories starting with a dot'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Virtual environments expire after 24 hours'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Python deletes .venv if pushed to GitHub'}],
                          'question': 'Why should the `.venv` directory NEVER be committed to a Git '
                                      'repository?'}],
             'title': 'Python Virtual Environments (venv)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Python checks folders in order when looking for a module.\n2. Use a small list to show that the project folder is checked first.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["search_path = ['project', 'site-packages', 'standard-library']\n"
                                       "print('First folder checked:', search_path[0])\n"
                                       "print('Folders are checked in order.')"],
                             'initial_code': '# Creating Custom Modules\n'
                                             "calc_code = 'def add(a, b): return a + b'\n"
                                             '\n'
                                             '# Step 1: Print confirmation below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "search_path = ['project', 'site-packages', "
                                              "'standard-library']\n"
                                              "print('First folder checked:', search_path[0])\n"
                                              "print('Folders are checked in order.')",
                             'test_cases': [{'expected_output': 'First folder checked: project\n'
                                                                'Folders are checked in order.',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Model Module Search Order',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use a small ordered path list to show that the first matching module file is found.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["search_path = ['project', 'site-packages', 'standard-library']\n"
                                       "module = 'helpers.py'\n"
                                       'found_at = next((folder for folder in search_path if folder == '
                                       "'project'), None)\n"
                                       "print(f'{module} found in: {found_at}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Module Public Interface\n'
                                             "exports = ['add', 'subtract', 'multiply']\n"
                                             '\n'
                                             '# Step 1: Print __all__ = {exports} below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "search_path = ['project', 'site-packages', "
                                              "'standard-library']\n"
                                              "module = 'helpers.py'\n"
                                              'found_at = next((folder for folder in search_path if folder '
                                              "== 'project'), None)\n"
                                              "print(f'{module} found in: {found_at}')",
                             'test_cases': [{'expected_output': 'helpers.py found in: project',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Find a Module in Search Folders',
                             'xp_reward': 150}],
             'description': 'Understand how Python locates imported files, resolves dependencies, and '
                            'leverages sys.path.',
             'lesson': {'common_mistakes': [{'fix': 'Understand the search path, then fix project structure '
                                                    'instead of patching it casually.',
                                             'mistake': 'editing sys.path at runtime is fragile; fix package '
                                                        'layout or environment instead',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Python needs a predictable rule for '
                                                'finding imported modules. This is the practical problem the '
                                                'feature solves.\n'
                                                '\n'
                                                'What it means: Sys.path is the list of locations searched '
                                                'for imports. Python uses this idea to inspect sys.path to '
                                                'debug; Python also uses the active environment and project '
                                                'layout\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Editing sys.path at runtime is fragile; fix '
                                                'package layout or environment instead. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'list\nIt stores import search locations',
                        'id': 93,
                        'introduction': 'Why learn this? Python needs a predictable rule for finding '
                                        'imported modules. In this lesson, we will see sys.path is the list '
                                        'of locations searched for imports, follow how Python handles it, '
                                        'and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain sys.path is the list of locations searched for '
                                                'imports in your own words.',
                                                'Trace a small Module Search Path (sys.path) example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'editing sys.path at runtime is fragile; fix package layout '
                                                'or environment instead.'],
                        'level_id': 93,
                        'line_by_line': [{'code': 'import sys',
                                          'explanation': 'Load the module sys so this file can use its '
                                                         'tools. An alias, if present, becomes the name used '
                                                         'below.',
                                          'line': '1'},
                                         {'code': 'print(type(sys.path).__name__)',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': "print('It stores import search locations')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'}],
                        'practical_examples': [{'code': 'import sys\n'
                                                        'print(type(sys.path).__name__)\n'
                                                        "print('It stores import search locations')",
                                                'explanation': 'Purpose: Inspect the shape of the import '
                                                               'search path shows the current lesson idea in '
                                                               'a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: import sys\n'
                                                               'Load the module sys so this file can use its '
                                                               'tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               'Line 2: print(type(sys.path).__name__)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 3: print('It stores import search "
                                                               "locations')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: list\n'
                                                               'It stores import search locations',
                                                'output': 'list\nIt stores import search locations',
                                                'title': 'Inspect the shape of the import search path'},
                                               {'code': 'try:\n'
                                                        '    import json\n'
                                                        "    print('json is available')\n"
                                                        'except ModuleNotFoundError:\n'
                                                        "    print('Check the active Python installation')",
                                                'explanation': 'Purpose: Check an import without editing '
                                                               'sys.path shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 2: import json\n'
                                                               'Load the module json so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               "Line 3: print('json is available')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: except ModuleNotFoundError:\n'
                                                               'Handle only a ModuleNotFoundError exception '
                                                               'here.\n'
                                                               '\n'
                                                               "Line 5: print('Check the active Python "
                                                               "installation')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: json is available',
                                                'output': 'json is available',
                                                'title': 'Check an import without editing sys.path'},
                                               {'code': '# Save this in helpers.py beside app.py.\n'
                                                        'def helper_name():\n'
                                                        "    return 'helper'\n"
                                                        '\n'
                                                        '# Save this in app.py in the same folder.\n'
                                                        'import helpers\n'
                                                        "print('Imported:', helpers.helper_name())",
                                                'explanation': 'Purpose: Fix a project import by organizing '
                                                               'files shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: # Save this in helpers.py beside '
                                                               'app.py.\n'
                                                               'This comment is a note for the reader. '
                                                               'Python skips it; it does not run.\n'
                                                               '\n'
                                                               'Line 2: def helper_name():\n'
                                                               'Define a function named helper_name. Its '
                                                               'parameters (none) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 3: return 'helper'\n"
                                                               "Send 'helper' back to the caller and end "
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 5: # Save this in app.py in the same '
                                                               'folder.\n'
                                                               'This comment is a note for the reader. '
                                                               'Python skips it; it does not run.\n'
                                                               '\n'
                                                               'Line 6: import helpers\n'
                                                               'Load the module helpers so this file can use '
                                                               'its tools. An alias, if present, becomes the '
                                                               'name used below.\n'
                                                               '\n'
                                                               "Line 7: print('Imported:', "
                                                               'helpers.helper_name())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Imported: helper',
                                                'output': 'Imported: helper',
                                                'title': 'Fix a project import by organizing files'}],
                        'practice_questions': [{'answer': 'Sys.path is the list of locations searched for '
                                                          'imports.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Python needs a predictable rule for finding '
                                                          'imported modules.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Editing sys.path at runtime is fragile; fix '
                                                          'package layout or environment instead.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is diagnosing why a project '
                                           'module cannot be imported. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Understand the search path, then fix project structure instead '
                                   'of patching it casually. Editing sys.path at runtime is fragile; fix '
                                   'package layout or environment instead The practical example and its '
                                   'line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': 'import sys\n'
                                            'print(type(sys.path).__name__)\n'
                                            "print('It stores import search locations')",
                        'terminology': [{'definition': 'The list of locations Python searches for imports.',
                                         'term': 'sys.path'},
                                        {'definition': 'Python’s process of locating a module.',
                                         'term': 'Import search'},
                                        {'definition': 'An exception raised when Python cannot find an '
                                                       'imported module.',
                                         'term': 'ModuleNotFoundError'}],
                        'title': 'Module Search Path (sys.path)'},
             'number': 93,
             'quizzes': [{'explanation': 'sys.path is a list of strings representing directory search paths '
                                         'for imports.',
                          'options': [{'explanation': 'Correct! sys.path is a list of directory path '
                                                      'strings.',
                                       'is_correct': True,
                                       'text': "<class 'list'>"},
                                      {'explanation': 'Incorrect. It is a list, allowing sys.path.append().',
                                       'is_correct': False,
                                       'text': "<class 'str'>"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "<class 'tuple'>"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "<class 'dict'>"}],
                          'question': 'What data type is `sys.path` in Python?'},
                         {'explanation': 'Attempting to import an unresolved module raises '
                                         'ModuleNotFoundError.',
                          'options': [{'explanation': 'Correct! Python raises ModuleNotFoundError when a '
                                                      'module cannot be found.',
                                       'is_correct': True,
                                       'text': 'ModuleNotFoundError: No module named ...'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'NameError: module is undefined'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'FileNotFoundError'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'SyntaxError: invalid module name'}],
                          'question': 'What error occurs if you import a module name that does not exist in '
                                      '`sys.path`?'}],
             'title': 'Module Search Path (sys.path)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a JSON event with an event name and a Unix timestamp.\n2. Turn the timestamp into a date and print the event name followed by the date in year-month-day order.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['import json\n'
                                       'from datetime import datetime\n'
                                       'raw = input().strip()\n'
                                       'd = json.loads(raw)\n'
                                       "ts = datetime.fromtimestamp(d['timestamp'])\n"
                                       'print(f"{d[\'event\']} occurred at {ts.strftime(\'%Y-%m-%d\')}")'],
                             'initial_code': '# World 9 Capstone: Webhook Event Processor\n'
                                             'import json\n'
                                             'from datetime import datetime\n'
                                             '# Step 1: Read JSON:\n'
                                             'raw = input().strip()\n'
                                             '\n'
                                             '# Step 2: Parse and format output below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import json\n'
                                              'from datetime import datetime\n'
                                              '\n'
                                              'payload = json.loads(input())\n'
                                              "timestamp = datetime.fromtimestamp(payload['timestamp'])\n"
                                              'print(f"{payload[\'event\']} occurred at '
                                              '{timestamp.strftime(\'%Y-%m-%d\')}")',
                             'test_cases': [{'expected_output': 'quest_started occurred at 1970-01-01',
                                             'input_data': '{"event":"quest_started","timestamp":0}\n',
                                             'is_hidden': False},
                                            {'expected_output': 'level_complete occurred at 1970-01-02',
                                             'input_data': '{"event":"level_complete","timestamp":86400}\n',
                                             'is_hidden': False}],
                             'title': 'World 9 Capstone: Event Timestamp Processor',
                             'xp_reward': 50},
                            {'description': 'Your task, step by step:\n1. Read a JSON object containing a circle’s radius.\n2. Calculate the circle’s area, rounded to two decimal places.\n3. Print JSON containing the area and radius, with the keys in alphabetical order.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import json, math\n'
                                       'payload = json.loads(input())\n'
                                       "radius = payload['radius']\n"
                                       'area = math.pi * (radius ** 2)\n'
                                       "resp = {'radius': radius, 'area': round(area, 2)}\n"
                                       'print(json.dumps(resp, sort_keys=True))'],
                             'initial_code': '# ⚔️ Boss Challenge: JSON Geometry Service\n'
                                             'import json, math\n'
                                             '# Step 1: Read payload:\n'
                                             'payload = json.loads(input())\n'
                                             '\n'
                                             '# Step 2: Calculate area and output sorted JSON below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import json\n'
                                              'import math\n'
                                              '\n'
                                              'payload = json.loads(input())\n'
                                              "radius = payload['radius']\n"
                                              "result = {'area': round(math.pi * radius ** 2, 2), 'radius': "
                                              'radius}\n'
                                              'print(json.dumps(result, sort_keys=True))',
                             'test_cases': [{'expected_output': '{"area": 78.54, "radius": 5}',
                                             'input_data': '{"radius":5}\n',
                                             'is_hidden': False},
                                            {'expected_output': '{"area": 12.57, "radius": 2}',
                                             'input_data': '{"radius":2}\n',
                                             'is_hidden': False}],
                             'title': 'JSON Geometry Service',
                             'xp_reward': 250}],
             'description': 'Architect a modular multi-tool CLI utility package featuring math, text '
                            'formatting, date utilities, and stats.',
             'lesson': {'common_mistakes': [{'fix': 'Organize utilities into modules and run the application '
                                                    'through a clear entry point.',
                                             'mistake': 'keep installation instructions separate from Python '
                                                        'code and avoid random for security',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A toolkit is easier to reuse when '
                                                'each tool has its own module. This is the practical problem '
                                                'the feature solves.\n'
                                                '\n'
                                                'What it means: The capstone combines module files, imports, '
                                                'standard-library helpers, and a main guard. Python uses '
                                                'this idea to define small functions in modules and have a '
                                                'main script call them\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Keep installation instructions separate '
                                                'from python code and avoid random for security. If you '
                                                'change the example’s input or value, check this rule again '
                                                'because it can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': '28.27\nREADY',
                        'id': 94,
                        'introduction': 'Why learn this? A toolkit is easier to reuse when each tool has its '
                                        'own module. In this lesson, we will see the capstone combines '
                                        'module files, imports, standard-library helpers, and a main guard, '
                                        'follow how Python handles it, and practice a small example you can '
                                        'change yourself.',
                        'learning_objectives': ['Explain the capstone combines module files, imports, '
                                                'standard-library helpers, and a main guard in your own '
                                                'words.',
                                                'Trace a small World 9 Examination & Capstone: Utility '
                                                'Toolkit example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: keep '
                                                'installation instructions separate from Python code and '
                                                'avoid random for security.'],
                        'level_id': 94,
                        'line_by_line': [{'code': '# File: math_tools.py',
                                          'explanation': 'This label says the following code belongs in the '
                                                         'separate file math_tools.py; it is not a Python '
                                                         'instruction.',
                                          'line': '1'},
                                         {'code': 'def circle_area(radius):',
                                          'explanation': 'Define a function named circle_area. Its '
                                                         'parameters (radius) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '2'},
                                         {'code': '    return 3.14159 * radius * radius',
                                          'explanation': 'Send 3.14159 * radius * radius back to the caller '
                                                         'and end this function call.',
                                          'line': '3'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '4'},
                                         {'code': '# File: text_tools.py',
                                          'explanation': 'This label says the following code belongs in the '
                                                         'separate file text_tools.py; it is not a Python '
                                                         'instruction.',
                                          'line': '5'},
                                         {'code': 'def shout(message):',
                                          'explanation': 'Define a function named shout. Its parameters '
                                                         '(message) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '6'},
                                         {'code': '    return message.upper()',
                                          'explanation': 'Send message.upper() back to the caller and end '
                                                         'this function call.',
                                          'line': '7'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '8'},
                                         {'code': '# File: app.py',
                                          'explanation': 'This label says the following code belongs in the '
                                                         'separate file app.py; it is not a Python '
                                                         'instruction.',
                                          'line': '9'},
                                         {'code': 'from math_tools import circle_area',
                                          'explanation': 'Import the named tool(s) from math_tools; the '
                                                         'names can then be used directly in this file.',
                                          'line': '10'},
                                         {'code': 'from text_tools import shout',
                                          'explanation': 'Import the named tool(s) from text_tools; the '
                                                         'names can then be used directly in this file.',
                                          'line': '11'},
                                         {'code': 'print(round(circle_area(3), 2))',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '12'},
                                         {'code': "print(shout('ready'))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '13'}],
                        'practical_examples': [{'code': '# File: math_tools.py\n'
                                                        'def circle_area(radius):\n'
                                                        '    return 3.14159 * radius * radius\n'
                                                        '\n'
                                                        '# File: text_tools.py\n'
                                                        'def shout(message):\n'
                                                        '    return message.upper()\n'
                                                        '\n'
                                                        '# File: app.py\n'
                                                        'from math_tools import circle_area\n'
                                                        'from text_tools import shout\n'
                                                        'print(round(circle_area(3), 2))\n'
                                                        "print(shout('ready'))",
                                                'explanation': 'Purpose: Use separate utility modules from '
                                                               'one application shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'These labels divide the example into '
                                                               'separate project files. Create each named '
                                                               'file, then run app.py to get the output '
                                                               'shown here.\n'
                                                               '\n'
                                                               'Line 1: # File: math_tools.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file math_tools.py; it is '
                                                               'not a Python instruction.\n'
                                                               '\n'
                                                               'Line 2: def circle_area(radius):\n'
                                                               'Define a function named circle_area. Its '
                                                               'parameters (radius) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: return 3.14159 * radius * radius\n'
                                                               'Send 3.14159 * radius * radius back to the '
                                                               'caller and end this function call.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 5: # File: text_tools.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file text_tools.py; it is '
                                                               'not a Python instruction.\n'
                                                               '\n'
                                                               'Line 6: def shout(message):\n'
                                                               'Define a function named shout. Its '
                                                               'parameters (message) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 7: return message.upper()\n'
                                                               'Send message.upper() back to the caller and '
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 8: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 9: # File: app.py\n'
                                                               'This label says the following code belongs '
                                                               'in the separate file app.py; it is not a '
                                                               'Python instruction.\n'
                                                               '\n'
                                                               'Line 10: from math_tools import circle_area\n'
                                                               'Import the named tool(s) from math_tools; '
                                                               'the names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 11: from text_tools import shout\n'
                                                               'Import the named tool(s) from text_tools; '
                                                               'the names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               'Line 12: print(round(circle_area(3), 2))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 13: print(shout('ready'))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 28.27\n'
                                                               'READY',
                                                'output': '28.27\nREADY',
                                                'title': 'Use separate utility modules from one application'},
                                               {'code': 'from collections import Counter\n'
                                                        "words = ['map', 'key', 'map']\n"
                                                        "print(Counter(words)['map'])",
                                                'explanation': 'Purpose: Use standard-library tools in the '
                                                               'toolkit shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: from collections import Counter\n'
                                                               'Import the named tool(s) from collections; '
                                                               'the names can then be used directly in this '
                                                               'file.\n'
                                                               '\n'
                                                               "Line 2: words = ['map', 'key', 'map']\n"
                                                               'Create the list shown and store it in words. '
                                                               'The list keeps items in order and can be '
                                                               'processed one item at a time.\n'
                                                               '\n'
                                                               "Line 3: print(Counter(words)['map'])\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 2',
                                                'output': '2',
                                                'title': 'Use standard-library tools in the toolkit'},
                                               {'code': 'def main():\n'
                                                        "    print('Utility toolkit ready')\n"
                                                        '\n'
                                                        "if __name__ == '__main__':\n"
                                                        '    main()',
                                                'explanation': 'Purpose: Run application-only behavior under '
                                                               'a main guard shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def main():\n'
                                                               'Define a function named main. Its parameters '
                                                               '(none) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               "Line 2: print('Utility toolkit ready')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: if __name__ == '__main__':\n"
                                                               "Check whether __name__ == '__main__' is "
                                                               'true. If it is, run the indented block; '
                                                               'otherwise Python skips that block.\n'
                                                               '\n'
                                                               'Line 5: main()\n'
                                                               'Call main now. Python runs its body, and any '
                                                               'returned result is available to the caller.\n'
                                                               '\n'
                                                               'Output trace: Utility toolkit ready',
                                                'output': 'Utility toolkit ready',
                                                'title': 'Run application-only behavior under a main guard'}],
                        'practice_questions': [{'answer': 'The capstone combines module files, imports, '
                                                          'standard-library helpers, and a main guard.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A toolkit is easier to reuse when each tool has '
                                                          'its own module.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Keep installation instructions separate from '
                                                          'python code and avoid random for security.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Functions, files, and basic Python statements from earlier worlds. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a reusable text and math '
                                           'utility folder. The same pattern helps a larger program stay '
                                           'clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Organize utilities into modules and run the application '
                                   'through a clear entry point. Keep installation instructions separate '
                                   'from python code and avoid random for security The practical example and '
                                   'its line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': '# File: math_tools.py\n'
                                            'def circle_area(radius):\n'
                                            '    return 3.14159 * radius * radius\n'
                                            '\n'
                                            '# File: text_tools.py\n'
                                            'def shout(message):\n'
                                            '    return message.upper()\n'
                                            '\n'
                                            '# File: app.py\n'
                                            'from math_tools import circle_area\n'
                                            'from text_tools import shout\n'
                                            'print(round(circle_area(3), 2))\n'
                                            "print(shout('ready'))",
                        'terminology': [{'definition': 'A file that contains reusable tools for a project.',
                                         'term': 'Utility module'},
                                        {'definition': 'The file or function used to start an application.',
                                         'term': 'Entry point'},
                                        {'definition': 'A check that separates direct-run behavior from '
                                                       'imported behavior.',
                                         'term': 'Main guard'}],
                        'title': 'World 9 Examination & Capstone: Utility Toolkit'},
             'number': 94,
             'quizzes': [{'explanation': "When 'QUEST_STAGE' is not set in the operating system environment, "
                                         "get() returns the fallback 'World_1'.",
                          'options': [{'explanation': 'Correct! get() returns the fallback value when key is '
                                                      'absent.',
                                       'is_correct': True,
                                       'text': 'World_1'},
                                      {'explanation': 'Incorrect. A fallback string was provided.',
                                       'is_correct': False,
                                       'text': 'None'},
                                      {'explanation': 'Incorrect. .get() does not raise KeyError.',
                                       'is_correct': False,
                                       'text': 'KeyError'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'QUEST_STAGE'}],
                          'question': 'What is the output of checking environment variables with a default '
                                      'fallback?\n'
                                      '\n'
                                      'import os\n'
                                      "print(os.environ.get('QUEST_STAGE', 'World_1'))"},
                         {'explanation': "sys.argv[0] is always the script name being executed: 'main.py'.",
                          'options': [{'explanation': 'Correct! sys.argv[0] is the script name.',
                                       'is_correct': True,
                                       'text': "'main.py'"},
                                      {'explanation': "Incorrect. '100' is at sys.argv[1].",
                                       'is_correct': False,
                                       'text': "'100'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': "'python'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '1'}],
                          'question': 'What is the output of: print(sys.argv[0]) when executing `python '
                                      'main.py 100`?'}],
             'title': 'World 9 Examination & Capstone: Utility Toolkit'}],
 'number': 9,
 'title': 'Modules and Python Tools'}
