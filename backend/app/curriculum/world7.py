"""
Curriculum module: WORLD_7
Upgraded with pedagogical question scenarios and scaffolded starter code.
"""

WORLD_7 = {'description': 'Master def, arguments, return values, *args, **kwargs, scope, lambdas, and higher-order '
                'functions.',
 'final_project_desc': 'Architect a multi-operation computational engine using modular functions, dispatch '
                       'dictionaries, and input validation.',
 'final_project_title': 'Modular Calculator',
 'goal': 'Build reusable, modular, testable code abstractions with function architecture.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Write a function named welcome_hero that displays the welcome message shown in the example.\n2. Then call the function so the message appears.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def welcome_hero():\n'
                                       "    print('Welcome, brave explorer of Python!')\n"
                                       'welcome_hero()'],
                             'initial_code': '# Defining and Calling Functions\n'
                                             '# Step 1: Define welcome_hero():\n'
                                             '\n'
                                             '# Step 2: Call welcome_hero() below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def welcome_hero():\n'
                                              "    print('Welcome, brave explorer of Python!')\n"
                                              '\n'
                                              'welcome_hero()',
                             'test_cases': [{'expected_output': 'Welcome, brave explorer of Python!',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Guild Welcome Herald',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write a function named sound_alarm that displays the warning shown in the example.\n2. Use a loop to call it three times, so the warning appears three times.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def sound_alarm():\n'
                                       "    print('[ALERT] Security breach detected!')\n"
                                       'for _ in range(3):\n'
                                       '    sound_alarm()'],
                             'initial_code': '# ⚔️ Boss Challenge: Triple Alarm Siren\n'
                                             '# Step 1: Define sound_alarm():\n'
                                             '\n'
                                             '# Step 2: Call it 3 times using for _ in range(3):\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def sound_alarm():\n'
                                              "    print('[ALERT] Security breach detected!')\n"
                                              '\n'
                                              'for _ in range(3):\n'
                                              '    sound_alarm()',
                             'test_cases': [{'expected_output': '[ALERT] Security breach detected!\n'
                                                                '[ALERT] Security breach detected!\n'
                                                                '[ALERT] Security breach detected!',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Triple Alarm Siren',
                             'xp_reward': 150}],
             'description': 'Define and invoke reusable blocks of code using the def keyword.',
             'lesson': {'common_mistakes': [{'fix': 'Define once with def, then call by name with '
                                                    'parentheses.',
                                             'mistake': 'defining is not calling, and indentation marks the '
                                                        'body',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Reusing a task avoids copy-and-paste '
                                                'drift. This is the practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: A function is a named group of instructions. '
                                                'Python uses this idea to def creates the function; a later '
                                                'call runs its indented body in order\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Defining is not calling, and indentation '
                                                'marks the body. If you change the example’s input or value, '
                                                'check this rule again because it can change the result or '
                                                'the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': '=== MAIN MENU ===\n1. Start Game\n2. Quit',
                        'id': 64,
                        'introduction': 'Why learn this? Reusing a task avoids copy-and-paste drift. In this '
                                        'lesson, we will see a function is a named group of instructions, '
                                        'follow how Python handles it, and practice a small example you can '
                                        'change yourself.',
                        'learning_objectives': ['Explain a function is a named group of instructions in your '
                                                'own words.',
                                                'Trace a small What Are Functions? example and predict what '
                                                'Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'defining is not calling, and indentation marks the body.'],
                        'level_id': 64,
                        'line_by_line': [{'code': 'def show_menu():',
                                          'explanation': 'Define a function named show_menu. Its parameters '
                                                         '(none) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '1'},
                                         {'code': "    print('=== MAIN MENU ===')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': "    print('1. Start Game')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'},
                                         {'code': "    print('2. Quit')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '4'},
                                         {'code': 'show_menu()',
                                          'explanation': 'Call show_menu now. Python runs its body, and any '
                                                         'returned result is available to the caller.',
                                          'line': '5'}],
                        'practical_examples': [{'code': 'def show_menu():\n'
                                                        "    print('=== MAIN MENU ===')\n"
                                                        "    print('1. Start Game')\n"
                                                        "    print('2. Quit')\n"
                                                        'show_menu()',
                                                'explanation': 'Purpose: Example 1: Simple banner printer '
                                                               'function shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def show_menu():\n'
                                                               'Define a function named show_menu. Its '
                                                               'parameters (none) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: print('=== MAIN MENU ===')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 3: print('1. Start Game')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 4: print('2. Quit')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 5: show_menu()\n'
                                                               'Call show_menu now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: === MAIN MENU ===\n'
                                                               '1. Start Game\n'
                                                               '2. Quit',
                                                'output': '=== MAIN MENU ===\n1. Start Game\n2. Quit',
                                                'title': 'Example 1: Simple banner printer function'},
                                               {'code': 'def print_price(cents):\n'
                                                        '    dollars = cents / 100\n'
                                                        "    print(f'Price: ${dollars:.2f}')\n"
                                                        'print_price(1999)\n'
                                                        'print_price(450)',
                                                'explanation': 'Purpose: Example 2: Formatting currency '
                                                               'readout shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def print_price(cents):\n'
                                                               'Define a function named print_price. Its '
                                                               'parameters (cents) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: dollars = cents / 100\n'
                                                               'Calculate or compare cents / 100, then save '
                                                               'the result in dollars.\n'
                                                               '\n'
                                                               "Line 3: print(f'Price: ${dollars:.2f}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: print_price(1999)\n'
                                                               'Call print_price now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Line 5: print_price(450)\n'
                                                               'Call print_price now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Price: $19.99\n'
                                                               'Price: $4.50',
                                                'output': 'Price: $19.99\nPrice: $4.50',
                                                'title': 'Example 2: Formatting currency readout'},
                                               {'code': 'def draw_health(hp):\n'
                                                        "    bar = '=' * (hp // 10)\n"
                                                        "    print(f'HP: [{bar:<10}] {hp}%')\n"
                                                        'draw_health(70)\n'
                                                        'draw_health(30)',
                                                'explanation': 'Purpose: Example 3: Reusable health bar '
                                                               'visualizer shows the current lesson idea in '
                                                               'a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def draw_health(hp):\n'
                                                               'Define a function named draw_health. Its '
                                                               'parameters (hp) are local names that receive '
                                                               'values when the function is called. The '
                                                               'colon starts the indented body; defining it '
                                                               'does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: bar = '=' * (hp // 10)\n"
                                                               "Calculate or compare '=' * (hp // 10), then "
                                                               'save the result in bar.\n'
                                                               '\n'
                                                               "Line 3: print(f'HP: [{bar:<10}] {hp}%')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: draw_health(70)\n'
                                                               'Call draw_health now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Line 5: draw_health(30)\n'
                                                               'Call draw_health now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: HP: [=======   ] 70%\n'
                                                               'HP: [===       ] 30%',
                                                'output': 'HP: [=======   ] 70%\nHP: [===       ] 30%',
                                                'title': 'Example 3: Reusable health bar visualizer'}],
                        'practice_questions': [{'answer': 'A function is a named group of instructions.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Reusing a task avoids copy-and-paste drift.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Defining is not calling, and indentation marks '
                                                          'the body.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a menu or status message '
                                           'used in several places. The same pattern helps a larger program '
                                           'stay clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Define once with def, then call by name with parentheses. '
                                   'Defining is not calling, and indentation marks the body The practical '
                                   'example and its line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': 'def show_menu():\n'
                                            "    print('=== MAIN MENU ===')\n"
                                            "    print('1. Start Game')\n"
                                            "    print('2. Quit')\n"
                                            'show_menu()',
                        'terminology': [{'definition': 'A named group of steps that can be called.',
                                         'term': 'Function'},
                                        {'definition': 'Create a function with def; this does not run its '
                                                       'body.',
                                         'term': 'Define'},
                                        {'definition': 'Use the function name with parentheses to run its '
                                                       'body.',
                                         'term': 'Call'}],
                        'title': 'What Are Functions?'},
             'number': 64,
             'quizzes': [{'explanation': "Calling greet() executes the function body and returns 'Hello, "
                                         "Quest!'.",
                          'options': [{'explanation': 'Correct! greet() returns the string.',
                                       'is_correct': True,
                                       'text': 'Hello, Quest!'},
                                      {'explanation': 'Incorrect. greet() calls the function; greet without '
                                                      '() references the object.',
                                       'is_correct': False,
                                       'text': '<function greet at 0x...>'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What is the output of the following function code?\n'
                                      '\n'
                                      'def greet():\n'
                                      "    return 'Hello, Quest!'\n"
                                      '\n'
                                      'print(greet())'},
                         {'explanation': 'Functions in Python are first-class objects with the type '
                                         "'function'.",
                          'options': [{'explanation': 'Correct! Functions are instances of function class.',
                                       'is_correct': True,
                                       'text': "<class 'function'>"},
                                      {'explanation': "Incorrect. 'def' is a keyword, not a type.",
                                       'is_correct': False,
                                       'text': "<class 'def'>"},
                                      {'explanation': 'Incorrect. Functions outside classes are functions, '
                                                      'not methods.',
                                       'is_correct': False,
                                       'text': "<class 'method'>"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'}],
                          'question': 'What will print(type(greet)) output when greet is a defined '
                                      'function?'}],
             'title': 'What Are Functions?'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Write print_badge so it receives a person’s name and role, then displays both in the badge format shown.\n2. Read the name and role from input and call the function.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def print_badge(name, role):\n'
                                       "    print(f'Badge: {name} | Role: {role}')\n"
                                       'name = input().strip()\n'
                                       'role = input().strip()\n'
                                       'print_badge(name, role)'],
                             'initial_code': '# Function Parameters and Arguments\n'
                                             '# Step 1: Define print_badge(name, role):\n'
                                             '\n'
                                             '# Step 2: Read inputs and call function below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def print_badge(name, role):\n'
                                              "    print(f'Badge: {name} | Role: {role}')\n"
                                              '\n'
                                              'name = input().strip()\n'
                                              'role = input().strip()\n'
                                              'print_badge(name, role)',
                             'test_cases': [{'expected_output': 'Badge: Sarah | Role: Lead Architect',
                                             'input_data': 'Sarah\nLead Architect\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Badge: Alex | Role: Developer',
                                             'input_data': 'Alex\nDeveloper\n',
                                             'is_hidden': False}],
                             'title': 'Personalized Badge Printer',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write calculate_area to multiply a rectangle’s width by its height.\n2. If either number is zero or below, print INVALID DIMENSIONS.\n3. Otherwise print the area as shown.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def calculate_area(width, height):\n'
                                       "    print(f'Area: {width * height}')\n"
                                       'w = int(input())\n'
                                       'h = int(input())\n'
                                       'calculate_area(w, h)'],
                             'initial_code': '# ⚔️ Boss Challenge: Bounded Rectangle Area Calculator\n'
                                             '# Step 1: Define calculate_area(width, height):\n'
                                             '\n'
                                             '# Step 2: Read w and h and call function:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def calculate_area(width, height):\n'
                                              '    if width <= 0 or height <= 0:\n'
                                              "        print('INVALID DIMENSIONS')\n"
                                              '    else:\n'
                                              "        print(f'Area: {width * height}')\n"
                                              '\n'
                                              'width = int(input())\n'
                                              'height = int(input())\n'
                                              'calculate_area(width, height)',
                             'test_cases': [{'expected_output': 'Area: 50',
                                             'input_data': '5\n10\n',
                                             'is_hidden': False},
                                            {'expected_output': 'INVALID DIMENSIONS',
                                             'input_data': '-3\n8\n',
                                             'is_hidden': False},
                                            {'expected_output': 'INVALID DIMENSIONS',
                                             'input_data': '7\n0\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Bounded Rectangle Area Calculator',
                             'xp_reward': 150}],
             'description': 'Pass dynamic inputs into functions and distinguish parameters from arguments.',
             'lesson': {'common_mistakes': [{'fix': 'Parameters are the receiving names; arguments are the '
                                                    'supplied values.',
                                             'mistake': 'missing required arguments raise TypeError; too '
                                                        'many do too',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: One operation often needs different '
                                                'data each time. This is the practical problem the feature '
                                                'solves.\n'
                                                '\n'
                                                'What it means: A parameter is a name in a definition; an '
                                                'argument is a value supplied by a caller. Python uses this '
                                                'idea to positional arguments fill parameters from left to '
                                                'right\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Missing required arguments raise typeerror; '
                                                'too many do too. If you change the example’s input or '
                                                'value, check this rule again because it can change the '
                                                'result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Hello, Ada. Rank: Captain',
                        'id': 65,
                        'introduction': 'Why learn this? One operation often needs different data each time. '
                                        'In this lesson, we will see a parameter is a name in a definition; '
                                        'an argument is a value supplied by a caller, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a parameter is a name in a definition; an argument '
                                                'is a value supplied by a caller in your own words.',
                                                'Trace a small Function Arguments and Parameters example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'missing required arguments raise TypeError; too many do '
                                                'too.'],
                        'level_id': 65,
                        'line_by_line': [{'code': 'def greet(name, rank):',
                                          'explanation': 'Define a function named greet. Its parameters '
                                                         '(name, rank) are local names that receive values '
                                                         'when the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '1'},
                                         {'code': "    print(f'Hello, {name}. Rank: {rank}')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '3'},
                                         {'code': "greet('Ada', 'Captain')",
                                          'explanation': 'Call greet now. Python runs its body, and any '
                                                         'returned result is available to the caller.',
                                          'line': '4'}],
                        'practical_examples': [{'code': 'def greet(name, rank):\n'
                                                        "    print(f'Hello, {name}. Rank: {rank}')\n"
                                                        '\n'
                                                        "greet('Ada', 'Captain')",
                                                'explanation': 'Purpose: Parameters receive arguments shows '
                                                               'the current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def greet(name, rank):\n'
                                                               'Define a function named greet. Its '
                                                               'parameters (name, rank) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: print(f'Hello, {name}. Rank: "
                                                               "{rank}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: greet('Ada', 'Captain')\n"
                                                               'Call greet now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Hello, Ada. Rank: Captain',
                                                'output': 'Hello, Ada. Rank: Captain',
                                                'title': 'Parameters receive arguments'},
                                               {'code': 'def show_pair(first, second):\n'
                                                        "    print(first, 'then', second)\n"
                                                        '\n'
                                                        "show_pair('North', 'South')",
                                                'explanation': 'Purpose: The order of positional arguments '
                                                               'matters shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def show_pair(first, second):\n'
                                                               'Define a function named show_pair. Its '
                                                               'parameters (first, second) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: print(first, 'then', second)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: show_pair('North', 'South')\n"
                                                               'Call show_pair now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: North then South',
                                                'output': 'North then South',
                                                'title': 'The order of positional arguments matters'},
                                               {'code': 'def announce(message):\n'
                                                        '    print(message)\n'
                                                        '\n'
                                                        "announce('Mission ready')",
                                                'explanation': 'Purpose: A missing required argument is an '
                                                               'error shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def announce(message):\n'
                                                               'Define a function named announce. Its '
                                                               'parameters (message) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: print(message)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: announce('Mission ready')\n"
                                                               'Call announce now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Mission ready',
                                                'output': 'Mission ready',
                                                'title': 'A missing required argument is an error'}],
                        'practice_questions': [{'answer': 'A parameter is a name in a definition; an '
                                                          'argument is a value supplied by a caller.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'One operation often needs different data each '
                                                          'time.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Missing required arguments raise typeerror; too '
                                                          'many do too.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a greeting function that '
                                           'receives each person name. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Parameters are the receiving names; arguments are the supplied '
                                   'values. Missing required arguments raise typeerror; too many do too The '
                                   'practical example and its line-by-line walkthrough show the idea in '
                                   'action.',
                        'syntax_breakdown': 'def greet(name, rank):\n'
                                            "    print(f'Hello, {name}. Rank: {rank}')\n"
                                            '\n'
                                            "greet('Ada', 'Captain')",
                        'terminology': [{'definition': 'A receiving name in the function definition.',
                                         'term': 'Parameter'},
                                        {'definition': 'A value supplied in a function call.',
                                         'term': 'Argument'},
                                        {'definition': 'A value matched to a parameter by its place in the '
                                                       'call.',
                                         'term': 'Positional argument'}],
                        'title': 'Function Arguments and Parameters'},
             'number': 65,
             'quizzes': [{'explanation': 'b defaults to 5. 10 + 5 = 15.',
                          'options': [{'explanation': 'Correct! 10 + 5 = 15.',
                                       'is_correct': True,
                                       'text': '15'},
                                      {'explanation': 'Incorrect. Default b=5 is added.',
                                       'is_correct': False,
                                       'text': '10'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '5'},
                                      {'explanation': 'Incorrect. b has a default value.',
                                       'is_correct': False,
                                       'text': 'TypeError: missing required argument'}],
                          'question': 'What is the output of:\n'
                                      '\n'
                                      'def add(a, b=5):\n'
                                      '    return a + b\n'
                                      '\n'
                                      'print(add(10))'},
                         {'explanation': 'Passing too many positional arguments triggers a TypeError.',
                          'options': [{'explanation': 'Correct! Argument count mismatch raises TypeError.',
                                       'is_correct': True,
                                       'text': 'TypeError: add() takes 2 positional arguments but 3 were '
                                               'given'},
                                      {'explanation': 'Incorrect. Python does not silently ignore extra '
                                                      'arguments.',
                                       'is_correct': False,
                                       'text': 'It ignores the 3rd argument and returns 3'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It returns 6'},
                                      {'explanation': 'Incorrect. It is a runtime TypeError.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What happens when you call a function expecting 2 arguments with 3 '
                                      'arguments?\n'
                                      '\n'
                                      'def add(a, b):\n'
                                      '    return a + b\n'
                                      'add(1, 2, 3)'}],
             'title': 'Function Arguments and Parameters'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Write cube so it gives back a number multiplied by itself three times.\n2. Read a whole number, call cube, and print the answer.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def cube(n):\n'
                                       '    return n ** 3\n'
                                       'val = int(input())\n'
                                       'print(cube(val))'],
                             'initial_code': '# Returning Values from Functions\n'
                                             '# Step 1: Define cube(n):\n'
                                             '\n'
                                             '# Step 2: Read val and print cube(val) below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def cube(n):\n'
                                              '    return n ** 3\n'
                                              '\n'
                                              'number = int(input())\n'
                                              'print(cube(number))',
                             'test_cases': [{'expected_output': '27',
                                             'input_data': '3\n',
                                             'is_hidden': False},
                                            {'expected_output': '125',
                                             'input_data': '5\n',
                                             'is_hidden': False}],
                             'title': 'Mathematical Cube Function',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write clamp to keep a number inside a range.\n2. Read a value, a low limit, and a high limit.\n3. Print the low limit if the value is too small, the high limit if it is too large, or the value itself if it is already inside.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def clamp(val, low, high):\n'
                                       '    return max(low, min(val, high))\n'
                                       'v = int(input())\n'
                                       'l = int(input())\n'
                                       'h = int(input())\n'
                                       'print(clamp(v, l, h))'],
                             'initial_code': '# ⚔️ Boss Challenge: Value Clamping Utility\n'
                                             '# Step 1: Define clamp(val, low, high):\n'
                                             '\n'
                                             '# Step 2: Read 3 inputs and print clamp(v, l, h):\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def clamp(val, low, high):\n'
                                              '    return max(low, min(val, high))\n'
                                              '\n'
                                              'value = int(input())\n'
                                              'low = int(input())\n'
                                              'high = int(input())\n'
                                              'print(clamp(value, low, high))',
                             'test_cases': [{'expected_output': '10',
                                             'input_data': '12\n0\n10\n',
                                             'is_hidden': False},
                                            {'expected_output': '0',
                                             'input_data': '-3\n0\n10\n',
                                             'is_hidden': False},
                                            {'expected_output': '5',
                                             'input_data': '5\n0\n10\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Value Clamping Utility',
                             'xp_reward': 150}],
             'description': "Send results back to callers using return and avoid the common 'printing "
                            "instead of returning' trap.",
             'lesson': {'common_mistakes': [{'fix': 'Use print to show a result and return to give a result '
                                                    'back.',
                                             'mistake': 'return ends that call immediately; code after it on '
                                                        'that path is skipped',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A result may need to be reused by '
                                                'another calculation. This is the practical problem the '
                                                'feature solves.\n'
                                                '\n'
                                                'What it means: Print displays a value; return hands a value '
                                                'back to the caller. Python uses this idea to the caller can '
                                                'save a returned value; a function without return gives '
                                                'None\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Return ends that call immediately; code '
                                                'after it on that path is skipped. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': '7\n14',
                        'id': 66,
                        'introduction': 'Why learn this? A result may need to be reused by another '
                                        'calculation. In this lesson, we will see print displays a value; '
                                        'return hands a value back to the caller, follow how Python handles '
                                        'it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain print displays a value; return hands a value back '
                                                'to the caller in your own words.',
                                                'Trace a small Return Statements vs print() example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'return ends that call immediately; code after it on that '
                                                'path is skipped.'],
                        'level_id': 66,
                        'line_by_line': [{'code': 'def show_total(a, b):',
                                          'explanation': 'Define a function named show_total. Its parameters '
                                                         '(a, b) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '1'},
                                         {'code': '    print(a + b)',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '3'},
                                         {'code': 'def make_total(a, b):',
                                          'explanation': 'Define a function named make_total. Its parameters '
                                                         '(a, b) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '4'},
                                         {'code': '    return a + b',
                                          'explanation': 'Send a + b back to the caller and end this '
                                                         'function call.',
                                          'line': '5'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '6'},
                                         {'code': 'show_total(4, 3)',
                                          'explanation': 'Call show_total now. Python runs its body, and any '
                                                         'returned result is available to the caller.',
                                          'line': '7'},
                                         {'code': 'total = make_total(4, 3)',
                                          'explanation': 'Store make_total(4, 3) in total so later '
                                                         'instructions can use it.',
                                          'line': '8'},
                                         {'code': 'print(total * 2)',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '9'}],
                        'practical_examples': [{'code': 'def show_total(a, b):\n'
                                                        '    print(a + b)\n'
                                                        '\n'
                                                        'def make_total(a, b):\n'
                                                        '    return a + b\n'
                                                        '\n'
                                                        'show_total(4, 3)\n'
                                                        'total = make_total(4, 3)\n'
                                                        'print(total * 2)',
                                                'explanation': 'Purpose: print shows a value but return '
                                                               'gives it back shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def show_total(a, b):\n'
                                                               'Define a function named show_total. Its '
                                                               'parameters (a, b) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: print(a + b)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 4: def make_total(a, b):\n'
                                                               'Define a function named make_total. Its '
                                                               'parameters (a, b) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 5: return a + b\n'
                                                               'Send a + b back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 6: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 7: show_total(4, 3)\n'
                                                               'Call show_total now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Line 8: total = make_total(4, 3)\n'
                                                               'Store make_total(4, 3) in total so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 9: print(total * 2)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 7\n'
                                                               '14',
                                                'output': '7\n14',
                                                'title': 'print shows a value but return gives it back'},
                                               {'code': 'def greet():\n'
                                                        "    print('Hi')\n"
                                                        '\n'
                                                        'result = greet()\n'
                                                        'print(result)',
                                                'explanation': 'Purpose: A function without return gives '
                                                               'None shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def greet():\n'
                                                               'Define a function named greet. Its '
                                                               'parameters (none) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: print('Hi')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 4: result = greet()\n'
                                                               'Store greet() in result so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: print(result)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Hi\n'
                                                               'None',
                                                'output': 'Hi\nNone',
                                                'title': 'A function without return gives None'},
                                               {'code': 'def first_match():\n'
                                                        "    return 'Found'\n"
                                                        "    print('This line is skipped')\n"
                                                        '\n'
                                                        'print(first_match())',
                                                'explanation': 'Purpose: return stops the current function '
                                                               'call shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def first_match():\n'
                                                               'Define a function named first_match. Its '
                                                               'parameters (none) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: return 'Found'\n"
                                                               "Send 'Found' back to the caller and end this "
                                                               'function call.\n'
                                                               '\n'
                                                               "Line 3: print('This line is skipped')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 5: print(first_match())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Found',
                                                'output': 'Found',
                                                'title': 'return stops the current function call'}],
                        'practice_questions': [{'answer': 'Print displays a value; return hands a value back '
                                                          'to the caller.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A result may need to be reused by another '
                                                          'calculation.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Return ends that call immediately; code after it '
                                                          'on that path is skipped.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a price calculator whose '
                                           'total is used in a receipt. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Use print to show a result and return to give a result back. '
                                   'Return ends that call immediately; code after it on that path is skipped '
                                   'The practical example and its line-by-line walkthrough show the idea in '
                                   'action.',
                        'syntax_breakdown': 'def show_total(a, b):\n'
                                            '    print(a + b)\n'
                                            '\n'
                                            'def make_total(a, b):\n'
                                            '    return a + b\n'
                                            '\n'
                                            'show_total(4, 3)\n'
                                            'total = make_total(4, 3)\n'
                                            'print(total * 2)',
                        'terminology': [{'definition': 'A result sent from a function back to its caller.',
                                         'term': 'Return value'},
                                        {'definition': 'A function that displays text or values.',
                                         'term': 'print'},
                                        {'definition': 'Python’s value meaning no result was returned.',
                                         'term': 'None'}],
                        'title': 'Return Statements vs print()'},
             'number': 66,
             'quizzes': [{'explanation': 'Python functions returning multiple comma-separated values return '
                                         'a tuple, which unpacks into hp and role.',
                          'options': [{'explanation': 'Correct! Tuple unpacking assigns hp = 100 and role = '
                                                      "'Warrior'.",
                                       'is_correct': True,
                                       'text': 'Warrior: 100 HP'},
                                      {'explanation': 'Incorrect. The order was hp, role.',
                                       'is_correct': False,
                                       'text': '100: Warrior HP'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "(100, 'Warrior'): HP"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the multiple-return function?\n'
                                      '\n'
                                      'def get_stats():\n'
                                      "    return 100, 'Warrior'\n"
                                      '\n'
                                      'hp, role = get_stats()\n'
                                      "print(f'{role}: {hp} HP')"},
                         {'explanation': 'The return statement immediately exits the function; subsequent '
                                         'code inside the function is unreachable.',
                          'options': [{'explanation': "Correct! The function terminates at return 'Done'. "
                                                      "print('End') is never reached.",
                                       'is_correct': True,
                                       'text': 'Done'},
                                      {'explanation': "Incorrect. Execution exits before print('End').",
                                       'is_correct': False,
                                       'text': 'Done\nEnd'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'End'},
                                      {'explanation': 'Incorrect. Python allows unreachable code without '
                                                      'syntax error.',
                                       'is_correct': False,
                                       'text': 'SyntaxError: unreachable code'}],
                          'question': 'What happens to lines of code written after a return statement in a '
                                      'function?\n'
                                      '\n'
                                      'def check():\n'
                                      "    return 'Done'\n"
                                      "    print('End')\n"
                                      '\n'
                                      'print(check())'}],
             'title': 'Return Statements vs print()'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Write greet with a default greeting of Hello.\n2. Call it once for Bob without choosing a greeting, then for Alice with Welcome.\n3. Print both messages.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["def greet(name, greeting='Hello'):\n"
                                       "    print(f'{greeting}, {name}!')\n"
                                       "greet('Bob')\n"
                                       "greet('Alice', 'Welcome')"],
                             'initial_code': '# Default Parameters\n'
                                             "# Step 1: Define greet(name, greeting='Hello'):\n"
                                             '\n'
                                             "# Step 2: Call greet('Bob') then greet('Alice', 'Welcome'):\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "def greet(name, greeting='Hello'):\n"
                                              "    print(f'{greeting}, {name}!')\n"
                                              '\n'
                                              "greet('Bob')\n"
                                              "greet('Alice', 'Welcome')",
                             'test_cases': [{'expected_output': 'Hello, Bob!\nWelcome, Alice!',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Configurable Greeting Herald',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write create_user so a new user gets the role guest and active status True unless different values are provided.\n2. Print the user details in the format shown.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["def create_user(username, role='guest', is_active=True):\n"
                                       "    print(f'User: {username}, Role: {role}, Active: {is_active}')\n"
                                       "create_user('john')\n"
                                       "create_user('admin_boss', 'admin', True)"],
                             'initial_code': '# ⚔️ Boss Challenge: User Account Factory\n'
                                             '# Step 1: Define create_user with defaults:\n'
                                             '\n'
                                             "# Step 2: Call create_user('john') and "
                                             "create_user('admin_boss', 'admin', True):\n"
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "def create_user(username, role='guest', is_active=True):\n"
                                              "    print(f'User: {username}, Role: {role}, Active: "
                                              "{is_active}')\n"
                                              '\n'
                                              "create_user('Mia')\n"
                                              "create_user('Kai', role='admin', is_active=False)",
                             'test_cases': [{'expected_output': 'User: Mia, Role: guest, Active: True\n'
                                                                'User: Kai, Role: admin, Active: False',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: User Account Factory',
                             'xp_reward': 150}],
             'description': 'Make parameters optional with sensible defaults and beware of mutable default '
                            'pitfalls.',
             'lesson': {'common_mistakes': [{'fix': 'Defaults are shared rules; mutable default objects can '
                                                    'unexpectedly be shared too.',
                                             'mistake': 'a mutable default list is reused across calls; use '
                                                        'None and create a fresh list inside',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Many calls need the same usual value '
                                                'but sometimes a custom one. This is the practical problem '
                                                'the feature solves.\n'
                                                '\n'
                                                'What it means: A default is used only when that argument is '
                                                'omitted. Python uses this idea to required parameters come '
                                                'before parameters with defaults\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: A mutable default list is reused across '
                                                'calls; use none and create a fresh list inside. If you '
                                                'change the example’s input or value, check this rule again '
                                                'because it can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': "['map']\n['key']",
                        'id': 67,
                        'introduction': 'Why learn this? Many calls need the same usual value but sometimes '
                                        'a custom one. In this lesson, we will see a default is used only '
                                        'when that argument is omitted, follow how Python handles it, and '
                                        'practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a default is used only when that argument is '
                                                'omitted in your own words.',
                                                'Trace a small Default Parameter Values example and predict '
                                                'what Python does next.',
                                                'Use the concept safely, including this important rule: a '
                                                'mutable default list is reused across calls; use None and '
                                                'create a fresh list inside.'],
                        'level_id': 67,
                        'line_by_line': [{'code': 'def add_item(item, items=None):',
                                          'explanation': 'Define a function named add_item. Its parameters '
                                                         '(item, items=None) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '1'},
                                         {'code': '    if items is None:',
                                          'explanation': 'Check whether items is None is true. If it is, run '
                                                         'the indented block; otherwise Python skips that '
                                                         'block.',
                                          'line': '2'},
                                         {'code': '        items = []',
                                          'explanation': 'Create the list shown and store it in items. The '
                                                         'list keeps items in order and can be processed one '
                                                         'item at a time.',
                                          'line': '3'},
                                         {'code': '    items.append(item)',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '4'},
                                         {'code': '    return items',
                                          'explanation': 'Send items back to the caller and end this '
                                                         'function call.',
                                          'line': '5'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '6'},
                                         {'code': "print(add_item('map'))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '7'},
                                         {'code': "print(add_item('key'))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '8'}],
                        'practical_examples': [{'code': 'def add_item(item, items=None):\n'
                                                        '    if items is None:\n'
                                                        '        items = []\n'
                                                        '    items.append(item)\n'
                                                        '    return items\n'
                                                        '\n'
                                                        "print(add_item('map'))\n"
                                                        "print(add_item('key'))",
                                                'explanation': 'Purpose: A safe default list uses None shows '
                                                               'the current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def add_item(item, items=None):\n'
                                                               'Define a function named add_item. Its '
                                                               'parameters (item, items=None) are local '
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: if items is None:\n'
                                                               'Check whether items is None is true. If it '
                                                               'is, run the indented block; otherwise Python '
                                                               'skips that block.\n'
                                                               '\n'
                                                               'Line 3: items = []\n'
                                                               'Create the list shown and store it in items. '
                                                               'The list keeps items in order and can be '
                                                               'processed one item at a time.\n'
                                                               '\n'
                                                               'Line 4: items.append(item)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 5: return items\n'
                                                               'Send items back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 6: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 7: print(add_item('map'))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 8: print(add_item('key'))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Output trace: ['map']\n"
                                                               "['key']",
                                                'output': "['map']\n['key']",
                                                'title': 'A safe default list uses None'},
                                               {'code': "def greet(name, greeting='Hello'):\n"
                                                        "    print(f'{greeting}, {name}!')\n"
                                                        '\n'
                                                        "greet('Mia')\n"
                                                        "greet('Mia', 'Welcome')",
                                                'explanation': 'Purpose: Omitted and supplied defaults shows '
                                                               'the current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: def greet(name, greeting='Hello'):\n"
                                                               'Define a function named greet. Its '
                                                               "parameters (name, greeting='Hello') are "
                                                               'local names that receive values when the '
                                                               'function is called. The colon starts the '
                                                               'indented body; defining it does not run it '
                                                               'yet.\n'
                                                               '\n'
                                                               "Line 2: print(f'{greeting}, {name}!')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: greet('Mia')\n"
                                                               'Call greet now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               "Line 5: greet('Mia', 'Welcome')\n"
                                                               'Call greet now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Hello, Mia!\n'
                                                               'Welcome, Mia!',
                                                'output': 'Hello, Mia!\nWelcome, Mia!',
                                                'title': 'Omitted and supplied defaults'},
                                               {'code': "def label(name, role='Explorer'):\n"
                                                        "    print(f'{name}: {role}')\n"
                                                        '\n'
                                                        "label('Kai')",
                                                'explanation': 'Purpose: Required parameters come first '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: def label(name, role='Explorer'):\n"
                                                               'Define a function named label. Its '
                                                               "parameters (name, role='Explorer') are local "
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: print(f'{name}: {role}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: label('Kai')\n"
                                                               'Call label now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Kai: Explorer',
                                                'output': 'Kai: Explorer',
                                                'title': 'Required parameters come first'}],
                        'practice_questions': [{'answer': 'A default is used only when that argument is '
                                                          'omitted.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Many calls need the same usual value but '
                                                          'sometimes a custom one.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'A mutable default list is reused across calls; '
                                                          'use none and create a fresh list inside.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is optional greeting text or '
                                           'a fresh list of reminders. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Defaults are shared rules; mutable default objects can '
                                   'unexpectedly be shared too. A mutable default list is reused across '
                                   'calls; use none and create a fresh list inside The practical example and '
                                   'its line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': 'def add_item(item, items=None):\n'
                                            '    if items is None:\n'
                                            '        items = []\n'
                                            '    items.append(item)\n'
                                            '    return items\n'
                                            '\n'
                                            "print(add_item('map'))\n"
                                            "print(add_item('key'))",
                        'terminology': [{'definition': 'A value used when a caller leaves an optional '
                                                       'argument out.',
                                         'term': 'Default value'},
                                        {'definition': 'An object, such as a list, whose contents can '
                                                       'change.',
                                         'term': 'Mutable'},
                                        {'definition': 'Use None as a default, then create a fresh mutable '
                                                       'object inside the function.',
                                         'term': 'None pattern'}],
                        'title': 'Default Parameter Values'},
             'number': 67,
             'quizzes': [{'explanation': 'Parameters without defaults cannot follow parameters with default '
                                         'values.',
                          'options': [{'explanation': "Correct! Non-default parameter 'b' cannot follow "
                                                      "default parameter 'a=10'.",
                                       'is_correct': True,
                                       'text': 'def calc(a=10, b): return a + b'},
                                      {'explanation': 'Valid parameter ordering.',
                                       'is_correct': False,
                                       'text': 'def calc(a, b=10): return a + b'},
                                      {'explanation': 'Valid: all have default values.',
                                       'is_correct': False,
                                       'text': 'def calc(a=5, b=10): return a + b'},
                                      {'explanation': 'Valid positional parameters.',
                                       'is_correct': False,
                                       'text': 'def calc(a, b): return a + b'}],
                          'question': 'Which of the following function definitions is invalid syntax in '
                                      'Python?'},
                         {'explanation': 'Default arguments are evaluated once at function definition. The '
                                         'same list is mutated across calls: [1, 2].',
                          'options': [{'explanation': 'Correct! The mutable default list persists state '
                                                      'between function calls.',
                                       'is_correct': True,
                                       'text': '[1, 2]'},
                                      {'explanation': 'Incorrect. The list was already mutated to [1] on the '
                                                      'first call.',
                                       'is_correct': False,
                                       'text': '[2]'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '[1]'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '[[1], [2]]'}],
                          'question': 'What is the output of this code with a mutable default argument?\n'
                                      '\n'
                                      'def add_item(item, lst=[]):\n'
                                      '    lst.append(item)\n'
                                      '    return lst\n'
                                      '\n'
                                      'add_item(1)\n'
                                      'print(add_item(2))'}],
             'title': 'Default Parameter Values'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Write send_email to receive a recipient, subject, and message.\n2. Read those three lines, pass them to the function by name, and print the email details in the shown format.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def send_email(to, subject, body):\n'
                                       "    print(f'To: {to} | Subject: {subject} | Body: {body}')\n"
                                       "send_email(subject='Meeting', to='boss@corp.com', body='Ready')"],
                             'initial_code': '# Keyword Arguments (kwargs)\n'
                                             '# Step 1: Define send_email(to, subject, body):\n'
                                             '\n'
                                             '# Step 2: Call with explicit keyword arguments:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def send_email(to, subject, body):\n'
                                              "    print(f'To: {to} | Subject: {subject} | Body: {body}')\n"
                                              '\n'
                                              'recipient = input().strip()\n'
                                              'subject = input().strip()\n'
                                              'body = input().strip()\n'
                                              'send_email(to=recipient, subject=subject, body=body)',
                             'test_cases': [{'expected_output': 'To: ada@example.com | Subject: Quest update '
                                                                '| Body: Your next level is ready.',
                                             'input_data': 'ada@example.com\n'
                                                           'Quest update\n'
                                                           'Your next level is ready.\n',
                                             'is_hidden': False},
                                            {'expected_output': 'To: kai@example.com | Subject: Welcome | '
                                                                'Body: Have fun learning Python.',
                                             'input_data': 'kai@example.com\n'
                                                           'Welcome\n'
                                                           'Have fun learning Python.\n',
                                             'is_hidden': False}],
                             'title': 'Explicit Named Parameters',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write build_query to create the SQL text shown in the example.\n2. Use ASC for the sort order and 10 for the row limit when those values are not provided.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["def build_query(table, limit=10, order='ASC'):\n"
                                       "    print(f'SELECT * FROM {table} ORDER BY id {order} LIMIT "
                                       "{limit}')\n"
                                       "build_query(table='users', order='DESC', limit=5)"],
                             'initial_code': '# ⚔️ Boss Challenge: Dynamic SQL Query Builder\n'
                                             '# Step 1: Define build_query:\n'
                                             '\n'
                                             '# Step 2: Call with custom order and limit:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "def build_query(table, limit=10, order='ASC'):\n"
                                              "    print(f'SELECT * FROM {table} ORDER BY id {order} LIMIT "
                                              "{limit}')\n"
                                              '\n'
                                              "build_query(table='users', order='DESC', limit=5)",
                             'test_cases': [{'expected_output': 'SELECT * FROM users ORDER BY id DESC LIMIT '
                                                                '5',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Dynamic SQL Query Builder',
                             'xp_reward': 150}],
             'description': 'Pass arguments by parameter name for clarity, self-documenting code, and '
                            'parameter reordering.',
             'lesson': {'common_mistakes': [{'fix': 'Use parameter_name=value when the name makes a call '
                                                    'clearer.',
                                             'mistake': 'positional arguments must come before keyword '
                                                        'arguments in a call',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Long calls become hard to read when '
                                                'values are only identified by position. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: A keyword argument names the parameter it '
                                                'fills. Python uses this idea to positional values bind by '
                                                'order; keyword values bind by name\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Positional arguments must come before '
                                                'keyword arguments in a call. If you change the example’s '
                                                'input or value, check this rule again because it can change '
                                                'the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Lina | Builder | Level 4',
                        'id': 68,
                        'introduction': 'Why learn this? Long calls become hard to read when values are only '
                                        'identified by position. In this lesson, we will see a keyword '
                                        'argument names the parameter it fills, follow how Python handles '
                                        'it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a keyword argument names the parameter it fills in '
                                                'your own words.',
                                                'Trace a small Keyword Arguments (Named Arguments) example '
                                                'and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'positional arguments must come before keyword arguments in '
                                                'a call.'],
                        'level_id': 68,
                        'line_by_line': [{'code': 'def make_badge(name, role, level):',
                                          'explanation': 'Define a function named make_badge. Its parameters '
                                                         '(name, role, level) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '1'},
                                         {'code': "    print(f'{name} | {role} | Level {level}')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '3'},
                                         {'code': "make_badge(name='Lina', level=4, role='Builder')",
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '4'}],
                        'practical_examples': [{'code': 'def make_badge(name, role, level):\n'
                                                        "    print(f'{name} | {role} | Level {level}')\n"
                                                        '\n'
                                                        "make_badge(name='Lina', level=4, role='Builder')",
                                                'explanation': 'Purpose: Name arguments to make a call clear '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def make_badge(name, role, level):\n'
                                                               'Define a function named make_badge. Its '
                                                               'parameters (name, role, level) are local '
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: print(f'{name} | {role} | Level "
                                                               "{level}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: make_badge(name='Lina', level=4, "
                                                               "role='Builder')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Output trace: Lina | Builder | Level 4',
                                                'output': 'Lina | Builder | Level 4',
                                                'title': 'Name arguments to make a call clear'},
                                               {'code': "def greet(name, greeting='Hello'):\n"
                                                        "    print(f'{greeting}, {name}!')\n"
                                                        '\n'
                                                        "greet('Sam', greeting='Welcome')",
                                                'explanation': 'Purpose: Positional first, then keyword '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: def greet(name, greeting='Hello'):\n"
                                                               'Define a function named greet. Its '
                                                               "parameters (name, greeting='Hello') are "
                                                               'local names that receive values when the '
                                                               'function is called. The colon starts the '
                                                               'indented body; defining it does not run it '
                                                               'yet.\n'
                                                               '\n'
                                                               "Line 2: print(f'{greeting}, {name}!')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: greet('Sam', greeting='Welcome')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Output trace: Welcome, Sam!',
                                                'output': 'Welcome, Sam!',
                                                'title': 'Positional first, then keyword'},
                                               {'code': 'def set_level(level):\n'
                                                        '    print(level)\n'
                                                        '\n'
                                                        'set_level(level=3)',
                                                'explanation': 'Purpose: A keyword cannot be supplied twice '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def set_level(level):\n'
                                                               'Define a function named set_level. Its '
                                                               'parameters (level) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: print(level)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 4: set_level(level=3)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Output trace: 3',
                                                'output': '3',
                                                'title': 'A keyword cannot be supplied twice'}],
                        'practice_questions': [{'answer': 'A keyword argument names the parameter it fills.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Long calls become hard to read when values are '
                                                          'only identified by position.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Positional arguments must come before keyword '
                                                          'arguments in a call.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is creating a report with '
                                           'named date, title, and format options. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Use parameter_name=value when the name makes a call clearer. '
                                   'Positional arguments must come before keyword arguments in a call The '
                                   'practical example and its line-by-line walkthrough show the idea in '
                                   'action.',
                        'syntax_breakdown': 'def make_badge(name, role, level):\n'
                                            "    print(f'{name} | {role} | Level {level}')\n"
                                            '\n'
                                            "make_badge(name='Lina', level=4, role='Builder')",
                        'terminology': [{'definition': 'A call value written with its parameter name.',
                                         'term': 'Keyword argument'},
                                        {'definition': 'Matching a supplied value to a parameter.',
                                         'term': 'Binding'},
                                        {'definition': 'Positional arguments come before keyword arguments.',
                                         'term': 'Call order'}],
                        'title': 'Keyword Arguments (Named Arguments)'},
             'number': 68,
             'quizzes': [{'explanation': 'Keyword arguments explicitly bind values by parameter name '
                                         'regardless of call order. 10 / 2 = 5.0.',
                          'options': [{'explanation': 'Correct! Keyword arguments map a=10 and b=2 '
                                                      'regardless of position.',
                                       'is_correct': True,
                                       'text': '5.0'},
                                      {'explanation': 'Incorrect. Parameter names explicitly map inputs.',
                                       'is_correct': False,
                                       'text': '0.2'},
                                      {'explanation': 'Incorrect. Division returns float.',
                                       'is_correct': False,
                                       'text': '5'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of calling a function with keyword arguments out '
                                      'of order?\n'
                                      '\n'
                                      'def divide(a, b):\n'
                                      '    return a / b\n'
                                      '\n'
                                      'print(divide(b=2, a=10))'},
                         {'explanation': 'Positional arguments cannot follow keyword arguments in Python '
                                         'function calls.',
                          'options': [{'explanation': 'Correct! Positional argument cannot follow keyword '
                                                      'argument.',
                                       'is_correct': True,
                                       'text': 'divide(a=10, 2)'},
                                      {'explanation': 'Valid: positional argument comes first.',
                                       'is_correct': False,
                                       'text': 'divide(10, b=2)'},
                                      {'explanation': 'Valid keyword arguments.',
                                       'is_correct': False,
                                       'text': 'divide(a=10, b=2)'},
                                      {'explanation': 'Valid positional arguments.',
                                       'is_correct': False,
                                       'text': 'divide(10, 2)'}],
                          'question': 'Which of the following function calls raises a SyntaxError?'}],
             'title': 'Keyword Arguments (Named Arguments)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Write sum_all so it can receive any number of values and give back their total.\n2. Read the values on one line, call the function, and print the total.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def sum_all(*args):\n'
                                       '    return sum(args)\n'
                                       'print(sum_all(1, 2, 3, 4, 5))'],
                             'initial_code': '# Arbitrary Arguments (*args)\n'
                                             '# Step 1: Define sum_all(*args):\n'
                                             '\n'
                                             '# Step 2: Print sum_all(1, 2, 3, 4, 5) below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def sum_all(*args):\n'
                                              '    return sum(args)\n'
                                              '\n'
                                              'numbers = [int(value) for value in input().split()]\n'
                                              'print(sum_all(*numbers))',
                             'test_cases': [{'expected_output': '15',
                                             'input_data': '1 2 3 4 5\n',
                                             'is_hidden': False},
                                            {'expected_output': '15',
                                             'input_data': '10 -2 7\n',
                                             'is_hidden': False}],
                             'title': 'Arbitrary Positional Sum',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write describe_pet to receive a pet’s name and any extra named details.\n2. Print the details in alphabetical order by their names, using the format shown.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def describe_pet(name, **kwargs):\n'
                                       "    parts = [f'{k}={v}' for k, v in sorted(kwargs.items())]\n"
                                       "    print(f'{name}: ' + ', '.join(parts))\n"
                                       "describe_pet('Buddy', age=3, breed='Golden')"],
                             'initial_code': '# ⚔️ Boss Challenge: Dynamic Entity Descriptor\n'
                                             '# Step 1: Define describe_pet(name, **kwargs):\n'
                                             '\n'
                                             "# Step 2: Call describe_pet('Buddy', age=3, breed='Golden'):\n"
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def describe_pet(name, **kwargs):\n'
                                              "    details = ', '.join(f'{key}={value}' for key, value in "
                                              'sorted(kwargs.items()))\n'
                                              "    print(f'{name}: {details}')\n"
                                              '\n'
                                              "describe_pet('Luna', species='cat', age=3)\n"
                                              "describe_pet('Rex', color='brown', species='dog')",
                             'test_cases': [{'expected_output': 'Luna: age=3, species=cat\n'
                                                                'Rex: color=brown, species=dog',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Dynamic Entity Descriptor',
                             'xp_reward': 150}],
             'description': 'Accept arbitrary numbers of positional arguments using the asterisk prefix.',
             'lesson': {'common_mistakes': [{'fix': 'In a definition *args collects; in a call *items '
                                                    'unpacks.',
                                             'mistake': 'collecting with *args differs from unpacking with * '
                                                        'at the call site',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Some functions should accept any '
                                                'number of same-kind values. This is the practical problem '
                                                'the feature solves.\n'
                                                '\n'
                                                'What it means: *args gathers extra positional arguments '
                                                'into a tuple named args by convention. Python uses this '
                                                'idea to the function can loop over that tuple; a call-site '
                                                '* unpacks an iterable\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Collecting with *args differs from '
                                                'unpacking with * at the call site. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'tuple\n60',
                        'id': 69,
                        'introduction': 'Why learn this? Some functions should accept any number of '
                                        'same-kind values. In this lesson, we will see *args gathers extra '
                                        'positional arguments into a tuple named args by convention, follow '
                                        'how Python handles it, and practice a small example you can change '
                                        'yourself.',
                        'learning_objectives': ['Explain *args gathers extra positional arguments into a '
                                                'tuple named args by convention in your own words.',
                                                'Trace a small Variable-Length Arguments (*args) example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'collecting with *args differs from unpacking with * at the '
                                                'call site.'],
                        'level_id': 69,
                        'line_by_line': [{'code': 'def add_scores(*scores):',
                                          'explanation': 'Define a function named add_scores. Its parameters '
                                                         '(*scores) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '1'},
                                         {'code': '    print(type(scores).__name__)',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': '    return sum(scores)',
                                          'explanation': 'Send sum(scores) back to the caller and end this '
                                                         'function call.',
                                          'line': '3'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '4'},
                                         {'code': 'print(add_scores(10, 20, 30))',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '5'}],
                        'practical_examples': [{'code': 'def add_scores(*scores):\n'
                                                        '    print(type(scores).__name__)\n'
                                                        '    return sum(scores)\n'
                                                        '\n'
                                                        'print(add_scores(10, 20, 30))',
                                                'explanation': 'Purpose: Collect any number of scores with '
                                                               '*args shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def add_scores(*scores):\n'
                                                               'Define a function named add_scores. Its '
                                                               'parameters (*scores) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: print(type(scores).__name__)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: return sum(scores)\n'
                                                               'Send sum(scores) back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 5: print(add_scores(10, 20, 30))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: tuple\n'
                                                               '60',
                                                'output': 'tuple\n60',
                                                'title': 'Collect any number of scores with *args'},
                                               {'code': 'def show_tags(*tags):\n'
                                                        '    for tag in tags:\n'
                                                        "        print('Tag:', tag)\n"
                                                        '\n'
                                                        "show_tags('new', 'sale')",
                                                'explanation': 'Purpose: Loop through the collected tuple '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def show_tags(*tags):\n'
                                                               'Define a function named show_tags. Its '
                                                               'parameters (*tags) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: for tag in tags:\n'
                                                               'Start a loop. Each turn, take the next value '
                                                               'from tags and store it in tag before running '
                                                               'the indented block.\n'
                                                               '\n'
                                                               "Line 3: print('Tag:', tag)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 5: show_tags('new', 'sale')\n"
                                                               'Call show_tags now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Tag: new\n'
                                                               'Tag: sale',
                                                'output': 'Tag: new\nTag: sale',
                                                'title': 'Loop through the collected tuple'},
                                               {'code': 'def add_scores(*scores):\n'
                                                        '    return sum(scores)\n'
                                                        '\n'
                                                        'points = [4, 6, 10]\n'
                                                        'print(add_scores(*points))',
                                                'explanation': 'Purpose: Unpack a list at the call site '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def add_scores(*scores):\n'
                                                               'Define a function named add_scores. Its '
                                                               'parameters (*scores) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: return sum(scores)\n'
                                                               'Send sum(scores) back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 4: points = [4, 6, 10]\n'
                                                               'Create the list shown and store it in '
                                                               'points. The list keeps items in order and '
                                                               'can be processed one item at a time.\n'
                                                               '\n'
                                                               'Line 5: print(add_scores(*points))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 20',
                                                'output': '20',
                                                'title': 'Unpack a list at the call site'}],
                        'practice_questions': [{'answer': '*args gathers extra positional arguments into a '
                                                          'tuple named args by convention.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Some functions should accept any number of '
                                                          'same-kind values.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Collecting with *args differs from unpacking with '
                                                          '* at the call site.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is adding an unknown number '
                                           'of quiz scores. The same pattern helps a larger program stay '
                                           'clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: In a definition *args collects; in a call *items unpacks. '
                                   'Collecting with *args differs from unpacking with * at the call site The '
                                   'practical example and its line-by-line walkthrough show the idea in '
                                   'action.',
                        'syntax_breakdown': 'def add_scores(*scores):\n'
                                            '    print(type(scores).__name__)\n'
                                            '    return sum(scores)\n'
                                            '\n'
                                            'print(add_scores(10, 20, 30))',
                        'terminology': [{'definition': 'A tuple that collects extra positional arguments.',
                                         'term': '*args'},
                                        {'definition': 'An ordered collection of values.', 'term': 'Tuple'},
                                        {'definition': 'Using * at a call site to pass items as separate '
                                                       'arguments.',
                                         'term': 'Unpacking'}],
                        'title': 'Variable-Length Arguments (*args)'},
             'number': 69,
             'quizzes': [{'explanation': '*args packs positional arguments into a tuple (10, 20, 30). '
                                         'sum(args) = 60.',
                          'options': [{'explanation': 'Correct! sum(10, 20, 30) = 60.',
                                       'is_correct': True,
                                       'text': '60'},
                                      {'explanation': 'Incorrect. The return value is sum(args).',
                                       'is_correct': False,
                                       'text': '(10, 20, 30)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '[10, 20, 30]'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the variable arguments function?\n'
                                      '\n'
                                      'def total(*args):\n'
                                      '    return sum(args)\n'
                                      '\n'
                                      'print(total(10, 20, 30))'},
                         {'explanation': '*args collects variable arguments into an immutable tuple.',
                          'options': [{'explanation': 'Correct! *args is packed into a tuple.',
                                       'is_correct': True,
                                       'text': "<class 'tuple'>"},
                                      {'explanation': 'Incorrect. args is a tuple, not a list.',
                                       'is_correct': False,
                                       'text': "<class 'list'>"},
                                      {'explanation': 'Incorrect. **kwargs is a dict.',
                                       'is_correct': False,
                                       'text': "<class 'dict'>"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "<class 'set'>"}],
                          'question': 'What data type does `args` hold inside a function with `def '
                                      'f(*args):`?'}],
             'title': 'Variable-Length Arguments (*args)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use extra named details to collect any named details.\n2. Call describe_user with a name, role, and level, then print the details in sorted order.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def describe_user(name, **details):\n'
                                       "    text = ', '.join(f'{key}={value}' for key, value in "
                                       'sorted(details.items()))\n'
                                       "    print(f'{name}: {text}')\n"
                                       "describe_user('Mia', role='mage', level=5)"],
                             'initial_code': '# Variable Scope: Local vs Global\n'
                                             'x = 10\n'
                                             '# Step 1: Define show_scope() with local x = 20:\n'
                                             '\n'
                                             '# Step 2: Call function and print global x:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def describe_user(name, **details):\n'
                                              "    text = ', '.join(f'{key}={value}' for key, value in "
                                              'sorted(details.items()))\n'
                                              "    print(f'{name}: {text}')\n"
                                              "describe_user('Mia', role='mage', level=5)",
                             'test_cases': [{'expected_output': 'Mia: level=5, role=mage',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Keyword Detail Builder',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write print_profile(name, details).\n2. Call it twice with different named details and print each profile.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def print_profile(name, **details):\n'
                                       "    details_text = ', '.join(f'{key}={value}' for key, value in "
                                       'sorted(details.items()))\n'
                                       "    print(f'{name}: {details_text}')\n"
                                       "print_profile('Ari', role='builder', active=True)\n"
                                       "print_profile('Bo', team='blue')"],
                             'initial_code': '# ⚔️ Boss Challenge: Global Score Accumulator\n'
                                             'score = 0\n'
                                             '# Step 1: Define add_points(pts) using global score:\n'
                                             '\n'
                                             '# Step 2: Call add_points(50), add_points(25), print(score):\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def print_profile(name, **details):\n'
                                              "    details_text = ', '.join(f'{key}={value}' for key, value "
                                              'in sorted(details.items()))\n'
                                              "    print(f'{name}: {details_text}')\n"
                                              "print_profile('Ari', role='builder', active=True)\n"
                                              "print_profile('Bo', team='blue')",
                             'test_cases': [{'expected_output': 'Ari: active=True, role=builder\n'
                                                                'Bo: team=blue',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Flexible Profile Printer',
                             'xp_reward': 150}],
             'description': 'Accept arbitrary named arguments packed into a dictionary using double '
                            'asterisks.',
             'lesson': {'common_mistakes': [{'fix': 'In a definition **kwargs collects named options into a '
                                                    'dictionary.',
                                             'mistake': 'a required named parameter can come before '
                                                        '**kwargs; **kwargs belongs last',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Some functions need flexible options '
                                                'whose names are chosen by callers. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: **kwargs collects extra named values into a '
                                                'dictionary. Python uses this idea to read values by key or '
                                                'loop through key-value pairs; **options unpacks a '
                                                'dictionary\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: A required named parameter can come before '
                                                '**kwargs; **kwargs belongs last. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'dict\nblue',
                        'id': 70,
                        'introduction': 'Why learn this? Some functions need flexible options whose names '
                                        'are chosen by callers. In this lesson, we will see **kwargs '
                                        'collects extra named values into a dictionary, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain **kwargs collects extra named values into a '
                                                'dictionary in your own words.',
                                                'Trace a small Variable-Length Keyword Arguments (**kwargs) '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: a '
                                                'required named parameter can come before **kwargs; **kwargs '
                                                'belongs last.'],
                        'level_id': 70,
                        'line_by_line': [{'code': 'def show_options(**options):',
                                          'explanation': 'Define a function named show_options. Its '
                                                         'parameters (**options) are local names that '
                                                         'receive values when the function is called. The '
                                                         'colon starts the indented body; defining it does '
                                                         'not run it yet.',
                                          'line': '1'},
                                         {'code': '    print(type(options).__name__)',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '2'},
                                         {'code': "    print(options['color'])",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '4'},
                                         {'code': "show_options(color='blue', size='large')",
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '5'}],
                        'practical_examples': [{'code': 'def show_options(**options):\n'
                                                        '    print(type(options).__name__)\n'
                                                        "    print(options['color'])\n"
                                                        '\n'
                                                        "show_options(color='blue', size='large')",
                                                'explanation': 'Purpose: Collect named options with **kwargs '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def show_options(**options):\n'
                                                               'Define a function named show_options. Its '
                                                               'parameters (**options) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: print(type(options).__name__)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 3: print(options['color'])\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 5: show_options(color='blue', "
                                                               "size='large')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Output trace: dict\n'
                                                               'blue',
                                                'output': 'dict\nblue',
                                                'title': 'Collect named options with **kwargs'},
                                               {'code': 'def show_settings(**settings):\n'
                                                        '    for name, value in settings.items():\n'
                                                        "        print(f'{name}: {value}')\n"
                                                        '\n'
                                                        "show_settings(sound='on', hints='yes')",
                                                'explanation': 'Purpose: Read each key and value shows the '
                                                               'current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def show_settings(**settings):\n'
                                                               'Define a function named show_settings. Its '
                                                               'parameters (**settings) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: for name, value in '
                                                               'settings.items():\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 3: print(f'{name}: {value}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 5: show_settings(sound='on', "
                                                               "hints='yes')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Output trace: sound: on\n'
                                                               'hints: yes',
                                                'output': 'sound: on\nhints: yes',
                                                'title': 'Read each key and value'},
                                               {'code': 'def greet(name, **details):\n'
                                                        "    print(name, details['role'])\n"
                                                        '\n'
                                                        "options = {'role': 'Guide'}\n"
                                                        "greet('Mina', **options)",
                                                'explanation': 'Purpose: Unpack a dictionary at the call '
                                                               'site shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def greet(name, **details):\n'
                                                               'Define a function named greet. Its '
                                                               'parameters (name, **details) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               "Line 2: print(name, details['role'])\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 4: options = {'role': 'Guide'}\n"
                                                               "Store {'role': 'Guide'} in options so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 5: greet('Mina', **options)\n"
                                                               'Call greet now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Output trace: Mina Guide',
                                                'output': 'Mina Guide',
                                                'title': 'Unpack a dictionary at the call site'}],
                        'practice_questions': [{'answer': '**kwargs collects extra named values into a '
                                                          'dictionary.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Some functions need flexible options whose names '
                                                          'are chosen by callers.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'A required named parameter can come before '
                                                          '**kwargs; **kwargs belongs last.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is optional profile or '
                                           'display settings. The same pattern helps a larger program stay '
                                           'clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: In a definition **kwargs collects named options into a '
                                   'dictionary. A required named parameter can come before **kwargs; '
                                   '**kwargs belongs last The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'def show_options(**options):\n'
                                            '    print(type(options).__name__)\n'
                                            "    print(options['color'])\n"
                                            '\n'
                                            "show_options(color='blue', size='large')",
                        'terminology': [{'definition': 'A dictionary that collects extra keyword arguments.',
                                         'term': '**kwargs'},
                                        {'definition': 'A collection of key-value pairs.',
                                         'term': 'Dictionary'},
                                        {'definition': 'A dictionary method that gives each key and value '
                                                       'together.',
                                         'term': 'items()'}],
                        'title': 'Variable-Length Keyword Arguments (**kwargs)'},
             'number': 70,
             'quizzes': [{'explanation': '**kwargs captures keyword arguments into a dict. '
                                         "kwargs.get('role') returns 'Mage'.",
                          'options': [{'explanation': "Correct! kwargs['role'] is 'Mage'.",
                                       'is_correct': True,
                                       'text': 'Mage'},
                                      {'explanation': "Incorrect. 'role' was provided as 'Mage'.",
                                       'is_correct': False,
                                       'text': 'Novice'},
                                      {'explanation': "Incorrect. The function returns kwargs.get('role').",
                                       'is_correct': False,
                                       'text': "{'name': 'Leo', 'role': 'Mage'}"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'Leo'}],
                          'question': 'What is the output of the kwargs function?\n'
                                      '\n'
                                      'def make_profile(**kwargs):\n'
                                      "    return kwargs.get('role', 'Novice')\n"
                                      '\n'
                                      "print(make_profile(name='Leo', role='Mage'))"},
                         {'explanation': 'Standard order: positional arguments, *args, keyword defaults, '
                                         '**kwargs.',
                          'options': [{'explanation': 'Correct! Positional, *args, keyword defaults, '
                                                      '**kwargs.',
                                       'is_correct': True,
                                       'text': 'def f(a, *args, b=10, **kwargs):'},
                                      {'explanation': 'Incorrect. **kwargs must come last.',
                                       'is_correct': False,
                                       'text': 'def f(**kwargs, *args):'},
                                      {'explanation': 'a would become keyword-only.',
                                       'is_correct': False,
                                       'text': 'def f(*args, a, **kwargs):'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'def f(**kwargs, a=10):'}],
                          'question': 'Which parameter order is strictly required by Python syntax?'}],
             'title': 'Variable-Length Keyword Arguments (**kwargs)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. A variable created inside a function is local to that function.\n2. Show a local score of 20 and the unchanged global score of 10.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['score = 10\n'
                                       'def show_score():\n'
                                       '    score = 20\n'
                                       "    print('Local:', score)\n"
                                       'show_score()\n'
                                       "print('Global:', score)"],
                             'initial_code': '# Lambda Functions: Anonymous Single-Line Functions\n'
                                             '# Step 1: Define double = lambda x: x * 2\n'
                                             '\n'
                                             '# Step 2: Read n and print double(n):\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'score = 10\n'
                                              'def show_score():\n'
                                              '    score = 20\n'
                                              "    print('Local:', score)\n"
                                              'show_score()\n'
                                              "print('Global:', score)",
                             'test_cases': [{'expected_output': 'Local: 20\nGlobal: 10',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Local and Global Score',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use global to add points to the shared score.\n2. Add 50 and then 25, and print the final score.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['score = 0\n'
                                       'def add_points(points):\n'
                                       '    global score\n'
                                       '    score += points\n'
                                       'add_points(50)\n'
                                       'add_points(25)\n'
                                       'print(score)'],
                             'initial_code': '# ⚔️ Boss Challenge: Custom Sorting Key with Lambda\n'
                                             "pairs = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]\n"
                                             '# Step 1: sorted_pairs = sorted(pairs, key=lambda x: x[1])\n'
                                             '\n'
                                             '# Step 2: Print sorted_pairs below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'score = 0\n'
                                              'def add_points(points):\n'
                                              '    global score\n'
                                              '    score += points\n'
                                              'add_points(50)\n'
                                              'add_points(25)\n'
                                              'print(score)',
                             'test_cases': [{'expected_output': '75', 'input_data': '', 'is_hidden': False}],
                             'title': 'Boss Challenge: Update a Global Score',
                             'xp_reward': 150}],
             'description': 'Understand variable visibility, the LEGB rule, and the global keyword.',
             'lesson': {'common_mistakes': [{'fix': 'Prefer arguments and return values; use global only '
                                                    'when truly needed.',
                                             'mistake': 'assigning inside a function creates a local name '
                                                        'unless declared global',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Separate functions need clear rules '
                                                'for where a name can be used. This is the practical problem '
                                                'the feature solves.\n'
                                                '\n'
                                                'What it means: Scope is the region where a name can be '
                                                'found; local names belong to a function call. Python uses '
                                                'this idea to python looks locally first, then enclosing and '
                                                'global scopes, then built-ins\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Assigning inside a function creates a local '
                                                'name unless declared global. If you change the example’s '
                                                'input or value, check this rule again because it can change '
                                                'the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Inside: 15\nOutside: 10',
                        'id': 71,
                        'introduction': 'Why learn this? Separate functions need clear rules for where a '
                                        'name can be used. In this lesson, we will see scope is the region '
                                        'where a name can be found; local names belong to a function call, '
                                        'follow how Python handles it, and practice a small example you can '
                                        'change yourself.',
                        'learning_objectives': ['Explain scope is the region where a name can be found; '
                                                'local names belong to a function call in your own words.',
                                                'Trace a small Variable Scope (Local vs Global) example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'assigning inside a function creates a local name unless '
                                                'declared global.'],
                        'level_id': 71,
                        'line_by_line': [{'code': 'score = 10',
                                          'explanation': 'Store 10 in score so later instructions can use '
                                                         'it.',
                                          'line': '1'},
                                         {'code': 'def add_bonus(score):',
                                          'explanation': 'Define a function named add_bonus. Its parameters '
                                                         '(score) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '2'},
                                         {'code': '    score = score + 5',
                                          'explanation': 'Calculate or compare score + 5, then save the '
                                                         'result in score.',
                                          'line': '3'},
                                         {'code': "    print('Inside:', score)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '4'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '5'},
                                         {'code': 'add_bonus(score)',
                                          'explanation': 'Call add_bonus now. Python runs its body, and any '
                                                         'returned result is available to the caller.',
                                          'line': '6'},
                                         {'code': "print('Outside:', score)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '7'}],
                        'practical_examples': [{'code': 'score = 10\n'
                                                        'def add_bonus(score):\n'
                                                        '    score = score + 5\n'
                                                        "    print('Inside:', score)\n"
                                                        '\n'
                                                        'add_bonus(score)\n'
                                                        "print('Outside:', score)",
                                                'explanation': 'Purpose: A function keeps its local names '
                                                               'inside the call shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: score = 10\n'
                                                               'Store 10 in score so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 2: def add_bonus(score):\n'
                                                               'Define a function named add_bonus. Its '
                                                               'parameters (score) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: score = score + 5\n'
                                                               'Calculate or compare score + 5, then save '
                                                               'the result in score.\n'
                                                               '\n'
                                                               "Line 4: print('Inside:', score)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 5: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 6: add_bonus(score)\n'
                                                               'Call add_bonus now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               "Line 7: print('Outside:', score)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Inside: 15\n'
                                                               'Outside: 10',
                                                'output': 'Inside: 15\nOutside: 10',
                                                'title': 'A function keeps its local names inside the call'},
                                               {'code': 'score = 10\n'
                                                        'def add_bonus(value):\n'
                                                        '    return value + 5\n'
                                                        '\n'
                                                        'score = add_bonus(score)\n'
                                                        'print(score)',
                                                'explanation': 'Purpose: Return a new value instead of '
                                                               'changing a global shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: score = 10\n'
                                                               'Store 10 in score so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 2: def add_bonus(value):\n'
                                                               'Define a function named add_bonus. Its '
                                                               'parameters (value) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: return value + 5\n'
                                                               'Send value + 5 back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 5: score = add_bonus(score)\n'
                                                               'Store add_bonus(score) in score so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 6: print(score)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 15',
                                                'output': '15',
                                                'title': 'Return a new value instead of changing a global'},
                                               {'code': 'score = 10\n'
                                                        'def reset_score():\n'
                                                        '    global score\n'
                                                        '    score = 0\n'
                                                        '\n'
                                                        'reset_score()\n'
                                                        'print(score)',
                                                'explanation': 'Purpose: global explicitly names a '
                                                               'module-level variable shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: score = 10\n'
                                                               'Store 10 in score so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 2: def reset_score():\n'
                                                               'Define a function named reset_score. Its '
                                                               'parameters (none) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: global score\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 4: score = 0\n'
                                                               'Store 0 in score so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 5: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 6: reset_score()\n'
                                                               'Call reset_score now. Python runs its body, '
                                                               'and any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Line 7: print(score)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 0',
                                                'output': '0',
                                                'title': 'global explicitly names a module-level variable'}],
                        'practice_questions': [{'answer': 'Scope is the region where a name can be found; '
                                                          'local names belong to a function call.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Separate functions need clear rules for where a '
                                                          'name can be used.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Assigning inside a function creates a local name '
                                                          'unless declared global.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is keeping a score update '
                                           'explicit by passing and returning its value. The same pattern '
                                           'helps a larger program stay clear when it handles the same kind '
                                           'of task repeatedly.',
                        'summary': 'Remember: Prefer arguments and return values; use global only when truly '
                                   'needed. Assigning inside a function creates a local name unless declared '
                                   'global The practical example and its line-by-line walkthrough show the '
                                   'idea in action.',
                        'syntax_breakdown': 'score = 10\n'
                                            'def add_bonus(score):\n'
                                            '    score = score + 5\n'
                                            "    print('Inside:', score)\n"
                                            '\n'
                                            'add_bonus(score)\n'
                                            "print('Outside:', score)",
                        'terminology': [{'definition': 'The part of a program where a name can be found.',
                                         'term': 'Scope'},
                                        {'definition': 'A name created inside a function call.',
                                         'term': 'Local name'},
                                        {'definition': 'A name created at the module level.',
                                         'term': 'Global name'}],
                        'title': 'Variable Scope (Local vs Global)'},
             'number': 71,
             'quizzes': [{'explanation': 'x = 20 inside modify() binds a local variable. The global x '
                                         'remains 10.',
                          'options': [{'explanation': 'Correct! The local x inside modify() does not affect '
                                                      'the global x.',
                                       'is_correct': True,
                                       'text': '10'},
                                      {'explanation': "Incorrect. Without the 'global' keyword, x is local "
                                                      'to modify().',
                                       'is_correct': False,
                                       'text': '20'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'UnboundLocalError'}],
                          'question': 'What is the output of the scope test?\n'
                                      '\n'
                                      'x = 10\n'
                                      'def modify():\n'
                                      '    x = 20\n'
                                      'modify()\n'
                                      'print(x)'},
                         {'explanation': 'Local -> Enclosing -> Global -> Built-in.',
                          'options': [{'explanation': 'Correct! Python searches Local scope, then Enclosing, '
                                                      'Global, and finally Built-in.',
                                       'is_correct': True,
                                       'text': 'Local, Enclosing, Global, Built-in'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Literal, Element, Group, Block'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Loop, Exception, Global, Base'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Local, Extended, General, Binary'}],
                          'question': "What is the search order represented by Python's LEGB rule?"}],
             'title': 'Variable Scope (Local vs Global)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create a lambda named with_tax that adds 5 percent tax.\n2. Read a price and print the total to two decimal places.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['with_tax = lambda price: price * 1.05\n'
                                       'price = float(input())\n'
                                       "print(f'{with_tax(price):.2f}')"],
                             'initial_code': '# Function Annotations and Docstrings\n'
                                             '# Step 1: Define multiply with annotations and docstring:\n'
                                             '\n'
                                             '# Step 2: Print multiply(4, 5) and multiply.__doc__ below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'with_tax = lambda price: price * 1.05\n'
                                              'price = float(input())\n'
                                              "print(f'{with_tax(price):.2f}')",
                             'test_cases': [{'expected_output': '105.00',
                                             'input_data': '100\n',
                                             'is_hidden': False},
                                            {'expected_output': '21.00',
                                             'input_data': '20\n',
                                             'is_hidden': False}],
                             'title': 'Lambda Price Calculator',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Sort the word and score pairs by score using a lambda as the sorting key.\n2. Print the sorted list.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["scores = [('Mia', 8), ('Ari', 5), ('Bo', 9)]\n"
                                       'print(sorted(scores, key=lambda item: item[1]))'],
                             'initial_code': '# ⚔️ Boss Challenge: Annotation Inspector\n'
                                             '# Step 1: Define annotated get_full_name:\n'
                                             '\n'
                                             '# Step 2: Print call result and .__annotations__:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "scores = [('Mia', 8), ('Ari', 5), ('Bo', 9)]\n"
                                              'print(sorted(scores, key=lambda item: item[1]))',
                             'test_cases': [{'expected_output': "[('Ari', 5), ('Mia', 8), ('Bo', 9)]",
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Lambda Sort Key',
                             'xp_reward': 150}],
             'description': 'Create concise, single-line functions using the lambda keyword.',
             'lesson': {'common_mistakes': [{'fix': 'Use lambda for a short expression; use def for named or '
                                                    'multi-step work.',
                                             'mistake': 'lambda cannot contain several statements or a '
                                                        'normal block',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A tiny one-use function can be '
                                                'written next to the operation using it. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: Lambda creates a small function whose body '
                                                'is one expression. Python uses this idea to its expression '
                                                'result is returned automatically; assign it or pass it to '
                                                'another function\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Lambda cannot contain several statements or '
                                                'a normal block. If you change the example’s input or value, '
                                                'check this rule again because it can change the result or '
                                                'the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': "Ranked Students: [('Bob', 95), ('Alice', 88), ('Charlie', 78)]",
                        'id': 72,
                        'introduction': 'Why learn this? A tiny one-use function can be written next to the '
                                        'operation using it. In this lesson, we will see lambda creates a '
                                        'small function whose body is one expression, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain lambda creates a small function whose body is one '
                                                'expression in your own words.',
                                                'Trace a small Anonymous Functions (Lambda Expressions) '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'lambda cannot contain several statements or a normal '
                                                'block.'],
                        'level_id': 72,
                        'line_by_line': [{'code': "students = [('Alice', 88), ('Bob', 95), ('Charlie', 78)]",
                                          'explanation': 'Create the list shown and store it in students. '
                                                         'The list keeps items in order and can be processed '
                                                         'one item at a time.',
                                          'line': '1'},
                                         {'code': 'students.sort(key=lambda s: s[1], reverse=True)',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '2'},
                                         {'code': "print('Ranked Students:', students)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'}],
                        'practical_examples': [{'code': "students = [('Alice', 88), ('Bob', 95), ('Charlie', "
                                                        '78)]\n'
                                                        'students.sort(key=lambda s: s[1], reverse=True)\n'
                                                        "print('Ranked Students:', students)",
                                                'explanation': 'Purpose: Example 1: Sorting a list of tuples '
                                                               'by second element shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: students = [('Alice', 88), ('Bob', "
                                                               "95), ('Charlie', 78)]\n"
                                                               'Create the list shown and store it in '
                                                               'students. The list keeps items in order and '
                                                               'can be processed one item at a time.\n'
                                                               '\n'
                                                               'Line 2: students.sort(key=lambda s: s[1], '
                                                               'reverse=True)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 3: print('Ranked Students:', students)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Output trace: Ranked Students: [('Bob', 95), "
                                                               "('Alice', 88), ('Charlie', 78)]",
                                                'output': "Ranked Students: [('Bob', 95), ('Alice', 88), "
                                                          "('Charlie', 78)]",
                                                'title': 'Example 1: Sorting a list of tuples by second '
                                                         'element'},
                                               {'code': 'c_to_f = lambda c: (c * 9/5) + 32\n'
                                                        "print('0C in F:', c_to_f(0))\n"
                                                        "print('100C in F:', c_to_f(100))",
                                                'explanation': 'Purpose: Example 2: Quick formula '
                                                               'calculation with lambda shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: c_to_f = lambda c: (c * 9/5) + 32\n'
                                                               'Create a small function and save it in this '
                                                               'name. The expression after the colon is its '
                                                               'returned result.\n'
                                                               '\n'
                                                               "Line 2: print('0C in F:', c_to_f(0))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 3: print('100C in F:', c_to_f(100))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 0C in F: 32.0\n'
                                                               '100C in F: 212.0',
                                                'output': '0C in F: 32.0\n100C in F: 212.0',
                                                'title': 'Example 2: Quick formula calculation with lambda'},
                                               {'code': "scores = {'Sam': 50, 'Alex': 90, 'Taylor': 75}\n"
                                                        'sorted_names = sorted(scores, key=lambda k: '
                                                        'scores[k], reverse=True)\n'
                                                        "print('Leaderboard order:', sorted_names)",
                                                'explanation': 'Purpose: Example 3: Sorting dictionary keys '
                                                               'by their values shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: scores = {'Sam': 50, 'Alex': 90, "
                                                               "'Taylor': 75}\n"
                                                               "Store {'Sam': 50, 'Alex': 90, 'Taylor': 75} "
                                                               'in scores so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 2: sorted_names = sorted(scores, '
                                                               'key=lambda k: scores[k], reverse=True)\n'
                                                               'Store sorted(scores, key=lambda k: '
                                                               'scores[k], reverse=True) in sorted_names so '
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               "Line 3: print('Leaderboard order:', "
                                                               'sorted_names)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Output trace: Leaderboard order: ['Alex', "
                                                               "'Taylor', 'Sam']",
                                                'output': "Leaderboard order: ['Alex', 'Taylor', 'Sam']",
                                                'title': 'Example 3: Sorting dictionary keys by their '
                                                         'values'}],
                        'practice_questions': [{'answer': 'Lambda creates a small function whose body is one '
                                                          'expression.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A tiny one-use function can be written next to '
                                                          'the operation using it.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Lambda cannot contain several statements or a '
                                                          'normal block.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a short sorting key or '
                                           'simple conversion rule. The same pattern helps a larger program '
                                           'stay clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Use lambda for a short expression; use def for named or '
                                   'multi-step work. Lambda cannot contain several statements or a normal '
                                   'block The practical example and its line-by-line walkthrough show the '
                                   'idea in action.',
                        'syntax_breakdown': "students = [('Alice', 88), ('Bob', 95), ('Charlie', 78)]\n"
                                            'students.sort(key=lambda s: s[1], reverse=True)\n'
                                            "print('Ranked Students:', students)",
                        'terminology': [{'definition': 'A small anonymous function with one expression.',
                                         'term': 'Lambda'},
                                        {'definition': 'A piece of code that evaluates to a value.',
                                         'term': 'Expression'},
                                        {'definition': 'Not given a regular def name when created.',
                                         'term': 'Anonymous'}],
                        'title': 'Anonymous Functions (Lambda Expressions)'},
             'number': 72,
             'quizzes': [{'explanation': "The 'global x' declaration instructs Python to modify the "
                                         'module-level variable x: 5 + 10 = 15.',
                          'options': [{'explanation': "Correct! 'global x' explicitly modifies the global "
                                                      'variable.',
                                       'is_correct': True,
                                       'text': '15'},
                                      {'explanation': "Incorrect. 'global x' allowed modification.",
                                       'is_correct': False,
                                       'text': '5'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '10'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'UnboundLocalError'}],
                          'question': 'What is the output of using the `global` keyword?\n'
                                      '\n'
                                      'x = 5\n'
                                      'def add():\n'
                                      '    global x\n'
                                      '    x += 10\n'
                                      'add()\n'
                                      'print(x)'},
                         {'explanation': 'nonlocal rebinds variables in the nearest enclosing non-global '
                                         'scope.',
                          'options': [{'explanation': "Correct! 'nonlocal' targets the enclosing outer "
                                                      'function scope.',
                                       'is_correct': True,
                                       'text': 'nonlocal'},
                                      {'explanation': "Incorrect. 'global' skips directly to the module "
                                                      'level.',
                                       'is_correct': False,
                                       'text': 'global'},
                                      {'explanation': 'Incorrect. Not a Python keyword.',
                                       'is_correct': False,
                                       'text': 'outer'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'parent'}],
                          'question': 'Which keyword allows an inner function to rebind a variable in an '
                                      'enclosing (non-global) function scope?'}],
             'title': 'Anonymous Functions (Lambda Expressions)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use map() with a lambda to make every word uppercase.\n2. Read words on one line and print the resulting list.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['words = input().split()\n'
                                       'upper_words = list(map(lambda word: word.upper(), words))\n'
                                       'print(upper_words)'],
                             'initial_code': '# Recursion: Functions Calling Themselves\n'
                                             '# Step 1: Define recursive countdown(n):\n'
                                             '\n'
                                             '# Step 2: Call countdown(3) below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'words = input().split()\n'
                                              'upper_words = list(map(lambda word: word.upper(), words))\n'
                                              'print(upper_words)',
                             'test_cases': [{'expected_output': "['PYTHON', 'QUEST']",
                                             'input_data': 'python quest\n',
                                             'is_hidden': False}],
                             'title': 'Map Names to Uppercase',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use filter() to keep scores of 70 or more.\n2. Read the scores and print the passing scores as a list.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['scores = [int(value) for value in input().split()]\n'
                                       'passing = list(filter(lambda score: score >= 70, scores))\n'
                                       'print(passing)'],
                             'initial_code': '# ⚔️ Boss Challenge: Recursive Factorial\n'
                                             '# Step 1: Define factorial(n) with base case n <= 1:\n'
                                             '\n'
                                             '# Step 2: Read int and print factorial below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'scores = [int(value) for value in input().split()]\n'
                                              'passing = list(filter(lambda score: score >= 70, scores))\n'
                                              'print(passing)',
                             'test_cases': [{'expected_output': '[70, 82]',
                                             'input_data': '55 70 82 68\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Filter Passing Scores',
                             'xp_reward': 150}],
             'description': 'Treat functions as first-class citizens: pass functions into map() and '
                            'filter().',
             'lesson': {'common_mistakes': [{'fix': 'map changes items; filter selects items; list displays '
                                                    'the iterator values.',
                                             'mistake': 'an iterator is consumed as it is read; list(...) '
                                                        'makes its values visible as a list',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Lists often need the same '
                                                'transformation or test applied to each item. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: A higher-order function accepts or returns '
                                                'another function. Python uses this idea to map transforms '
                                                'each item and filter keeps matching items; both return lazy '
                                                'iterators in Python 3\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: An iterator is consumed as it is read; '
                                                'list(...) makes its values visible as a list. If you change '
                                                'the example’s input or value, check this rule again because '
                                                'it can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': '[4, 6, 8]',
                        'id': 73,
                        'introduction': 'Why learn this? Lists often need the same transformation or test '
                                        'applied to each item. In this lesson, we will see a higher-order '
                                        'function accepts or returns another function, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a higher-order function accepts or returns another '
                                                'function in your own words.',
                                                'Trace a small Higher-Order Functions (map and filter) '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: an '
                                                'iterator is consumed as it is read; list(...) makes its '
                                                'values visible as a list.'],
                        'level_id': 73,
                        'line_by_line': [{'code': 'prices = [2, 3, 4]',
                                          'explanation': 'Create the list shown and store it in prices. The '
                                                         'list keeps items in order and can be processed one '
                                                         'item at a time.',
                                          'line': '1'},
                                         {'code': 'doubled = map(lambda price: price * 2, prices)',
                                          'explanation': 'Calculate or compare map(lambda price: price * 2, '
                                                         'prices), then save the result in doubled.',
                                          'line': '2'},
                                         {'code': 'print(list(doubled))',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '3'}],
                        'practical_examples': [{'code': 'prices = [2, 3, 4]\n'
                                                        'doubled = map(lambda price: price * 2, prices)\n'
                                                        'print(list(doubled))',
                                                'explanation': 'Purpose: map transforms every item lazily '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: prices = [2, 3, 4]\n'
                                                               'Create the list shown and store it in '
                                                               'prices. The list keeps items in order and '
                                                               'can be processed one item at a time.\n'
                                                               '\n'
                                                               'Line 2: doubled = map(lambda price: price * '
                                                               '2, prices)\n'
                                                               'Calculate or compare map(lambda price: price '
                                                               '* 2, prices), then save the result in '
                                                               'doubled.\n'
                                                               '\n'
                                                               'Line 3: print(list(doubled))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: [4, 6, 8]',
                                                'output': '[4, 6, 8]',
                                                'title': 'map transforms every item lazily'},
                                               {'code': 'scores = [45, 72, 90]\n'
                                                        'passed = filter(lambda score: score >= 50, scores)\n'
                                                        'print(list(passed))',
                                                'explanation': 'Purpose: filter keeps items that pass a test '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: scores = [45, 72, 90]\n'
                                                               'Create the list shown and store it in '
                                                               'scores. The list keeps items in order and '
                                                               'can be processed one item at a time.\n'
                                                               '\n'
                                                               'Line 2: passed = filter(lambda score: score '
                                                               '>= 50, scores)\n'
                                                               'Calculate or compare filter(lambda score: '
                                                               'score >= 50, scores), then save the result '
                                                               'in passed.\n'
                                                               '\n'
                                                               'Line 3: print(list(passed))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: [72, 90]',
                                                'output': '[72, 90]',
                                                'title': 'filter keeps items that pass a test'},
                                               {'code': "names = ['Mia', 'Bo']\n"
                                                        'upper_names = map(str.upper, names)\n'
                                                        'print(list(upper_names))',
                                                'explanation': 'Purpose: A map iterator is consumed when '
                                                               'read shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               "Line 1: names = ['Mia', 'Bo']\n"
                                                               'Create the list shown and store it in names. '
                                                               'The list keeps items in order and can be '
                                                               'processed one item at a time.\n'
                                                               '\n'
                                                               'Line 2: upper_names = map(str.upper, names)\n'
                                                               'Store map(str.upper, names) in upper_names '
                                                               'so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 3: print(list(upper_names))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Output trace: ['MIA', 'BO']",
                                                'output': "['MIA', 'BO']",
                                                'title': 'A map iterator is consumed when read'}],
                        'practice_questions': [{'answer': 'A higher-order function accepts or returns '
                                                          'another function.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Lists often need the same transformation or test '
                                                          'applied to each item.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'An iterator is consumed as it is read; list(...) '
                                                          'makes its values visible as a list.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is converting temperatures or '
                                           'selecting passing scores. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: map changes items; filter selects items; list displays the '
                                   'iterator values. An iterator is consumed as it is read; list(...) makes '
                                   'its values visible as a list The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'prices = [2, 3, 4]\n'
                                            'doubled = map(lambda price: price * 2, prices)\n'
                                            'print(list(doubled))',
                        'terminology': [{'definition': 'A function that accepts another function or returns '
                                                       'one.',
                                         'term': 'Higher-order function'},
                                        {'definition': 'An object that provides values one at a time.',
                                         'term': 'Iterator'},
                                        {'definition': 'Values are produced when requested, not all at once.',
                                         'term': 'Lazy'}],
                        'title': 'Higher-Order Functions (map and filter)'},
             'number': 73,
             'quizzes': [{'explanation': 'The lambda takes x (5) and returns 5 ** 2 = 25.',
                          'options': [{'explanation': 'Correct! 5 ** 2 = 25.',
                                       'is_correct': True,
                                       'text': '25'},
                                      {'explanation': 'Incorrect. ** is exponentiation.',
                                       'is_correct': False,
                                       'text': '10'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '5'},
                                      {'explanation': 'Incorrect. square(5) invokes the function.',
                                       'is_correct': False,
                                       'text': '<function <lambda>>'}],
                          'question': 'What is the output of this lambda function?\n'
                                      '\n'
                                      'square = lambda x: x ** 2\n'
                                      'print(square(5))'},
                         {'explanation': 'map applies the doubling lambda to each element in [1, 2, 3]: [2, '
                                         '4, 6].',
                          'options': [{'explanation': 'Correct! Each element is multiplied by 2.',
                                       'is_correct': True,
                                       'text': '[2, 4, 6]'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '[1, 2, 3, 1, 2, 3]'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '[1, 4, 9]'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '12'}],
                          'question': 'What will be printed by: print(list(map(lambda x: x * 2, [1, 2, '
                                      '3])))?'}],
             'title': 'Higher-Order Functions (map and filter)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Write calc_order to add tax to a price and then subtract a discount.\n2. Tax should be 5 percent by default and discount should be zero by default.\n3. Print both totals shown, with two digits after the decimal point.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['def calc_order(price, tax_rate=0.05, discount=0.0):\n'
                                       '    return price * (1 + tax_rate) - discount\n'
                                       "print(f'${calc_order(100.0):.2f}')\n"
                                       "print(f'${calc_order(100.0, 0.10, 15.0):.2f}')"],
                             'initial_code': '# World 7 Capstone: Checkout Calculator\n'
                                             '# Step 1: Define calc_order with defaults:\n'
                                             '\n'
                                             '# Step 2: Print formatted results below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def calc_order(price, tax_rate=0.05, discount=0.0):\n'
                                              '    return price * (1 + tax_rate) - discount\n'
                                              '\n'
                                              "print(f'${calc_order(100):.2f}')\n"
                                              "print(f'${calc_order(100, discount=10):.2f}')",
                             'test_cases': [{'expected_output': '$105.00\n$95.00',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'World 7 Capstone: Order Calculation Utility',
                             'xp_reward': 50},
                            {'description': 'Your task, step by step:\n1. Write apply_pipeline(number, functions) so each function receives the previous result.\n2. Pass 10 through double and add_five, then print the result.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def double(number):\n'
                                       '    return number * 2\n'
                                       'def add_five(number):\n'
                                       '    return number + 5\n'
                                       'def apply_pipeline(number, functions):\n'
                                       '    for function in functions:\n'
                                       '        number = function(number)\n'
                                       '    return number\n'
                                       'print(apply_pipeline(10, [double, add_five]))'],
                             'initial_code': '# ⚔️ Boss Challenge: Higher-Order Function Pipeline\n'
                                             '\n'
                                             '# Step 1: Define double(n):\n'
                                             '\n'
                                             '\n'
                                             '# Step 2: Define add_five(n):\n'
                                             '\n'
                                             '\n'
                                             '# Step 3: Define apply_pipeline(num, funcs) that loops through '
                                             'funcs:\n'
                                             '\n'
                                             '\n'
                                             '# Step 4: Run number 10 through [double, add_five] and print:\n'
                                             'result = apply_pipeline(10, [double, add_five])\n'
                                             "print(f'Pipeline Result: {result}')\n",
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def double(number):\n'
                                              '    return number * 2\n'
                                              'def add_five(number):\n'
                                              '    return number + 5\n'
                                              'def apply_pipeline(number, functions):\n'
                                              '    for function in functions:\n'
                                              '        number = function(number)\n'
                                              '    return number\n'
                                              'print(apply_pipeline(10, [double, add_five]))',
                             'test_cases': [{'expected_output': '25', 'input_data': '', 'is_hidden': False}],
                             'title': 'Boss Challenge: Higher-Order Function Pipeline',
                             'xp_reward': 250}],
             'description': 'Architect a modular mathematical calculation engine with dispatch tables, input '
                            'validation, and clean abstractions.',
             'lesson': {'common_mistakes': [{'fix': 'Small functions plus validation make calculator '
                                                    'behavior easier to test.',
                                             'mistake': 'reject unsupported symbols and division by zero '
                                                        'before calculating',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A calculator should separate '
                                                'operations so they can be reused and checked. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: A modular calculator divides work into small '
                                                'functions with clear inputs and results. Python uses this '
                                                'idea to validate the operation and divisor, dispatch to a '
                                                'matching function, and return its result\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Reject unsupported symbols and division by '
                                                'zero before calculating. If you change the example’s input '
                                                'or value, check this rule again because it can change the '
                                                'result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': '11\n5',
                        'id': 74,
                        'introduction': 'Why learn this? A calculator should separate operations so they can '
                                        'be reused and checked. In this lesson, we will see a modular '
                                        'calculator divides work into small functions with clear inputs and '
                                        'results, follow how Python handles it, and practice a small example '
                                        'you can change yourself.',
                        'learning_objectives': ['Explain a modular calculator divides work into small '
                                                'functions with clear inputs and results in your own words.',
                                                'Trace a small World 7 Examination & Capstone: Modular '
                                                'Calculator example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'reject unsupported symbols and division by zero before '
                                                'calculating.'],
                        'level_id': 74,
                        'line_by_line': [{'code': 'def add(a, b):',
                                          'explanation': 'Define a function named add. Its parameters (a, b) '
                                                         'are local names that receive values when the '
                                                         'function is called. The colon starts the indented '
                                                         'body; defining it does not run it yet.',
                                          'line': '1'},
                                         {'code': '    return a + b',
                                          'explanation': 'Send a + b back to the caller and end this '
                                                         'function call.',
                                          'line': '2'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '3'},
                                         {'code': 'def subtract(a, b):',
                                          'explanation': 'Define a function named subtract. Its parameters '
                                                         '(a, b) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '4'},
                                         {'code': '    return a - b',
                                          'explanation': 'Send a - b back to the caller and end this '
                                                         'function call.',
                                          'line': '5'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '6'},
                                         {'code': 'print(add(8, 3))',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '7'},
                                         {'code': 'print(subtract(8, 3))',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '8'}],
                        'practical_examples': [{'code': 'def add(a, b):\n'
                                                        '    return a + b\n'
                                                        '\n'
                                                        'def subtract(a, b):\n'
                                                        '    return a - b\n'
                                                        '\n'
                                                        'print(add(8, 3))\n'
                                                        'print(subtract(8, 3))',
                                                'explanation': 'Purpose: Build small calculator functions '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def add(a, b):\n'
                                                               'Define a function named add. Its parameters '
                                                               '(a, b) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               'Line 2: return a + b\n'
                                                               'Send a + b back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 3: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 4: def subtract(a, b):\n'
                                                               'Define a function named subtract. Its '
                                                               'parameters (a, b) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 5: return a - b\n'
                                                               'Send a - b back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 6: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 7: print(add(8, 3))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 8: print(subtract(8, 3))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 11\n'
                                                               '5',
                                                'output': '11\n5',
                                                'title': 'Build small calculator functions'},
                                               {'code': 'def divide(a, b):\n'
                                                        '    if b == 0:\n'
                                                        "        raise ValueError('Cannot divide by zero')\n"
                                                        '    return a / b\n'
                                                        '\n'
                                                        'try:\n'
                                                        '    print(divide(12, 3))\n'
                                                        '    print(divide(12, 0))\n'
                                                        'except ValueError as error:\n'
                                                        '    print(error)',
                                                'explanation': 'Purpose: Validate the operation and division '
                                                               'by zero shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def divide(a, b):\n'
                                                               'Define a function named divide. Its '
                                                               'parameters (a, b) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 2: if b == 0:\n'
                                                               'Check whether b == 0 is true. If it is, run '
                                                               'the indented block; otherwise Python skips '
                                                               'that block.\n'
                                                               '\n'
                                                               "Line 3: raise ValueError('Cannot divide by "
                                                               "zero')\n"
                                                               "Stop this path by raising ValueError('Cannot "
                                                               "divide by zero'). Python passes that error "
                                                               'to the caller unless a matching except block '
                                                               'handles it.\n'
                                                               '\n'
                                                               'Line 4: return a / b\n'
                                                               'Send a / b back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 5: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 6: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               'Line 7: print(divide(12, 3))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 8: print(divide(12, 0))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 9: except ValueError as error:\n'
                                                               'Handle only a ValueError exception here. The '
                                                               'exception details are stored in error.\n'
                                                               '\n'
                                                               'Line 10: print(error)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 4.0\n'
                                                               'Cannot divide by zero',
                                                'output': '4.0\nCannot divide by zero',
                                                'title': 'Validate the operation and division by zero'},
                                               {'code': 'def add(a, b):\n'
                                                        '    return a + b\n'
                                                        'def multiply(a, b):\n'
                                                        '    return a * b\n'
                                                        '\n'
                                                        "operations = {'+': add, '*': multiply}\n"
                                                        'def calculate(a, b, symbol):\n'
                                                        '    if symbol not in operations:\n'
                                                        "        raise ValueError('Unsupported operation: ' "
                                                        '+ symbol)\n'
                                                        '    return operations[symbol](a, b)\n'
                                                        '\n'
                                                        'try:\n'
                                                        "    print(calculate(6, 7, '?'))\n"
                                                        'except ValueError as error:\n'
                                                        '    print(error)',
                                                'explanation': 'Purpose: Choose an operation by its symbol '
                                                               'and reject unknown choices shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: def add(a, b):\n'
                                                               'Define a function named add. Its parameters '
                                                               '(a, b) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               'Line 2: return a + b\n'
                                                               'Send a + b back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 3: def multiply(a, b):\n'
                                                               'Define a function named multiply. Its '
                                                               'parameters (a, b) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 4: return a * b\n'
                                                               'Send a * b back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 5: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 6: operations = {'+': add, '*': "
                                                               'multiply}\n'
                                                               "Store {'+': add, '*': multiply} in "
                                                               'operations so later instructions can use '
                                                               'it.\n'
                                                               '\n'
                                                               'Line 7: def calculate(a, b, symbol):\n'
                                                               'Define a function named calculate. Its '
                                                               'parameters (a, b, symbol) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 8: if symbol not in operations:\n'
                                                               'Check whether symbol not in operations is '
                                                               'true. If it is, run the indented block; '
                                                               'otherwise Python skips that block.\n'
                                                               '\n'
                                                               "Line 9: raise ValueError('Unsupported "
                                                               "operation: ' + symbol)\n"
                                                               'Stop this path by raising '
                                                               "ValueError('Unsupported operation: ' + "
                                                               'symbol). Python passes that error to the '
                                                               'caller unless a matching except block '
                                                               'handles it.\n'
                                                               '\n'
                                                               'Line 10: return operations[symbol](a, b)\n'
                                                               'Send operations[symbol](a, b) back to the '
                                                               'caller and end this function call.\n'
                                                               '\n'
                                                               'Line 11: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 12: try:\n'
                                                               'Start the block that may fail. If a matching '
                                                               'exception happens, Python jumps to an except '
                                                               'block.\n'
                                                               '\n'
                                                               "Line 13: print(calculate(6, 7, '?'))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 14: except ValueError as error:\n'
                                                               'Handle only a ValueError exception here. The '
                                                               'exception details are stored in error.\n'
                                                               '\n'
                                                               'Line 15: print(error)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Unsupported operation: ?',
                                                'output': 'Unsupported operation: ?',
                                                'title': 'Choose an operation by its symbol and reject '
                                                         'unknown choices'}],
                        'practice_questions': [{'answer': 'A modular calculator divides work into small '
                                                          'functions with clear inputs and results.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A calculator should separate operations so they '
                                                          'can be reused and checked.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Reject unsupported symbols and division by zero '
                                                          'before calculating.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'World 6 collection basics, variables, print(), and reading '
                                         'indentation. The lesson briefly explains any new word before '
                                         'relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a classroom calculator '
                                           'with add, subtract, multiply, and divide. The same pattern helps '
                                           'a larger program stay clear when it handles the same kind of '
                                           'task repeatedly.',
                        'summary': 'Remember: Small functions plus validation make calculator behavior '
                                   'easier to test. Reject unsupported symbols and division by zero before '
                                   'calculating The practical example and its line-by-line walkthrough show '
                                   'the idea in action.',
                        'syntax_breakdown': 'def add(a, b):\n'
                                            '    return a + b\n'
                                            '\n'
                                            'def subtract(a, b):\n'
                                            '    return a - b\n'
                                            '\n'
                                            'print(add(8, 3))\n'
                                            'print(subtract(8, 3))',
                        'terminology': [{'definition': 'Choose which function to call based on an operation.',
                                         'term': 'Dispatch'},
                                        {'definition': 'Check input before using it.', 'term': 'Validation'},
                                        {'definition': 'Split a program into small parts with clear jobs.',
                                         'term': 'Modular'}],
                        'title': 'World 7 Examination & Capstone: Modular Calculator'},
             'number': 74,
             'quizzes': [{'explanation': 'filter keeps elements where the lambda returns True: [2, 4].',
                          'options': [{'explanation': 'Correct! 2 and 4 are the even numbers.',
                                       'is_correct': True,
                                       'text': '[2, 4]'},
                                      {'explanation': 'Incorrect. Those are odd numbers.',
                                       'is_correct': False,
                                       'text': '[1, 3, 5]'},
                                      {'explanation': 'Incorrect. filter yields the matching elements, not '
                                                      'booleans.',
                                       'is_correct': False,
                                       'text': '[True, False, True, False, True]'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '6'}],
                          'question': 'What is the output of the higher-order function pipeline?\n'
                                      '\n'
                                      'nums = [1, 2, 3, 4, 5]\n'
                                      'print(list(filter(lambda x: x % 2 == 0, nums)))'},
                         {'explanation': "Elements are sorted by character length: 'pie' (3), 'apple' (5), "
                                         "'banana' (6).",
                          'options': [{'explanation': 'Correct! 3 letters < 5 letters < 6 letters.',
                                       'is_correct': True,
                                       'text': "['pie', 'apple', 'banana']"},
                                      {'explanation': 'Incorrect. That is alphabetical order.',
                                       'is_correct': False,
                                       'text': "['apple', 'banana', 'pie']"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "['banana', 'apple', 'pie']"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '[3, 5, 6]'}],
                          'question': "What is the output of: print(sorted(['apple', 'pie', 'banana'], "
                                      'key=len))?'}],
             'title': 'World 7 Examination & Capstone: Modular Calculator'}],
 'number': 7,
 'title': 'Functions'}
