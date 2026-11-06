"""
Curriculum module: WORLD_3
World 3 lessons and practice challenges.
"""

WORLD_3 = {'description': 'Learn to collect user answers, convert number text, calculate with operators, compare '
                'values, and combine True/False conditions.',
 'final_project_desc': 'Build a command-line calculator that takes numbers and performs selected arithmetic.',
 'final_project_title': 'Interactive Calculator',
 'goal': 'Build interactive programs that take user input and perform mathematical calculations.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Ask the person to type their name.\n2. Save the answer in name, then display Welcome, followed by their name and an exclamation mark.\n3. If they type Alex, show Welcome, Alex!.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Ask the person to type their name. Save the answer in name, '
                                             'then display Welcome, followed by their name and an '
                                             'exclamation mark. If they type Alex, show Welcome, Alex!.',
                             'solution_code': "name = input()\nprint(f'Welcome, {name}!')",
                             'test_cases': [{'input_data': 'Alex',
                                             'expected_output': 'Welcome, Alex!',
                                             'is_hidden': False},
                                            {'input_data': 'Samira',
                                             'expected_output': 'Welcome, Samira!',
                                             'is_hidden': False}],
                             'title': 'Interactive Welcome',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read one message from input.\n2. Print it twice: first with the label Echo 1: and then with Echo 2:.\n3. Each echo must be on its own line.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read one message from input. Print it twice: first with the '
                                             'label Echo 1: and then with Echo 2:. Each echo must be on its '
                                             'own line.',
                             'solution_code': 'message = input()\n'
                                              "print(f'Echo 1: {message}')\n"
                                              "print(f'Echo 2: {message}')",
                             'test_cases': [{'input_data': 'Hello World',
                                             'expected_output': 'Echo 1: Hello World\nEcho 2: Hello World',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Echo Chamber',
                             'xp_reward': 150}],
             'description': "A program can ask you for information while it runs Python's `input()` pauses "
                            'and waits for a person to type a line and press Enter',
             'lesson': {'common_mistakes': [{'mistake': 'Forgetting to save the answer',
                                             'why': 'Without a variable, your program cannot easily use the '
                                                    'typed answer later.',
                                             'fix': 'Write name = input() and use name in the next line.'}],
                        'detailed_explanation': 'Try this complete program:\n'
                                                "name = input('What is your name? ')\n"
                                                "print(f'Welcome, {name}!')\n"
                                                '\n'
                                                'Python shows the question and waits. If the person types '
                                                'Alex and presses Enter, input() gives the text Alex back. '
                                                'The assignment stores it in name. The f-string puts that '
                                                'saved answer into the welcome message.\n'
                                                '\n'
                                                '`input()` always gives back text, even if the person types '
                                                'digits. This level uses text answers. The next level shows '
                                                'how to turn digit text into a number for math.',
                        'expected_output': 'What is your name? Alex\nWelcome, Alex!',
                        'introduction': "A program can ask you for information while it runs. Python's "
                                        '`input()` pauses and waits for a person to type a line and press '
                                        "Enter. The text inside `input('Your name: ')` is a prompt: it tells "
                                        'the person what to type. The answer is saved in a variable so the '
                                        'program can use it.',
                        'learning_objectives': ['Use input() to let a person type an answer',
                                                'Save the answer in a variable',
                                                'Use the saved answer in a message'],
                        'line_by_line': [{'line': '1', 'code': "color = input('Favorite color? ')", 'explanation': "Ask the player to type an answer and store that text in color. The question 'Favorite color? ' appears first so the player knows what to type."}, {'line': '2', 'code': "print(f'You chose {color}.')", 'explanation': 'Build this message, replace each {name} with that variable’s current value, then show the message on the screen.'}],
                        'practical_examples': [{'title': 'Ask for a favorite color',
                                                'code': "color = input('Favorite color? ')\n"
                                                        "print(f'You chose {color}.')",
                                                'explanation': 'If you type blue at the prompt and press '
                                                               'Enter, color stores blue.',
                                                'output': 'You chose blue.'},
                                               {'title': 'Ask for a game name',
                                                'code': "game = input()\nprint(f'Let us play {game}!')",
                                                'explanation': 'If you type Chess and press Enter, game '
                                                               'stores Chess.',
                                                'output': 'Let us play Chess!'}],
                        'practice_questions': ['What does input() wait for?',
                                               'What kind of value does input() return?'],
                        'prerequisites': 'World 2: Variables and Data Types',
                        'real_world_apps': 'Programs use input() for names, search words, messages, and '
                                           'other information typed by a person.',
                        'summary': 'Try this complete program:\n'
                                   "name = input('What is your name? ')\n"
                                   "print(f'Welcome, {name}!')",
                        'syntax_breakdown': "name = input('What is your name? ')\nprint(f'Welcome, {name}!')",
                        'terminology': [{'term': 'input()',
                                         'definition': 'Waits for a person to type a line and press Enter.'},
                                        {'term': 'prompt',
                                         'definition': 'A short message that tells the person what to type.'},
                                        {'term': 'string',
                                         'definition': 'Text, such as the answer returned by input().'}],
                        'title': 'Understanding input()'},
             'number': 22,
             'quizzes': [{'explanation': 'input() always returns a string, even if the user types numeric '
                                         'digits.',
                          'options': [{'explanation': 'Correct! input() always yields a string.',
                                       'is_correct': True,
                                       'text': "<class 'str'>"},
                                      {'explanation': 'Incorrect. input() never automatically converts to '
                                                      'int.',
                                       'is_correct': False,
                                       'text': "<class 'int'>"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "<class 'float'>"},
                                      {'explanation': 'Incorrect. type() outputs the type object.',
                                       'is_correct': False,
                                       'text': '50'}],
                          'question': 'Given the code:\n'
                                      '\n'
                                      '# User enters 50 at prompt\n'
                                      "x = input('Enter a number: ')\n"
                                      'print(type(x))\n'
                                      '\n'
                                      'What is printed to the terminal?'},
                         {'explanation': "Because x is a string ('7'), multiplying by 2 repeats the string "
                                         "into '77'.",
                          'options': [{'explanation': "Correct! String repetition produces '77'.",
                                       'is_correct': True,
                                       'text': '77'},
                                      {'explanation': 'Incorrect. Numeric multiplication requires converting '
                                                      'to int first.',
                                       'is_correct': False,
                                       'text': '14'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '49'},
                                      {'explanation': 'Incorrect. Multiplying a string by an integer is '
                                                      'legal in Python.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What will this code output if the user types 7 at the prompt?\n'
                                      '\n'
                                      'x = input()\n'
                                      'print(x * 2)'}],
             'title': 'Understanding input()'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a city on the first line and a country on the second line.\n2. Display them together in this format: Location: Kyoto, Japan.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read a city on the first line and a country on the second '
                                             'line. Display them together in this format: Location: Kyoto, '
                                             'Japan.',
                             'solution_code': 'city = input()\n'
                                              'country = input()\n'
                                              "print(f'Location: {city}, {country}')",
                             'test_cases': [{'input_data': 'Kyoto\nJapan',
                                             'expected_output': 'Location: Kyoto, Japan',
                                             'is_hidden': False}],
                             'title': 'City and Country Registry',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read a hero name, a hero class, and a guild name on three separate lines.\n2. Print a four-line card with the heading === GUILD ROSTER ===, then Hero:, Class:, and Guild: with the supplied answers.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read a hero name, a hero class, and a guild name on three '
                                             'separate lines. Print a four-line card with the heading === '
                                             'GUILD ROSTER ===, then Hero:, Class:, and Guild: with the '
                                             'supplied answers.',
                             'solution_code': 'name = input()\n'
                                              'hero_class = input()\n'
                                              'guild = input()\n'
                                              "print('=== GUILD ROSTER ===')\n"
                                              "print(f'Hero: {name}')\n"
                                              "print(f'Class: {hero_class}')\n"
                                              "print(f'Guild: {guild}')",
                             'test_cases': [{'input_data': 'Kaelen\nMage\nSilverhand',
                                             'expected_output': '=== GUILD ROSTER ===\n'
                                                                'Hero: Kaelen\n'
                                                                'Class: Mage\n'
                                                                'Guild: Silverhand',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Hero Character Card',
                             'xp_reward': 150}],
             'description': 'A program can ask for several answers, one after another Each call to `input()` '
                            'reads one line',
             'lesson': {'common_mistakes': [{'mistake': 'Reading answers in the wrong order',
                                             'why': 'The first input() receives the first line typed.',
                                             'fix': 'Ask for and save each answer in the same order as the '
                                                    'task.'}],
                        'detailed_explanation': 'Complete example:\n'
                                                'city = input()\n'
                                                'country = input()\n'
                                                "print(f'Location: {city}, {country}')\n"
                                                '\n'
                                                'The program waits for the first line and stores it in city. '
                                                'Then it waits for a second line and stores it in country. '
                                                'If the person types Kyoto, presses Enter, then types Japan '
                                                'and presses Enter, the output is Location: Kyoto, Japan.\n'
                                                '\n'
                                                'Order matters: first input() gets the first answer, and the '
                                                'next input() gets the next answer. Use a clear variable '
                                                'name for each answer.',
                        'expected_output': 'Kyoto\nJapan\nLocation: Kyoto, Japan',
                        'introduction': 'A program can ask for several answers, one after another. Each call '
                                        'to `input()` reads one line. Save each answer in its own variable '
                                        'so you can tell which answer is the city and which is the country.',
                        'learning_objectives': ['Read more than one answer in order',
                                                'Store each answer in a separate variable',
                                                'Use the right answer in the output'],
                        'line_by_line': [{'line': '1', 'code': 'first = input()', 'explanation': 'Ask the player to type an answer and store that text in first.'}, {'line': '2', 'code': 'last = input()', 'explanation': 'Ask the player to type an answer and store that text in last.'}, {'line': '3', 'code': "print(f'Hello, {first} {last}!')", 'explanation': 'Build this message, replace each {name} with that variable’s current value, then show the message on the screen.'}],
                        'practical_examples': [{'title': 'Ask for a first and last name',
                                                'code': 'first = input()\n'
                                                        'last = input()\n'
                                                        "print(f'Hello, {first} {last}!')",
                                                'explanation': 'Type Mia on the first line and Patel on the '
                                                               'second line. Each answer goes into its own '
                                                               'variable.',
                                                'output': 'Hello, Mia Patel!'},
                                               {'title': 'Ask for a menu choice and quantity',
                                                'code': 'item = input()\n'
                                                        'quantity = input()\n'
                                                        "print(f'{quantity} {item}(s)')",
                                                'explanation': 'Type apple, then 3 on the next line. The '
                                                               'program keeps the item and quantity '
                                                               'separate.',
                                                'output': '3 apple(s)'}],
                        'practice_questions': ['How does Python get the second answer?',
                                               'Why should city and country use separate variables?'],
                        'prerequisites': 'World 3: Understanding input()',
                        'real_world_apps': 'Sign-up forms, surveys, and checkout screens ask several '
                                           'questions and save each answer separately.',
                        'summary': 'Complete example:\n'
                                   'city = input()\n'
                                   'country = input()\n'
                                   "print(f'Location: {city}, {country}')",
                        'syntax_breakdown': 'city = input()\n'
                                            'country = input()\n'
                                            "print(f'Location: {city}, {country}')",
                        'terminology': [{'term': 'input line',
                                         'definition': 'One answer typed before pressing Enter.'},
                                        {'term': 'variable', 'definition': 'A name that stores an answer.'},
                                        {'term': 'order',
                                         'definition': 'The sequence in which the program asks for '
                                                       'answers.'}],
                        'title': 'Reading Multiple Inputs'},
             'number': 23,
             'quizzes': [{'question': 'A person types Kyoto, presses Enter, then types Japan and presses '
                                      'Enter. What will this program display?\n'
                                      '\n'
                                      'city = input()\n'
                                      'country = input()\n'
                                      "print(f'Location: {city}, {country}')",
                          'explanation': 'The first input line is stored in city and the second in country. '
                                         'The f-string places both answers in the message.',
                          'options': [{'text': 'Location: Kyoto, Japan',
                                       'is_correct': True,
                                       'explanation': 'Correct! The answers go into the matching variables '
                                                      'in order.'},
                                      {'text': 'Location: Japan, Kyoto',
                                       'is_correct': False,
                                       'explanation': 'The first answer is stored in city, so the order is '
                                                      'Kyoto then Japan.'},
                                      {'text': 'Location: city, country',
                                       'is_correct': False,
                                       'explanation': 'Inside an f-string, braces insert the values stored '
                                                      'in the variables.'},
                                      {'text': 'The program only reads one answer',
                                       'is_correct': False,
                                       'explanation': 'Each input() call reads one line, so this program '
                                                      'reads two.'}]},
                         {'question': 'Why should a program use separate variables when it asks for a city '
                                      'and a country?',
                          'explanation': 'A variable name helps the program remember what each answer means.',
                          'options': [{'text': 'So it can remember which answer is the city and which is the '
                                               'country',
                                       'is_correct': True,
                                       'explanation': 'Correct! Clear names help you use each answer in the '
                                                      'right place.'},
                                      {'text': 'Because input() can only be used once',
                                       'is_correct': False,
                                       'explanation': 'input() can be used as many times as needed.'},
                                      {'text': 'So Python will automatically translate the answers',
                                       'is_correct': False,
                                       'explanation': 'Variables store the answers; they do not translate '
                                                      'them.'},
                                      {'text': 'Because variables turn text into numbers',
                                       'is_correct': False,
                                       'explanation': 'Variables store values. Use int() or float() to '
                                                      'convert number text.'}]}],
             'title': 'Reading Multiple Inputs'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read an age as a whole number.\n2. Display the age it will be next year.\n3. If the person types 19, display\n4. Next year you will be 20.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read an age as a whole number. Display the age it will be next '
                                             'year. If the person types 19, display Next year you will be '
                                             '20.',
                             'solution_code': "age = int(input())\nprint(f'Next year you will be {age + 1}')",
                             'test_cases': [{'input_data': '19',
                                             'expected_output': 'Next year you will be 20',
                                             'is_hidden': False}],
                             'title': 'Age Next Year',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read two whole numbers on separate lines.\n2. Multiply them and display the answer with the label Product:.\n3. For inputs 7 and 8, display Product: 56.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read two whole numbers on separate lines. Multiply them and '
                                             'display the answer with the label Product:. For inputs 7 and '
                                             '8, display Product: 56.',
                             'solution_code': 'n1 = int(input())\n'
                                              'n2 = int(input())\n'
                                              "print(f'Product: {n1 * n2}')",
                             'test_cases': [{'input_data': '7\n8',
                                             'expected_output': 'Product: 56',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Two-Number Multiplier',
                             'xp_reward': 150}],
             'description': 'An answer from `input()` is text If someone types 20, Python receives the text '
                            "'20', not the number 20",
             'lesson': {'common_mistakes': [{'mistake': 'Trying to add 1 to input() directly',
                                             'why': 'The answer is text, and text is not a number for '
                                                    'arithmetic.',
                                             'fix': 'Use int(input()) for a whole number or float(input()) '
                                                    'for a decimal.'}],
                        'detailed_explanation': 'Example with a whole number:\n'
                                                'age = int(input())\n'
                                                "print(f'Next year you will be {age + 1}')\n"
                                                '\n'
                                                "If the person types 19, input() first reads the text '19'. "
                                                'int() changes it to the number 19. Python can add 1, so it '
                                                'prints Next year you will be 20.\n'
                                                '\n'
                                                'Example with a decimal:\n'
                                                'price = float(input())\n'
                                                'print(price)\n'
                                                '\n'
                                                'If the person types 2.50, float() makes it a decimal '
                                                'number. Use int() for counts and ages; use float() for '
                                                'prices or measurements that can include a decimal. The '
                                                'typed answer must look like a number or Python reports an '
                                                'error.',
                        'expected_output': '19\nNext year you will be 20',
                        'introduction': 'An answer from `input()` is text. If someone types 20, Python '
                                        "receives the text '20', not the number 20. To calculate with it, "
                                        'wrap input() in `int()` for a whole number or `float()` for a '
                                        'number that may have a decimal part.',
                        'learning_objectives': ['Explain why input() returns text',
                                                'Use int() to convert whole-number text',
                                                'Use float() to convert decimal text before calculating'],
                        'line_by_line': [{'line': '1', 'code': 'age = int(input())', 'explanation': 'Ask the player to type an answer, convert that text into a whole number, and store it in age.'}, {'line': '2', 'code': 'print(age + 1)', 'explanation': 'Work out age + 1, then show the answer on the screen.'}],
                        'practical_examples': [{'title': 'Convert a typed age',
                                                'code': 'age = int(input())\nprint(age + 1)',
                                                'explanation': 'Type 20 and press Enter. int() makes it a '
                                                               'number, so adding one gives 21.',
                                                'output': '21'},
                                               {'title': 'Convert a typed price',
                                                'code': 'price = float(input())\nprint(price * 2)',
                                                'explanation': 'Type 2.5 and press Enter. float() keeps the '
                                                               'decimal, then Python doubles it.',
                                                'output': '5.0'}],
                        'practice_questions': ['What does int() do to digit text?',
                                               'When is float() useful?'],
                        'prerequisites': 'World 3: Reading Multiple Inputs',
                        'real_world_apps': 'Calculators and forms convert typed numbers before adding '
                                           'prices, counting items, or calculating ages.',
                        'summary': 'Example with a whole number:\n'
                                   'age = int(input())\n'
                                   "print(f'Next year you will be {age + 1}')",
                        'syntax_breakdown': "age = int(input())\nprint(f'Next year you will be {age + 1}')",
                        'terminology': [{'term': 'int()',
                                         'definition': 'Converts suitable text or another number to a whole '
                                                       'number.'},
                                        {'term': 'float()',
                                         'definition': 'Converts suitable text or another number to a '
                                                       'decimal number.'},
                                        {'term': 'conversion',
                                         'definition': 'Changing a value from one type to another.'}],
                        'title': 'Understanding int() and float()'},
             'number': 24,
             'quizzes': [{'explanation': "input() returns '4'. Multiplying string '4' by 3 gives '444'.",
                          'options': [{'explanation': "Correct! String repetition repeats '4' three times.",
                                       'is_correct': True,
                                       'text': '444'},
                                      {'explanation': 'Incorrect. val is a string, not an integer.',
                                       'is_correct': False,
                                       'text': '12'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '64'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the result of running val = input(); print(val * 3) if the '
                                      'user types 4?'},
                         {'explanation': 'float(input()) converts user input to a decimal number, allowing '
                                         'multiplication with 0.10.',
                          'options': [{'explanation': 'Correct! float(input()) safely parses decimal values.',
                                       'is_correct': True,
                                       'text': 'price = float(input()); print(price * 0.10)'},
                                      {'explanation': 'Incorrect. Cannot multiply a string by a float.',
                                       'is_correct': False,
                                       'text': 'price = input(); print(price * 0.10)'},
                                      {'explanation': 'Incorrect. int() will crash if the user enters '
                                                      "decimals like '19.99'.",
                                       'is_correct': False,
                                       'text': 'price = int(input()); print(price * 0.10)'},
                                      {'explanation': 'Incorrect syntax.',
                                       'is_correct': False,
                                       'text': 'price = input(float) * 0.10'}],
                          'question': 'Which code snippet correctly reads a decimal price from the user and '
                                      'calculates 10% tax?'}],
             'title': 'Understanding int() and float()'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read two whole numbers a and b.\n2. Display the whole-number quotient a // b on the first line and the remainder a % b on the second.\n3. For 29 and 6, show Quotient: 4, then Remainder: 5.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read two whole numbers a and b. Display the whole-number '
                                             'quotient a // b on the first line and the remainder a % b on '
                                             'the second. For 29 and 6, show Quotient: 4, then Remainder: 5.',
                             'solution_code': 'a = int(input())\n'
                                              'b = int(input())\n'
                                              "print(f'Quotient: {a // b}')\n"
                                              "print(f'Remainder: {a % b}')",
                             'test_cases': [{'input_data': '29\n6',
                                             'expected_output': 'Quotient: 4\nRemainder: 5',
                                             'is_hidden': False}],
                             'title': 'Quotient and Remainder',
                             'xp_reward': 30},
                            {'description': "Your task, step by step:\n1. Read base, exponent, and modulus as whole numbers on separate lines.\n2. Calculate base ** exponent, then find that answer's remainder when divided by modulus.\n3. Print Power: and Remainder: on separate lines.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.",
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read base, exponent, and modulus as whole numbers on separate '
                                             "lines. Calculate base ** exponent, then find that answer's "
                                             'remainder when divided by modulus. Print Power: and Remainder: '
                                             'on separate lines.',
                             'solution_code': 'base = int(input())\n'
                                              'exponent = int(input())\n'
                                              'modulus = int(input())\n'
                                              'power = base ** exponent\n'
                                              "print(f'Power: {power}')\n"
                                              "print(f'Remainder: {power % modulus}')",
                             'test_cases': [{'input_data': '3\n4\n5',
                                             'expected_output': 'Power: 81\nRemainder: 1',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Power and Modulo',
                             'xp_reward': 150}],
             'description': 'Python can do arithmetic with numbers The main symbols are `+` add, `-` '
                            'subtract, `*` multiply, `/` divide, `//` divide into whole groups, `%` find '
                            'what is left over, and `**` raise a number to a power',
             'lesson': {'common_mistakes': [{'mistake': 'Using / when you need a whole-group count',
                                             'why': '/ can return a decimal.',
                                             'fix': 'Use // for the number of whole groups and % for what '
                                                    'remains.'}],
                        'detailed_explanation': 'Complete example:\n'
                                                'a = 17\n'
                                                'b = 5\n'
                                                'print(a + b)\n'
                                                'print(a // b)\n'
                                                'print(a % b)\n'
                                                '\n'
                                                'The answers are 22, 3, and 2. `17 // 5` asks how many full '
                                                'groups of 5 fit in 17. Three groups fit. `17 % 5` asks what '
                                                'remains, which is 2.\n'
                                                '\n'
                                                'More examples: `6 * 4` gives 24, `8 / 2` gives 4.0, and `2 '
                                                '** 3` gives 8. Division with / can produce a decimal. Floor '
                                                'division // gives the whole-number quotient.',
                        'expected_output': '22\n3\n2',
                        'introduction': 'Python can do arithmetic with numbers. The main symbols are `+` '
                                        'add, `-` subtract, `*` multiply, `/` divide, `//` divide into whole '
                                        'groups, `%` find what is left over, and `**` raise a number to a '
                                        'power. Use the symbol that matches the calculation you need.',
                        'learning_objectives': ['Recognize the arithmetic symbols',
                                                'Use // to find the whole-number quotient',
                                                'Use % to find a remainder'],
                        'line_by_line': [{'line': '1', 'code': 'a = int(input())', 'explanation': 'Ask the player to type an answer, convert that text into a whole number, and store it in a.'}, {'line': '2', 'code': 'b = int(input())', 'explanation': 'Ask the player to type an answer, convert that text into a whole number, and store it in b.'}, {'line': '3', 'code': 'print(a + b)', 'explanation': 'Work out a + b, then show the answer on the screen.'}],
                        'practical_examples': [{'title': 'Add two typed numbers',
                                                'code': 'a = int(input())\nb = int(input())\nprint(a + b)',
                                                'explanation': 'Convert each answer to a whole number, then '
                                                               'add them.',
                                                'output': '15'},
                                               {'title': 'Find full groups and what remains',
                                                'code': 'print(17 // 5)\nprint(17 % 5)',
                                                'explanation': 'Three groups of five fit in 17, with two '
                                                               'left over.',
                                                'output': '3\n2'}],
                        'practice_questions': ['What does % find?',
                                               'What is the difference between / and //?'],
                        'prerequisites': 'World 3: Understanding int() and float()',
                        'real_world_apps': 'Arithmetic operators are used in calculators, shopping totals, '
                                           'game scores, and splitting objects into equal groups.',
                        'summary': 'Complete example:\n'
                                   'a = 17\n'
                                   'b = 5\n'
                                   'print(a + b)\n'
                                   'print(a // b)\n'
                                   'print(a % b)',
                        'syntax_breakdown': 'a = 17\nb = 5\nprint(a + b)\nprint(a // b)\nprint(a % b)',
                        'terminology': [{'term': 'operator',
                                         'definition': 'A symbol that tells Python what calculation to do.'},
                                        {'term': 'quotient',
                                         'definition': 'The answer to a division calculation.'},
                                        {'term': 'remainder',
                                         'definition': 'What is left after making whole groups.'}],
                        'title': 'Arithmetic Operators'},
             'number': 25,
             'quizzes': [{'explanation': 'The modulo operator (%) returns the remainder of division. 15 / 4 '
                                         'is 3 with remainder 3.',
                          'options': [{'explanation': 'Correct! 15 = 4 * 3 + 3.',
                                       'is_correct': True,
                                       'text': '3'},
                                      {'explanation': 'Incorrect. Modulo returns the remainder, not the '
                                                      'float quotient.',
                                       'is_correct': False,
                                       'text': '3.75'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '1'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '0'}],
                          'question': 'What is the value of 15 % 4 in Python?'},
                         {'explanation': '** is the exponentiation operator in Python. 2 ** 5 = 32.',
                          'options': [{'explanation': 'Correct! 2 ** 5 = 32.',
                                       'is_correct': True,
                                       'text': '32'},
                                      {'explanation': 'Incorrect. 2 * 5 = 10, but ** is exponentiation.',
                                       'is_correct': False,
                                       'text': '10'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '25'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '64'}],
                          'question': 'What is the output of print(2 ** 5) in Python?'}],
             'title': 'Arithmetic Operators'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a starting score.\n2. Add 5 to the score using +=, then display Score: followed by the new value.\n3. For input 10, show Score: 15.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read a starting score. Add 5 to the score using +=, then '
                                             'display Score: followed by the new value. For input 10, show '
                                             'Score: 15.',
                             'solution_code': "score = int(input())\nscore += 5\nprint(f'Score: {score}')",
                             'test_cases': [{'input_data': '10',
                                             'expected_output': 'Score: 15',
                                             'is_hidden': False}],
                             'title': 'Score Update',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read x as a whole number.\n2. In order, add 10 using +=, multiply by 2 using *=, then subtract 5 using -=.\n3. Display Accumulated: followed by the final value.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read x as a whole number. In order, add 10 using +=, multiply '
                                             'by 2 using *=, then subtract 5 using -=. Display Accumulated: '
                                             'followed by the final value.',
                             'solution_code': 'x = int(input())\n'
                                              'x += 10\n'
                                              'x *= 2\n'
                                              'x -= 5\n'
                                              "print(f'Accumulated: {x}')",
                             'test_cases': [{'input_data': '5',
                                             'expected_output': 'Accumulated: 25',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Step Accumulator',
                             'xp_reward': 150}],
             'description': 'An assignment operator updates a variable and saves the new value For example, '
                            '`score += 5` means add 5 to score and keep the answer in score',
             'lesson': {'common_mistakes': [{'mistake': 'Thinking += creates a second variable',
                                             'why': '+= changes the variable that is already on its left.',
                                             'fix': 'Read it as: calculate with the current value, then save '
                                                    'the answer back.'}],
                        'detailed_explanation': 'Complete example:\n'
                                                'score = 10\n'
                                                'score += 5\n'
                                                'score *= 2\n'
                                                'print(score)\n'
                                                '\n'
                                                'First score is 10. `score += 5` changes it to 15. `score *= '
                                                '2` changes the current 15 to 30. The output is 30. Each '
                                                'shortcut uses the current value, does the calculation, and '
                                                'stores the answer back in the same variable.\n'
                                                '\n'
                                                'Other shortcuts include `-=`, `/=`, `//=`, `%=`, and `**=`. '
                                                'The order matters because every step updates the value used '
                                                'by the next step.',
                        'expected_output': '30',
                        'introduction': 'An assignment operator updates a variable and saves the new value. '
                                        'For example, `score += 5` means add 5 to score and keep the answer '
                                        'in score. This is a shorter way to write `score = score + 5`. '
                                        'Python has similar shortcuts for subtracting, multiplying, and '
                                        'dividing.',
                        'learning_objectives': ['Use +=, -=, and *= to update a variable',
                                                'Understand that each step saves a new value',
                                                'Follow updates in the order they happen'],
                        'line_by_line': [{'line': '1', 'code': 'points = 10', 'explanation': 'Store the number 10 in points.'}, {'line': '2', 'code': 'points += 4', 'explanation': 'Add 4 to points and save the new value back in points.'}, {'line': '3', 'code': 'print(points)', 'explanation': 'Work out points, then show the answer on the screen.'}],
                        'practical_examples': [{'title': 'Add points to a score',
                                                'code': 'points = 10\npoints += 4\nprint(points)',
                                                'explanation': '+= adds to the current score and saves the '
                                                               'updated value.',
                                                'output': '14'},
                                               {'title': 'Update a number twice',
                                                'code': 'number = 6\nnumber *= 2\nnumber -= 3\nprint(number)',
                                                'explanation': 'First number becomes 12, then becomes 9. '
                                                               'Each line uses the latest value.',
                                                'output': '9'}],
                        'practice_questions': ['What does points += 2 mean?',
                                               'Why does the order of updates matter?'],
                        'prerequisites': 'World 3: Arithmetic Operators',
                        'real_world_apps': 'Programs update totals, balances, scores, and counters as events '
                                           'happen.',
                        'summary': 'Complete example:\nscore = 10\nscore += 5\nscore *= 2\nprint(score)',
                        'syntax_breakdown': 'score = 10\nscore += 5\nscore *= 2\nprint(score)',
                        'terminology': [{'term': 'assignment',
                                         'definition': 'Storing a value in a variable.'},
                                        {'term': 'compound assignment',
                                         'definition': 'A shortcut that calculates and updates the same '
                                                       'variable.'},
                                        {'term': 'current value',
                                         'definition': 'The value stored in the variable right now.'}],
                        'title': 'Assignment Operators'},
             'number': 26,
             'quizzes': [{'explanation': 'n //= 4 is equivalent to n = n // 4. 10 // 4 is 2 (floor '
                                         'division).',
                          'options': [{'explanation': 'Correct! 10 // 4 = 2.',
                                       'is_correct': True,
                                       'text': '2'},
                                      {'explanation': 'Incorrect. Floor division // discards decimals.',
                                       'is_correct': False,
                                       'text': '2.5'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '4'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '0'}],
                          'question': 'If n = 10, what is the value of n after executing n //= 4?'},
                         {'explanation': 'x =+ 5 assigns the positive unary number +5 to x; it is not '
                                         'compound addition +=.',
                          'options': [{'explanation': 'Correct! The operator is +=, not =+.',
                                       'is_correct': True,
                                       'text': 'x =+ 5'},
                                      {'explanation': 'Valid compound addition.',
                                       'is_correct': False,
                                       'text': 'x += 5'},
                                      {'explanation': 'Valid compound multiplication.',
                                       'is_correct': False,
                                       'text': 'x *= 2'},
                                      {'explanation': 'Valid compound subtraction.',
                                       'is_correct': False,
                                       'text': 'x -= 3'}],
                          'question': 'Which of the following lines is invalid syntax for compound '
                                      'assignment in Python?'}],
             'title': 'Assignment Operators'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a whole number n.\n2. Use a comparison to check whether it is between 10 and 50, including both endpoints.\n3. Display True if it is in that range, otherwise display False.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read a whole number n. Use a comparison to check whether it is '
                                             'between 10 and 50, including both endpoints. Display True if '
                                             'it is in that range, otherwise display False.',
                             'solution_code': 'n = int(input())\nprint(10 <= n <= 50)',
                             'test_cases': [{'input_data': '25',
                                             'expected_output': 'True',
                                             'is_hidden': False},
                                            {'input_data': '8',
                                             'expected_output': 'False',
                                             'is_hidden': False},
                                            {'input_data': '50',
                                             'expected_output': 'True',
                                             'is_hidden': False}],
                             'title': 'Inclusive Range Check',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read a score as a whole number.\n2. On separate lines, display Pass: and whether the score is at least 50, then Perfect: and whether the score equals 100.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read a score as a whole number. On separate lines, display '
                                             'Pass: and whether the score is at least 50, then Perfect: and '
                                             'whether the score equals 100.',
                             'solution_code': 'score = int(input())\n'
                                              "print(f'Pass: {score >= 50}')\n"
                                              "print(f'Perfect: {score == 100}')",
                             'test_cases': [{'input_data': '75',
                                             'expected_output': 'Pass: True\nPerfect: False',
                                             'is_hidden': False},
                                            {'input_data': '100',
                                             'expected_output': 'Pass: True\nPerfect: True',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Score Boundary Checks',
                             'xp_reward': 150}],
             'description': 'A comparison checks how two values relate and gives the answer `True` or '
                            '`False` Use `==` to check if values are equal, `!=` for not equal, and `<`, '
                            '`>`, `<=`, or `>=` to compare size',
             'lesson': {'common_mistakes': [{'mistake': 'Using = to ask a question',
                                             'why': 'A single equals sign stores a value instead of '
                                                    'comparing.',
                                             'fix': 'Use == for equality checks.'}],
                        'detailed_explanation': 'Complete example:\n'
                                                'score = 75\n'
                                                'print(score >= 50)\n'
                                                'print(score == 100)\n'
                                                '\n'
                                                'The first comparison asks whether 75 is at least 50, so '
                                                'Python prints True. The second asks whether 75 equals 100, '
                                                'so it prints False.\n'
                                                '\n'
                                                'You can chain comparisons to check a range: `10 <= number '
                                                '<= 50` means number is at least 10 and at most 50. The '
                                                'endpoints are included. A comparison does not change the '
                                                'values; it gives a True or False answer.',
                        'expected_output': 'True\nFalse',
                        'introduction': 'A comparison checks how two values relate and gives the answer '
                                        '`True` or `False`. Use `==` to check if values are equal, `!=` for '
                                        'not equal, and `<`, `>`, `<=`, or `>=` to compare size. A single '
                                        '`=` stores a value; two equals signs `==` ask a question.',
                        'learning_objectives': ['Use comparison symbols to ask questions about values',
                                                'Tell == apart from =',
                                                'Understand that comparisons give True or False'],
                        'line_by_line': [{'line': '1', 'code': "password = 'sun'", 'explanation': "Store the text 'sun' in password."}, {'line': '2', 'code': "print(password == 'sun')", 'explanation': "Work out password == 'sun', then show the answer on the screen."}],
                        'practical_examples': [{'title': 'Check whether two values match',
                                                'code': "password = 'sun'\nprint(password == 'sun')",
                                                'explanation': '== asks whether the two pieces of text are '
                                                               'the same.',
                                                'output': 'True'},
                                               {'title': 'Check a number range',
                                                'code': 'age = 12\nprint(10 <= age <= 15)',
                                                'explanation': 'Both ends are included, so ages 10 through '
                                                               '15 pass the check.',
                                                'output': 'True'}],
                        'practice_questions': ['What does >= mean?',
                                               'What kind of answer does a comparison give?'],
                        'prerequisites': 'World 3: Assignment Operators',
                        'real_world_apps': 'Comparisons help programs check age limits, scores, prices, and '
                                           'whether a value is inside a range.',
                        'summary': 'Complete example:\nscore = 75\nprint(score >= 50)\nprint(score == 100)',
                        'syntax_breakdown': 'score = 75\nprint(score >= 50)\nprint(score == 100)',
                        'terminology': [{'term': 'comparison',
                                         'definition': 'A check that asks how values relate.'},
                                        {'term': 'equal to (==)',
                                         'definition': 'Checks whether two values are the same.'},
                                        {'term': 'Boolean', 'definition': 'A True or False answer.'}],
                        'title': 'Comparison Operators'},
             'number': 27,
             'quizzes': [{'explanation': '10 == 20 is False, and 10 != 20 is True.',
                          'options': [{'explanation': 'Correct! a == b is False, a != b is True.',
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
                          'question': 'What is the output of the following comparison code?\n'
                                      '\n'
                                      'a = 10\n'
                                      'b = 20\n'
                                      'print(a == b, a != b)'},
                         {'explanation': '5 != 5 is False (5 is equal to 5), and 10 >= 10 is True.',
                          'options': [{'explanation': 'Correct! 5 != 5 is False, 10 >= 10 is True.',
                                       'is_correct': True,
                                       'text': 'False True'},
                                      {'explanation': 'Incorrect. 5 != 5 is False.',
                                       'is_correct': False,
                                       'text': 'True True'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'False False'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'True False'}],
                          'question': 'What will be printed by: print(5 != 5, 10 >= 10)?'}],
             'title': 'Comparison Operators'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read an age, then read whether the person has a pass as the text True or False.\n2. Display Admitted: True only when the person is at least 18 and has a pass.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read an age, then read whether the person has a pass as the '
                                             'text True or False. Display Admitted: True only when the '
                                             'person is at least 18 and has a pass.',
                             'solution_code': 'age = int(input())\n'
                                              "has_pass = input() == 'True'\n"
                                              "print(f'Admitted: {age >= 18 and has_pass}')",
                             'test_cases': [{'input_data': '20\nTrue',
                                             'expected_output': 'Admitted: True',
                                             'is_hidden': False},
                                            {'input_data': '16\nTrue',
                                             'expected_output': 'Admitted: False',
                                             'is_hidden': False},
                                            {'input_data': '20\nFalse',
                                             'expected_output': 'Admitted: False',
                                             'is_hidden': False}],
                             'title': 'Two-Condition Admission Check',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read three answers as True or False: is_admin, is_vip, and is_banned.\n2. Access is allowed when the person is an admin or VIP and is not banned.\n3. Display Access Granted: followed by True or False.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read three answers as True or False: is_admin, is_vip, and '
                                             'is_banned. Access is allowed when the person is an admin or '
                                             'VIP and is not banned. Display Access Granted: followed by '
                                             'True or False.',
                             'solution_code': "is_admin = input() == 'True'\n"
                                              "is_vip = input() == 'True'\n"
                                              "is_banned = input() == 'True'\n"
                                              'granted = (is_admin or is_vip) and not is_banned\n'
                                              "print(f'Access Granted: {granted}')",
                             'test_cases': [{'input_data': 'True\nFalse\nFalse',
                                             'expected_output': 'Access Granted: True',
                                             'is_hidden': False},
                                            {'input_data': 'False\nTrue\nTrue',
                                             'expected_output': 'Access Granted: False',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Secure Door Access Check',
                             'xp_reward': 150}],
             'description': 'Sometimes a program makes a decision using more than one yes-or-no answer `and` '
                            'means both checks must be True',
             'lesson': {'common_mistakes': [{'mistake': 'Using and when either choice should work',
                                             'why': 'and requires both checks to be True.',
                                             'fix': 'Use or when one of the choices is enough.'}],
                        'detailed_explanation': 'Complete example:\n'
                                                'age = 20\n'
                                                'has_ticket = True\n'
                                                'allowed = age >= 18 and has_ticket\n'
                                                'print(allowed)\n'
                                                '\n'
                                                'The person is at least 18, so the first check is True. They '
                                                'also have a ticket, so the second check is True. With '
                                                '`and`, both must be True; allowed becomes True.\n'
                                                '\n'
                                                'For `or`, one True answer is enough: `has_ticket or '
                                                'is_vip`. For `not`, `not is_banned` is True when is_banned '
                                                'is False. Use parentheses to make a longer decision easier '
                                                'to read.',
                        'expected_output': 'True',
                        'introduction': 'Sometimes a program makes a decision using more than one yes-or-no '
                                        'answer. `and` means both checks must be True. `or` means at least '
                                        'one check must be True. `not` flips an answer: True becomes False, '
                                        'and False becomes True.',
                        'learning_objectives': ['Use and when both conditions must be true',
                                                'Use or when either condition is enough',
                                                'Use not to reverse True and False'],
                        'line_by_line': [{'line': '1', 'code': 'is_adult = True', 'explanation': 'Store True in is_adult. This variable records a yes-or-no answer.'}, {'line': '2', 'code': 'has_ticket = True', 'explanation': 'Store True in has_ticket. This variable records a yes-or-no answer.'}, {'line': '3', 'code': 'print(is_adult and has_ticket)', 'explanation': 'Work out is_adult and has_ticket, then show the answer on the screen.'}],
                        'practical_examples': [{'title': 'Require both conditions',
                                                'code': 'is_adult = True\n'
                                                        'has_ticket = True\n'
                                                        'print(is_adult and has_ticket)',
                                                'explanation': 'and is True only because both answers are '
                                                               'True.',
                                                'output': 'True'},
                                               {'title': 'Allow either choice, unless blocked',
                                                'code': 'has_ticket = False\n'
                                                        'is_vip = True\n'
                                                        'is_banned = False\n'
                                                        'print((has_ticket or is_vip) and not is_banned)',
                                                'explanation': 'VIP is enough for the first check, and not '
                                                               'is_banned is also True.',
                                                'output': 'True'}],
                        'practice_questions': ['When does and return True?', 'What does not False become?'],
                        'prerequisites': 'World 3: Comparison Operators',
                        'real_world_apps': 'Logical operators help combine rules for admission, account '
                                           'access, discounts, and game conditions.',
                        'summary': 'Complete example:\n'
                                   'age = 20\n'
                                   'has_ticket = True\n'
                                   'allowed = age >= 18 and has_ticket\n'
                                   'print(allowed)',
                        'syntax_breakdown': 'age = 20\n'
                                            'has_ticket = True\n'
                                            'allowed = age >= 18 and has_ticket\n'
                                            'print(allowed)',
                        'terminology': [{'term': 'and', 'definition': 'True only when both sides are True.'},
                                        {'term': 'or', 'definition': 'True when at least one side is True.'},
                                        {'term': 'not', 'definition': 'Reverses a Boolean answer.'}],
                        'title': 'Logical Operators'},
             'number': 28,
             'quizzes': [{'explanation': "In Python, 'and' has higher operator precedence than 'or'. So "
                                         'False and False -> False. Then True or False -> True.',
                          'options': [{'explanation': "Correct! 'and' takes precedence: True or (False and "
                                                      'False) -> True.',
                                       'is_correct': True,
                                       'text': 'True'},
                                      {'explanation': "Incorrect. 'and' evaluates before 'or'.",
                                       'is_correct': False,
                                       'text': 'False'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What is the output of: print(True or False and False)?'},
                         {'explanation': '5 > 2 is True, so not True is False. not False is True.',
                          'options': [{'explanation': 'Correct! not (True) -> False, not False -> True.',
                                       'is_correct': True,
                                       'text': 'False True'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'True False'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'True True'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'False False'}],
                          'question': 'What is the output of running: print(not (5 > 2), not False)?'}],
             'title': 'Logical Operators'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read three whole numbers a, b, and c on separate lines.\n2. Calculate (a + b) * c and display Weighted score: followed by the answer.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read three whole numbers a, b, and c on separate lines. '
                                             'Calculate (a + b) * c and display Weighted score: followed by '
                                             'the answer.',
                             'solution_code': 'a = int(input())\n'
                                              'b = int(input())\n'
                                              'c = int(input())\n'
                                              'weighted_score = (a + b) * c\n'
                                              "print(f'Weighted score: {weighted_score}')",
                             'test_cases': [{'input_data': '2\n3\n4',
                                             'expected_output': 'Weighted score: 20',
                                             'is_hidden': False}],
                             'title': 'Weighted Score Calculator',
                             'xp_reward': 30},
                            {'description': "Your task, step by step:\n1. Read x, y, and z as whole numbers.\n2. Calculate x + y * z ** 2 using Python's normal operation order.\n3. Display the answer with the label Result:.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.",
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Estimate an investment using compound interest. Enter the '
                                             'principal, a yearly rate as a decimal (0.05 means 5%), and the '
                                             'number of years, each on a separate line. Calculate principal '
                                             '* (1 + rate) ** years and print Final amount: $ followed by '
                                             'the answer with two decimal places. For 1000, 0.05, and 2, '
                                             'show Final amount: $1102.50.',
                             'solution_code': 'x = int(input())\n'
                                              'y = int(input())\n'
                                              'z = int(input())\n'
                                              'result = x + y * z ** 2\n'
                                              "print(f'Result: {result}')",
                             'test_cases': [{'input_data': '2\n3\n4',
                                             'expected_output': 'Result: 50',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Precedence Verifier',
                             'xp_reward': 150}],
             'description': 'When a calculation has several operations, Python follows a set order so it '
                            'gets the same answer every time Parentheses are done first, then powers, then '
                            'multiplication and division, then addition and subtraction',
             'lesson': {'common_mistakes': [{'mistake': 'Assuming Python always calculates from left to '
                                                        'right',
                                             'why': 'Multiplication and powers have higher priority than '
                                                    'addition.',
                                             'fix': 'Use the operation order or add parentheses to show your '
                                                    'intended order.'}],
                        'detailed_explanation': 'Compare these calculations:\n'
                                                'print(2 + 3 * 4)\n'
                                                'print((2 + 3) * 4)\n'
                                                '\n'
                                                'The first answer is 14 because Python multiplies 3 by 4 '
                                                'before adding 2. The second answer is 20 because the '
                                                'parentheses tell Python to add 2 and 3 first.\n'
                                                '\n'
                                                'A useful order to remember is: parentheses, powers (**), '
                                                'multiplication or division (*, /, //, %), then addition or '
                                                'subtraction (+, -). If two operations have the same '
                                                'priority, Python usually works from left to right. '
                                                'Parentheses can make your intention easier to see.',
                        'expected_output': '14\n20',
                        'introduction': 'When a calculation has several operations, Python follows a set '
                                        'order so it gets the same answer every time. Parentheses are done '
                                        'first, then powers, then multiplication and division, then addition '
                                        'and subtraction. Use parentheses when you want to make the order '
                                        'especially clear.',
                        'learning_objectives': ['Explain why Python follows a calculation order',
                                                'Use parentheses to choose what happens first',
                                                'Work through a mixed calculation step by step'],
                        'line_by_line': [{'line': '1', 'code': 'print(2 + 3 * 4)', 'explanation': 'Work out 2 + 3 * 4, then show the answer on the screen.'}],
                        'practical_examples': [{'title': 'Multiply before adding',
                                                'code': 'print(2 + 3 * 4)',
                                                'explanation': 'Python multiplies first, so it calculates 2 '
                                                               '+ 12.',
                                                'output': '14'},
                                               {'title': 'Use parentheses to add first',
                                                'code': 'print((2 + 3) * 4)',
                                                'explanation': 'Parentheses make Python add 2 and 3 before '
                                                               'multiplying by 4.',
                                                'output': '20'}],
                        'practice_questions': ['What is calculated first in 2 + 3 * 4?',
                                               'How can parentheses change the answer?'],
                        'prerequisites': 'World 3: Logical Operators',
                        'real_world_apps': 'The same calculation rules help calculators, price totals, and '
                                           'formulas produce predictable answers.',
                        'summary': 'Compare these calculations:\nprint(2 + 3 * 4)\nprint((2 + 3) * 4)',
                        'syntax_breakdown': 'print(2 + 3 * 4)\nprint((2 + 3) * 4)',
                        'terminology': [{'term': 'precedence',
                                         'definition': 'The order Python uses to do operations.'},
                                        {'term': 'parentheses',
                                         'definition': 'Marks that tell Python to calculate that part '
                                                       'first.'},
                                        {'term': 'expression',
                                         'definition': 'Numbers and operators that make a calculation.'}],
                        'title': 'Operator Precedence'},
             'number': 29,
             'quizzes': [{'explanation': '(2 + 3) * 4 = 5 * 4 = 20. 2 + 3 * 4 = 2 + 12 = 14.',
                          'options': [{'explanation': 'Correct! Parentheses override multiplication '
                                                      'precedence.',
                                       'is_correct': True,
                                       'text': '20 14'},
                                      {'explanation': 'Incorrect. 3 * 4 is done before + in 2 + 3 * 4.',
                                       'is_correct': False,
                                       'text': '20 20'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '14 14'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '14 20'}],
                          'question': 'What is the output of print((2 + 3) * 4, 2 + 3 * 4)?'},
                         {'explanation': 'Subtraction is left-associative: (10 - 4) - 2 = 4. With '
                                         'parentheses: 10 - 2 = 8.',
                          'options': [{'explanation': 'Correct! Left-associative evaluates to 4; parentheses '
                                                      'evaluate to 8.',
                                       'is_correct': True,
                                       'text': '4 8'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '4 4'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '8 8'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '8 4'}],
                          'question': 'What is the output of: print(10 - 4 - 2, 10 - (4 - 2))?'}],
             'title': 'Operator Precedence'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read two whole numbers and then an operation: add, sub, mul, or power.\n2. Perform that operation and print one clear line showing the calculation and answer.\n3. Example: 12, 8, add should display 12 + 8 = 20.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read two whole numbers and then an operation: add, sub, mul, '
                                             'or power. Perform that operation and print one clear line '
                                             'showing the calculation and answer. Example: 12, 8, add should '
                                             'display 12 + 8 = 20.',
                             'solution_code': 'a = int(input())\n'
                                              'b = int(input())\n'
                                              'operation = input()\n'
                                              "if operation == 'add':\n"
                                              "    print(f'{a} + {b} = {a + b}')\n"
                                              "elif operation == 'sub':\n"
                                              "    print(f'{a} - {b} = {a - b}')\n"
                                              "elif operation == 'mul':\n"
                                              "    print(f'{a} * {b} = {a * b}')\n"
                                              "elif operation == 'power':\n"
                                              "    print(f'{a} ** {b} = {a ** b}')",
                             'test_cases': [{'input_data': '12\n8\nadd',
                                             'expected_output': '12 + 8 = 20',
                                             'is_hidden': False},
                                            {'input_data': '6\n7\nmul',
                                             'expected_output': '6 * 7 = 42',
                                             'is_hidden': False},
                                            {'input_data': '2\n5\npower',
                                             'expected_output': '2 ** 5 = 32',
                                             'is_hidden': False}],
                             'title': 'Interactive Two-Number Calculator',
                             'xp_reward': 50},
                            {'description': 'Your task, step by step:\n1. Estimate an investment using compound interest.\n2. Read principal and rate as decimals, then years as a whole number.\n3. Calculate principal * (1 + rate) ** years and display the result with two digits after the decimal point, labeled Final amount: $.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['First, read each input in the order the task gives it.',
                                       'Save answers in clear variable names. Convert an answer with int() '
                                       'or float() if you need to calculate with it.',
                                       'Use the operator from the lesson, then print the label and answer in '
                                       'the requested format.'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Estimate an investment using compound interest. Read principal '
                                             'and rate as decimals, then years as a whole number. Calculate '
                                             'principal * (1 + rate) ** years and display the result with '
                                             'two digits after the decimal point, labeled Final amount: $.',
                             'solution_code': 'principal = float(input())\n'
                                              'rate = float(input())\n'
                                              'years = int(input())\n'
                                              'amount = principal * (1 + rate) ** years\n'
                                              "print(f'Final amount: ${amount:.2f}')",
                             'test_cases': [{'input_data': '1000\n0.05\n2',
                                             'expected_output': 'Final amount: $1102.50',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Compound Interest Estimator',
                             'xp_reward': 150}],
             'description': 'This review combines the World 3 ideas: ask for answers, convert number text, '
                            'calculate, update values, compare results, and combine True or False checks A '
                            'good program handles one small step at a time and prints a clear result.',
             'lesson': {'common_mistakes': [{'mistake': 'Trying to write the whole program as one '
                                                        'complicated expression',
                                             'why': 'It is hard to spot a wrong step when everything is '
                                                    'mixed together.',
                                             'fix': 'Store answers, convert them, calculate, and display the '
                                                    'result in separate steps.'}],
                        'detailed_explanation': 'Example: a small calculator\n'
                                                'a = int(input())\n'
                                                'b = int(input())\n'
                                                "print(f'Sum: {a + b}')\n"
                                                '\n'
                                                'If the person types 12 and then 8, input() reads each line. '
                                                'int() changes both answers from text to whole numbers. '
                                                'Python adds them, and print() displays Sum: 20.\n'
                                                '\n'
                                                'For a decision, compare a result and combine checks: '
                                                '`passed = score >= 50 and not absent`. First Python checks '
                                                'whether the score is high enough, then whether the person '
                                                'was not absent, then combines the two True or False '
                                                'answers. Keep each line focused on one step.',
                        'expected_output': '12\n8\nSum: 20',
                        'introduction': 'This review combines the World 3 ideas: ask for answers, convert '
                                        'number text, calculate, update values, compare results, and combine '
                                        'True or False checks. A good program handles one small step at a '
                                        'time and prints a clear result.',
                        'learning_objectives': ['Use input() and convert answers for arithmetic',
                                                'Combine the right operators to solve a task',
                                                'Print a clear result for the person using the program'],
                        'line_by_line': [{'line': '1', 'code': 'a = int(input())', 'explanation': 'Ask the player to type an answer, convert that text into a whole number, and store it in a.'}, {'line': '2', 'code': 'b = int(input())', 'explanation': 'Ask the player to type an answer, convert that text into a whole number, and store it in b.'}, {'line': '3', 'code': "print(f'Sum: {a + b}')", 'explanation': 'Build this message, replace each {name} with that variable’s current value, then show the message on the screen.'}],
                        'practical_examples': [{'title': 'Make a small addition calculator',
                                                'code': 'a = int(input())\n'
                                                        'b = int(input())\n'
                                                        "print(f'Sum: {a + b}')",
                                                'explanation': 'Type 12, press Enter, type 8, then press '
                                                               'Enter. The calculator shows their sum.',
                                                'output': 'Sum: 20'},
                                               {'title': 'Check a result before showing a message',
                                                'code': 'score = int(input())\n'
                                                        'passed = score >= 50\n'
                                                        "print(f'Passed: {passed}')",
                                                'explanation': 'Type 75 and press Enter. Python checks '
                                                               'whether 75 is at least 50, then displays '
                                                               'True.',
                                                'output': 'Passed: True'}],
                        'practice_questions': ['Why must typed numbers be converted before math?',
                                               'What does and require from its two checks?'],
                        'prerequisites': 'World 3: Operator Precedence',
                        'real_world_apps': 'These building blocks are used by simple calculators, checkout '
                                           'forms, quizzes, and access checks.',
                        'summary': 'Example: a small calculator\n'
                                   'a = int(input())\n'
                                   'b = int(input())\n'
                                   "print(f'Sum: {a + b}')",
                        'syntax_breakdown': "a = int(input())\nb = int(input())\nprint(f'Sum: {a + b}')",
                        'terminology': [{'term': 'input', 'definition': 'Information typed by a person.'},
                                        {'term': 'conversion',
                                         'definition': 'Changing text to a number so math can be done.'},
                                        {'term': 'logical condition',
                                         'definition': 'A decision made from one or more True or False '
                                                       'checks.'}],
                        'title': 'World 3 Examination'},
             'number': 30,
             'quizzes': [{'question': 'A calculator reads two whole-number answers using input(). What '
                                      'should it do before adding them?',
                          'explanation': 'input() returns text. int() converts digit text into whole numbers '
                                         'that can be added.',
                          'options': [{'text': 'Convert each answer with int()',
                                       'is_correct': True,
                                       'explanation': 'Correct! Then Python can add the numbers.'},
                                      {'text': 'Put each answer inside print()',
                                       'is_correct': False,
                                       'explanation': 'print() displays information; it does not convert '
                                                      'text to a number.'},
                                      {'text': 'Use len() on each answer',
                                       'is_correct': False,
                                       'explanation': 'len() counts characters. It does not convert text for '
                                                      'arithmetic.'},
                                      {'text': 'Add the text values directly',
                                       'is_correct': False,
                                       'explanation': 'Adding text joins it together; it does not add the '
                                                      'numeric values.'}]},
                         {'question': 'A person invests $1,000 at a yearly rate of 0.05 for 2 years. Which '
                                      'line correctly calculates the amount using principal * (1 + rate) ** '
                                      'years?',
                          'explanation': 'The parentheses calculate 1 plus the rate first, and ** raises it '
                                         'to the number of years.',
                          'options': [{'text': 'amount = 1000 * (1 + 0.05) ** 2',
                                       'is_correct': True,
                                       'explanation': 'Correct! The expression follows the compound-interest '
                                                      'formula.'},
                                      {'text': 'amount = 1000 + 0.05 ** 2',
                                       'is_correct': False,
                                       'explanation': 'This does not multiply the principal by the growth '
                                                      'factor.'},
                                      {'text': 'amount = (1000 * 1 + 0.05) ** 2',
                                       'is_correct': False,
                                       'explanation': 'These parentheses change which values are multiplied '
                                                      'and raised to a power.'},
                                      {'text': 'amount = 1000 * 0.05 + 2',
                                       'is_correct': False,
                                       'explanation': 'This multiplies by the rate and adds the years; it '
                                                      'does not calculate growth.'}]}],
             'title': 'World 3 Examination'}],
 'number': 3,
 'title': 'User Input and Operators'}
