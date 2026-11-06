"""
Curriculum module: WORLD_2
World 2 lessons and practice challenges.
"""

WORLD_2 = {'description': 'Master variables, memory references, integers, floats, booleans, and type conversion.',
 'final_project_desc': 'Create a data store for a contact profile with type validation and conversions.',
 'final_project_title': 'Personal Information Management Program',
 'goal': 'Store, manipulate, and convert different kinds of data in computer memory.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Make a variable named hero_title and store the text Python Explorer in it.\n2. Then display the variable.\n3. The screen should show Python Explorer.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Make a variable named hero_title and store the text Python '
                                             'Explorer in it. Then display the variable. The screen should '
                                             'show Python Explorer.',
                             'solution_code': "hero_title = 'Python Explorer'\nprint(hero_title)",
                             'test_cases': [{'expected_output': 'Python Explorer',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Declaring Your First Variable',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Create quest_rank with the text Novice and quest_gold with the number 100.\n2. Display Rank: Novice on line one and Gold: 100 on line two.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Create quest_rank with the text Novice and quest_gold with the '
                                             'number 100. Display Rank: Novice on line one and Gold: 100 on '
                                             'line two.',
                             'solution_code': "quest_rank = 'Novice'\n"
                                              'quest_gold = 100\n'
                                              "print('Rank:', quest_rank)\n"
                                              "print('Gold:', quest_gold)",
                             'test_cases': [{'expected_output': 'Rank: Novice\nGold: 100',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Dual Variable Profile',
                             'xp_reward': 150}],
             'description': 'A variable is a name that points to a value.',
             'lesson': {'common_mistakes': [{'fix': "player_name = 'Nova'",
                                             'mistake': "'Nova' = player_name",
                                             'why': 'In Python, the variable name MUST always be on the left '
                                                    'side of the = operator.'}],
                        'detailed_explanation': "hero_title = 'Python Explorer'\n"
                                                'print(hero_title)\n'
                                                '\n'
                                                'The first line stores text under the name hero_title. The '
                                                'second line asks Python to show that value. The screen says '
                                                'Python Explorer. Quotes mark text values; when you want the '
                                                'value from a variable, write its name without quotes.\n'
                                                '\n'
                                                'Another example:\n'
                                                'coins = 25\n'
                                                'print(coins)\n'
                                                '\n'
                                                'This stores the number 25 and displays it. A variable can '
                                                'hold text, numbers, and other kinds of values.',
                        'expected_output': 'Player: Nova\nScore: 250',
                        'introduction': 'A variable is a name that points to a value. Think of it like a '
                                        'labeled box: the label helps you find what you stored. In '
                                        "`hero_title = 'Python Explorer'`, the name is hero_title, the "
                                        'equals sign stores the value, and the value is text. You can use '
                                        'the name later instead of typing the value again.',
                        'learning_objectives': ['Understand how computers store information in memory (RAM)',
                                                'Learn what a variable is and why programmers use them',
                                                'Understand variables as labeled containers or name tags '
                                                'referencing data',
                                                'Distinguish between a variable name and its stored value'],
                        'line_by_line': [{'line': '1', 'code': "player_name = 'Nova'", 'explanation': "Store the text 'Nova' in player_name."}, {'line': '2', 'code': 'score = 250', 'explanation': 'Store the number 250 in score.'}, {'line': '3', 'code': "print('Player:', player_name)", 'explanation': "Show the text 'Player:', followed by the current value of player_name. Python puts a space between comma-separated print items."}, {'line': '4', 'code': "print('Score:', score)", 'explanation': "Show the text 'Score:', followed by the current value of score. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Storing hero profile in memory',
                                                'code': "player_name = 'Nova'\n"
                                                        'score = 250\n'
                                                        "print('Player:', player_name)\n"
                                                        "print('Score:', score)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Player: Nova\nScore: 250'},
                                               {'title': 'Example 2: Bank account ledger',
                                                'code': "customer = 'Jordan'\n"
                                                        'balance = 1250\n'
                                                        "print('Customer:', customer)\n"
                                                        "print('Balance: $', balance)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Customer: Jordan\nBalance: $ 1250'},
                                               {'title': 'Example 3: Weather station readout',
                                                'code': "city = 'Kyoto'\n"
                                                        'temperature = 22\n'
                                                        "print('City:', city)\n"
                                                        "print('Temperature:', temperature, 'deg C')",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'City: Kyoto\nTemperature: 22 deg C'}],
                        'practice_questions': ["Why can't the stored value go on the left of the = sign?",
                                               'What happens to variable values when a program finishes '
                                               'running?'],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'Every login system holds your current session ID in a variable; '
                                           'shopping carts store your item count in a variable.',
                        'summary': "hero_title = 'Python Explorer'\nprint(hero_title)",
                        'syntax_breakdown': '# 1. Variable name (the descriptive identifier): hero_name\n'
                                            '# 2. Assignment operator (=): stores data on the right into the '
                                            'container on the left\n'
                                            "# 3. Value (the data): 'Aria'\n"
                                            "hero_name = 'Aria'\n"
                                            'hero_health = 100\n'
                                            '\n'
                                            "print('Hero Name:', hero_name)\n"
                                            "print('Current Health:', hero_health)",
                        'terminology': [{'definition': 'A named reference in computer memory used to store '
                                                       'and retrieve data.',
                                         'term': 'Variable'},
                                        {'definition': 'Temporary high-speed storage where your computer '
                                                       'holds active data while programs run.',
                                         'term': 'Memory (RAM)'},
                                        {'definition': 'The name given to a variable, function, or other '
                                                       'programmer-defined entity.',
                                         'term': 'Identifier'}],
                        'title': 'What Are Variables?'},
             'number': 11,
             'quizzes': [{'explanation': 'Variables store values. When y = x executes, y receives 15. '
                                         'Reassigning x later to 30 does not change y.',
                          'options': [{'explanation': 'Correct! y maintains the value 15 assigned from x.',
                                       'is_correct': True,
                                       'text': '15'},
                                      {'explanation': 'Incorrect. Reassigning x does not modify y.',
                                       'is_correct': False,
                                       'text': '30'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '45'},
                                      {'explanation': 'Incorrect. Both variables are properly defined.',
                                       'is_correct': False,
                                       'text': 'NameError'}],
                          'question': 'What is the output of the following Python code?\n'
                                      '\n'
                                      'x = 15\n'
                                      'y = x\n'
                                      'x = 30\n'
                                      'print(y)'},
                         {'explanation': 'In Python, assignment uses a single equals sign with the variable '
                                         'name on the left and the value on the right.',
                          'options': [{'explanation': 'Correct! variable = value is standard Python syntax.',
                                       'is_correct': True,
                                       'text': 'answer = 42'},
                                      {'explanation': 'Incorrect. A literal number cannot be on the left of '
                                                      'an assignment.',
                                       'is_correct': False,
                                       'text': '42 = answer'},
                                      {'explanation': 'Incorrect. That is not Python syntax.',
                                       'is_correct': False,
                                       'text': 'var answer := 42'},
                                      {'explanation': 'Incorrect. Python does not use static type keywords '
                                                      'for assignment.',
                                       'is_correct': False,
                                       'text': 'int answer = 42'}],
                          'question': 'Which statement correctly assigns the integer 42 to the variable '
                                      "'answer' in Python?"}],
             'title': 'What Are Variables?'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Store 0 in start_x and 10 in start_y on one line.\n2. Display the position as Position: 0, 10.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Store 0 in start_x and 10 in start_y on one line. Display the '
                                             'position as Position: 0, 10.',
                             'solution_code': 'start_x, start_y = 0, 10\n'
                                              "print(f'Position: {start_x}, {start_y}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Position: 0, 10',
                                             'is_hidden': False}],
                             'title': 'Multiple Coordinate Assignment',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Set length to 4, width to 5, and height to 6.\n2. Multiply them and print Volume: 120.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Set length to 4, width to 5, and height to 6. Multiply them '
                                             'and print Volume: 120.',
                             'solution_code': 'length = 4\n'
                                              'width = 5\n'
                                              'height = 6\n'
                                              'volume = length * width * height\n'
                                              "print('Volume:', volume)",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Volume: 120',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Dimension Specifier',
                             'xp_reward': 150}],
             'description': 'In Python, create a variable with a name, an equals sign, and a value.',
             'lesson': {'common_mistakes': [{'fix': 'x = 10; y = 10  or  x, y = 10, 10',
                                             'mistake': 'x, y = 10',
                                             'why': 'Unpacking requires the number of variables on the left '
                                                    'to match the number of values on the right.'}],
                        'detailed_explanation': 'start_x, start_y = 0, 10\n'
                                                "print(f'Position: {start_x}, {start_y}')\n"
                                                '\n'
                                                'Python matches values from left to right: 0 goes into '
                                                'start_x and 10 goes into start_y. The f-string displays '
                                                'both values with a comma between them. You may also put '
                                                'each assignment on its own line. One-line assignment is '
                                                'handy when related values are created together.',
                        'expected_output': 'Resolution: 1920 x 1080',
                        'introduction': 'In Python, create a variable with a name, an equals sign, and a '
                                        'value. Python works out the kind of value for you. You can assign '
                                        'two related variables on one line: `start_x, start_y = 0, 10` '
                                        'stores 0 in start_x and 10 in start_y, in that order.',
                        'learning_objectives': ['Master creating variables with descriptive, readable names',
                                                'Understand how Python allocates memory automatically',
                                                'Understand multiple assignments in a single statement'],
                        'line_by_line': [{'line': '1', 'code': 'start_x, start_y = 100, 200', 'explanation': 'Store 100, 200 in start_x, start_y in the same left-to-right order.'}, {'line': '2', 'code': "print('Starting Position:', start_x, start_y)", 'explanation': "Show the text 'Starting Position:', followed by the current value of start_x, followed by the current value of start_y. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Coordinate mapping',
                                                'code': 'start_x, start_y = 100, 200\n'
                                                        "print('Starting Position:', start_x, start_y)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Starting Position: 100 200'},
                                               {'title': 'Example 2: RGB color channels',
                                                'code': 'red, green, blue = 255, 128, 0\n'
                                                        "print('RGB Color Code:', red, green, blue)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'RGB Color Code: 255 128 0'},
                                               {'title': 'Example 3: Mirroring variable values',
                                                'code': 'primary_score = 500\n'
                                                        'backup_score = primary_score\n'
                                                        "print('Primary:', primary_score, 'Backup:', "
                                                        'backup_score)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Primary: 500 Backup: 500'}],
                        'practice_questions': ['What happens if you try to print a variable before creating '
                                               'it?',
                                               'How can you assign three variables in a single line?'],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'Game engines unpack coordinates (x, y, z = '
                                           'get_player_position()) using multiple assignments.',
                        'summary': "start_x, start_y = 0, 10\nprint(f'Position: {start_x}, {start_y}')",
                        'syntax_breakdown': '# Individual variable declaration:\n'
                                            "item_name = 'Energy Shield'\n"
                                            'item_cost = 45\n'
                                            '\n'
                                            '# Multiple variable assignment on a single line:\n'
                                            'pos_x, pos_y = 120, 350\n'
                                            '\n'
                                            "print('Equipped Item:', item_name, 'Cost:', item_cost)\n"
                                            "print('Coordinates:', pos_x, pos_y)",
                        'terminology': [{'definition': 'The single equals sign used to assign the value on '
                                                       'its right to the variable on its left.',
                                         'term': 'Assignment Operator (=)'},
                                        {'definition': 'A feature where Python automatically determines the '
                                                       'data type of a variable at runtime.',
                                         'term': 'Dynamic Typing'}],
                        'title': 'Creating Variables'},
             'number': 12,
             'quizzes': [{'explanation': 'Referencing a variable that has never been assigned raises a '
                                         'NameError.',
                          'options': [{'explanation': 'Correct! Python raises NameError when referencing an '
                                                      'unassigned identifier.',
                                       'is_correct': True,
                                       'text': "NameError: name 'player_score' is not defined"},
                                      {'explanation': 'Incorrect. Python raises NameError.',
                                       'is_correct': False,
                                       'text': 'TypeError: null reference'},
                                      {'explanation': 'Incorrect. Variables must be defined before use.',
                                       'is_correct': False,
                                       'text': 'It prints None'},
                                      {'explanation': 'Incorrect. Syntax is valid, but the name is undefined '
                                                      'at runtime.',
                                       'is_correct': False,
                                       'text': 'SyntaxError: variable missing'}],
                          'question': 'What exception is raised when executing this code?\n'
                                      '\n'
                                      'print(player_score)'},
                         {'explanation': 'Multiple assignment allows swapping values in a single line. a '
                                         'becomes 20 and b becomes 10.',
                          'options': [{'explanation': 'Correct! Python evaluates the right side first (20, '
                                                      '10) and assigns to (a, b).',
                                       'is_correct': True,
                                       'text': '20 10'},
                                      {'explanation': 'Incorrect. The variables were swapped.',
                                       'is_correct': False,
                                       'text': '10 20'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '20 20'},
                                      {'explanation': 'Incorrect. Multiple assignment swapping is idiomatic '
                                                      'Python.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What is the output of the following code?\n'
                                      '\n'
                                      'a, b = 10, 20\n'
                                      'a, b = b, a\n'
                                      'print(a, b)'}],
             'title': 'Creating Variables'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create favorite_programming_language and store Python in it.\n2. Display its value.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Create favorite_programming_language and store Python in it. '
                                             'Display its value.',
                             'solution_code': "favorite_programming_language = 'Python'\n"
                                              'print(favorite_programming_language)',
                             'test_cases': [{'expected_output': 'Python',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Adopting snake_case',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Create first_score with 90 and player_name with Alex.\n2. Display Player Alex scored 90 on one line.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Create first_score with 90 and player_name with Alex. Display '
                                             'Player Alex scored 90 on one line.',
                             'solution_code': 'first_score = 90\n'
                                              "player_name = 'Alex'\n"
                                              "print('Player', player_name, 'scored', first_score)",
                             'test_cases': [{'expected_output': 'Player Alex scored 90',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Correcting Illegal Identifiers',
                             'xp_reward': 150}],
             'description': 'A variable name can use letters, numbers, and underscores, but cannot begin '
                            'with a number.',
             'lesson': {'common_mistakes': [{'fix': 'user_score = 50 (use underscore)',
                                             'mistake': 'user-score = 50',
                                             'why': 'Hyphens (-) mean subtraction in Python! Python thinks '
                                                    "you are trying to subtract 'score' from 'user'."}],
                        'detailed_explanation': "favorite_language = 'Python'\n"
                                                'first_score = 90\n'
                                                "player_name = 'Alex'\n"
                                                '\n'
                                                'These are valid names. Names like 2score, player name, and '
                                                'first-score are invalid because they start with a number or '
                                                'contain a space or hyphen. Python reports a syntax error '
                                                'when it cannot read a name. Choose a clear name and spell '
                                                'it the same way each time.',
                        'expected_output': 'Health: 75 / 100',
                        'introduction': 'A variable name can use letters, numbers, and underscores, but '
                                        'cannot begin with a number. Names cannot contain spaces, and Python '
                                        'special words cannot be used as names. Uppercase and lowercase are '
                                        'different, so score and Score are separate names. Use underscores '
                                        'between words, like favorite_language.',
                        'learning_objectives': ["Learn Python's strict rules for legal variable names",
                                                'Understand why variable names cannot start with a digit',
                                                'Master snake_case naming conventions (PEP 8)',
                                                'Identify Python reserved keywords that cannot be used as '
                                                'names'],
                        'line_by_line': [{'line': '1', 'code': 'max_health_points = 500', 'explanation': 'Store the number 500 in max_health_points.'}, {'line': '2', 'code': 'current_shield = 75', 'explanation': 'Store the number 75 in current_shield.'}, {'line': '3', 'code': "print('Defense Stats:', max_health_points, current_shield)", 'explanation': "Show the text 'Defense Stats:', followed by the current value of max_health_points, followed by the current value of current_shield. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Clean snake_case naming style',
                                                'code': 'max_health_points = 500\n'
                                                        'current_shield = 75\n'
                                                        "print('Defense Stats:', max_health_points, "
                                                        'current_shield)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Defense Stats: 500 75'},
                                               {'title': 'Example 2: Self-documenting time calculation',
                                                'code': 'seconds_per_hour = 3600\n'
                                                        'hours_elapsed = 4\n'
                                                        'total_seconds = hours_elapsed * seconds_per_hour\n'
                                                        "print('Total Seconds:', total_seconds)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Total Seconds: 14400'},
                                               {'title': 'Example 3: Case-sensitive variable uniqueness',
                                                'code': 'score = 10\n'
                                                        'Score = 20\n'
                                                        'SCORE = 30\n'
                                                        "print('Distinct values:', score, Score, SCORE)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Distinct values: 10 20 30'}],
                        'practice_questions': ["Why is 'user-name' an invalid variable name in Python?",
                                               "Can a variable name be 'class'? Why or why not?"],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'Strict adherence to PEP 8 snake_case is mandatory in top '
                                           'open-source projects and enterprise codebases.',
                        'summary': "favorite_language = 'Python'\nfirst_score = 90\nplayer_name = 'Alex'",
                        'syntax_breakdown': '# VALID Python variable names (follow snake_case):\n'
                                            'user_age = 25          # Lowercase words separated by '
                                            'underscores\n'
                                            'player_1_score = 950   # Digits are allowed after the first '
                                            'character\n'
                                            "_system_id = 'SYS-99'  # Leading underscore is legal (indicates "
                                            'internal use)\n'
                                            '\n'
                                            '# INVALID variable names (will cause SyntaxError):\n'
                                            "# 1st_player = 'Sam'   # CANNOT start with a number!\n"
                                            "# user-name = 'Sam'    # CANNOT contain hyphens (looks like "
                                            'subtraction)!\n'
                                            "# user name = 'Sam'    # CANNOT contain spaces!\n"
                                            "# class = 'Warrior'    # CANNOT use Python reserved keywords!",
                        'terminology': [{'definition': 'A naming style where words are written in lowercase '
                                                       'and separated by underscores (e.g. max_health).',
                                         'term': 'snake_case'},
                                        {'definition': 'Special words reserved by Python for language '
                                                       'mechanics that cannot be used as variable names '
                                                       '(e.g., while, import, def).',
                                         'term': 'Reserved Keyword'}],
                        'title': 'Variable Naming Rules'},
             'number': 13,
             'quizzes': [{'explanation': 'Python variable names cannot begin with a number.',
                          'options': [{'explanation': 'Correct! Variable names cannot begin with a digit.',
                                       'is_correct': True,
                                       'text': "1st_place = 'Gold'"},
                                      {'explanation': 'Valid variable name using snake_case.',
                                       'is_correct': False,
                                       'text': "first_place = 'Gold'"},
                                      {'explanation': 'Valid variable name starting with an underscore.',
                                       'is_correct': False,
                                       'text': "_gold_medal = 'Gold'"},
                                      {'explanation': 'Valid variable name ending with a digit.',
                                       'is_correct': False,
                                       'text': "place1 = 'Gold'"}],
                          'question': 'Which of the following variable assignments will cause a SyntaxError '
                                      'in Python?'},
                         {'explanation': 'Python interprets the hyphen (-) as the subtraction operator, not '
                                         'part of an identifier.',
                          'options': [{'explanation': 'Correct! Identifiers cannot contain hyphens.',
                                       'is_correct': True,
                                       'text': 'Python interprets the hyphen (-) as the subtraction '
                                               'operator'},
                                      {'explanation': 'Incorrect. Identifiers can be arbitrarily long.',
                                       'is_correct': False,
                                       'text': 'Variable names cannot exceed 8 characters'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'The equal sign cannot be preceded by letters'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Numbers cannot be assigned to variables with hyphens'}],
                          'question': 'Why does executing `user-score = 100` cause a SyntaxError in '
                                      'Python?'}],
             'title': 'Variable Naming Rules'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Start coins at 50.\n2. Add 25 to the same variable using +=, then display 75.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Start coins at 50. Add 25 to the same variable using +=, then '
                                             'display 75.',
                             'solution_code': 'coins = 50\ncoins += 25\nprint(coins)',
                             'test_cases': [{'expected_output': '75', 'input_data': '', 'is_hidden': False}],
                             'title': 'Score Incrementer',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Start hp at 100.\n2. Subtract 20, add 5, then subtract 10.\n3. Display Final HP: 75.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Start hp at 100. Subtract 20, add 5, then subtract 10. Display '
                                             'Final HP: 75.',
                             'solution_code': 'hp = 100\n'
                                              'hp -= 30\n'
                                              'hp -= 15\n'
                                              'hp += 20\n'
                                              "print('Final HP:', hp)",
                             'test_cases': [{'expected_output': 'Final HP: 75',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Health Bar Simulation',
                             'xp_reward': 150}],
             'description': 'A variable can be updated after it is created.',
             'lesson': {'common_mistakes': [{'fix': 'x += 5',
                                             'mistake': 'x =+ 5',
                                             'why': '=+ is not an operator; Python treats it as x = (+5), '
                                                    'overwriting x instead of adding!'}],
                        'detailed_explanation': 'coins = 50\n'
                                                'coins += 25\n'
                                                'print(coins)\n'
                                                '\n'
                                                'After line one, coins is 50. The next line adds 25 and '
                                                'saves 75 back in coins. The last line displays 75. `coins '
                                                '-= 10` subtracts 10; `coins *= 2` multiplies by 2. The '
                                                'equals sign means the updated answer is stored in the '
                                                'variable.',
                        'expected_output': 'Initial: 100\nAfter damage: 75\nAfter healing potion: 85',
                        'introduction': 'A variable can be updated after it is created. The short form '
                                        '`coins += 25` means add 25 to the current value and save the answer '
                                        'back in coins. This is useful for scores, health, and counters that '
                                        'change while a program runs.',
                        'learning_objectives': ['Understand that variables can be updated and reassigned '
                                                'over time',
                                                'Learn how Python evaluates the right side of = before '
                                                'updating the left',
                                                'Master augmented assignment operators (+=, -=, *=, /=)'],
                        'line_by_line': [{'line': '1', 'code': 'score = 0', 'explanation': 'Store the number 0 in score.'}, {'line': '2', 'code': 'score += 50', 'explanation': 'Add 50 to score and save the new value back in score.'}, {'line': '3', 'code': 'score += 100', 'explanation': 'Add 100 to score and save the new value back in score.'}, {'line': '4', 'code': "print('Final Arcade Score:', score)", 'explanation': "Show the text 'Final Arcade Score:', followed by the current value of score. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Arcade score counter',
                                                'code': 'score = 0\n'
                                                        'score += 50\n'
                                                        'score += 100\n'
                                                        "print('Final Arcade Score:', score)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Final Arcade Score: 150'},
                                               {'title': 'Example 2: Fuel consumption in flight',
                                                'code': 'fuel = 100\n'
                                                        'fuel -= 15\n'
                                                        'fuel -= 20\n'
                                                        "print('Remaining Fuel %:', fuel)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Remaining Fuel %: 65'},
                                               {'title': 'Example 3: Level-up XP multiplier',
                                                'code': 'required_xp = 1000\n'
                                                        'required_xp *= 2\n'
                                                        "print('Next Level XP Required:', required_xp)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Next Level XP Required: 2000'}],
                        'practice_questions': ['If x = 10 and you run x += 5, what is x?',
                                               'What is the difference between x = x + 1 and x += 1?'],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'Shopping apps update total bill as items are scanned using total '
                                           '+= item_price.',
                        'summary': 'coins = 50\ncoins += 25\nprint(coins)',
                        'syntax_breakdown': '# Updating a variable by reassigning its current value:\n'
                                            'wallet = 100\n'
                                            'wallet = wallet + 50   # Regular reassignment: 150\n'
                                            '\n'
                                            '# Augmented assignment shortcuts (cleaner and faster):\n'
                                            'wallet += 25   # Equivalent to wallet = wallet + 25 (175)\n'
                                            'wallet -= 10   # Equivalent to wallet = wallet - 10 (165)\n'
                                            'wallet *= 2    # Equivalent to wallet = wallet * 2  (330)\n'
                                            '\n'
                                            "print('Final Wallet Balance:', wallet)",
                        'terminology': [{'definition': "Overwriting a variable's existing stored value with "
                                                       'a new value.',
                                         'term': 'Reassignment'},
                                        {'definition': 'A shorthand operator like += or -= that modifies a '
                                                       'variable in place.',
                                         'term': 'Augmented Assignment'}],
                        'title': 'Updating Variables'},
             'number': 14,
             'quizzes': [{'explanation': 'count *= 3 is equivalent to count = count * 3, which is 5 * 3 = '
                                         '15.',
                          'options': [{'explanation': 'Correct! 5 * 3 = 15.',
                                       'is_correct': True,
                                       'text': '15'},
                                      {'explanation': 'Incorrect. *= multiplies rather than adds.',
                                       'is_correct': False,
                                       'text': '8'},
                                      {'explanation': 'Incorrect. Exponentiation is **=.',
                                       'is_correct': False,
                                       'text': '125'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '5'}],
                          'question': "What is the value of 'count' after running this code?\n"
                                      '\n'
                                      'count = 5\n'
                                      'count *= 3\n'
                                      'print(count)'},
                         {'explanation': 'mana starts at 100, decreases by 25 to 75, then increases by 10 to '
                                         '85.',
                          'options': [{'explanation': 'Correct! 100 - 25 = 75, 75 + 10 = 85.',
                                       'is_correct': True,
                                       'text': '85'},
                                      {'explanation': 'Incorrect calculation.',
                                       'is_correct': False,
                                       'text': '65'},
                                      {'explanation': 'Incorrect calculation.',
                                       'is_correct': False,
                                       'text': '90'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '100'}],
                          'question': 'What is the value of `mana` after executing:\n'
                                      '\n'
                                      'mana = 100\n'
                                      'mana -= 25\n'
                                      'mana += 10\n'
                                      'print(mana)'}],
             'title': 'Updating Variables'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Store one million in credits.\n2. You may use underscores to make the number easier to read.\n3. Display 1000000.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Store one million in credits. You may use underscores to make '
                                             'the number easier to read. Display 1000000.',
                             'solution_code': 'credits = 1_000_000\nprint(credits)',
                             'test_cases': [{'expected_output': '1000000',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Readable Large Integers',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Add the population values in alpha, beta, and gamma.\n2. Display the label Total Population: followed by the sum.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Add the population values in alpha, beta, and gamma. Display '
                                             'the label Total Population: followed by the sum.',
                             'solution_code': 'alpha = 100000\n'
                                              'beta = 250000\n'
                                              'gamma = 650000\n'
                                              'total_pop = alpha + beta + gamma\n'
                                              "print('Total Population:', total_pop)",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Total Population: 1000000',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Galactic Population',
                             'xp_reward': 150}],
             'description': 'An integer is a whole number with no decimal part, such as 0, 7, or -12.',
             'lesson': {'common_mistakes': [{'fix': 'price = 1_000_000 or price = 1000000',
                                             'mistake': 'price = 1,000,000',
                                             'why': 'Using commas creates a tuple (1, 0, 0), NOT an '
                                                    'integer!'}],
                        'detailed_explanation': 'credits = 1_000_000\n'
                                                'print(credits)\n'
                                                '\n'
                                                'The underscores help a person read the number; Python '
                                                'ignores them. The output is 1000000. You can do arithmetic '
                                                'with integers too: `total = 12 + 8` stores 20. Use a float '
                                                'when the number needs a decimal part.',
                        'expected_output': 'Estimated stars: 100000000000',
                        'introduction': 'An integer is a whole number with no decimal part, such as 0, 7, or '
                                        '-12. Python calls it an int. Integers are useful for counts, ages, '
                                        'and scores. Underscores can make large numbers easier to read: '
                                        '`1_000_000` has the same value as `1000000`.',
                        'learning_objectives': ['Understand the int data type in Python',
                                                'Learn that Python integers have arbitrary precision (no '
                                                'overflow)',
                                                'Use underscores as visual digit separators in large numbers '
                                                '(e.g. 1_000_000)'],
                        'line_by_line': [{'line': '1', 'code': 'lives = 3', 'explanation': 'Store the number 3 in lives.'}, {'line': '2', 'code': 'lives -= 1', 'explanation': 'Subtract 1 from lives and save the new value back in lives.'}, {'line': '3', 'code': "print('Lives remaining:', lives)", 'explanation': "Show the text 'Lives remaining:', followed by the current value of lives. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Life counter countdown',
                                                'code': 'lives = 3\n'
                                                        'lives -= 1\n'
                                                        "print('Lives remaining:', lives)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Lives remaining: 2'},
                                               {'title': 'Example 2: Floor division and remainder (modulo)',
                                                'code': 'items = 14\n'
                                                        'box_size = 4\n'
                                                        'boxes = items // box_size\n'
                                                        'leftover = items % box_size\n'
                                                        "print('Full Boxes:', boxes, 'Leftover Items:', "
                                                        'leftover)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Full Boxes: 3 Leftover Items: 2'},
                                               {'title': 'Example 3: Negative depth tracking',
                                                'code': 'depth = -20\n'
                                                        'depth -= 15\n'
                                                        "print('Submarine Depth:', depth, 'meters')",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Submarine Depth: -35 meters'}],
                        'practice_questions': ['Can an integer in Python be negative?',
                                               'What happens if you type commas inside a number in Python?'],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'Cryptography, astronomical simulations, and banking ledgers use '
                                           'arbitrary-precision integers.',
                        'summary': 'credits = 1_000_000\nprint(credits)',
                        'syntax_breakdown': '# Integers (int) are whole numbers with NO decimal point:\n'
                                            'player_lives = 3\n'
                                            'monsters_slain = 42\n'
                                            'temperature = -8   # Integers can be negative\n'
                                            '\n'
                                            "print('Lives:', player_lives)\n"
                                            "print('Monsters Slain:', monsters_slain)\n"
                                            "print('Sub-Zero Temp:', temperature)",
                        'terminology': [{'definition': "Python's built-in data type for whole numbers.",
                                         'term': 'int'},
                                        {'definition': 'A feature where numbers can grow as large as your '
                                                       "computer's RAM permits without overflow errors.",
                                         'term': 'Arbitrary Precision'}],
                        'title': 'Understanding Integers'},
             'number': 15,
             'quizzes': [{'explanation': 'Underscores in numeric literals are ignored by Python and serve '
                                         'only to improve human readability.',
                          'options': [{'explanation': 'Correct! Underscores in numbers are visual separators '
                                                      'and do not affect the value.',
                                       'is_correct': True,
                                       'text': '5000001'},
                                      {'explanation': 'Incorrect. Python prints integers without '
                                                      'underscores.',
                                       'is_correct': False,
                                       'text': '5_000_001'},
                                      {'explanation': 'Incorrect. Underscores in numbers are fully valid '
                                                      'syntax in Python 3.6+.',
                                       'is_correct': False,
                                       'text': 'TypeError: unsupported operand for underscore'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '5000000'}],
                          'question': 'What is the output of the following code snippet?\n'
                                      '\n'
                                      'amount = 5_000_000\n'
                                      'print(amount + 1)'},
                         {'explanation': 'int() converts strings of digits into integers. 25 + 15 = 40.',
                          'options': [{'explanation': 'Correct! 25 + 15 = 40.',
                                       'is_correct': True,
                                       'text': '40'},
                                      {'explanation': "Incorrect. That would happen without int(): '25' + "
                                                      "'15' = '2515'.",
                                       'is_correct': False,
                                       'text': '2515'},
                                      {'explanation': 'Incorrect. int() returns integer types, not strings.',
                                       'is_correct': False,
                                       'text': "'40'"},
                                      {'explanation': 'Incorrect. Both strings contain valid integers.',
                                       'is_correct': False,
                                       'text': 'ValueError'}],
                          'question': 'What is the output of running this code?\n'
                                      '\n'
                                      "val = int('25') + int('15')\n"
                                      'print(val)'}],
             'title': 'Understanding Integers'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Add price and tax, save the answer in total, and display it with the label Total:.\n2. The sample values add up to 21.6.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Add price and tax, save the answer in total, and display it '
                                             'with the label Total:. The sample values add up to 21.6.',
                             'solution_code': 'price = 20.0\n'
                                              'tax = 1.6\n'
                                              'total = price + tax\n'
                                              "print('Total:', total)",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Total: 21.6',
                                             'is_hidden': False}],
                             'title': 'Price with Tax',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Calculate speed by dividing distance by time.\n2. Display Speed: and the unit km/h.\n3. The sample answer is 60.2 km/h.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Calculate speed by dividing distance by time. Display Speed: '
                                             'and the unit km/h. The sample answer is 60.2 km/h.',
                             'solution_code': 'distance = 301.0\n'
                                              'time = 5.0\n'
                                              'speed = distance / time\n'
                                              "print('Speed:', speed, 'km/h')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Speed: 60.2 km/h',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Distance Formula',
                             'xp_reward': 150}],
             'description': 'A float is a number with a decimal point, such as 2.',
             'lesson': {'common_mistakes': [{'fix': 'price = 19.99',
                                             'mistake': 'price = $19.99',
                                             'why': 'Dollar signs ($) are invalid syntax in numeric '
                                                    'literals.'}],
                        'detailed_explanation': 'price = 20.0\n'
                                                'tax = 1.6\n'
                                                'total = price + tax\n'
                                                "print('Total:', total)\n"
                                                '\n'
                                                'The first two lines store decimal numbers. The third adds '
                                                'them and saves 21.6 in total. The last line prints a label '
                                                'and the answer. Keep a decimal when the information '
                                                'represents a measurement or amount that can be fractional.',
                        'expected_output': 'Circumference: 31.4159',
                        'introduction': 'A float is a number with a decimal point, such as 2.5 or 21.6. '
                                        'Floats are useful for prices, distances, and measurements that can '
                                        'have a fraction. Python can add, subtract, multiply, and divide '
                                        'them. Division with / gives a float.',
                        'learning_objectives': ['Understand the float data type in Python',
                                                'Learn how decimal fractions are represented in binary',
                                                'Recognize floating-point rounding quirks (e.g. 0.1 + 0.2)'],
                        'line_by_line': [{'line': '1', 'code': 'latitude = 35.6762', 'explanation': 'Store the number 35.6762 in latitude.'}, {'line': '2', 'code': 'longitude = 139.6503', 'explanation': 'Store the number 139.6503 in longitude.'}, {'line': '3', 'code': "print('GPS Position:', latitude, longitude)", 'explanation': "Show the text 'GPS Position:', followed by the current value of latitude, followed by the current value of longitude. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: GPS coordinate tracking',
                                                'code': 'latitude = 35.6762\n'
                                                        'longitude = 139.6503\n'
                                                        "print('GPS Position:', latitude, longitude)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'GPS Position: 35.6762 139.6503'},
                                               {'title': 'Example 2: Compound savings interest',
                                                'code': 'principal = 1000.0\n'
                                                        'interest_rate = 0.05\n'
                                                        'earnings = principal * interest_rate\n'
                                                        "print('Annual Interest Earned: $', earnings)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Annual Interest Earned: $ 50.0'},
                                               {'title': 'Example 3: Precise division producing floats',
                                                'code': 'slices = 9\n'
                                                        'people = 4\n'
                                                        "print('Slices per person:', slices / people)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Slices per person: 2.25'}],
                        'practice_questions': ['Is 5.0 an integer or a float?',
                                               'Why does 0.1 + 0.2 produce 0.30000000000000004 in modern '
                                               'computers?'],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'Scientific simulations, 3D graphics engines, and physics '
                                           'simulators rely on floats.',
                        'summary': "price = 20.0\ntax = 1.6\ntotal = price + tax\nprint('Total:', total)",
                        'syntax_breakdown': '# Floating-point numbers (float) contain a decimal point:\n'
                                            'unit_price = 19.99\n'
                                            'tax_multiplier = 0.08\n'
                                            'total_cost = unit_price * (1 + tax_multiplier)\n'
                                            '\n'
                                            "print('Raw total:', total_cost)\n"
                                            "print('Formatted total:', round(total_cost, 2))",
                        'terminology': [{'definition': "Python's data type for numbers with decimal points.",
                                         'term': 'float'},
                                        {'definition': 'The degree of accuracy to which a fractional '
                                                       'quantity is specified.',
                                         'term': 'Precision'}],
                        'title': 'Understanding Floats'},
             'number': 16,
             'quizzes': [{'explanation': 'Multiplying an integer by a float promotes the result to a float '
                                         'in Python.',
                          'options': [{'explanation': 'Correct! 5 * 2.0 produces 10.0, which is of type '
                                                      'float.',
                                       'is_correct': True,
                                       'text': "<class 'float'>"},
                                      {'explanation': 'Incorrect. Operating with a float produces a float.',
                                       'is_correct': False,
                                       'text': "<class 'int'>"},
                                      {'explanation': "Incorrect. Python does not have a 'double' type, it "
                                                      "uses 'float'.",
                                       'is_correct': False,
                                       'text': "<class 'double'>"},
                                      {'explanation': 'Incorrect. type() returns the type object, not the '
                                                      'numeric value.',
                                       'is_correct': False,
                                       'text': '10.0'}],
                          'question': 'What is the output of running:\n'
                                      '\n'
                                      'result = 5 * 2.0\n'
                                      'print(type(result))'},
                         {'explanation': '// performs floor division yielding an integer (3), while / '
                                         'performs true division yielding a float (3.5).',
                          'options': [{'explanation': 'Correct! // yields 3, while / yields 3.5.',
                                       'is_correct': True,
                                       'text': '3 3.5'},
                                      {'explanation': 'Incorrect. Floor division // truncates the decimal '
                                                      'portion.',
                                       'is_correct': False,
                                       'text': '3.5 3.5'},
                                      {'explanation': 'Incorrect. True division / always returns a float.',
                                       'is_correct': False,
                                       'text': '3 3'},
                                      {'explanation': 'Incorrect. Floor division rounds down, not up.',
                                       'is_correct': False,
                                       'text': '4 3.5'}],
                          'question': 'What is the exact output of:\n\nprint(7 // 2, 7 / 2)'}],
             'title': 'Understanding Floats'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use an f-string to display Player Mia has 12 gold.\n2. Store the name in player and the number in gold.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Use an f-string to display Player Mia has 12 gold. Store the '
                                             'name in player and the number in gold.',
                             'solution_code': "player = 'Mia'\n"
                                              'gold = 12\n'
                                              "print(f'Player {player} has {gold} gold')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Player Mia has 12 gold',
                                             'is_hidden': False}],
                             'title': 'Formatting with f-strings',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Store Shadowhunter in character_name.\n2. Use len() to count its characters.\n3. Display Name: Shadowhunter on one line and Length: 12 on the next.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Store Shadowhunter in character_name. Use len() to count its '
                                             'characters. Display Name: Shadowhunter on one line and Length: '
                                             '12 on the next.',
                             'solution_code': "character_name = 'Shadowhunter'\n"
                                              "print(f'Name: {character_name}')\n"
                                              "print(f'Length: {len(character_name)}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Name: Shadowhunter\nLength: 12',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Character Name Length Checker',
                             'xp_reward': 150}],
             'description': 'A string is text between matching quote marks.',
             'lesson': {'common_mistakes': [{'fix': "print(f'Hello {name}')",
                                             'mistake': "print('Hello {name}')  # forgot the f prefix",
                                             'why': "Without the 'f' in front of quotes, Python prints "
                                                    "literal '{name}' without replacing it!"}],
                        'detailed_explanation': "player = 'Mia'\n"
                                                'gold = 12\n'
                                                "print(f'Player {player} has {gold} gold')\n"
                                                '\n'
                                                'Python replaces {player} with Mia and {gold} with 12, so '
                                                'the output is Player Mia has 12 gold. The braces are '
                                                'instructions and do not appear in the output. Without f, '
                                                'Python would show the braces as text. `len(text)` counts '
                                                'the characters in a string.',
                        'expected_output': 'Hero: Cipher | Level: 5 | XP: 450',
                        'introduction': 'A string is text between matching quote marks. An f-string mixes '
                                        'text and variable values: put f before the quote, then put a '
                                        'variable inside curly braces where its value should appear.',
                        'learning_objectives': ['Store text in variables using str data type',
                                                'Learn string length using the len() function',
                                                'Format variables into strings using f-strings'],
                        'line_by_line': [{'line': '1', 'code': "username = 'alex'", 'explanation': "Store the text 'alex' in username."}, {'line': '2', 'code': "domain = 'quest.org'", 'explanation': "Store the text 'quest.org' in domain."}, {'line': '3', 'code': "email = username + '@' + domain", 'explanation': "Calculate username + '@' + domain, then store the answer in email."}, {'line': '4', 'code': "print('Generated Email:', email)", 'explanation': "Show the text 'Generated Email:', followed by the current value of email. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Dynamic email generation',
                                                'code': "username = 'alex'\n"
                                                        "domain = 'quest.org'\n"
                                                        "email = username + '@' + domain\n"
                                                        "print('Generated Email:', email)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Generated Email: alex@quest.org'},
                                               {'title': 'Example 2: Auto-sized banner box',
                                                'code': "header = 'MISSION DEPLOYMENT'\n"
                                                        "print('=' * len(header))\n"
                                                        'print(header)\n'
                                                        "print('=' * len(header))",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': '==================\n'
                                                          'MISSION DEPLOYMENT\n'
                                                          '=================='},
                                               {'title': 'Example 3: Password length check',
                                                'code': "secret_pin = 'vault-2026'\n"
                                                        "print('PIN length:', len(secret_pin))",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'PIN length: 10'}],
                        'practice_questions': ["What happens if you omit the 'f' before an f-string?",
                                               "What does len('Python 3') return?"],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': "Every personalized email notification ('Hello John, your order "
                                           "is shipped') uses f-string formatting.",
                        'summary': "player = 'Mia'\ngold = 12\nprint(f'Player {player} has {gold} gold')",
                        'syntax_breakdown': '# Strings (str) store sequences of characters in quotes:\n'
                                            "first_name = 'Ada'\n"
                                            "last_name = 'Lovelace'\n"
                                            "full_name = first_name + ' ' + last_name\n"
                                            '\n'
                                            "print('Full Name:', full_name)\n"
                                            "print('Total Characters:', len(full_name))",
                        'terminology': [{'definition': "Python's data type representing textual character "
                                                       'strings.',
                                         'term': 'str'},
                                        {'definition': 'A formatted string literal prefixed with f that '
                                                       'evaluates embedded expressions inside {}.',
                                         'term': 'f-string'},
                                        {'definition': 'A built-in Python function that returns the total '
                                                       'count of items or characters.',
                                         'term': 'len()'}],
                        'title': 'Formatting Strings with f-strings'},
             'number': 17,
             'quizzes': [{'explanation': 'len() counts every character in the string, including the space. '
                                         "'Code Quest' has 10 characters.",
                          'options': [{'explanation': 'Correct! 4 letters + 1 space + 5 letters = 10 '
                                                      'characters.',
                                       'is_correct': True,
                                       'text': '10'},
                                      {'explanation': 'Incorrect. The space character is counted in len().',
                                       'is_correct': False,
                                       'text': '9'},
                                      {'explanation': 'Incorrect. len() counts characters, not words.',
                                       'is_correct': False,
                                       'text': '2'},
                                      {'explanation': 'Incorrect. len() works on strings.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the following code?\n'
                                      '\n'
                                      "text = 'Code Quest'\n"
                                      'print(len(text))'},
                         {'explanation': 'f-strings evaluate expressions inside curly braces {} at runtime. '
                                         'level * 2 = 10.',
                          'options': [{'explanation': 'Correct! The f-string evaluates {name} as Cipher and '
                                                      '{level * 2} as 10.',
                                       'is_correct': True,
                                       'text': 'Cipher is at level 10'},
                                      {'explanation': 'Incorrect. Expressions inside {} in f-strings are '
                                                      'evaluated.',
                                       'is_correct': False,
                                       'text': 'Cipher is at level level * 2'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '{name} is at level {10}'},
                                      {'explanation': 'Incorrect. Expressions inside f-strings are '
                                                      'completely legal.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What is the output of this f-string code snippet?\n'
                                      '\n'
                                      "name = 'Cipher'\n"
                                      'level = 5\n'
                                      "print(f'{name} is at level {level * 2}')"}],
             'title': 'Formatting Strings with f-strings'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Store True in is_online and False in has_shield.\n2. Display each value on its own line.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Store True in is_online and False in has_shield. Display each '
                                             'value on its own line.',
                             'solution_code': 'is_online = True\n'
                                              'has_shield = False\n'
                                              'print(is_online)\n'
                                              'print(has_shield)',
                             'test_cases': [{'expected_output': 'True\nFalse',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boolean State Tracking',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Store True in engines and shields, and False in autopilot.\n2. Use an f-string to display exactly: ENGINES: True | SHIELDS: True | AUTOPILOT: False\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Store True in engines and shields, and False in autopilot. Use '
                                             'an f-string to display exactly: ENGINES: True | SHIELDS: True '
                                             '| AUTOPILOT: False',
                             'solution_code': 'engines = True\n'
                                              'shields = True\n'
                                              'autopilot = False\n'
                                              "print(f'ENGINES: {engines} | SHIELDS: {shields} | AUTOPILOT: "
                                              "{autopilot}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'ENGINES: True | SHIELDS: True | AUTOPILOT: '
                                                                'False',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: System Status Flags',
                             'xp_reward': 150}],
             'description': 'A Boolean is either True or False.',
             'lesson': {'common_mistakes': [{'fix': 'is_active = True',
                                             'mistake': 'is_active = true',
                                             'why': "Python booleans are capitalized! 'true' is not "
                                                    'recognized and triggers NameError.'},
                                            {'fix': 'is_active = True',
                                             'mistake': "is_active = 'True'",
                                             'why': 'Quotes turn it into a text string, not a true '
                                                    'boolean.'}],
                        'detailed_explanation': 'is_online = True\n'
                                                'has_shield = False\n'
                                                'print(is_online)\n'
                                                'print(has_shield)\n'
                                                '\n'
                                                'The output is True on the first line and False on the '
                                                'second. Other code can check these answers to choose what '
                                                'to do. Python uses exactly True and False for Boolean '
                                                'values.',
                        'expected_output': 'Quest Active: True\nPremium: False',
                        'introduction': 'A Boolean is either True or False. These values answer yes-or-no '
                                        'questions, such as whether a player is online or a shield is '
                                        'active. Capitalize the first letter and do not use quotes: True is '
                                        "a Boolean, while 'True' is text.",
                        'learning_objectives': ['Understand the bool data type and its two values: True and '
                                                'False',
                                                'Learn why Booleans are the foundation of computer '
                                                'decision-making',
                                                'Recognize that True and False must be capitalized in '
                                                'Python'],
                        'line_by_line': [{'line': '1', 'code': 'has_vip_pass = True', 'explanation': 'Store True in has_vip_pass. This variable records a yes-or-no answer.'}, {'line': '2', 'code': "print('Access Granted:', has_vip_pass)", 'explanation': "Show the text 'Access Granted:', followed by the current value of has_vip_pass. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: VIP access verification',
                                                'code': 'has_vip_pass = True\n'
                                                        "print('Access Granted:', has_vip_pass)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Access Granted: True'},
                                               {'title': "Example 2: Inverting state with 'not'",
                                                'code': 'is_maintenance_mode = False\n'
                                                        "print('Server Open for Players:', not "
                                                        'is_maintenance_mode)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Server Open for Players: True'},
                                               {'title': 'Example 3: Evaluating boolean comparisons',
                                                'code': 'player_level = 15\n'
                                                        'is_eligible = player_level >= 10\n'
                                                        "print('Eligible for Dungeon:', is_eligible)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Eligible for Dungeon: True'}],
                        'practice_questions': ['What are the only two values a boolean can hold?',
                                               'Why is is_ready = true invalid in Python?'],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'Every permission check (`is_admin`), toggle switch (dark mode '
                                           'enabled), and authentication status uses booleans.',
                        'summary': 'is_online = True\n'
                                   'has_shield = False\n'
                                   'print(is_online)\n'
                                   'print(has_shield)',
                        'syntax_breakdown': '# Booleans (bool) represent binary truth: True or False '
                                            '(capitalized!)\n'
                                            'is_game_running = True\n'
                                            'has_gold_key = False\n'
                                            'server_connected = True\n'
                                            '\n'
                                            "print('Game Running:', is_game_running)\n"
                                            "print('Has Gold Key:', has_gold_key)\n"
                                            "print('Connection Status:', server_connected)",
                        'terminology': [{'definition': "Python's data type representing truth values: either "
                                                       'True or False.',
                                         'term': 'bool'},
                                        {'definition': 'A variable holding True or False used to indicate '
                                                       'whether a condition or mode is active.',
                                         'term': 'Boolean Flag'}],
                        'title': 'Understanding Booleans'},
             'number': 18,
             'quizzes': [{'explanation': "True and False are boolean literals in Python with type 'bool'.",
                          'options': [{'explanation': "Correct! True has the boolean type 'bool'.",
                                       'is_correct': True,
                                       'text': "<class 'bool'>"},
                                      {'explanation': 'Incorrect. Without quotes, True is a boolean, not a '
                                                      'string.',
                                       'is_correct': False,
                                       'text': "<class 'str'>"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "<class 'int'>"},
                                      {'explanation': 'Incorrect. type() prints the class, not the value.',
                                       'is_correct': False,
                                       'text': 'True'}],
                          'question': 'What will be printed by the following code?\n'
                                      '\n'
                                      'is_online = True\n'
                                      'print(type(is_online))'},
                         {'explanation': '10 > 20 is False, and 10 < 20 is True.',
                          'options': [{'explanation': 'Correct! 10 > 20 is False, 10 < 20 is True.',
                                       'is_correct': True,
                                       'text': 'False True'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'True False'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'False False'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'True True'}],
                          'question': 'What is the output of the following comparison?\n'
                                      '\n'
                                      'x = 10\n'
                                      'y = 20\n'
                                      'print(x > y, x < y)'}],
             'title': 'Understanding Booleans'},
            {'challenges': [{'description': "Your task, step by step:\n1. Store 99 in quest_id.\n2. Use type() and print() to display its type: <class 'int'>.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.",
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Store 99 in quest_id. Use type() and print() to display its '
                                             "type: <class 'int'>.",
                             'solution_code': 'quest_id = 99\nprint(type(quest_id))',
                             'test_cases': [{'expected_output': "<class 'int'>",
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Type Inspection',
                             'xp_reward': 30},
                            {'description': "Your task, step by step:\n1. Use type() to check a decimal number and a Boolean.\n2. Display <class 'float'> on line one and <class 'bool'> on line two.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.",
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Use type() to check a decimal number and a Boolean. Display '
                                             "<class 'float'> on line one and <class 'bool'> on line two.",
                             'solution_code': 'score_val = 98.6\n'
                                              'is_passed = True\n'
                                              'print(type(score_val))\n'
                                              'print(type(is_passed))',
                             'test_cases': [{'expected_output': "<class 'float'>\n<class 'bool'>",
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Dual Type Auditor',
                             'xp_reward': 150}],
             'description': 'The `type()` function tells you what kind of value Python is holding.',
             'lesson': {'common_mistakes': [{'fix': "print(type('Hello'))",
                                             'mistake': "type('Hello')",
                                             'why': 'Calling type() without print() in a script will not '
                                                    'display anything to the console.'}],
                        'detailed_explanation': 'quest_id = 99\n'
                                                'print(type(quest_id))\n'
                                                '\n'
                                                'The first line stores an integer. type(quest_id) checks it, '
                                                "and print shows <class 'int'>. Text has type str, decimal "
                                                'numbers have type float, and yes-or-no values have type '
                                                "bool. The angle-bracket output is Python's way of showing "
                                                'the type.',
                        'expected_output': "<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>",
                        'introduction': 'The `type()` function tells you what kind of value Python is '
                                        'holding. Put a value or variable inside its parentheses. For '
                                        'example, type(99) reports that 99 is an integer. This helps you '
                                        'understand why an operation behaves a certain way.',
                        'learning_objectives': ["Use the built-in type() function to inspect any variable's "
                                                'data type',
                                                "Recognize Python type representations: <class 'int'>, "
                                                "<class 'str'>, <class 'float'>, <class 'bool'>",
                                                'Understand how Python tracks type information internally'],
                        'line_by_line': [{'line': '1', 'code': "raw_tax = '0.08'", 'explanation': "Store the text '0.08' in raw_tax."}, {'line': '2', 'code': 'tax_multiplier = float(raw_tax)', 'explanation': 'Store float(raw_tax) in tax_multiplier, so the program can use it later.'}, {'line': '3', 'code': 'base_price = 100', 'explanation': 'Store the number 100 in base_price.'}, {'line': '4', 'code': "print('Calculated Tax: $', base_price * tax_multiplier)", 'explanation': "Show the text 'Calculated Tax: $', followed by the current value of base_price * tax_multiplier. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Parsing user text input for '
                                                         'calculations',
                                                'code': "raw_tax = '0.08'\n"
                                                        'tax_multiplier = float(raw_tax)\n'
                                                        'base_price = 100\n'
                                                        "print('Calculated Tax: $', base_price * "
                                                        'tax_multiplier)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Calculated Tax: $ 8.0'},
                                               {'title': 'Example 2: Concatenating numbers into strings '
                                                         'safely',
                                                'code': 'player_level = 5\n'
                                                        "message = 'Player is currently Level ' + "
                                                        'str(player_level)\n'
                                                        'print(message)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Player is currently Level 5'},
                                               {'title': 'Example 3: Truncating decimals with int()',
                                                'code': 'precise_pi = 3.99\n'
                                                        'truncated_pi = int(precise_pi)\n'
                                                        "print('Truncated Int:', truncated_pi)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Truncated Int: 3'}],
                        'practice_questions': ["What does print(type('42')) output?",
                                               'What does print(type(True)) output?'],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'APIs inspect incoming JSON payloads to ensure fields match '
                                           'expected types before storing them in databases.',
                        'summary': 'quest_id = 99\nprint(type(quest_id))',
                        'syntax_breakdown': '# Type conversion functions: int(), float(), str(), bool()\n'
                                            "str_val = '42'\n"
                                            "int_val = int(str_val)       # '42' -> 42 (integer)\n"
                                            "float_val = float(str_val)   # '42' -> 42.0 (float)\n"
                                            "text_val = str(float_val)    # 42.0 -> '42.0' (string)\n"
                                            '\n'
                                            "print('Integer + 8:', int_val + 8)\n"
                                            "print('Float / 2:', float_val / 2)\n"
                                            "print('Text Output: ' + text_val)",
                        'terminology': [{'definition': 'A built-in Python function that inspects and returns '
                                                       'the data type of any object.',
                                         'term': 'type()'},
                                        {'definition': 'The blueprint or category defining a data type in '
                                                       'Python.',
                                         'term': 'class'}],
                        'title': 'Checking Data Types with type()'},
             'number': 19,
             'quizzes': [{'explanation': "Because 'True' is wrapped in quotation marks, it is a string "
                                         '(str), not a boolean.',
                          'options': [{'explanation': 'Correct! Quotation marks indicate a string.',
                                       'is_correct': True,
                                       'text': "<class 'str'>"},
                                      {'explanation': "Incorrect. 'True' in quotes is a string, not a bool.",
                                       'is_correct': False,
                                       'text': "<class 'bool'>"},
                                      {'explanation': "Incorrect. Python's boolean type name is 'bool'.",
                                       'is_correct': False,
                                       'text': "<class 'boolean'>"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'True'}],
                          'question': "What will print(type('True')) output in Python?"},
                         {'explanation': 'type(3.14) is float, so the comparison evaluates to True.',
                          'options': [{'explanation': 'Correct! type(val) is equal to float.',
                                       'is_correct': True,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect. 3.14 is indeed a float.',
                                       'is_correct': False,
                                       'text': 'False'},
                                      {'explanation': 'Incorrect. The equality comparison == returns a '
                                                      'boolean.',
                                       'is_correct': False,
                                       'text': "<class 'float'>"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of running this comparison?\n'
                                      '\n'
                                      'val = 3.14\n'
                                      'print(type(val) == float)'}],
             'title': 'Checking Data Types with type()'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Convert raw_xp to an integer, add bonus_xp, and display the result.\n2. With the sample values, the answer is 200.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Convert raw_xp to an integer, add bonus_xp, and display the '
                                             'result. With the sample values, the answer is 200.',
                             'solution_code': "raw_xp = '120'\ntotal_xp = int(raw_xp) + 80\nprint(total_xp)",
                             'test_cases': [{'expected_output': '200', 'input_data': '', 'is_hidden': False}],
                             'title': 'String to Integer Calculation',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Convert str_hours from text to an integer, multiply by hourly_rate, then display Earnings: $204.0 using an f-string.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Convert str_hours from text to an integer, multiply by '
                                             'hourly_rate, then display Earnings: $204.0 using an f-string.',
                             'solution_code': "str_hours = '8'\n"
                                              'hourly_rate = 25.5\n'
                                              'earnings = int(str_hours) * hourly_rate\n'
                                              "print(f'Earnings: ${earnings}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Earnings: $204.0',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Mixed Type Conversion Pipeline',
                             'xp_reward': 150}],
             'description': 'Sometimes a number arrives as text, such as from a form.',
             'lesson': {'common_mistakes': [{'fix': 'Only pass valid numeric digits into int().',
                                             'mistake': "int('hello')",
                                             'why': 'Python cannot convert non-numeric words into numbers '
                                                    'and raises ValueError.'},
                                            {'fix': "float('3.14')",
                                             'mistake': "int('3.14')",
                                             'why': 'int() cannot directly parse a decimal point string. You '
                                                    "must convert to float first: int(float('3.14'))."}],
                        'detailed_explanation': "raw_xp = '175'\n"
                                                'bonus_xp = 25\n'
                                                'total_xp = int(raw_xp) + bonus_xp\n'
                                                'print(total_xp)\n'
                                                '\n'
                                                'raw_xp starts as text because it is in quotes. int(raw_xp) '
                                                'converts it to the number 175. Python can then add 25, so '
                                                'the output is 200. int() drops the decimal part rather than '
                                                'rounding; use float() to keep a decimal.',
                        'expected_output': 'Total Score: 200',
                        'introduction': 'Sometimes a number arrives as text, such as from a form. Python '
                                        "cannot do arithmetic with the text '100' until you convert it. "
                                        '`int(text)` makes a whole number and `float(text)` makes a decimal '
                                        'number. The text must contain a suitable number.',
                        'learning_objectives': ['Understand type casting (type conversion) in Python',
                                                'Use int(), float(), str(), and bool() constructor functions',
                                                'Learn how converting a float to an int truncates decimal '
                                                'places (not rounding)'],
                        'line_by_line': [{'line': '1', 'code': "player_name = 'Elena'", 'explanation': "Store the text 'Elena' in player_name."}, {'line': '2', 'code': '# print(playr_name) <-- Typo causes NameError', 'explanation': 'This is a note for the person reading the code. Python skips comments, so this line does not run or print anything.'}, {'line': '3', 'code': "print('Player:', player_name)", 'explanation': "Show the text 'Player:', followed by the current value of player_name. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Fixing typos in variable identifiers',
                                                'code': "player_name = 'Elena'\n"
                                                        '# print(playr_name) <-- Typo causes NameError\n'
                                                        "print('Player:', player_name)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Player: Elena'},
                                               {'title': 'Example 2: Protecting built-in function names',
                                                'code': "# Never do: print = 'Hello' (destroys built-in "
                                                        'print!)\n'
                                                        "custom_greeting = 'Hello, Quest!'\n"
                                                        'print(custom_greeting)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Hello, Quest!'},
                                               {'title': 'Example 3: Safe string-to-number conversion',
                                                'code': "valid_digit_str = '25'\n"
                                                        "# int('twenty-five') <-- ValueError!\n"
                                                        'count = int(valid_digit_str)\n'
                                                        "print('Converted count times 2:', count * 2)",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Converted count times 2: 50'}],
                        'practice_questions': ['What does int(7.8) produce in Python?',
                                               "What does bool('') return?"],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'Every web form submission and user input arrives as strings and '
                                           'must be cast to `int` or `float` before math can occur.',
                        'summary': "raw_xp = '175'\n"
                                   'bonus_xp = 25\n'
                                   'total_xp = int(raw_xp) + bonus_xp\n'
                                   'print(total_xp)',
                        'syntax_breakdown': '# Trap 1: Using a variable before assigning it (causes '
                                            'NameError)\n'
                                            '# print(hero_score)  <-- NameError!\n'
                                            'hero_score = 100     # Fix: Define first!\n'
                                            "print('Hero Score:', hero_score)\n"
                                            '\n'
                                            '# Trap 2: Mixing incompatible types (causes TypeError)\n'
                                            "# result = 'Score: ' + 50  <-- TypeError!\n"
                                            "result = 'Score: ' + str(50)  # Fix: Convert to string!\n"
                                            'print(result)',
                        'terminology': [{'definition': 'Explicitly converting a value from one data type to '
                                                       'another using constructor functions.',
                                         'term': 'Type Casting'},
                                        {'definition': 'Discarding the fractional/decimal portion of a '
                                                       'number when converting to an integer.',
                                         'term': 'Truncation'}],
                        'title': 'Type Conversion'},
             'number': 20,
             'quizzes': [{'explanation': 'int() truncates floating-point numbers toward zero, discarding '
                                         'everything after the decimal.',
                          'options': [{'explanation': 'Correct! int() truncates decimals, it does not round '
                                                      'up.',
                                       'is_correct': True,
                                       'text': '9'},
                                      {'explanation': 'Incorrect. int() does not round to nearest; use '
                                                      'round() for that.',
                                       'is_correct': False,
                                       'text': '10'},
                                      {'explanation': 'Incorrect. int() converts to a whole number.',
                                       'is_correct': False,
                                       'text': '9.99'},
                                      {'explanation': 'Incorrect. int(float) is fully valid.',
                                       'is_correct': False,
                                       'text': 'ValueError'}],
                          'question': 'What does print(int(9.99)) output in Python?'},
                         {'explanation': '0 is falsy, non-zero integers are truthy, and empty strings are '
                                         'falsy.',
                          'options': [{'explanation': "Correct! 0 is False, 10 is True, '' is False.",
                                       'is_correct': True,
                                       'text': 'False True False'},
                                      {'explanation': "Incorrect. 0 and '' are falsy.",
                                       'is_correct': False,
                                       'text': 'True True True'},
                                      {'explanation': 'Incorrect. 10 is truthy.',
                                       'is_correct': False,
                                       'text': 'False False False'},
                                      {'explanation': 'Incorrect. bool() returns booleans.',
                                       'is_correct': False,
                                       'text': '0 10 None'}],
                          'question': 'What will be printed by the following code?\n'
                                      '\n'
                                      "print(bool(0), bool(10), bool(''))"}],
             'title': 'Type Conversion'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Convert str_val to a float and store it in result.\n2. Display Result: 75.5 using an f-string.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Convert str_val to a float and store it in result. Display '
                                             'Result: 75.5 using an f-string.',
                             'solution_code': "str_val = '75.5'\n"
                                              'result = float(str_val)\n'
                                              "print(f'Result: {result}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Result: 75.5',
                                             'is_hidden': False}],
                             'title': 'Type Synthesis Challenge',
                             'xp_reward': 150},
                            {'description': 'Your task, step by step:\n1. Create full_name, age, salary, and is_certified with the sample values.\n2. Use an f-string to display: Name: Sarah Connor | Age: 29 | Salary: $75000.5 | Certified: True\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['First, create a variable for each value named in the task.',
                                       'Use print() to display the answer. Put text labels in quotes and '
                                       'variable names without quotes.',
                                       'For a formatted line, put f before the quote and place each variable '
                                       'inside curly braces.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Create full_name, age, salary, and is_certified with the '
                                             'sample values. Use an f-string to display: Name: Sarah Connor '
                                             '| Age: 29 | Salary: $75000.5 | Certified: True',
                             'solution_code': "full_name = 'Sarah Connor'\n"
                                              'age = 29\n'
                                              'salary = 75000.50\n'
                                              'is_certified = True\n'
                                              "print(f'Name: {full_name} | Age: {age} | Salary: ${salary} | "
                                              "Certified: {is_certified}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Name: Sarah Connor | Age: 29 | Salary: '
                                                                '$75000.5 | Certified: True',
                                             'is_hidden': False}],
                             'title': 'World 2 Capstone: Personal Information Management Program',
                             'xp_reward': 50}],
             'description': 'This level brings together World 2 ideas: store values in variables, choose '
                            'useful names, work with numbers and text, check types, and convert text before '
                            'doing math.',
             'lesson': {'common_mistakes': [{'fix': 'Use int() or float()',
                                             'mistake': 'Mixing types without casting',
                                             'why': 'Ensure strings containing digits are cast before '
                                                    'arithmetic.'}],
                        'detailed_explanation': "full_name = 'Sam Lee'\n"
                                                'age = 10\n'
                                                'is_member = True\n'
                                                "print(f'{full_name} is {age}. Member: {is_member}')\n"
                                                '\n'
                                                'The variables keep each piece of information separate. The '
                                                'f-string places their values into one readable sentence. '
                                                "For a calculation, convert text first: `raw_score = '70'` "
                                                'then `score = int(raw_score) + 5` produces 75. Check a '
                                                "value's type when unsure what it contains.",
                        'expected_output': 'User Evelyn is 336 months old.',
                        'introduction': 'This level brings together World 2 ideas: store values in '
                                        'variables, choose useful names, work with numbers and text, check '
                                        'types, and convert text before doing math. Read the requested '
                                        'output and build it from small steps.',
                        'learning_objectives': ['Synthesize all concepts from World 2 into a complete data '
                                                'management program',
                                                'Handle multiple data types: strings, integers, floats, and '
                                                'booleans',
                                                'Complete the World 2 Capstone: Personal Information '
                                                'Management Program'],
                        'line_by_line': [{'line': '1', 'code': "hero_class = 'Mage'", 'explanation': "Store the text 'Mage' in hero_class."}, {'line': '2', 'code': 'mana = 250', 'explanation': 'Store the number 250 in mana.'}, {'line': '3', 'code': 'spell_cost = 45', 'explanation': 'Store the number 45 in spell_cost.'}, {'line': '4', 'code': 'mana -= spell_cost', 'explanation': 'Subtract spell_cost from mana and save the new value back in mana.'}, {'line': '5', 'code': "print('Class:', hero_class, '| Remaining Mana:', mana)", 'explanation': "Show the text 'Class:', followed by the current value of hero_class, followed by the text '| Remaining Mana:', followed by the current value of mana. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: RPG Hero Character Sheet',
                                                'code': "hero_class = 'Mage'\n"
                                                        'mana = 250\n'
                                                        'spell_cost = 45\n'
                                                        'mana -= spell_cost\n'
                                                        "print('Class:', hero_class, '| Remaining Mana:', "
                                                        'mana)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Class: Mage | Remaining Mana: 205'},
                                               {'title': 'Example 2: Warehouse inventory valuation',
                                                'code': "sku = 'W-104'\n"
                                                        'unit_cost = 12.50\n'
                                                        'quantity = 80\n'
                                                        'total_value = unit_cost * quantity\n'
                                                        "print('SKU:', sku, '| Total Stock Value: $', "
                                                        'total_value)',
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'SKU: W-104 | Total Stock Value: $ 1000.0'},
                                               {'title': 'Example 3: Flight telemetry cockpit monitor',
                                                'code': "callsign = 'Aero-7'\n"
                                                        'altitude_meters = 10500\n'
                                                        'airspeed_kmh = 880.4\n'
                                                        "print('Callsign:', callsign, '| Alt:', "
                                                        "altitude_meters, 'm | Speed:', airspeed_kmh, "
                                                        "'km/h')",
                                                'explanation': 'The first lines store information. The '
                                                               'print() lines show that information on the '
                                                               'screen. Run the complete code and compare '
                                                               'what you see with the expected output.',
                                                'output': 'Callsign: Aero-7 | Alt: 10500 m | Speed: 880.4 '
                                                          'km/h'}],
                        'practice_questions': ['What are the four core primitive data types in Python?',
                                               'How do f-strings streamline multi-variable reporting?'],
                        'prerequisites': 'No prior Python knowledge is needed.',
                        'real_world_apps': 'User profile management systems in web portals and enterprise '
                                           'directory software.',
                        'summary': "full_name = 'Sam Lee'\n"
                                   'age = 10\n'
                                   'is_member = True\n'
                                   "print(f'{full_name} is {age}. Member: {is_member}')",
                        'syntax_breakdown': '# World 2 Capstone: Personal Information Management System\n'
                                            "full_name = 'Sarah Connor'\n"
                                            'age = 29\n'
                                            'salary = 75000.50\n'
                                            'is_certified = True\n'
                                            '\n'
                                            "print('=== EMPLOYEE DOSSIER ===')\n"
                                            "print('Name:', full_name)\n"
                                            "print('Age Next Year:', age + 1)\n"
                                            "print('Monthly Rate: $', round(salary / 12, 2))\n"
                                            "print('Certified:', is_certified)",
                        'terminology': [{'definition': 'A collection of related attributes describing an '
                                                       'entity such as a person, user, or product.',
                                         'term': 'Data Record'}],
                        'title': 'World 2 Examination'},
             'number': 21,
             'quizzes': [{'explanation': "f-strings embed expressions inside curly braces: f'Items: {items} "
                                         "| Total: ${total}'.",
                          'options': [{'explanation': 'Correct! The f prefix and curly braces format both '
                                                      'variables properly.',
                                       'is_correct': True,
                                       'text': "items = 5; total = 25.0; print(f'Items: {items} | Total: "
                                               "${total}')"},
                                      {'explanation': "Incorrect. Missing the 'f' prefix prints the curly "
                                                      'braces literally.',
                                       'is_correct': False,
                                       'text': "items = 5; total = 25.0; print('Items: {items} | Total: "
                                               "${total}')"},
                                      {'explanation': 'Incorrect. Missing curly braces around variable '
                                                      'names.',
                                       'is_correct': False,
                                       'text': "items = 5; total = 25.0; print(f'Items: items | Total: "
                                               "$total')"},
                                      {'explanation': 'Incorrect. Concatenating strings with ints/floats '
                                                      'raises a TypeError.',
                                       'is_correct': False,
                                       'text': "items = 5; total = 25.0; print('Items: ' + items + ' | "
                                               "Total: $' + total)"}],
                          'question': "Which of the following lines correctly outputs: 'Items: 5 | Total: "
                                      "$25.0' using an f-string?"},
                         {'explanation': '15 > 8 evaluates to True, which is a bool. type(True) is <class '
                                         "'bool'>.",
                          'options': [{'explanation': 'Correct! The comparison produces a boolean value, '
                                                      'whose type is bool.',
                                       'is_correct': True,
                                       'text': "<class 'bool'>"},
                                      {'explanation': 'Incorrect. Comparisons produce booleans, not '
                                                      'integers.',
                                       'is_correct': False,
                                       'text': "<class 'int'>"},
                                      {'explanation': 'Incorrect. type() outputs the type object, not the '
                                                      'boolean value itself.',
                                       'is_correct': False,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect. In Python, print(type(...)) formats as '
                                                      "<class 'bool'>.",
                                       'is_correct': False,
                                       'text': 'bool'}],
                          'question': 'What is the output of running this code?\n'
                                      '\n'
                                      'result = type(15 > 8)\n'
                                      'print(result)'}],
             'title': 'World 2 Examination'}],
 'number': 2,
 'title': 'Variables and Data Types'}
