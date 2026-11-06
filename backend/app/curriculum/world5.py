"""Curriculum module: WORLD_5
Beginner-friendly lessons and challenges about loops.
"""

WORLD_5 = {'description': 'Master while loops, for loops, range(), break, and continue.',
 'final_project_desc': 'Develop a classic interactive guessing game with hint feedback and attempt limits.',
 'final_project_title': 'Number Guessing Game',
 'goal': 'Automate repetitive tasks through iteration and loop controls.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'title': 'Repeat a Message',
                             'description': 'Your task, step by step:\n1. Use a for loop with range(3) to print Looping is powerful three times, each on its own line.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Use a for loop with range(3) to print Looping is powerful '
                                             'three times, each on its own line.',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': '',
                             'solution_code': "for _ in range(3):\n    print('Looping is powerful')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Looping is powerful\n'
                                                                'Looping is powerful\n'
                                                                'Looping is powerful',
                                             'is_hidden': False}],
                             'hints': ['Use a for loop with range(3) to print Looping is powerful three '
                                       'times, each on its own line.',
                                       'Complete solution:\n'
                                       'for _ in range(3):\n'
                                       "    print('Looping is powerful')"],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Echo Repeater',
                             'description': 'Your task, step by step:\n1. Read a whole number count.\n2. Print Echo exactly count times, one per line.\n3. If count is 0, print nothing.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read a whole number count. Print Echo exactly count times, one '
                                             'per line. If count is 0, print nothing.',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': 'count = int(input())\n\n# Repeat Echo count times below:\n',
                             'solution_code': 'count = int(input())\n'
                                              'for _ in range(count):\n'
                                              "    print('Echo')",
                             'test_cases': [{'input_data': '3\n',
                                             'expected_output': 'Echo\nEcho\nEcho',
                                             'is_hidden': False},
                                            {'input_data': '1\n',
                                             'expected_output': 'Echo',
                                             'is_hidden': False},
                                            {'input_data': '0\n', 'expected_output': '', 'is_hidden': False}],
                             'hints': ['Read a whole number count. Print Echo exactly count times, one per '
                                       'line. If count is 0, print nothing.',
                                       'Complete solution:\n'
                                       'count = int(input())\n'
                                       'for _ in range(count):\n'
                                       "    print('Echo')"],
                             'xp_reward': 150}],
             'description': 'Understand iteration and repeating execution blocks in computer science.',
             'lesson': {'common_mistakes': [{'fix': 'Use a loop whenever instructions repeat.',
                                             'mistake': 'Copy-pasting lines instead of using a loop',
                                             'why': 'Copy-pasting leads to bloated, unmaintainable code that '
                                                    'is prone to copy-paste typos.'}],
                        'detailed_explanation': 'A loop asks Python to repeat instructions. Without a loop, '
                                                'you might copy the same print line three times. With a '
                                                'loop, write it once and let Python repeat it.\n'
                                                '\n'
                                                'Use a for loop when you know what items to visit or how '
                                                'many turns you want. Use a while loop when you want to keep '
                                                'going until a condition changes. For example, for _ in '
                                                'range(3): means repeat the indented lines three times. The '
                                                'underscore is a name used when we do not need the turn '
                                                'number.',
                        'expected_output': 'Python Quest iteration\n'
                                           'Python Quest iteration\n'
                                           'Python Quest iteration\n'
                                           'Done',
                        'introduction': "Imagine being asked to write 'I will write clean Python code' 1,000 "
                                        'times by hand. It would take hours of tedious, mind-numbing effort. '
                                        'But for a computer, repeating a task 1,000 times takes less than a '
                                        'millisecond! Loops are the engine of repetition in programming.',
                        'learning_objectives': ['Understand what loops and iteration are in computer '
                                                'programming',
                                                "Understand the DRY (Don't Repeat Yourself) principle",
                                                'Recognize the two primary loop types in Python: while and '
                                                'for'],
                        'line_by_line': [{'line': '1', 'code': 'countdown = 3', 'explanation': 'Store the number 3 in countdown.'}, {'line': '2', 'code': 'while countdown > 0:', 'explanation': 'Repeat the indented lines below while countdown is greater than 0 is true. The loop changes a value so this check can eventually become false.'}, {'line': '3', 'code': '    print(countdown)', 'explanation': 'Work out countdown, then show the answer on the screen.'}, {'line': '4', 'code': '    countdown -= 1', 'explanation': 'Subtract 1 from countdown and save the new value back in countdown.'}, {'line': '5', 'code': "print('Blastoff!')", 'explanation': "Show the text 'Blastoff!' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Spaceship countdown sequence',
                                                'code': 'countdown = 3\n'
                                                        'while countdown > 0:\n'
                                                        '    print(countdown)\n'
                                                        '    countdown -= 1\n'
                                                        "print('Blastoff!')",
                                                'explanation': 'Executes 3 iterations decreasing the '
                                                               'countdown counter by 1 each time.',
                                                'output': '3\n2\n1\nBlastoff!'},
                                               {'title': 'Example 2: Iterating through an inventory list',
                                                'code': "inventory = ['Torch', 'Rope', 'Compass']\n"
                                                        'for item in inventory:\n'
                                                        "    print('Carrying:', item)",
                                                'explanation': 'Extracts each string in inventory one by one '
                                                               'and displays it.',
                                                'output': 'Carrying: Torch\n'
                                                          'Carrying: Rope\n'
                                                          'Carrying: Compass'},
                                               {'title': 'Example 3: Accumulating a running total',
                                                'code': 'scores = [10, 20, 30]\n'
                                                        'total = 0\n'
                                                        'for s in scores:\n'
                                                        '    total += s\n'
                                                        "print('Total Game Points:', total)",
                                                'explanation': 'Iterates over numeric scores and accumulates '
                                                               'them into total.',
                                                'output': 'Total Game Points: 60'}],
                        'practice_questions': ['What does the DRY principle stand for?',
                                               'What is a single pass through a loop called?'],
                        'prerequisites': 'World 4: Conditional Statements',
                        'real_world_apps': 'Processing music playlist tracks, calculating payroll for '
                                           'thousands of employees, rendering video game frames (the 60 FPS '
                                           'game loop).',
                        'summary': 'A loop repeats instructions. for is handy for a known list or count; '
                                   'while repeats until a condition changes.',
                        'syntax_breakdown': "# Loops automate repetition so you don't repeat code manually:\n"
                                            '# 1. Condition-controlled loop (while): repeats while a test '
                                            'remains True\n'
                                            'fuel = 3\n'
                                            'while fuel > 0:\n'
                                            "    print('Thruster burning, fuel left:', fuel)\n"
                                            '    fuel -= 1\n'
                                            '\n'
                                            '# 2. Collection-controlled loop (for): repeats once for every '
                                            'element in a list\n'
                                            "for color in ['Red', 'Green', 'Blue']:\n"
                                            "    print('RGB Channel:', color)",
                        'terminology': [{'definition': 'A single repetition or pass through the body of a '
                                                       'loop.',
                                         'term': 'Iteration'},
                                        {'definition': "Don't Repeat Yourself — a core software engineering "
                                                       'principle advocating for reusable code patterns.',
                                         'term': 'DRY'},
                                        {'definition': 'The indented block of statements executed on each '
                                                       'cycle of a loop.',
                                         'term': 'Loop Body'}]},
             'number': 40,
             'quizzes': [{'question': "What does this code print?\n\nfor _ in range(3):\n    print('Go')",
                          'explanation': 'range(3) gives the loop three turns.',
                          'options': [{'text': 'Go on three lines',
                                       'is_correct': True,
                                       'explanation': 'Correct. range(3) gives the loop three turns.'},
                                      {'text': 'Go once',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Go Go Go on one line',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'A for loop visits this list. How many times does the print line run?\n'
                                      '\n'
                                      "colors = ['red', 'blue']\n"
                                      'for color in colors:\n'
                                      '    print(color)',
                          'explanation': 'The loop visits each of the two items once.',
                          'options': [{'text': '2 times',
                                       'is_correct': True,
                                       'explanation': 'Correct. The loop visits each of the two items once.'},
                                      {'text': '1 time',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '3 times',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Forever',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'What Are Loops?'},
            {'challenges': [{'title': 'Count Down with while',
                             'description': 'Your task, step by step:\n1. Start with count = 4.\n2. Print 4, 3, 2, 1 with a while loop.\n3. Subtract 1 each turn so it stops, then print Done.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 5 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Start with count = 4. Print 4, 3, 2, 1 with a while loop. '
                                             'Subtract 1 each turn so it stops, then print Done.',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': 'count = 4\n\n# Add your while loop below:\n',
                             'solution_code': 'count = 4\n'
                                              'while count > 0:\n'
                                              '    print(count)\n'
                                              '    count -= 1\n'
                                              "print('Done')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': '4\n3\n2\n1\nDone',
                                             'is_hidden': False}],
                             'hints': ['Start with count = 4. Print 4, 3, 2, 1 with a while loop. Subtract 1 '
                                       'each turn so it stops, then print Done.',
                                       'Complete solution:\n'
                                       'count = 4\n'
                                       'while count > 0:\n'
                                       '    print(count)\n'
                                       '    count -= 1\n'
                                       "print('Done')"],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Add Until Zero',
                             'description': 'Your task, step by step:\n1. Read whole numbers until the user enters 0.\n2. Add the nonzero numbers and print Sum: followed by the total.\n3. Do not add the 0.\n\nInput for this example: The Input box shows 4 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read whole numbers until the user enters 0. Add the nonzero '
                                             'numbers and print Sum: followed by the total. Do not add the '
                                             '0.',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': 'total = 0\n\n# Read values until 0, then print the sum:\n',
                             'solution_code': 'total = 0\n'
                                              'while True:\n'
                                              '    value = int(input())\n'
                                              '    if value == 0:\n'
                                              '        break\n'
                                              '    total += value\n'
                                              "print(f'Sum: {total}')",
                             'test_cases': [{'input_data': '10\n25\n5\n0\n',
                                             'expected_output': 'Sum: 40',
                                             'is_hidden': False},
                                            {'input_data': '100\n0\n',
                                             'expected_output': 'Sum: 100',
                                             'is_hidden': False},
                                            {'input_data': '0\n',
                                             'expected_output': 'Sum: 0',
                                             'is_hidden': False}],
                             'hints': ['Read whole numbers until the user enters 0. Add the nonzero numbers '
                                       'and print Sum: followed by the total. Do not add the 0.',
                                       'Complete solution:\n'
                                       'total = 0\n'
                                       'while True:\n'
                                       '    value = int(input())\n'
                                       '    if value == 0:\n'
                                       '        break\n'
                                       '    total += value\n'
                                       "print(f'Sum: {total}')"],
                             'xp_reward': 150}],
             'description': 'Loop as long as a boolean condition remains True.',
             'lesson': {'common_mistakes': [{'fix': 'Always increment or decrement your loop counter inside '
                                                    'the loop body.',
                                             'mistake': 'while count < 5:\n'
                                                        '    print(count)\n'
                                                        '    # forgot count += 1',
                                             'why': 'Without modifying count, count is always 0, running '
                                                    'forever in an infinite loop.'}],
                        'detailed_explanation': 'Python checks the condition after while before every turn. '
                                                'If it is True, Python runs the indented lines and checks '
                                                'again. If it is False, the loop ends.\n'
                                                '\n'
                                                'A counter is a number that changes each turn. Give it a '
                                                'starting value, check it in the while line, and update it '
                                                'inside the loop. For example, start at 3, print the number, '
                                                'and subtract 1. It prints 3, 2, and 1. At 0, count > 0 is '
                                                'False, so the loop stops. Without the update, the loop '
                                                'might never stop.',
                        'expected_output': 'T-minus 3\nT-minus 2\nT-minus 1\nBlastoff!',
                        'introduction': 'A `while` loop is like an `if` statement that refuses to leave! '
                                        'When an `if` statement is True, it runs once and finishes. When a '
                                        '`while` loop is True, it runs, goes back to the top, checks the '
                                        'condition again, and repeats as long as the condition stays True.',
                        'learning_objectives': ['Master the syntax of the while loop in Python',
                                                'Understand loop variables, initialization, and loop '
                                                'incrementers',
                                                'Learn how to guarantee loop termination'],
                        'line_by_line': [{'line': '1', 'code': 'battery = 70', 'explanation': 'Store the number 70 in battery.'}, {'line': '2', 'code': 'while battery < 100:', 'explanation': 'Repeat the indented lines below while battery is less than 100 is true. The loop changes a value so this check can eventually become false.'}, {'line': '3', 'code': "    print('Charging... Current:', battery, '%')", 'explanation': "Show the text 'Charging... Current:', followed by the current value of battery, followed by the text '%'. Python puts a space between comma-separated print items."}, {'line': '4', 'code': '    battery += 10', 'explanation': 'Add 10 to battery and save the new value back in battery.'}, {'line': '5', 'code': "print('Battery Full: 100%')", 'explanation': "Show the text 'Battery Full: 100%' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Safe battery recharge simulation',
                                                'code': 'battery = 70\n'
                                                        'while battery < 100:\n'
                                                        "    print('Charging... Current:', battery, '%')\n"
                                                        '    battery += 10\n'
                                                        "print('Battery Full: 100%')",
                                                'explanation': 'Simulates battery charging by 10% steps '
                                                               'until reaching 100%.',
                                                'output': 'Charging... Current: 70 %\n'
                                                          'Charging... Current: 80 %\n'
                                                          'Charging... Current: 90 %\n'
                                                          'Battery Full: 100%'},
                                               {'title': 'Example 2: Halving radioactive half-life decay',
                                                'code': 'sample = 80\n'
                                                        'while sample > 15:\n'
                                                        "    print('Mass remaining:', sample, 'grams')\n"
                                                        '    sample = sample // 2\n'
                                                        "print('Safe threshold reached.')",
                                                'explanation': 'Halves the sample mass on each pass until it '
                                                               'drops below 15 grams.',
                                                'output': 'Mass remaining: 80 grams\n'
                                                          'Mass remaining: 40 grams\n'
                                                          'Mass remaining: 20 grams\n'
                                                          'Safe threshold reached.'},
                                               {'title': 'Example 3: Pin retry attempts limiter',
                                                'code': 'attempts = 0\n'
                                                        'max_attempts = 3\n'
                                                        'while attempts < max_attempts:\n'
                                                        '    attempts += 1\n'
                                                        "    print('Attempt', attempts, 'recorded.')\n"
                                                        "print('Security log updated.')",
                                                'explanation': 'Guarantees exactly 3 execution cycles before '
                                                               'transitioning.',
                                                'output': 'Attempt 1 recorded.\n'
                                                          'Attempt 2 recorded.\n'
                                                          'Attempt 3 recorded.\n'
                                                          'Security log updated.'}],
                        'practice_questions': ['What happens if a while loop condition is False right from '
                                               'the beginning?',
                                               'Why must the loop counter change inside the loop?'],
                        'prerequisites': 'Level 40: What Are Loops?',
                        'real_world_apps': 'Waiting for user input, polling network servers until a '
                                           'connection succeeds, event-driven loops.',
                        'summary': 'A while loop repeats while its condition is True. Start a counter, check '
                                   'it, and update it so the loop can finish.',
                        'syntax_breakdown': '# 1. Loop variable initialized BEFORE the loop:\n'
                                            'counter = 1\n'
                                            '\n'
                                            "# 2. 'while' keyword + boolean condition + colon ':':\n"
                                            'while counter <= 3:\n'
                                            '    # 3. Indented body: executes repeatedly as long as counter '
                                            '<= 3 is True\n'
                                            "    print('Processing packet #', counter)\n"
                                            '    # 4. State update: CRUCIAL to advance counter and prevent '
                                            'an infinite loop!\n'
                                            '    counter += 1\n'
                                            '\n'
                                            '# 5. Code after loop: runs once loop terminates\n'
                                            "print('All packets processed.')",
                        'terminology': [{'definition': 'A loop that continues executing its body repeatedly '
                                                       'as long as its test condition evaluates to True.',
                                         'term': 'while Loop'},
                                        {'definition': 'A variable initialized before a loop and updated '
                                                       'during each iteration to control loop termination.',
                                         'term': 'Loop Counter'}]},
             'number': 41,
             'quizzes': [{'question': 'What does this code print?\n'
                                      '\n'
                                      'count = 2\n'
                                      'while count > 0:\n'
                                      '    print(count)\n'
                                      '    count -= 1',
                          'explanation': 'It prints 2, then 1. At 0 the condition is False, so the loop '
                                         'ends.',
                          'options': [{'text': '2 then 1',
                                       'is_correct': True,
                                       'explanation': 'Correct. It prints 2, then 1. At 0 the condition is '
                                                      'False, so the loop ends.'},
                                      {'text': '2 then 1 then 0',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '2 forever',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'What does this code print?\n'
                                      '\n'
                                      'count = 5\n'
                                      'while count < 3:\n'
                                      "    print('Go')\n"
                                      '    count += 1\n'
                                      'print(count)',
                          'explanation': 'The condition is False at the start, so the loop is skipped and '
                                         'count stays 5.',
                          'options': [{'text': '5',
                                       'is_correct': True,
                                       'explanation': 'Correct. The condition is False at the start, so the '
                                                      'loop is skipped and count stays 5.'},
                                      {'text': 'Go then 6',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '3',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'It runs forever',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'Understanding while Loops'},
            {'challenges': [{'title': 'Print Every Item',
                             'description': 'Your task, step by step:\n1. Use the given list.\n2. Visit each item with a for loop and print Item: followed by its name.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Use the given list. Visit each item with a for loop and print '
                                             'Item: followed by its name.',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': "items = ['Sword', 'Shield', 'Potion']\n"
                                             '\n'
                                             '# Visit and print each item below:\n',
                             'solution_code': "items = ['Sword', 'Shield', 'Potion']\n"
                                              'for item in items:\n'
                                              "    print(f'Item: {item}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Item: Sword\nItem: Shield\nItem: Potion',
                                             'is_hidden': False}],
                             'hints': ['Use the given list. Visit each item with a for loop and print Item: '
                                       'followed by its name.',
                                       'Complete solution:\n'
                                       "items = ['Sword', 'Shield', 'Potion']\n"
                                       'for item in items:\n'
                                       "    print(f'Item: {item}')"],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Add Four Scores',
                             'description': 'Your task, step by step:\n1. Read exactly four whole-number scores with a for loop.\n2. Add them, then print Total: followed by the sum.\n\nInput for this example: The Input box shows 4 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read exactly four whole-number scores with a for loop. Add '
                                             'them, then print Total: followed by the sum.',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': 'total = 0\n\n# Read and add four scores:\n',
                             'solution_code': 'total = 0\n'
                                              'for _ in range(4):\n'
                                              '    total += int(input())\n'
                                              "print(f'Total: {total}')",
                             'test_cases': [{'input_data': '10\n20\n30\n40\n',
                                             'expected_output': 'Total: 100',
                                             'is_hidden': False},
                                            {'input_data': '5\n5\n5\n5\n',
                                             'expected_output': 'Total: 20',
                                             'is_hidden': False}],
                             'hints': ['Read exactly four whole-number scores with a for loop. Add them, '
                                       'then print Total: followed by the sum.',
                                       'Complete solution:\n'
                                       'total = 0\n'
                                       'for _ in range(4):\n'
                                       '    total += int(input())\n'
                                       "print(f'Total: {total}')"],
                             'xp_reward': 150}],
             'description': 'Iterate cleanly over sequences, lists, and character strings.',
             'lesson': {'common_mistakes': [{'fix': 'for item in range(100):',
                                             'mistake': 'for item in 100:',
                                             'why': 'A raw integer is not an iterable sequence! Python '
                                                    "raises TypeError: 'int' object is not iterable. Use "
                                                    'range(100) instead.'}],
                        'detailed_explanation': 'A for loop takes items from a group one at a time. The name '
                                                'after for holds the current item. Python runs the indented '
                                                'lines for that item, then moves to the next one. When there '
                                                'are no more items, the loop ends.\n'
                                                '\n'
                                                'In for fruit in fruits:, fruit first means Apple, then '
                                                'Banana, then Pear. You do not need to move a counter '
                                                'yourself. A word is a group of characters too, so for '
                                                "letter in 'CAT': visits C, A, and T. Use for to do a job "
                                                'for every item in a list or word.',
                        'expected_output': 'Letter: P\nLetter: Y\nLetter: T\nLetter: H\nLetter: O\nLetter: N',
                        'introduction': 'In many languages, running a loop requires declaring counters, '
                                        'conditions, and incrementers manually. In Python, `for` loops are '
                                        'fundamentally different: they iterate directly over sequences of '
                                        "items! It reads like plain English: 'For each item in this "
                                        "collection, do this.'",
                        'learning_objectives': ['Master the syntax of for loops in Python',
                                                'Understand how Python iterates directly over items without '
                                                'manual counters',
                                                'Iterate over characters in a string'],
                        'line_by_line': [{'line': '1', 'code': "stats = ['Strength: 18', 'Agility: 14', 'Intellect: 20']", 'explanation': 'Create a list named stats with Strength: 18, Agility: 14 and Intellect: 20 in this order. A loop can take one item from the list at a time.'}, {'line': '2', 'code': 'for s in stats:', 'explanation': 'Take each item from stats in order. During each turn, s holds the current item.'}, {'line': '3', 'code': "    print('[STAT]', s)", 'explanation': "Show the text '[STAT]', followed by the current value of s. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Character stat readout',
                                                'code': "stats = ['Strength: 18', 'Agility: 14', 'Intellect: "
                                                        "20']\n"
                                                        'for s in stats:\n'
                                                        "    print('[STAT]', s)",
                                                'explanation': 'Loops over three string items and displays '
                                                               'them with a custom prefix.',
                                                'output': '[STAT] Strength: 18\n'
                                                          '[STAT] Agility: 14\n'
                                                          '[STAT] Intellect: 20'},
                                               {'title': 'Example 2: Iterating over string characters',
                                                'code': "word = 'PYTHON'\n"
                                                        'for letter in word:\n'
                                                        "    print('Letter:', letter)",
                                                'explanation': 'Strings are sequences; the for loop visits '
                                                               'every single character in order.',
                                                'output': 'Letter: P\n'
                                                          'Letter: Y\n'
                                                          'Letter: T\n'
                                                          'Letter: H\n'
                                                          'Letter: O\n'
                                                          'Letter: N'},
                                               {'title': 'Example 3: Calculating price discounts',
                                                'code': 'prices = [10.0, 25.0, 50.0]\n'
                                                        'for p in prices:\n'
                                                        '    discounted = p * 0.9\n'
                                                        "    print('Original:', p, '| 10% Off:', discounted)",
                                                'explanation': 'Calculates and prints the 10% discounted '
                                                               'price for each catalog item.',
                                                'output': 'Original: 10.0 | 10% Off: 9.0\n'
                                                          'Original: 25.0 | 10% Off: 22.5\n'
                                                          'Original: 50.0 | 10% Off: 45.0'}],
                        'practice_questions': ['Can you iterate over a string using a for loop?',
                                               'What error happens if you try to loop over a raw integer: '
                                               'for i in 5:?'],
                        'prerequisites': 'Level 41: Understanding while Loops',
                        'real_world_apps': 'Processing customer email lists, analyzing sensor data records, '
                                           'reading lines in a text file.',
                        'summary': 'A for loop visits each item in order and stops by itself when it reaches '
                                   'the end.',
                        'syntax_breakdown': "# 1. 'for' keyword + target variable name ('planet')\n"
                                            "# 2. 'in' keyword + iterable collection (['Mars', 'Jupiter', "
                                            "'Saturn'])\n"
                                            "# 3. Colon ':' followed by indented block (4 spaces):\n"
                                            "planets = ['Mars', 'Jupiter', 'Saturn']\n"
                                            'for planet in planets:\n'
                                            "    print('Navigating toward:', planet)\n"
                                            '\n'
                                            "print('Interplanetary travel sequence complete.')",
                        'terminology': [{'definition': 'A loop that iterates over the elements of any '
                                                       'sequence or iterable in order.',
                                         'term': 'for Loop'},
                                        {'definition': 'Any Python object capable of returning its members '
                                                       'one at a time (like strings, lists, tuples, or '
                                                       'ranges).',
                                         'term': 'Iterable'},
                                        {'definition': 'The variable that holds the current item during each '
                                                       'pass through the loop.',
                                         'term': 'Loop Variable'}]},
             'number': 42,
             'quizzes': [{'question': "What does this code print?\n\nfor letter in 'CAT':\n    print(letter)",
                          'explanation': 'The loop visits each character in order, and print starts a new '
                                         'line each time.',
                          'options': [{'text': 'C, A, and T on separate lines',
                                       'is_correct': True,
                                       'explanation': 'Correct. The loop visits each character in order, and '
                                                      'print starts a new line each time.'},
                                      {'text': 'CAT on one line',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Only C',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'An error',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'What is printed on the second turn?\n'
                                      '\n'
                                      "items = ['Map', 'Key', 'Torch']\n"
                                      'for item in items:\n'
                                      '    print(item)',
                          'explanation': 'On turn two, item holds the second list value.',
                          'options': [{'text': 'Key',
                                       'is_correct': True,
                                       'explanation': 'Correct. On turn two, item holds the second list '
                                                      'value.'},
                                      {'text': 'Map',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Torch',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'Understanding for Loops'},
            {'challenges': [{'title': 'Print Even Numbers',
                             'description': 'Your task, step by step:\n1. Use range(2, 11, 2) to print the even numbers from 2 through 10, one per line.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 5 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Use range(2, 11, 2) to print the even numbers from 2 through '
                                             '10, one per line.',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': '\n# Use range with a start, stop, and step:\n',
                             'solution_code': 'for number in range(2, 11, 2):\n    print(number)',
                             'test_cases': [{'input_data': '',
                                             'expected_output': '2\n4\n6\n8\n10',
                                             'is_hidden': False}],
                             'hints': ['Use range(2, 11, 2) to print the even numbers from 2 through 10, one '
                                       'per line.',
                                       'Complete solution:\n'
                                       'for number in range(2, 11, 2):\n'
                                       '    print(number)'],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Countdown',
                             'description': 'Your task, step by step:\n1. Count down from 5 to 1 with range(5, 0, -1).\n2. Print Countdown: and each number.\n3. After the loop, print Blastoff!\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 6 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Count down from 5 to 1 with range(5, 0, -1). Print Countdown: '
                                             'and each number. After the loop, print Blastoff!',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': '\n# Count down using a negative range step:\n',
                             'solution_code': 'for number in range(5, 0, -1):\n'
                                              "    print(f'Countdown: {number}')\n"
                                              "print('Blastoff!')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Countdown: 5\n'
                                                                'Countdown: 4\n'
                                                                'Countdown: 3\n'
                                                                'Countdown: 2\n'
                                                                'Countdown: 1\n'
                                                                'Blastoff!',
                                             'is_hidden': False}],
                             'hints': ['Count down from 5 to 1 with range(5, 0, -1). Print Countdown: and '
                                       'each number. After the loop, print Blastoff!',
                                       'Complete solution:\n'
                                       'for number in range(5, 0, -1):\n'
                                       "    print(f'Countdown: {number}')\n"
                                       "print('Blastoff!')"],
                             'xp_reward': 150}],
             'description': 'Generate numeric arithmetic sequences with start, stop, and step parameters.',
             'lesson': {'common_mistakes': [{'fix': 'range(1, 11)',
                                             'mistake': 'range(1, 10) expecting numbers 1 through 10',
                                             'why': 'The stop value is exclusive. range(1, 10) only reaches '
                                                    '9!'}],
                        'detailed_explanation': 'range() gives a for loop a sequence of whole numbers. The '
                                                'stop number is left out. range(1, 5) gives 1, 2, 3, 4 and '
                                                'stops before 5.\n'
                                                '\n'
                                                'With one number, range(4) gives 0, 1, 2, 3. With two, '
                                                'range(2, 6) starts at 2 and gives 2, 3, 4, 5. With three, '
                                                'the third number is the step: range(2, 11, 2) gives 2, 4, '
                                                '6, 8, 10. A negative step counts down, as in range(5, 0, '
                                                '-1), which gives 5, 4, 3, 2, 1.',
                        'expected_output': '10\n20\n30\n40\n50',
                        'introduction': 'What if you want a `for` loop to run 100 times, or count from 10 to '
                                        "50, or count by 5s? You don't want to type out a list of 100 "
                                        'numbers by hand! In Python, the `range()` function generates '
                                        'arithmetic numeric sequences on demand with incredible memory '
                                        'efficiency.',
                        'learning_objectives': ['Master the range() built-in generator function',
                                                'Understand 1-argument range(stop), 2-argument range(start, '
                                                'stop), and 3-argument range(start, stop, step)',
                                                'Learn why the stop parameter is exclusive (up to, but not '
                                                'including stop)',
                                                'Generate descending reverse sequences using negative steps'],
                        'line_by_line': [{'line': '1', 'code': 'for lap in range(1, 4):', 'explanation': 'range(1, 4) gives 1, 2 and 3; it stops before the ending number. Python repeats the indented lines with the current number saved in lap.'}, {'line': '2', 'code': "    print('Lap', lap, 'completed!')", 'explanation': "Show the text 'Lap', followed by the current value of lap, followed by the text 'completed!'. Python puts a space between comma-separated print items."}, {'line': '3', 'code': "print('Race finished!')", 'explanation': "Show the text 'Race finished!' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Fixed repetition count',
                                                'code': 'for lap in range(1, 4):\n'
                                                        "    print('Lap', lap, 'completed!')\n"
                                                        "print('Race finished!')",
                                                'explanation': 'Runs the loop body exactly 3 times with lap '
                                                               'starting at 1 and ending at 3.',
                                                'output': 'Lap 1 completed!\n'
                                                          'Lap 2 completed!\n'
                                                          'Lap 3 completed!\n'
                                                          'Race finished!'},
                                               {'title': 'Example 2: Stepping backwards (countdown)',
                                                'code': 'for sec in range(5, 0, -1):\n'
                                                        "    print('T-minus:', sec)\n"
                                                        "print('Ignition!')",
                                                'explanation': 'A negative step of -1 counts downwards from '
                                                               '5 down to 1.',
                                                'output': 'T-minus: 5\n'
                                                          'T-minus: 4\n'
                                                          'T-minus: 3\n'
                                                          'T-minus: 2\n'
                                                          'T-minus: 1\n'
                                                          'Ignition!'},
                                               {'title': 'Example 3: Multiplication table row',
                                                'code': 'base = 7\n'
                                                        'for multiplier in range(1, 5):\n'
                                                        "    print(base, 'x', multiplier, '=', base * "
                                                        'multiplier)',
                                                'explanation': 'Generates the 7 times table for multipliers '
                                                               '1 through 4.',
                                                'output': '7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28'}],
                        'practice_questions': ['What numbers are generated by range(3)?',
                                               'How do you count down from 5 to 1 using range()?'],
                        'prerequisites': 'Level 42: Understanding for Loops',
                        'real_world_apps': 'Pagination calculations, generating time step ticks in '
                                           'animations, calculating financial intervals.',
                        'summary': 'range() makes number patterns. The start is included and the stop is '
                                   'left out. The step controls the gap and direction.',
                        'syntax_breakdown': '# range(stop): generates numbers from 0 up to (stop - 1)\n'
                                            'for i in range(3):\n'
                                            "    print('Index:', i)\n"
                                            '\n'
                                            '# range(start, stop): generates from start up to (stop - 1)\n'
                                            'for page in range(1, 4):\n'
                                            "    print('Reading page:', page)\n"
                                            '\n'
                                            '# range(start, stop, step): counts by step increments\n'
                                            'for even in range(2, 9, 2):\n'
                                            "    print('Even number:', even)",
                        'terminology': [{'definition': 'A built-in sequence generator that produces an '
                                                       'immutable arithmetic sequence of integers.',
                                         'term': 'range()'},
                                        {'definition': 'A convention where the boundary number is not '
                                                       'included in the generated sequence.',
                                         'term': 'Exclusive Stop'},
                                        {'definition': 'The increment (or decrement if negative) between '
                                                       'each consecutive number in a range.',
                                         'term': 'Step'}]},
             'number': 43,
             'quizzes': [{'question': 'Which numbers does range(2, 8, 2) give?',
                          'explanation': 'Start at 2, add 2, and stop before 8.',
                          'options': [{'text': '2, 4, 6',
                                       'is_correct': True,
                                       'explanation': 'Correct. Start at 2, add 2, and stop before 8.'},
                                      {'text': '2, 4, 6, 8',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '0, 2, 4, 6',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '2, 3, 4, 5, 6, 7',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'What does this code print?\n'
                                      '\n'
                                      'for n in range(3, 0, -1):\n'
                                      "    print(n, end=' ')",
                          'explanation': 'The negative step counts down and range stops before 0.',
                          'options': [{'text': '3 2 1',
                                       'is_correct': True,
                                       'explanation': 'Correct. The negative step counts down and range '
                                                      'stops before 0.'},
                                      {'text': '3 2 1 0',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '0 1 2 3',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'Understanding range()'},
            {'challenges': [{'title': 'Stop at Five',
                             'description': 'Your task, step by step:\n1. Check numbers 1 to 9.\n2. When number is 5, use break.\n3. Print each number before 5, so the output is 1, 2, 3, 4.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Check numbers 1 to 9. When number is 5, use break. Print each '
                                             'number before 5, so the output is 1, 2, 3, 4.',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': '\n# Check numbers and use break when number reaches 5:\n',
                             'solution_code': 'for number in range(1, 10):\n'
                                              '    if number == 5:\n'
                                              '        break\n'
                                              '    print(number)',
                             'test_cases': [{'input_data': '',
                                             'expected_output': '1\n2\n3\n4',
                                             'is_hidden': False}],
                             'hints': ['Check numbers 1 to 9. When number is 5, use break. Print each number '
                                       'before 5, so the output is 1, 2, 3, 4.',
                                       'Complete solution:\n'
                                       'for number in range(1, 10):\n'
                                       '    if number == 5:\n'
                                       '        break\n'
                                       '    print(number)'],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Find the Target',
                             'description': 'Your task, step by step:\n1. Read a target number, then up to five more numbers.\n2. If one matches, print Target acquired and stop.\n3. If none match, print Target not found.\n\nInput for this example: The Input box shows 6 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read a target number, then up to five more numbers. If one '
                                             'matches, print Target acquired and stop. If none match, print '
                                             'Target not found.',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': 'target = int(input())\n\n# Check up to five readings below:\n',
                             'solution_code': 'target = int(input())\n'
                                              'found = False\n'
                                              'for _ in range(5):\n'
                                              '    value = int(input())\n'
                                              '    if value == target:\n'
                                              "        print('Target acquired')\n"
                                              '        found = True\n'
                                              '        break\n'
                                              'if not found:\n'
                                              "    print('Target not found')",
                             'test_cases': [{'input_data': '7\n2\n7\n9\n0\n0\n',
                                             'expected_output': 'Target acquired',
                                             'is_hidden': False},
                                            {'input_data': '4\n1\n2\n3\n5\n6\n',
                                             'expected_output': 'Target not found',
                                             'is_hidden': False}],
                             'hints': ['Read a target number, then up to five more numbers. If one matches, '
                                       'print Target acquired and stop. If none match, print Target not '
                                       'found.',
                                       'Complete solution:\n'
                                       'target = int(input())\n'
                                       'found = False\n'
                                       'for _ in range(5):\n'
                                       '    value = int(input())\n'
                                       '    if value == target:\n'
                                       "        print('Target acquired')\n"
                                       '        found = True\n'
                                       '        break\n'
                                       'if not found:\n'
                                       "    print('Target not found')"],
                             'xp_reward': 150}],
             'description': 'Exit and terminate a loop immediately when a condition is met.',
             'lesson': {'common_mistakes': [{'fix': 'Only use break within while or for loops.',
                                             'mistake': 'Placing break outside of a loop',
                                             'why': 'break can ONLY be placed inside a loop body; using it '
                                                    "in top-level code triggers SyntaxError: 'break' outside "
                                                    'loop.'}],
                        'detailed_explanation': 'break tells Python to leave a loop right away. Python skips '
                                                'the remaining turns and continues with the first line after '
                                                'the loop.\n'
                                                '\n'
                                                'This is useful when searching. Check items one by one, and '
                                                'as soon as the item you want is found, use break so you do '
                                                'not check the rest. An if line can decide when to stop; the '
                                                'indented break does the stopping. In a nested loop, break '
                                                'leaves only the nearest loop around it.',
                        'expected_output': 'Checking 10\n'
                                           'Checking 25\n'
                                           'Checking 42\n'
                                           'Found 42! Stopping search.\n'
                                           'Search complete.',
                        'introduction': 'Imagine searching through a deck of 52 playing cards for the Ace of '
                                        'Spades. Once you find it on card #7, do you keep searching through '
                                        'the remaining 45 cards? Of course not! You stop searching '
                                        'immediately. In Python, `break` lets you bail out of a loop the '
                                        'instant you have found what you need.',
                        'learning_objectives': ['Understand how the break keyword works in both for and '
                                                'while loops',
                                                'Prematurely terminate a loop when a target item or error '
                                                'condition is encountered',
                                                'Recognize that execution jumps immediately to the line '
                                                'following the loop block'],
                        'line_by_line': [{'line': '1', 'code': "names = ['Alice', 'Bob', 'Charlie', 'David']", 'explanation': 'Create a list named names with Alice, Bob, Charlie and David in this order. A loop can take one item from the list at a time.'}, {'line': '2', 'code': 'for n in names:', 'explanation': 'Take each item from names in order. During each turn, n holds the current item.'}, {'line': '3', 'code': "    if n == 'Bob':", 'explanation': "Check whether n is the same as 'Bob'. If that is true, run the indented lines below; otherwise, skip them."}, {'line': '4', 'code': "        print('Target found: Bob')", 'explanation': "Show the text 'Target found: Bob' on the screen."}, {'line': '5', 'code': '        break', 'explanation': 'Stop this loop now. Python moves to the first line after the loop.'}, {'line': '6', 'code': "    print('Inspecting:', n)", 'explanation': "Show the text 'Inspecting:', followed by the current value of n. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Early search termination',
                                                'code': "names = ['Alice', 'Bob', 'Charlie', 'David']\n"
                                                        'for n in names:\n'
                                                        "    if n == 'Bob':\n"
                                                        "        print('Target found: Bob')\n"
                                                        '        break\n'
                                                        "    print('Inspecting:', n)",
                                                'explanation': "Stops inspecting immediately when 'Bob' is "
                                                               'discovered, skipping Charlie and David.',
                                                'output': 'Inspecting: Alice\nTarget found: Bob'},
                                               {'title': 'Example 2: Emergency pressure shutdown',
                                                'code': 'pressure = 90\n'
                                                        'while pressure < 150:\n'
                                                        "    print('Pressure level:', pressure)\n"
                                                        '    if pressure >= 120:\n'
                                                        "        print('EMERGENCY: Valve relief "
                                                        "triggered!')\n"
                                                        '        break\n'
                                                        '    pressure += 10',
                                                'explanation': 'Breaks out of the loop the instant pressure '
                                                               'reaches dangerous 120 threshold.',
                                                'output': 'Pressure level: 90\n'
                                                          'Pressure level: 100\n'
                                                          'Pressure level: 110\n'
                                                          'Pressure level: 120\n'
                                                          'EMERGENCY: Valve relief triggered!'},
                                               {'title': 'Example 3: Finding the first negative number',
                                                'code': 'readings = [12, 18, 5, -3, 14, -8]\n'
                                                        'for r in readings:\n'
                                                        '    if r < 0:\n'
                                                        "        print('First anomaly detected:', r)\n"
                                                        '        break',
                                                'explanation': 'Halts iteration upon finding -3 without '
                                                               'examining subsequent numbers.',
                                                'output': 'First anomaly detected: -3'}],
                        'practice_questions': ['What happens to the remaining iterations when break is '
                                               'executed?',
                                               'Can you use break inside both while and for loops?'],
                        'prerequisites': 'Level 43: Understanding range()',
                        'real_world_apps': 'Database query record matching, user cancellation handling, '
                                           'detecting corrupt packet frames in network streams.',
                        'summary': 'break exits the current loop immediately. It is useful when you have '
                                   'found what you need or must stop early.',
                        'syntax_breakdown': "# The 'break' statement terminates the enclosing loop "
                                            'IMMEDIATELY:\n'
                                            'target_id = 103\n'
                                            'ids = [101, 102, 103, 104, 105]\n'
                                            '\n'
                                            'for item in ids:\n'
                                            "    print('Checking ID:', item)\n"
                                            '    if item == target_id:\n'
                                            "        print('Found match! Halting search.')\n"
                                            '        break\n'
                                            '\n'
                                            "print('Search completed.')",
                        'terminology': [{'definition': 'A Python control statement that immediately '
                                                       'terminates the active loop.',
                                         'term': 'break'},
                                        {'definition': 'Terminating a loop before it reaches its natural end '
                                                       'because an objective has been satisfied.',
                                         'term': 'Early Exit'}]},
             'number': 44,
             'quizzes': [{'question': 'What does this code print?\n'
                                      '\n'
                                      'for n in range(1, 6):\n'
                                      '    if n == 4:\n'
                                      '        break\n'
                                      '    print(n)',
                          'explanation': 'When n reaches 4, break exits before print(n).',
                          'options': [{'text': '1, 2, 3',
                                       'is_correct': True,
                                       'explanation': 'Correct. When n reaches 4, break exits before '
                                                      'print(n).'},
                                      {'text': '1, 2, 3, 4',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '4, 5',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '1, 2, 3, 4, 5',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'A loop finds the number it was looking for. What does break do next?',
                          'explanation': 'break leaves the current loop immediately.',
                          'options': [{'text': 'Stops the loop',
                                       'is_correct': True,
                                       'explanation': 'Correct. break leaves the current loop immediately.'},
                                      {'text': 'Skips just this turn',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Restarts at 1',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Pauses forever',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'break Statement'},
            {'challenges': [{'title': 'Skip Negative Numbers',
                             'description': 'Your task, step by step:\n1. Read five whole numbers.\n2. Use continue to skip a number below 0.\n3. Print every number that is 0 or more.\n\nInput for this example: The Input box shows 5 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read five whole numbers. Use continue to skip a number below '
                                             '0. Print every number that is 0 or more.',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': 'for _ in range(5):\n'
                                             '    value = int(input())\n'
                                             '    # Skip negative values and print the others:\n',
                             'solution_code': 'for _ in range(5):\n'
                                              '    value = int(input())\n'
                                              '    if value < 0:\n'
                                              '        continue\n'
                                              '    print(value)',
                             'test_cases': [{'input_data': '10\n-5\n20\n-2\n30\n',
                                             'expected_output': '10\n20\n30',
                                             'is_hidden': False},
                                            {'input_data': '-1\n0\n2\n-3\n4\n',
                                             'expected_output': '0\n2\n4',
                                             'is_hidden': False}],
                             'hints': ['Read five whole numbers. Use continue to skip a number below 0. '
                                       'Print every number that is 0 or more.',
                                       'Complete solution:\n'
                                       'for _ in range(5):\n'
                                       '    value = int(input())\n'
                                       '    if value < 0:\n'
                                       '        continue\n'
                                       '    print(value)'],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Keep Valid Scores',
                             'description': 'Your task, step by step:\n1. Read five scores.\n2. Skip each score below 0 with continue.\n3. Print Valid: and every score that is 0 or more.\n\nInput for this example: The Input box shows 5 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read five scores. Skip each score below 0 with continue. Print '
                                             'Valid: and every score that is 0 or more.',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': 'for _ in range(5):\n'
                                             '    score = int(input())\n'
                                             '    # Skip a score below 0 and print the others:\n',
                             'solution_code': 'for _ in range(5):\n'
                                              '    score = int(input())\n'
                                              '    if score < 0:\n'
                                              '        continue\n'
                                              "    print(f'Valid: {score}')",
                             'test_cases': [{'input_data': '10\n-5\n20\n-2\n30\n',
                                             'expected_output': 'Valid: 10\nValid: 20\nValid: 30',
                                             'is_hidden': False},
                                            {'input_data': '0\n-1\n5\n-9\n8\n',
                                             'expected_output': 'Valid: 0\nValid: 5\nValid: 8',
                                             'is_hidden': False}],
                             'hints': ['Read five scores. Skip each score below 0 with continue. Print '
                                       'Valid: and every score that is 0 or more.',
                                       'Complete solution:\n'
                                       'for _ in range(5):\n'
                                       '    score = int(input())\n'
                                       '    if score < 0:\n'
                                       '        continue\n'
                                       "    print(f'Valid: {score}')"],
                             'xp_reward': 150}],
             'description': 'Skip the current iteration and advance immediately to the next.',
             'lesson': {'common_mistakes': [{'fix': 'Use break to stop; use continue to skip.',
                                             'mistake': 'Confusing break and continue',
                                             'why': 'break kills the entire loop; continue only skips the '
                                                    'current iteration.'}],
                        'detailed_explanation': 'continue skips the rest of the current turn through a loop, '
                                                'then starts the next turn. The loop itself keeps going.\n'
                                                '\n'
                                                'For example, while checking numbers 1 through 5, continue '
                                                'can skip number 3. Python still checks 4 and 5. Use it when '
                                                'some items should be ignored but you still want to process '
                                                'the rest.\n'
                                                '\n'
                                                'break and continue are different: break ends the current '
                                                'loop; continue skips one turn.',
                        'expected_output': 'Odd: 1\nOdd: 3\nOdd: 5',
                        'introduction': "While `break` says 'I am quitting this entire loop right now!', "
                                        "`continue` says 'I am skipping ONLY this specific item—let's move "
                                        "on to the next one!'",
                        'learning_objectives': ['Understand how the continue statement differs from break',
                                                'Skip unwanted or invalid items without terminating the '
                                                'entire loop',
                                                'Filter sequences during iteration cleanly'],
                        'line_by_line': [{'line': '1', 'code': "records = ['User1', 'CORRUPT', 'User2', 'CORRUPT', 'User3']", 'explanation': 'Create a list named records with User1, CORRUPT, User2, CORRUPT and User3 in this order. A loop can take one item from the list at a time.'}, {'line': '2', 'code': 'for r in records:', 'explanation': 'Take each item from records in order. During each turn, r holds the current item.'}, {'line': '3', 'code': "    if r == 'CORRUPT':", 'explanation': "Check whether r is the same as 'CORRUPT'. If that is true, run the indented lines below; otherwise, skip them."}, {'line': '4', 'code': '        continue', 'explanation': 'Skip the rest of this turn and move to the next loop item.'}, {'line': '5', 'code': "    print('Syncing valid:', r)", 'explanation': "Show the text 'Syncing valid:', followed by the current value of r. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Skipping corrupt records',
                                                'code': "records = ['User1', 'CORRUPT', 'User2', 'CORRUPT', "
                                                        "'User3']\n"
                                                        'for r in records:\n'
                                                        "    if r == 'CORRUPT':\n"
                                                        '        continue\n'
                                                        "    print('Syncing valid:', r)",
                                                'explanation': "continue bypasses 'CORRUPT' entries and "
                                                               'processes only legitimate records.',
                                                'output': 'Syncing valid: User1\n'
                                                          'Syncing valid: User2\n'
                                                          'Syncing valid: User3'},
                                               {'title': 'Example 2: Skipping free tier users in billing',
                                                'code': "tiers = ['premium', 'free', 'enterprise', 'free']\n"
                                                        'for t in tiers:\n'
                                                        "    if t == 'free':\n"
                                                        '        continue\n'
                                                        "    print('Generating invoice for tier:', t)",
                                                'explanation': 'Skips invoices for free accounts while '
                                                               'processing paid subscribers.',
                                                'output': 'Generating invoice for tier: premium\n'
                                                          'Generating invoice for tier: enterprise'},
                                               {'title': 'Example 3: Printing non-zero coordinates',
                                                'code': 'points = [5, 0, 12, 0, 9]\n'
                                                        'for p in points:\n'
                                                        '    if p == 0:\n'
                                                        '        continue\n'
                                                        "    print('Active coordinate:', p)",
                                                'explanation': 'Skips dead 0 values and outputs only '
                                                               'non-zero coordinates.',
                                                'output': 'Active coordinate: 5\n'
                                                          'Active coordinate: 12\n'
                                                          'Active coordinate: 9'}],
                        'practice_questions': ['What is the difference in behavior between break and '
                                               'continue?',
                                               'If a loop iterates from 1 to 5 and has if i == 3: continue, '
                                               'which numbers are printed?'],
                        'prerequisites': 'Level 44: break Statement',
                        'real_world_apps': 'Skipping blank lines when reading configuration files, bypassing '
                                           'empty database rows, ignoring spam messages in email queues.',
                        'summary': 'continue skips one turn and moves to the next. break ends the current '
                                   'loop.',
                        'syntax_breakdown': "# The 'continue' statement skips the REST of the CURRENT "
                                            'iteration\n'
                                            '# and jumps directly to the NEXT cycle:\n'
                                            'numbers = [1, 2, 3, 4, 5]\n'
                                            '\n'
                                            'for num in numbers:\n'
                                            '    if num % 2 != 0:\n'
                                            '        continue  # Skip odd numbers!\n'
                                            "    print('Even number:', num)\n"
                                            '\n'
                                            "print('Filtered scan complete.')",
                        'terminology': [{'definition': 'A Python control statement that skips the remainder '
                                                       'of the current iteration and advances to the next '
                                                       'iteration.',
                                         'term': 'continue'},
                                        {'definition': 'Using continue to bypass invalid or unwanted values '
                                                       'in a data stream.',
                                         'term': 'Filter Pattern'}]},
             'number': 45,
             'quizzes': [{'question': 'What does this code print?\n'
                                      '\n'
                                      'for n in range(1, 5):\n'
                                      '    if n == 2:\n'
                                      '        continue\n'
                                      '    print(n)',
                          'explanation': 'continue skips the print for 2, then the loop continues.',
                          'options': [{'text': '1, 3, 4',
                                       'is_correct': True,
                                       'explanation': 'Correct. continue skips the print for 2, then the '
                                                      'loop continues.'},
                                      {'text': '1 only',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '1, 2, 3, 4',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'How is continue different from break?',
                          'explanation': 'continue skips this turn; break exits the current loop.',
                          'options': [{'text': 'continue skips a turn; break ends the loop',
                                       'is_correct': True,
                                       'explanation': 'Correct. continue skips this turn; break exits the '
                                                      'current loop.'},
                                      {'text': 'Both end the loop',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'continue repeats the same turn',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'break skips just one turn',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'continue Statement'},
            {'challenges': [{'title': 'Make a Small Grid',
                             'description': 'Your task, step by step:\n1. Use two loops: row in range(2) and column in range(3).\n2. Print each coordinate like (row, column), from (0, 0) through (1, 2).\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 6 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Use two loops: row in range(2) and column in range(3). Print '
                                             'each coordinate like (row, column), from (0, 0) through (1, '
                                             '2).',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': '\n# Add the outside row loop and inside column loop:\n',
                             'solution_code': 'for row in range(2):\n'
                                              '    for column in range(3):\n'
                                              "        print(f'({row}, {column})')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': '(0, 0)\n'
                                                                '(0, 1)\n'
                                                                '(0, 2)\n'
                                                                '(1, 0)\n'
                                                                '(1, 1)\n'
                                                                '(1, 2)',
                                             'is_hidden': False}],
                             'hints': ['Use two loops: row in range(2) and column in range(3). Print each '
                                       'coordinate like (row, column), from (0, 0) through (1, 2).',
                                       'Complete solution:\n'
                                       'for row in range(2):\n'
                                       '    for column in range(3):\n'
                                       "        print(f'({row}, {column})')"],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Star Steps',
                             'description': 'Your task, step by step:\n1. Read a height.\n2. Print a staircase: line 1 has one star, line 2 has two stars, and so on up to the height.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read a height. Print a staircase: line 1 has one star, line 2 '
                                             'has two stars, and so on up to the height.',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': 'height = int(input())\n\n# Print one more star on each row:\n',
                             'solution_code': 'height = int(input())\n'
                                              'for row in range(1, height + 1):\n'
                                              "    print('*' * row)",
                             'test_cases': [{'input_data': '4\n',
                                             'expected_output': '*\n**\n***\n****',
                                             'is_hidden': False},
                                            {'input_data': '1\n', 'expected_output': '*', 'is_hidden': False},
                                            {'input_data': '0\n', 'expected_output': '', 'is_hidden': False}],
                             'hints': ['Read a height. Print a staircase: line 1 has one star, line 2 has '
                                       'two stars, and so on up to the height.',
                                       'Complete solution:\n'
                                       'height = int(input())\n'
                                       'for row in range(1, height + 1):\n'
                                       "    print('*' * row)"],
                             'xp_reward': 150}],
             'description': 'Run loops inside loops for matrices, grids, and combinations.',
             'lesson': {'common_mistakes': [{'fix': 'Always use distinct variable names (e.g. row/col or '
                                                    'i/j).',
                                             'mistake': 'Reusing the same loop variable for both outer and '
                                                        'inner loops (e.g. for i in range: for i in range:)',
                                             'why': "The inner loop overwrites the outer loop's counter, "
                                                    'corrupting the execution state.'}],
                        'detailed_explanation': 'A nested loop is a loop inside another loop. For every turn '
                                                'of the outside loop, Python runs the inside loop all the '
                                                'way through.\n'
                                                '\n'
                                                'If there are two rows and three columns, the outside loop '
                                                'picks row 0, then row 1. For each row, the inside loop '
                                                'visits columns 0, 1, and 2. That makes six coordinates.\n'
                                                '\n'
                                                'Nested loops can make grids or check every pair of items. '
                                                'Give the two loops different variable names, like row and '
                                                'column, so it is easier to follow.',
                        'expected_output': '[0,0] [0,1] [0,2] \n[1,0] [1,1] [1,2] ',
                        'introduction': 'How does a digital clock display time? For every 1 hour that '
                                        'passes, the minute hand ticks through 60 minutes! And for every 1 '
                                        'minute, the second hand ticks 60 seconds! That is a nested loop: an '
                                        'inner loop cycling fully for every single tick of an outer loop.',
                        'learning_objectives': ['Understand nested loops (loops inside loops)',
                                                'Track outer loop cycles vs inner loop cycles',
                                                'Calculate coordinates for grids, matrices, and game boards'],
                        'line_by_line': [{'line': '1', 'code': 'for r in range(1, 3):', 'explanation': 'range(1, 3) gives 1 and 2; it stops before the ending number. Python repeats the indented lines with the current number saved in r.'}, {'line': '2', 'code': '    for c in range(1, 3):', 'explanation': 'range(1, 3) gives 1 and 2; it stops before the ending number. Python repeats the indented lines with the current number saved in c.'}, {'line': '3', 'code': "        print('Sector (' + str(r) + ',' + str(c) + ')')", 'explanation': "Work out 'Sector (' + str(r) + ',' + str(c) + ')', then show the answer on the screen."}],
                        'practical_examples': [{'title': 'Example 1: 2D Matrix coordinate map',
                                                'code': 'for r in range(1, 3):\n'
                                                        '    for c in range(1, 3):\n'
                                                        "        print('Sector (' + str(r) + ',' + str(c) + "
                                                        "')')",
                                                'explanation': 'Produces all combinations of rows (1, 2) and '
                                                               'columns (1, 2).',
                                                'output': 'Sector (1,1)\n'
                                                          'Sector (1,2)\n'
                                                          'Sector (2,1)\n'
                                                          'Sector (2,2)'},
                                               {'title': 'Example 2: Multi-day schedule planner',
                                                'code': "days = ['Mon', 'Tue']\n"
                                                        "sessions = ['Morning', 'Evening']\n"
                                                        'for d in days:\n'
                                                        '    for s in sessions:\n'
                                                        "        print(d + ' - ' + s)",
                                                'explanation': 'Generates a full schedule combining each day '
                                                               'with each shift.',
                                                'output': 'Mon - Morning\n'
                                                          'Mon - Evening\n'
                                                          'Tue - Morning\n'
                                                          'Tue - Evening'},
                                               {'title': 'Example 3: Character visual box pattern',
                                                'code': 'for i in range(2):\n'
                                                        "    line = ''\n"
                                                        '    for j in range(3):\n'
                                                        "        line += '# '\n"
                                                        '    print(line)',
                                                'explanation': 'Constructs a 2x3 hashtag grid line by line.',
                                                'output': '# # # \n# # # '}],
                        'practice_questions': ['If an outer loop runs 4 times and an inner loop runs 5 '
                                               'times, how many total iterations occur?',
                                               'Why must outer and inner loops use distinct variable names?'],
                        'prerequisites': 'Level 45: continue Statement',
                        'real_world_apps': 'Pixel processing in image filters, 2D game map generation '
                                           '(Minecraft chunks), matrix math in machine learning.',
                        'summary': 'The inner loop completes for every turn of the outer loop. Two rows '
                                   'times three columns makes six coordinate pairs.',
                        'syntax_breakdown': '# Nested Loops: A loop inside another loop\n'
                                            '# For each cycle of the OUTER loop, the INNER loop completes '
                                            'ALL its iterations:\n'
                                            'for row in [1, 2]:\n'
                                            "    for col in ['A', 'B']:\n"
                                            "        print('Grid cell:', row, col)\n"
                                            '\n'
                                            "print('Grid traversal complete.')",
                        'terminology': [{'definition': 'A loop statement placed inside the body of another '
                                                       'loop.',
                                         'term': 'Nested Loop'},
                                        {'definition': 'The encompassing loop that governs the primary '
                                                       'high-level iterations.',
                                         'term': 'Outer Loop'},
                                        {'definition': 'The nested loop that completes a full cycle for each '
                                                       'individual step of the outer loop.',
                                         'term': 'Inner Loop'}]},
             'number': 46,
             'quizzes': [{'question': 'The outer loop runs 2 times and the inner loop 3 times per turn. How '
                                      'many times does the inner print run?',
                          'explanation': 'The inner loop runs three times for each of two outer turns: 2 '
                                         'times 3 equals 6.',
                          'options': [{'text': '6 times',
                                       'is_correct': True,
                                       'explanation': 'Correct. The inner loop runs three times for each of '
                                                      'two outer turns: 2 times 3 equals 6.'},
                                      {'text': '5 times',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '3 times',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '2 times',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'What pairs does this code print?\n'
                                      '\n'
                                      'for row in range(2):\n'
                                      '    for col in range(2):\n'
                                      '        print(row, col)',
                          'explanation': 'For row 0, columns 0 and 1 run; then the same happens for row 1.',
                          'options': [{'text': '0 0, 0 1, 1 0, 1 1',
                                       'is_correct': True,
                                       'explanation': 'Correct. For row 0, columns 0 and 1 run; then the '
                                                      'same happens for row 1.'},
                                      {'text': '0 0, 1 1',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '0 0, 0 1',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '1 1 only',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'Nested Loops'},
            {'challenges': [{'title': 'Count Safely to Four',
                             'description': 'Your task, step by step:\n1. Start at 1.\n2. Use a while loop to print 1, 2, 3, 4.\n3. Update the counter every turn so the loop stops.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Start at 1. Use a while loop to print 1, 2, 3, 4. Update the '
                                             'counter every turn so the loop stops.',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': 'count = 1\n\n# Write a while loop that updates count:\n',
                             'solution_code': 'count = 1\n'
                                              'while count <= 4:\n'
                                              '    print(count)\n'
                                              '    count += 1',
                             'test_cases': [{'input_data': '',
                                             'expected_output': '1\n2\n3\n4',
                                             'is_hidden': False}],
                             'hints': ['Start at 1. Use a while loop to print 1, 2, 3, 4. Update the counter '
                                       'every turn so the loop stops.',
                                       'Complete solution:\n'
                                       'count = 1\n'
                                       'while count <= 4:\n'
                                       '    print(count)\n'
                                       '    count += 1'],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Safe Halving',
                             'description': 'Your task, step by step:\n1. Read a positive whole number.\n2. While it is bigger than 1 and you have taken fewer than 10 steps, divide it by 2 using whole-number division.\n3. Print the number of steps and the final number.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read a positive whole number. While it is bigger than 1 and '
                                             'you have taken fewer than 10 steps, divide it by 2 using '
                                             'whole-number division. Print the number of steps and the final '
                                             'number.',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': 'number = int(input())\n'
                                             'steps = 0\n'
                                             '\n'
                                             '# Keep halving safely below:\n',
                             'solution_code': 'number = int(input())\n'
                                              'steps = 0\n'
                                              'while number > 1 and steps < 10:\n'
                                              '    number //= 2\n'
                                              '    steps += 1\n'
                                              "print(f'Steps: {steps}')\n"
                                              "print(f'Final number: {number}')",
                             'test_cases': [{'input_data': '16\n',
                                             'expected_output': 'Steps: 4\nFinal number: 1',
                                             'is_hidden': False},
                                            {'input_data': '1000\n',
                                             'expected_output': 'Steps: 9\nFinal number: 1',
                                             'is_hidden': False},
                                            {'input_data': '1\n',
                                             'expected_output': 'Steps: 0\nFinal number: 1',
                                             'is_hidden': False}],
                             'hints': ['Read a positive whole number. While it is bigger than 1 and you have '
                                       'taken fewer than 10 steps, divide it by 2 using whole-number '
                                       'division. Print the number of steps and the final number.',
                                       'Complete solution:\n'
                                       'number = int(input())\n'
                                       'steps = 0\n'
                                       'while number > 1 and steps < 10:\n'
                                       '    number //= 2\n'
                                       '    steps += 1\n'
                                       "print(f'Steps: {steps}')\n"
                                       "print(f'Final number: {number}')"],
                             'xp_reward': 150}],
             'description': 'Recognize loop termination conditions and avoid system hangs.',
             'lesson': {'common_mistakes': [{'fix': 'Use >= or <= rather than exact != when incrementing by '
                                                    'steps.',
                                             'mistake': 'while x != 10: with x += 2 starting at 1',
                                             'why': 'x takes values 1, 3, 5, 7, 9, 11, 13... It skips 10 '
                                                    'completely and runs forever!'}],
                        'detailed_explanation': 'An infinite loop never reaches its stopping point. One '
                                                'common cause is forgetting to change the value in a while '
                                                'condition. If count starts at 1 and the code only prints '
                                                'count while count < 4, count stays 1 and the condition '
                                                'stays True forever.\n'
                                                '\n'
                                                'To fix this, change count inside the loop so it moves '
                                                'toward the stopping point. You can also add a maximum turn '
                                                'limit as an extra safety check. Before running a while '
                                                'loop, ask: what changes each turn, and when will the '
                                                'condition become False? If a program gets stuck in a '
                                                'terminal, Ctrl+C usually stops it.',
                        'expected_output': 'Attempt 1 processed\n'
                                           'Attempt 2 processed\n'
                                           'Attempt 3 processed\n'
                                           'Safely completed',
                        'introduction': 'Have you ever seen an app freeze, showing a spinning beach ball or '
                                        "'Not Responding' dialog? In many cases, that freeze is caused by an "
                                        'infinite loop: a loop that never reaches a stopping condition and '
                                        'runs forever, eating 100% of a CPU core.',
                        'learning_objectives': ['Understand what causes an infinite loop in computer '
                                                'software',
                                                'Identify non-terminating while loop conditions',
                                                'Use timeout guards, maximum iteration caps, and break '
                                                'conditions to prevent infinite loops'],
                        'line_by_line': [{'line': '1', 'code': 'step = 0', 'explanation': 'Store the number 0 in step.'}, {'line': '2', 'code': 'while step < 3:', 'explanation': 'Repeat the indented lines below while step is less than 3 is true. The loop changes a value so this check can eventually become false.'}, {'line': '3', 'code': "    print('Step:', step)", 'explanation': "Show the text 'Step:', followed by the current value of step. Python puts a space between comma-separated print items."}, {'line': '4', 'code': '    step += 1  # Crucial increment!', 'explanation': 'Add 1  # Crucial increment! to step and save the new value back in step.'}, {'line': '5', 'code': "print('Loop exited safely.')", 'explanation': "Show the text 'Loop exited safely.' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Preventing infinite while loops',
                                                'code': 'step = 0\n'
                                                        'while step < 3:\n'
                                                        "    print('Step:', step)\n"
                                                        '    step += 1  # Crucial increment!\n'
                                                        "print('Loop exited safely.')",
                                                'explanation': 'Ensures the state variable advances toward '
                                                               'termination condition on every loop cycle.',
                                                'output': 'Step: 0\nStep: 1\nStep: 2\nLoop exited safely.'},
                                               {'title': 'Example 2: Understanding range(1, n+1) boundary',
                                                'code': "print('1 to 3 inclusive:')\n"
                                                        'for i in range(1, 4):\n'
                                                        '    print(i)',
                                                'explanation': 'To include the number 3, the stop parameter '
                                                               'must be 4.',
                                                'output': '1 to 3 inclusive:\n1\n2\n3'},
                                               {'title': 'Example 3: Modifying a list while iterating over '
                                                         'it (Bug & Fix)',
                                                'code': "items = ['a', 'b', 'c']\n"
                                                        '# Safe: Iterate over a copy items[:]\n'
                                                        'for it in items[:]:\n'
                                                        "    print('Inspecting:', it)",
                                                'explanation': 'Iterating over a slice copy items[:] '
                                                               'prevents skipping items during deletion.',
                                                'output': 'Inspecting: a\nInspecting: b\nInspecting: c'}],
                        'practice_questions': ['Why can while x != 10: be dangerous if x starts at 1 and '
                                               'increases by 2?',
                                               'What is a watchdog counter?'],
                        'prerequisites': 'Level 46: Nested Loops',
                        'real_world_apps': 'Network timeout handlers in web browsers, game physics '
                                           'convergence limits, robot obstacle avoidance fail-safes.',
                        'summary': 'A while loop needs a way to become False. Update the value in its '
                                   'condition and consider a safety limit.',
                        'syntax_breakdown': '# Trap 1: Forgetting to update loop variable in while (INFINITE '
                                            'LOOP!)\n'
                                            '# count = 1\n'
                                            '# while count <= 3:\n'
                                            '#     print(count)  <-- NEVER finishes because count never '
                                            'changes!\n'
                                            '\n'
                                            '# Fix: Always update counter:\n'
                                            'count = 1\n'
                                            'while count <= 3:\n'
                                            "    print('Safe count:', count)\n"
                                            '    count += 1\n'
                                            '\n'
                                            '# Trap 2: Off-by-one errors with range()\n'
                                            '# range(5) produces 0, 1, 2, 3, 4 (DOES NOT include 5!)',
                        'terminology': [{'definition': 'A sequence of instructions that loops endlessly '
                                                       'because its termination condition is never reached.',
                                         'term': 'Infinite Loop'},
                                        {'definition': 'A safety counter that forcibly terminates an '
                                                       'algorithm if it exceeds an emergency threshold of '
                                                       'iterations.',
                                         'term': 'Watchdog / Circuit Breaker'}]},
             'number': 47,
             'quizzes': [{'question': 'Why does this loop stop?\n'
                                      '\n'
                                      'count = 1\n'
                                      'while count <= 3:\n'
                                      '    print(count)\n'
                                      '    count += 1',
                          'explanation': 'count increases. After printing 3 it becomes 4, so the condition '
                                         'is False.',
                          'options': [{'text': 'count becomes 4',
                                       'is_correct': True,
                                       'explanation': 'Correct. count increases. After printing 3 it becomes '
                                                      '4, so the condition is False.'},
                                      {'text': 'print stops the loop',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'It never stops',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'It runs once',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'What is wrong with this code?\n'
                                      '\n'
                                      'count = 1\n'
                                      'while count <= 3:\n'
                                      '    print(count)',
                          'explanation': 'count never changes, so the condition stays True and the loop does '
                                         'not end.',
                          'options': [{'text': 'count never changes',
                                       'is_correct': True,
                                       'explanation': 'Correct. count never changes, so the condition stays '
                                                      'True and the loop does not end.'},
                                      {'text': 'It stops after 3',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'It prints 1, 2, 3',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'while cannot use numbers',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'Infinite Loops and Prevention'},
            {'challenges': [{'title': 'Number Guessing Game',
                             'description': 'Your task, step by step:\n1. The secret number is 42.\n2. Read guesses until it is found.\n3. Print Higher for a smaller guess and Lower for a larger guess.\n4. When correct, print the success message and the number of attempts.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'The secret number is 42. Read guesses until it is found. Print '
                                             'Higher for a smaller guess and Lower for a larger guess. When '
                                             'correct, print the success message and the number of attempts.',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'initial_code': 'secret = 42\n'
                                             'attempts = 0\n'
                                             '\n'
                                             '# Ask for guesses until the secret is found:\n',
                             'solution_code': 'secret = 42\n'
                                              'attempts = 0\n'
                                              'while True:\n'
                                              '    guess = int(input())\n'
                                              '    attempts += 1\n'
                                              '    if guess < secret:\n'
                                              "        print('Higher')\n"
                                              '    elif guess > secret:\n'
                                              "        print('Lower')\n"
                                              '    else:\n'
                                              "        print('Correct! You found the secret number.')\n"
                                              '        break\n'
                                              "print(f'Attempts: {attempts}')",
                             'test_cases': [{'input_data': '20\n50\n42\n',
                                             'expected_output': 'Higher\n'
                                                                'Lower\n'
                                                                'Correct! You found the secret number.\n'
                                                                'Attempts: 3',
                                             'is_hidden': False},
                                            {'input_data': '42\n',
                                             'expected_output': 'Correct! You found the secret number.\n'
                                                                'Attempts: 1',
                                             'is_hidden': False}],
                             'hints': ['The secret number is 42. Read guesses until it is found. Print '
                                       'Higher for a smaller guess and Lower for a larger guess. When '
                                       'correct, print the success message and the number of attempts.',
                                       'Complete solution:\n'
                                       'secret = 42\n'
                                       'attempts = 0\n'
                                       'while True:\n'
                                       '    guess = int(input())\n'
                                       '    attempts += 1\n'
                                       '    if guess < secret:\n'
                                       "        print('Higher')\n"
                                       '    elif guess > secret:\n'
                                       "        print('Lower')\n"
                                       '    else:\n'
                                       "        print('Correct! You found the secret number.')\n"
                                       '        break\n'
                                       "print(f'Attempts: {attempts}')"],
                             'xp_reward': 30},
                            {'title': 'Boss Challenge: Prime Check with break',
                             'description': 'Your task, step by step:\n1. Read a whole number n.\n2. If it is below 2, print that it is not prime.\n3. Otherwise, check numbers from 2 up to n - 1.\n4. If one divides n evenly, print that n is not prime and use break.\n5. If none divide it evenly, print that n is prime.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Read a whole number n. If it is below 2, print that it is not '
                                             'prime. Otherwise, check numbers from 2 up to n - 1. If one '
                                             'divides n evenly, print that n is not prime and use break. If '
                                             'none divide it evenly, print that n is prime.',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'initial_code': 'n = int(input())\n'
                                             '\n'
                                             '# Check possible divisors and report the result:\n',
                             'solution_code': 'n = int(input())\n'
                                              'if n < 2:\n'
                                              "    print(f'{n} is not prime')\n"
                                              'else:\n'
                                              '    is_prime = True\n'
                                              '    for divisor in range(2, n):\n'
                                              '        if n % divisor == 0:\n'
                                              '            is_prime = False\n'
                                              '            break\n'
                                              '    if is_prime:\n'
                                              "        print(f'{n} is prime')\n"
                                              '    else:\n'
                                              "        print(f'{n} is not prime')",
                             'test_cases': [{'input_data': '1\n',
                                             'expected_output': '1 is not prime',
                                             'is_hidden': False},
                                            {'input_data': '9\n',
                                             'expected_output': '9 is not prime',
                                             'is_hidden': False},
                                            {'input_data': '17\n',
                                             'expected_output': '17 is prime',
                                             'is_hidden': False},
                                            {'input_data': '2\n',
                                             'expected_output': '2 is prime',
                                             'is_hidden': False}],
                             'hints': ['A prime number is greater than 1 and has no divisor except 1 and '
                                       'itself.',
                                       'Try divisors from 2 up to n - 1. If n % divisor is 0, set is_prime '
                                       'to False and use break.',
                                       'n = int(input())\n'
                                       'if n < 2:\n'
                                       "    print(f'{n} is not prime')\n"
                                       'else:\n'
                                       '    is_prime = True\n'
                                       '    for divisor in range(2, n):\n'
                                       '        if n % divisor == 0:\n'
                                       '            is_prime = False\n'
                                       '            break\n'
                                       '    if is_prime:\n'
                                       "        print(f'{n} is prime')\n"
                                       '    else:\n'
                                       "        print(f'{n} is not prime')"],
                             'xp_reward': 150}],
             'description': 'Synthesize loops, counters, and controls to build the Number Guessing Game.',
             'lesson': {'common_mistakes': [{'fix': 'Increment attempts += 1 on each guess.',
                                             'mistake': 'Forgetting to increment attempt counter',
                                             'why': 'Tracking attempts is required to provide accurate game '
                                                    'statistics.'}],
                        'detailed_explanation': 'This level reviews the loop tools from World 5. Use for '
                                                'when you know the items or repeat count. Use while when a '
                                                'condition decides when to stop. Use range() to make a '
                                                'counting pattern, break to leave early, and continue to '
                                                'skip one turn.\n'
                                                '\n'
                                                'In the guessing game, the player tries to find 42. Each '
                                                'guess increases the attempt count. If it is too small, '
                                                'print Higher. If it is too large, print Lower. When it '
                                                'matches, print the success message and use break to end the '
                                                'loop.\n'
                                                '\n'
                                                'Try entering 20, then 50, then 42. The program gives '
                                                'feedback after each guess and stops after the correct '
                                                'answer.',
                        'expected_output': 'Higher',
                        'introduction': 'Welcome to the World 5 Examination! You have mastered loops, while '
                                        'iteration, for loops, range(), break, continue, nested structures, '
                                        'and loop safety guards. Now you will construct the Capstone '
                                        'Project: The Number Guessing Game.',
                        'learning_objectives': ['Synthesize all concepts from World 5 into a complete game '
                                                'simulation',
                                                'Implement while loops with interactive user inputs and '
                                                'break conditions',
                                                'Complete the World 5 Capstone: Number Guessing Game'],
                        'line_by_line': [{'line': '1', 'code': 'crates = [45, 12, 80, 5, 60]', 'explanation': 'Create a list named crates with the numbers 45, 12, 80, 5 and 60 in this order. A loop can check one number at a time.'}, {'line': '2', 'code': 'restock_needed = 0', 'explanation': 'Store the number 0 in restock_needed.'}, {'line': '3', 'code': 'for c in crates:', 'explanation': 'Take each item from crates in order. During each turn, c holds the current item.'}, {'line': '4', 'code': '    if c < 15:', 'explanation': 'Check whether c is less than 15. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '5', 'code': '        restock_needed += 1', 'explanation': 'Add 1 to restock_needed and save the new value back in restock_needed.'}, {'line': '6', 'code': "print('Total low-stock crates needing refill:', restock_needed)", 'explanation': "Show the text 'Total low-stock crates needing refill:', followed by the current value of restock_needed. Python puts a space between comma-separated print items."}],
                        'practical_examples': [{'title': 'Example 1: Total inventory audit with threshold '
                                                         'alerts',
                                                'code': 'crates = [45, 12, 80, 5, 60]\n'
                                                        'restock_needed = 0\n'
                                                        'for c in crates:\n'
                                                        '    if c < 15:\n'
                                                        '        restock_needed += 1\n'
                                                        "print('Total low-stock crates needing refill:', "
                                                        'restock_needed)',
                                                'explanation': 'Scans crate quantities and tallies how many '
                                                               'fall below safety threshold 15.',
                                                'output': 'Total low-stock crates needing refill: 2'},
                                               {'title': 'Example 2: Transaction ledger batch processor',
                                                'code': 'transactions = [100, -25, -50, 200, -10]\n'
                                                        'balance = 500\n'
                                                        'for t in transactions:\n'
                                                        '    balance += t\n'
                                                        "print('Final Reconciled Balance: $', balance)",
                                                'explanation': 'Applies credits and debits sequentially to '
                                                               'reach the final ledger balance.',
                                                'output': 'Final Reconciled Balance: $ 715'},
                                               {'title': 'Example 3: Sensor telemetry anomaly scan',
                                                'code': 'readings = [98.6, 99.1, 104.5, 98.4]\n'
                                                        'for temp in readings:\n'
                                                        '    if temp > 103.0:\n'
                                                        "        print('CRITICAL FEVER ALERT:', temp)\n"
                                                        '        break',
                                                'explanation': 'Stops temperature monitoring and raises '
                                                               'alarm immediately when dangerous spike '
                                                               'occurs.',
                                                'output': 'CRITICAL FEVER ALERT: 104.5'}],
                        'practice_questions': ['How does break terminate a while True loop?',
                                               'Why is directional feedback (Higher/Lower) helpful in search '
                                               'algorithms?'],
                        'prerequisites': 'Levels 40 through 47',
                        'real_world_apps': 'Interactive terminal games, binary search algorithms, iterative '
                                           'approximation solvers.',
                        'summary': 'Loops repeat instructions. Choose the kind of loop that fits, update '
                                   'while conditions, and use break or continue carefully.',
                        'syntax_breakdown': '# World 5 Capstone: Autonomous Patrol Drone Navigator\n'
                                            'battery = 100\n'
                                            "patrol_sectors = ['Sector-Alpha', 'Sector-Beta', "
                                            "'Sector-Gamma']\n"
                                            '\n'
                                            "print('--- DRONE PATROL COMMENCING ---')\n"
                                            'for sector in patrol_sectors:\n'
                                            '    if battery < 30:\n'
                                            "        print('LOW BATTERY WARNING! Returning to base.')\n"
                                            '        break\n'
                                            "    print('Patrolling:', sector)\n"
                                            '    battery -= 25\n'
                                            '\n'
                                            "print('Patrol ended. Remaining Battery:', battery, '%')",
                        'terminology': [{'definition': 'A central loop that continuously runs the game '
                                                       'state, receives inputs, and checks victory '
                                                       'conditions.',
                                         'term': 'Game Loop'}]},
             'number': 48,
             'quizzes': [{'question': 'What does this code print?\n'
                                      '\n'
                                      'for n in range(1, 5):\n'
                                      '    if n == 3:\n'
                                      '        continue\n'
                                      "    print(n, end=' ')",
                          'explanation': 'continue skips 3, then the loop carries on.',
                          'options': [{'text': '1 2 4',
                                       'is_correct': True,
                                       'explanation': 'Correct. continue skips 3, then the loop carries on.'},
                                      {'text': '1 2',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '1 2 3 4',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': '3 only',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]},
                         {'question': 'In the guessing game, what happens when guess equals secret?',
                          'explanation': 'The matching guess reaches the success branch, and break stops the '
                                         'loop.',
                          'options': [{'text': 'It prints success and stops',
                                       'is_correct': True,
                                       'explanation': 'Correct. The matching guess reaches the success '
                                                      'branch, and break stops the loop.'},
                                      {'text': 'It prints Higher',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'It prints Lower',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'},
                                      {'text': 'It repeats forever',
                                       'is_correct': False,
                                       'explanation': 'Try tracing the loop one turn at a time.'}]}],
             'title': 'World 5 Examination'}],
 'number': 5,
 'title': 'Loops'}
