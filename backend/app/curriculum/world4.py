"""World 4: beginner-friendly conditional decisions curriculum."""

WORLD_4 = {'description': 'Learn how Python makes choices. Start with if, add else and elif, combine conditions, and '
                'practice avoiding common mistakes.',
 'final_project_desc': 'Practice nested decisions with a safe ATM withdrawal check, then combine conditions '
                       'and elif choices in FizzBuzz.',
 'final_project_title': 'ATM Withdrawal and FizzBuzz',
 'goal': 'Learn how Python makes choices using if, else, elif, nested decisions, and combined conditions.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Read True or False.\n2. If the answer is True, print Gate is open.\n3. If it is False, print no gate message.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['Read with input(), compare to the text True using ==, and indent the '
                                       'message under if.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'is_open = input()\nif is_open == "True":\n    print("Gate is open")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read True or False. If the answer is True, print Gate is open. '
                                             'If it is False, print no gate message.',
                             'solution_code': 'is_open = input()\n'
                                              'if is_open == "True":\n'
                                              '    print("Gate is open")',
                             'test_cases': [{'input_data': 'True\n',
                                             'expected_output': 'Gate is open',
                                             'is_hidden': False},
                                            {'input_data': 'False\n',
                                             'expected_output': '',
                                             'is_hidden': False}],
                             'title': 'Gate Status Check',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read a whole-number power level.\n2. At 50 or more print Engines ready otherwise print Backup power.\n3. Then always print Check complete.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Use if/else with power >= 50. Print Check complete after the '
                                       'branches.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'power = int(input())\n'
                                       'if power >= 50:\n'
                                       '    print("Engines ready")\n'
                                       'else:\n'
                                       '    print("Backup power")\n'
                                       'print("Check complete")'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read a whole-number power level. At 50 or more print Engines '
                                             'ready; otherwise print Backup power. Then always print Check '
                                             'complete.',
                             'solution_code': 'power = int(input())\n'
                                              'if power >= 50:\n'
                                              '    print("Engines ready")\n'
                                              'else:\n'
                                              '    print("Backup power")\n'
                                              'print("Check complete")',
                             'test_cases': [{'input_data': '50\n',
                                             'expected_output': 'Engines ready\nCheck complete',
                                             'is_hidden': False},
                                            {'input_data': '49\n',
                                             'expected_output': 'Backup power\nCheck complete',
                                             'is_hidden': False},
                                            {'input_data': '80\n',
                                             'expected_output': 'Engines ready\nCheck complete',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Power Level Warning',
                             'xp_reward': 150}],
             'description': 'An if statement lets a program run an instruction only when a question is true. '
                            'Python checks the question, runs the indented lines if the answer is True, then '
                            'continues past them.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'Python checks the condition after the word if and before '
                                                'the colon. A condition is a question, such as door_open or '
                                                'score >= 5. If the answer is True, the indented lines are '
                                                'the action for that situation. If the answer is False, '
                                                'Python skips those indented lines. The next line that '
                                                'returns to the left margin is outside the branch and '
                                                'carries on either way. This is why indentation changes what '
                                                'your program does.',
                        'expected_output': 'The door is open\nSensor finished',
                        'introduction': 'An if statement lets a program run an instruction only when a '
                                        'question is true. Python checks the question, runs the indented '
                                        'lines if the answer is True, then continues past them.',
                        'learning_objectives': ['Understand making a choice with if.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'door_open = True', 'explanation': 'Store True in door_open. This variable records a yes-or-no answer.'}, {'line': '2', 'code': 'if door_open:', 'explanation': 'Check whether door_open. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '3', 'code': '    print("The door is open")', 'explanation': "Show the text 'The door is open' on the screen."}, {'line': '4', 'code': 'print("Sensor finished")', 'explanation': "Show the text 'Sensor finished' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Open door',
                                                'code': 'door_open = True\n'
                                                        'if door_open:\n'
                                                        '    print("The door is open")\n'
                                                        'print("Sensor finished")',
                                                'explanation': 'The condition is True, so both messages '
                                                               'appear.',
                                                'output': 'The door is open\nSensor finished'},
                                               {'title': 'Example 2: Cold day',
                                                'code': 'temperature = -5\n'
                                                        'if temperature <= 0:\n'
                                                        '    print("Watch for ice")',
                                                'explanation': '-5 is at most zero, so the warning appears.',
                                                'output': 'Watch for ice'},
                                               {'title': 'Example 3: Closed door',
                                                'code': 'door_open = False\n'
                                                        'if door_open:\n'
                                                        '    print("Come in")\n'
                                                        'print("Goodbye")',
                                                'explanation': 'The condition is False, so Come in is '
                                                               'skipped. Goodbye still appears.',
                                                'output': 'Goodbye'}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'An if statement lets a program run an instruction only when a question '
                                   'is true. Python checks the question, runs the indented lines if the '
                                   'answer is True, then continues past them. if door_open: The indented '
                                   'lines belong to their decision.',
                        'syntax_breakdown': 'if door_open:\n    print("Come in")\nprint("Check finished")',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 31,
             'quizzes': [{'question': 'What does this code print?\n'
                                      '\n'
                                      'is_open = True\n'
                                      'if is_open:\n'
                                      "    print('Gate is open')",
                          'explanation': 'The condition is True, so Python runs the indented print line.',
                          'options': [{'text': 'Gate is open',
                                       'is_correct': True,
                                       'explanation': 'Correct. The if condition is True, so its indented '
                                                      'line runs.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'The if condition is True, so the line inside the if '
                                                      'runs.'},
                                      {'text': 'True',
                                       'is_correct': False,
                                       'explanation': "Python does not print a condition's value unless you "
                                                      'ask it to.'},
                                      {'text': 'SyntaxError',
                                       'is_correct': False,
                                       'explanation': 'This is valid Python: the if line ends with a colon '
                                                      'and the next line is indented.'}]},
                         {'question': 'What does this code print?\n'
                                      '\n'
                                      'energy = 0\n'
                                      'if energy:\n'
                                      "    print('Power on')\n"
                                      'else:\n'
                                      "    print('Power off')",
                          'explanation': 'The number 0 counts as False in an if condition, so Python uses '
                                         'else.',
                          'options': [{'text': 'Power off',
                                       'is_correct': True,
                                       'explanation': 'Correct. Zero is treated as False, so the else branch '
                                                      'runs.'},
                                      {'text': 'Power on',
                                       'is_correct': False,
                                       'explanation': 'Zero is treated as False, so Python skips the if '
                                                      'branch.'},
                                      {'text': '0',
                                       'is_correct': False,
                                       'explanation': 'The program prints the words in the chosen print '
                                                      'statement, not the value of energy.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'The else branch runs and prints Power off.'}]}],
             'title': 'Making a Choice with if'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a whole-number temperature.\n2. Print Freezing alert only when it is zero or below.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['Convert input to int and check temperature <= 0. A one-way if is '
                                       'enough.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'temperature = int(input())\n'
                                       'if temperature <= 0:\n'
                                       '    print("Freezing alert")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read a whole-number temperature. Print Freezing alert only '
                                             'when it is zero or below.',
                             'solution_code': 'temperature = int(input())\n'
                                              'if temperature <= 0:\n'
                                              '    print("Freezing alert")',
                             'test_cases': [{'input_data': '-3\n',
                                             'expected_output': 'Freezing alert',
                                             'is_hidden': False},
                                            {'input_data': '0\n',
                                             'expected_output': 'Freezing alert',
                                             'is_hidden': False},
                                            {'input_data': '8\n', 'expected_output': '', 'is_hidden': False}],
                             'title': 'Freezing Weather Alert',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read a whole-number order total.\n2. If it is 100 or more, subtract 20 and print Discount applied.\n3. Always print Final total: followed by the resulting total.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Use if total >= 100 to subtract 20. Print the final total after the '
                                       'if so it appears for every order.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'total = int(input())\n'
                                       'if total >= 100:\n'
                                       '    total -= 20\n'
                                       '    print("Discount applied")\n'
                                       'print(f"Final total: {total}")'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read a whole-number order total. If it is 100 or more, '
                                             'subtract 20 and print Discount applied. Always print Final '
                                             'total: followed by the resulting total.',
                             'solution_code': 'total = int(input())\n'
                                              'if total >= 100:\n'
                                              '    total -= 20\n'
                                              '    print("Discount applied")\n'
                                              'print(f"Final total: {total}")',
                             'test_cases': [{'input_data': '100\n',
                                             'expected_output': 'Discount applied\nFinal total: 80',
                                             'is_hidden': False},
                                            {'input_data': '99\n',
                                             'expected_output': 'Final total: 99',
                                             'is_hidden': False},
                                            {'input_data': '150\n',
                                             'expected_output': 'Discount applied\nFinal total: 130',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Cart Discount',
                             'xp_reward': 150}],
             'description': 'Use a plain if when there is one special action and nothing else is needed when '
                            'the condition is false. The program simply skips that action and carries on.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'A one-way if is like a motion-sensor light: when the sensor '
                                                'detects movement it turns on, and when it does not, the '
                                                'light instruction is skipped. There is no need to invent a '
                                                'second action if nothing should happen. Lines after the if '
                                                'block still run. Try the exact boundary too: with '
                                                'temperature <= 0, zero counts as freezing because <= '
                                                'includes equality.',
                        'expected_output': 'Watch for ice',
                        'introduction': 'Use a plain if when there is one special action and nothing else is '
                                        'needed when the condition is false. The program simply skips that '
                                        'action and carries on.',
                        'learning_objectives': ['Understand using if for a one-way choice.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'temperature = -3', 'explanation': 'Store the number -3 in temperature.'}, {'line': '2', 'code': 'if temperature <= 0:', 'explanation': 'Check whether temperature is at most 0. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '3', 'code': '    print("Watch for ice")', 'explanation': "Show the text 'Watch for ice' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Freezing',
                                                'code': 'temperature = -3\n'
                                                        'if temperature <= 0:\n'
                                                        '    print("Watch for ice")',
                                                'explanation': 'The temperature is at most zero, so Python '
                                                               'prints the warning.',
                                                'output': 'Watch for ice'},
                                               {'title': 'Example 2: Warm day',
                                                'code': 'temperature = 12\n'
                                                        'if temperature <= 0:\n'
                                                        '    print("Watch for ice")\n'
                                                        'print("Weather check finished")',
                                                'explanation': '12 is warmer than zero, so Python skips the '
                                                               'warning.',
                                                'output': 'Weather check finished'},
                                               {'title': 'Example 3: Free shipping',
                                                'code': 'total = 45\n'
                                                        'if total >= 50:\n'
                                                        '    print("Shipping is free")',
                                                'explanation': '45 is below 50. There is no message because '
                                                               'this one-way choice has no else.',
                                                'output': ''}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'Use a plain if when there is one special action and nothing else is '
                                   'needed when the condition is false. The program simply skips that action '
                                   'and carries on. temperature = 0 The indented lines belong to their '
                                   'decision.',
                        'syntax_breakdown': 'temperature = 0\nif temperature <= 0:\n    print("Freezing")',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 32,
             'quizzes': [{'question': 'A heater should print a warning only when the temperature is 0 or '
                                      'below. What is printed here?\n'
                                      '\n'
                                      'temperature = 0\n'
                                      'if temperature <= 0:\n'
                                      "    print('Freezing')",
                          'explanation': 'The condition uses <=, which includes 0. An if-only choice has no '
                                         'else branch.',
                          'options': [{'text': 'Freezing',
                                       'is_correct': True,
                                       'explanation': 'Correct. 0 is less than or equal to 0, so the '
                                                      'indented message prints.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'The condition is True at 0, so the message prints.'},
                                      {'text': 'Freezing then Nothing',
                                       'is_correct': False,
                                       'explanation': 'The if has one message to print; it does not print a '
                                                      'second message afterward.'},
                                      {'text': 'SyntaxError',
                                       'is_correct': False,
                                       'explanation': 'The condition and indentation are valid Python.'}]},
                         {'question': 'The program warns only at temperatures of 0 or below. What does it '
                                      'print when the temperature is 12?\n'
                                      '\n'
                                      'temperature = 12\n'
                                      'if temperature <= 0:\n'
                                      "    print('Freezing')",
                          'explanation': '12 <= 0 is False. With no else branch, Python skips the indented '
                                         'action and continues.',
                          'options': [{'text': 'Nothing',
                                       'is_correct': True,
                                       'explanation': 'Correct. The condition is False, and there is no else '
                                                      'action to run.'},
                                      {'text': 'Freezing',
                                       'is_correct': False,
                                       'explanation': '12 is above 0, so the condition is False and the '
                                                      'indented line is skipped.'},
                                      {'text': '12',
                                       'is_correct': False,
                                       'explanation': 'The code never asks Python to print the temperature.'},
                                      {'text': 'SyntaxError',
                                       'is_correct': False,
                                       'explanation': 'This is valid Python. An if statement can have no '
                                                      'else branch.'}]}],
             'title': 'Using if for a One-Way Choice'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read age.\n2. Print Access allowed for age 18 or more otherwise print Ask an adult.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['Convert the input to int, then use if age >= 18 and else.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'age = int(input())\n'
                                       'if age >= 18:\n'
                                       '    print("Access allowed")\n'
                                       'else:\n'
                                       '    print("Ask an adult")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read age. Print Access allowed for age 18 or more; otherwise '
                                             'print Ask an adult.',
                             'solution_code': 'age = int(input())\n'
                                              'if age >= 18:\n'
                                              '    print("Access allowed")\n'
                                              'else:\n'
                                              '    print("Ask an adult")',
                             'test_cases': [{'input_data': '18\n',
                                             'expected_output': 'Access allowed',
                                             'is_hidden': False},
                                            {'input_data': '17\n',
                                             'expected_output': 'Ask an adult',
                                             'is_hidden': False},
                                            {'input_data': '25\n',
                                             'expected_output': 'Access allowed',
                                             'is_hidden': False}],
                             'title': 'Age Access Check',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read a whole number.\n2. Print Even when dividing by 2 leaves remainder 0 otherwise print Odd.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Use number % 2 == 0. The percent symbol gives the remainder after '
                                       'division.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'number = int(input())\n'
                                       'if number % 2 == 0:\n'
                                       '    print("Even")\n'
                                       'else:\n'
                                       '    print("Odd")'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read a whole number. Print Even when dividing by 2 leaves '
                                             'remainder 0; otherwise print Odd.',
                             'solution_code': 'number = int(input())\n'
                                              'if number % 2 == 0:\n'
                                              '    print("Even")\n'
                                              'else:\n'
                                              '    print("Odd")',
                             'test_cases': [{'input_data': '8\n',
                                             'expected_output': 'Even',
                                             'is_hidden': False},
                                            {'input_data': '7\n',
                                             'expected_output': 'Odd',
                                             'is_hidden': False},
                                            {'input_data': '0\n',
                                             'expected_output': 'Even',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Even or Odd',
                             'xp_reward': 150}],
             'description': 'Use else when the program needs a second action if the if condition is false. '
                            'Python runs exactly one of the two branches.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'Python checks the if condition first. When it is True, it '
                                                'runs that block and skips else. When it is False, it skips '
                                                'the if block and runs else. This guarantees one of the two '
                                                'outcomes. The two branches should describe the outcomes '
                                                'clearly, and the colon plus indentation mark the start of '
                                                'each group. At age 18, age >= 18 is True; at 17, it is '
                                                'False.',
                        'expected_output': 'Access allowed',
                        'introduction': 'Use else when the program needs a second action if the if condition '
                                        'is false. Python runs exactly one of the two branches.',
                        'learning_objectives': ['Understand choosing between if and else.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'age = 20', 'explanation': 'Store the number 20 in age.'}, {'line': '2', 'code': 'if age >= 18:', 'explanation': 'Check whether age is at least 18. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '3', 'code': '    print("Access allowed")', 'explanation': "Show the text 'Access allowed' on the screen."}, {'line': '4', 'code': 'else:', 'explanation': 'Run the indented lines below only when the earlier if check was false.'}, {'line': '5', 'code': '    print("Ask an adult")', 'explanation': "Show the text 'Ask an adult' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Adult',
                                                'code': 'age = 20\n'
                                                        'if age >= 18:\n'
                                                        '    print("Access allowed")\n'
                                                        'else:\n'
                                                        '    print("Ask an adult")',
                                                'explanation': '20 meets the rule, so Python runs the if '
                                                               'branch.',
                                                'output': 'Access allowed'},
                                               {'title': 'Example 2: Younger visitor',
                                                'code': 'age = 12\n'
                                                        'if age >= 18:\n'
                                                        '    print("Access allowed")\n'
                                                        'else:\n'
                                                        '    print("Ask an adult")',
                                                'explanation': '12 does not meet the rule, so Python runs '
                                                               'else.',
                                                'output': 'Ask an adult'},
                                               {'title': 'Example 3: Even or odd',
                                                'code': 'number = 7\n'
                                                        'if number % 2 == 0:\n'
                                                        '    print("Even")\n'
                                                        'else:\n'
                                                        '    print("Odd")',
                                                'explanation': '% gives a division remainder. 7 leaves '
                                                               'remainder 1, so it is odd.',
                                                'output': 'Odd'}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'Use else when the program needs a second action if the if condition is '
                                   'false. Python runs exactly one of the two branches. age = 12 The '
                                   'indented lines belong to their decision.',
                        'syntax_breakdown': 'age = 12\n'
                                            'if age >= 18:\n'
                                            '    print("Adult")\n'
                                            'else:\n'
                                            '    print("Under 18")',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 33,
             'quizzes': [{'question': 'A ride allows people who are 12 or older. What does this code print '
                                      'for age 12?\n'
                                      '\n'
                                      'age = 12\n'
                                      'if age >= 12:\n'
                                      "    print('You may ride')\n"
                                      'else:\n'
                                      "    print('Please wait')",
                          'explanation': 'The condition is True at the boundary age 12, so the if branch '
                                         'runs and else is skipped.',
                          'options': [{'text': 'You may ride',
                                       'is_correct': True,
                                       'explanation': 'Correct. 12 >= 12 is True, so the if message prints.'},
                                      {'text': 'Please wait',
                                       'is_correct': False,
                                       'explanation': 'The else branch runs only when the condition is '
                                                      'False.'},
                                      {'text': 'Both messages',
                                       'is_correct': False,
                                       'explanation': 'Python runs either the if branch or the else branch, '
                                                      'not both.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'One branch always runs in a complete if/else '
                                                      'statement.'}]},
                         {'question': 'A ride allows people who are 12 or older. What does this code print '
                                      'for age 11?\n'
                                      '\n'
                                      'age = 11\n'
                                      'if age >= 12:\n'
                                      "    print('You may ride')\n"
                                      'else:\n'
                                      "    print('Please wait')",
                          'explanation': '11 >= 12 is False, so Python runs the else branch.',
                          'options': [{'text': 'Please wait',
                                       'is_correct': True,
                                       'explanation': 'Correct. 11 is less than 12, so the else message '
                                                      'prints.'},
                                      {'text': 'You may ride',
                                       'is_correct': False,
                                       'explanation': 'The condition is False for age 11, so the if message '
                                                      'is skipped.'},
                                      {'text': 'Both messages',
                                       'is_correct': False,
                                       'explanation': 'Only one branch runs.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'The else branch prints a message when the condition '
                                                      'is False.'}]}],
             'title': 'Choosing Between if and else'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a score from 0 to 100.\n2. Print A for 90+, B for 80–89, C for 70–79, and Needs practice below 70.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['Check 90 first, then use elif for 80 and 70. Use else for the final '
                                       'range.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'score = int(input())\n'
                                       'if score >= 90:\n'
                                       '    print("A")\n'
                                       'elif score >= 80:\n'
                                       '    print("B")\n'
                                       'elif score >= 70:\n'
                                       '    print("C")\n'
                                       'else:\n'
                                       '    print("Needs practice")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read a score from 0 to 100. Print A for 90+, B for 80–89, C '
                                             'for 70–79, and Needs practice below 70.',
                             'solution_code': 'score = int(input())\n'
                                              'if score >= 90:\n'
                                              '    print("A")\n'
                                              'elif score >= 80:\n'
                                              '    print("B")\n'
                                              'elif score >= 70:\n'
                                              '    print("C")\n'
                                              'else:\n'
                                              '    print("Needs practice")',
                             'test_cases': [{'input_data': '95\n',
                                             'expected_output': 'A',
                                             'is_hidden': False},
                                            {'input_data': '80\n',
                                             'expected_output': 'B',
                                             'is_hidden': False},
                                            {'input_data': '75\n',
                                             'expected_output': 'C',
                                             'is_hidden': False},
                                            {'input_data': '69\n',
                                             'expected_output': 'Needs practice',
                                             'is_hidden': False}],
                             'title': 'Exam Grade Classifier',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read a lowercase color.\n2. Print Stop for red, Wait for yellow, Go for green, or Unknown color for any other input.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Compare each color with ==, use elif for the next colors, and else '
                                       'for unknown colors.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'color = input()\n'
                                       'if color == "red":\n'
                                       '    print("Stop")\n'
                                       'elif color == "yellow":\n'
                                       '    print("Wait")\n'
                                       'elif color == "green":\n'
                                       '    print("Go")\n'
                                       'else:\n'
                                       '    print("Unknown color")'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read a lowercase color. Print Stop for red, Wait for yellow, '
                                             'Go for green, or Unknown color for any other input.',
                             'solution_code': 'color = input()\n'
                                              'if color == "red":\n'
                                              '    print("Stop")\n'
                                              'elif color == "yellow":\n'
                                              '    print("Wait")\n'
                                              'elif color == "green":\n'
                                              '    print("Go")\n'
                                              'else:\n'
                                              '    print("Unknown color")',
                             'test_cases': [{'input_data': 'red\n',
                                             'expected_output': 'Stop',
                                             'is_hidden': False},
                                            {'input_data': 'yellow\n',
                                             'expected_output': 'Wait',
                                             'is_hidden': False},
                                            {'input_data': 'green\n',
                                             'expected_output': 'Go',
                                             'is_hidden': False},
                                            {'input_data': 'blue\n',
                                             'expected_output': 'Unknown color',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Traffic Light Guide',
                             'xp_reward': 150}],
             'description': 'elif means “else if.” It checks another possibility when earlier checks were '
                            'false. Python stops at the first true choice, so put high or specific '
                            'thresholds first.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'Python reads an if/elif/else chain from top to bottom. It '
                                                'checks the first condition; if that fails, it tries the '
                                                'next elif. As soon as one condition is True, it runs that '
                                                'block and skips the rest. This matters for scores: 95 is '
                                                'also at least 70, so a 70 check placed first would '
                                                'incorrectly catch it. Check higher score bands before lower '
                                                'ones, and use else for the remaining values.',
                        'expected_output': 'B',
                        'introduction': 'elif means “else if.” It checks another possibility when earlier '
                                        'checks were false. Python stops at the first true choice, so put '
                                        'high or specific thresholds first.',
                        'learning_objectives': ['Understand checking several choices with elif.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'score = 84', 'explanation': 'Store the number 84 in score.'}, {'line': '2', 'code': 'if score >= 90:', 'explanation': 'Check whether score is at least 90. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '3', 'code': '    print("A")', 'explanation': "Show the text 'A' on the screen."}, {'line': '4', 'code': 'elif score >= 80:', 'explanation': 'If the earlier choices were false, check this next rule: score is at least 80.'}, {'line': '5', 'code': '    print("B")', 'explanation': "Show the text 'B' on the screen."}, {'line': '6', 'code': 'else:', 'explanation': 'Run the indented lines below only when the earlier if check was false.'}, {'line': '7', 'code': '    print("Practice")', 'explanation': "Show the text 'Practice' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Grade B',
                                                'code': 'score = 84\n'
                                                        'if score >= 90:\n'
                                                        '    print("A")\n'
                                                        'elif score >= 80:\n'
                                                        '    print("B")\n'
                                                        'else:\n'
                                                        '    print("Practice")',
                                                'explanation': '84 fails the first check but passes the '
                                                               'elif, so Python prints B.',
                                                'output': 'B'},
                                               {'title': 'Example 2: Traffic light',
                                                'code': 'light = "yellow"\n'
                                                        'if light == "red":\n'
                                                        '    print("Stop")\n'
                                                        'elif light == "yellow":\n'
                                                        '    print("Wait")\n'
                                                        'elif light == "green":\n'
                                                        '    print("Go")\n'
                                                        'else:\n'
                                                        '    print("Unknown")',
                                                'explanation': 'The second comparison matches, so Python '
                                                               'prints Wait and skips later branches.',
                                                'output': 'Wait'},
                                               {'title': 'Example 3: Highest grade first',
                                                'code': 'score = 95\n'
                                                        'if score >= 90:\n'
                                                        '    print("A")\n'
                                                        'elif score >= 70:\n'
                                                        '    print("Passing")',
                                                'explanation': 'The first condition succeeds. Python does '
                                                               'not also print Passing.',
                                                'output': 'A'}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'elif means “else if.” It checks another possibility when earlier checks '
                                   'were false. Python stops at the first true choice, so put high or '
                                   'specific thresholds first. score = 84 The indented lines belong to their '
                                   'decision.',
                        'syntax_breakdown': 'score = 84\n'
                                            'if score >= 90:\n'
                                            '    print("A")\n'
                                            'elif score >= 80:\n'
                                            '    print("B")\n'
                                            'else:\n'
                                            '    print("Keep practicing")',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 34,
             'quizzes': [{'question': 'A score of 84 is checked from top to bottom. Which grade is printed?\n'
                                      '\n'
                                      'score = 84\n'
                                      'if score >= 90:\n'
                                      "    print('A')\n"
                                      'elif score >= 80:\n'
                                      "    print('B')\n"
                                      'else:\n'
                                      "    print('Needs practice')",
                          'explanation': '84 does not reach 90, but it does reach 80. Python stops at the '
                                         'first True choice and prints B.',
                          'options': [{'text': 'B',
                                       'is_correct': True,
                                       'explanation': 'Correct. The first condition is False; score >= 80 is '
                                                      'True.'},
                                      {'text': 'A',
                                       'is_correct': False,
                                       'explanation': '84 is below 90, so the first branch does not run.'},
                                      {'text': 'Needs practice',
                                       'is_correct': False,
                                       'explanation': 'The else branch runs only if all earlier conditions '
                                                      'are False.'},
                                      {'text': 'A and B',
                                       'is_correct': False,
                                       'explanation': 'Python stops after the first matching branch, so it '
                                                      'prints only one grade.'}]},
                         {'question': 'A traffic light program checks red, then yellow, then uses green as '
                                      'the final choice. What does it print for yellow?\n'
                                      '\n'
                                      "light = 'yellow'\n"
                                      "if light == 'red':\n"
                                      "    print('Stop')\n"
                                      "elif light == 'yellow':\n"
                                      "    print('Wait')\n"
                                      'else:\n'
                                      "    print('Go')",
                          'explanation': 'The red check is False. The elif check matches yellow, so Python '
                                         'prints Wait and skips else.',
                          'options': [{'text': 'Wait',
                                       'is_correct': True,
                                       'explanation': 'Correct. The elif condition matches yellow, so that '
                                                      'message prints.'},
                                      {'text': 'Stop',
                                       'is_correct': False,
                                       'explanation': 'The light is not red, so the first branch is '
                                                      'skipped.'},
                                      {'text': 'Go',
                                       'is_correct': False,
                                       'explanation': 'The else branch is skipped because the yellow elif '
                                                      'matched.'},
                                      {'text': 'Stop and Wait',
                                       'is_correct': False,
                                       'explanation': 'Only the first matching branch runs.'}]}],
             'title': 'Checking Several Choices with elif'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read has_key and knows_code on separate lines as True or False.\n2. Unlock only if both are True otherwise print Door stays locked.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['Compare each input with True. Join both checks with and because both '
                                       'are required.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'has_key = input() == "True"\n'
                                       'knows_code = input() == "True"\n'
                                       'if has_key and knows_code:\n'
                                       '    print("Door unlocked")\n'
                                       'else:\n'
                                       '    print("Door stays locked")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read has_key and knows_code on separate lines as True or '
                                             'False. Unlock only if both are True; otherwise print Door '
                                             'stays locked.',
                             'solution_code': 'has_key = input() == "True"\n'
                                              'knows_code = input() == "True"\n'
                                              'if has_key and knows_code:\n'
                                              '    print("Door unlocked")\n'
                                              'else:\n'
                                              '    print("Door stays locked")',
                             'test_cases': [{'input_data': 'True\nTrue\n',
                                             'expected_output': 'Door unlocked',
                                             'is_hidden': False},
                                            {'input_data': 'True\nFalse\n',
                                             'expected_output': 'Door stays locked',
                                             'is_hidden': False},
                                            {'input_data': 'False\nTrue\n',
                                             'expected_output': 'Door stays locked',
                                             'is_hidden': False}],
                             'title': 'Two-Part Door Lock',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read member and large_order as True or False on separate lines.\n2. Print Discount available if either is True otherwise print No discount.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Use or because either qualifying fact is enough.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'member = input() == "True"\n'
                                       'large_order = input() == "True"\n'
                                       'if member or large_order:\n'
                                       '    print("Discount available")\n'
                                       'else:\n'
                                       '    print("No discount")'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read member and large_order as True or False on separate '
                                             'lines. Print Discount available if either is True; otherwise '
                                             'print No discount.',
                             'solution_code': 'member = input() == "True"\n'
                                              'large_order = input() == "True"\n'
                                              'if member or large_order:\n'
                                              '    print("Discount available")\n'
                                              'else:\n'
                                              '    print("No discount")',
                             'test_cases': [{'input_data': 'True\nFalse\n',
                                             'expected_output': 'Discount available',
                                             'is_hidden': False},
                                            {'input_data': 'False\nTrue\n',
                                             'expected_output': 'Discount available',
                                             'is_hidden': False},
                                            {'input_data': 'False\nFalse\n',
                                             'expected_output': 'No discount',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Member or Large Order',
                             'xp_reward': 150}],
             'description': 'and means every joined rule must be true. or means at least one rule must be '
                            'true. These words help describe real requirements clearly.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'Look at each small question separately before joining them. '
                                                'In has_key and knows_code, both comparisons must be True. '
                                                'In member or large_order, either comparison being True is '
                                                'enough. A simple memory trick is: and means all, or means '
                                                'one or more. When you compare a number with a range, both '
                                                'the lower-bound check and upper-bound check must pass, so '
                                                'and is the right word.',
                        'expected_output': 'Stay outside',
                        'introduction': 'and means every joined rule must be true. or means at least one '
                                        'rule must be true. These words help describe real requirements '
                                        'clearly.',
                        'learning_objectives': ['Understand combining conditions with and and or.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'has_key = True', 'explanation': 'Store True in has_key. This variable records a yes-or-no answer.'}, {'line': '2', 'code': 'knows_code = False', 'explanation': 'Store False in knows_code. This variable records a yes-or-no answer.'}, {'line': '3', 'code': 'if has_key and knows_code:', 'explanation': 'Check whether has_key and knows_code. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '4', 'code': '    print("Open")', 'explanation': "Show the text 'Open' on the screen."}, {'line': '5', 'code': 'else:', 'explanation': 'Run the indented lines below only when the earlier if check was false.'}, {'line': '6', 'code': '    print("Stay outside")', 'explanation': "Show the text 'Stay outside' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Both needed',
                                                'code': 'has_key = True\n'
                                                        'knows_code = False\n'
                                                        'if has_key and knows_code:\n'
                                                        '    print("Open")\n'
                                                        'else:\n'
                                                        '    print("Stay outside")',
                                                'explanation': 'and needs both facts to be true. The code '
                                                               'check fails.',
                                                'output': 'Stay outside'},
                                               {'title': 'Example 2: Either is enough',
                                                'code': 'member = False\n'
                                                        'large_order = True\n'
                                                        'if member or large_order:\n'
                                                        '    print("Discount")',
                                                'explanation': 'or needs one true fact, so the large order '
                                                               'qualifies.',
                                                'output': 'Discount'},
                                               {'title': 'Example 3: Check an age range',
                                                'code': 'age = 12\n'
                                                        'if age >= 10 and age <= 15:\n'
                                                        '    print("Middle group")',
                                                'explanation': 'Both comparisons are true, so 12 is in the '
                                                               'range.',
                                                'output': 'Middle group'}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'and means every joined rule must be true. or means at least one rule '
                                   'must be true. These words help describe real requirements clearly. '
                                   'has_key = True The indented lines belong to their decision.',
                        'syntax_breakdown': 'has_key = True\n'
                                            'knows_code = True\n'
                                            'if has_key and knows_code:\n'
                                            '    print("Door unlocked")',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 35,
             'quizzes': [{'question': 'A door opens only when both checks are True. The key check is True '
                                      'and the code check is False. What is has_key and knows_code?\n'
                                      '\n'
                                      'has_key = True\n'
                                      'knows_code = False\n'
                                      'print(has_key and knows_code)',
                          'explanation': 'and needs both sides to be True. Since one side is False, the '
                                         'whole result is False.',
                          'options': [{'text': 'False',
                                       'is_correct': True,
                                       'explanation': 'Correct. With and, both values must be True; one is '
                                                      'False.'},
                                      {'text': 'True',
                                       'is_correct': False,
                                       'explanation': 'and does not pass when either side is False.'},
                                      {'text': 'The key value',
                                       'is_correct': False,
                                       'explanation': 'and checks both values, not just the first one.'},
                                      {'text': 'An error',
                                       'is_correct': False,
                                       'explanation': 'Combining two Boolean values with and is valid '
                                                      'Python.'}]},
                         {'question': 'A museum gives entry to a member or to someone with a large booking. '
                                      'What does this code print?\n'
                                      '\n'
                                      'is_member = False\n'
                                      'large_booking = True\n'
                                      'print(is_member or large_booking)',
                          'explanation': 'or is True when at least one side is True. Here, large_booking is '
                                         'True.',
                          'options': [{'text': 'True',
                                       'is_correct': True,
                                       'explanation': 'Correct. With or, one True value is enough.'},
                                      {'text': 'False',
                                       'is_correct': False,
                                       'explanation': 'or is True because large_booking is True.'},
                                      {'text': 'The word large_booking',
                                       'is_correct': False,
                                       'explanation': 'The code prints the result of the condition, not the '
                                                      'variable name.'},
                                      {'text': 'An error',
                                       'is_correct': False,
                                       'explanation': 'Combining Boolean values with or is valid Python.'}]}],
             'title': 'Combining Conditions with and and or'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read GPA as a decimal and credits as a whole number.\n2. Check credits >= 60 first.\n3. If enough credits, check GPA >= 3.5.\n4. Print Dean list, GPA too low, or More credits needed as appropriate.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['Convert GPA with float and credits with int. Nest the GPA if inside '
                                       'the credits if.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'gpa = float(input())\n'
                                       'credits = int(input())\n'
                                       'if credits >= 60:\n'
                                       '    if gpa >= 3.5:\n'
                                       '        print("Dean list")\n'
                                       '    else:\n'
                                       '        print("GPA too low")\n'
                                       'else:\n'
                                       '    print("More credits needed")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read GPA as a decimal and credits as a whole number. Check '
                                             'credits >= 60 first. If enough credits, check GPA >= 3.5. '
                                             'Print Dean list, GPA too low, or More credits needed as '
                                             'appropriate.',
                             'solution_code': 'gpa = float(input())\n'
                                              'credits = int(input())\n'
                                              'if credits >= 60:\n'
                                              '    if gpa >= 3.5:\n'
                                              '        print("Dean list")\n'
                                              '    else:\n'
                                              '        print("GPA too low")\n'
                                              'else:\n'
                                              '    print("More credits needed")',
                             'test_cases': [{'input_data': '3.8\n60\n',
                                             'expected_output': 'Dean list',
                                             'is_hidden': False},
                                            {'input_data': '3.2\n60\n',
                                             'expected_output': 'GPA too low',
                                             'is_hidden': False},
                                            {'input_data': '4.0\n59\n',
                                             'expected_output': 'More credits needed',
                                             'is_hidden': False}],
                             'title': "Dean's List Check",
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read card_ok and pin_ok as True/False on separate lines, then amount as a whole number.\n2. Check for card, then correct PIN, then approve amounts up to 500.\n3. Print Insert card, Wrong PIN, Amount too large, or Withdrawal approved.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Put the PIN check inside the card check. Put the amount check inside '
                                       'the correct PIN branch.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'card_ok = input() == "True"\n'
                                       'pin_ok = input() == "True"\n'
                                       'amount = int(input())\n'
                                       'if card_ok:\n'
                                       '    if pin_ok:\n'
                                       '        if amount <= 500:\n'
                                       '            print("Withdrawal approved")\n'
                                       '        else:\n'
                                       '            print("Amount too large")\n'
                                       '    else:\n'
                                       '        print("Wrong PIN")\n'
                                       'else:\n'
                                       '    print("Insert card")'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read card_ok and pin_ok as True/False on separate lines, then '
                                             'amount as a whole number. Check for card, then correct PIN, '
                                             'then approve amounts up to 500. Print Insert card, Wrong PIN, '
                                             'Amount too large, or Withdrawal approved.',
                             'solution_code': 'card_ok = input() == "True"\n'
                                              'pin_ok = input() == "True"\n'
                                              'amount = int(input())\n'
                                              'if card_ok:\n'
                                              '    if pin_ok:\n'
                                              '        if amount <= 500:\n'
                                              '            print("Withdrawal approved")\n'
                                              '        else:\n'
                                              '            print("Amount too large")\n'
                                              '    else:\n'
                                              '        print("Wrong PIN")\n'
                                              'else:\n'
                                              '    print("Insert card")',
                             'test_cases': [{'input_data': 'True\nTrue\n200\n',
                                             'expected_output': 'Withdrawal approved',
                                             'is_hidden': False},
                                            {'input_data': 'True\nFalse\n200\n',
                                             'expected_output': 'Wrong PIN',
                                             'is_hidden': False},
                                            {'input_data': 'False\nTrue\n200\n',
                                             'expected_output': 'Insert card',
                                             'is_hidden': False},
                                            {'input_data': 'True\nTrue\n600\n',
                                             'expected_output': 'Amount too large',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Safe ATM Withdrawal',
                             'xp_reward': 150}],
             'description': 'A nested if is an if inside another decision. Python checks the outside rule '
                            'first and reaches the inside rule only if the outer path allows it.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'A nested if works like a checklist with steps. Python must '
                                                'pass the outside check before it can reach the inside '
                                                'check. In the school example it first checks credits. Only '
                                                'a student with enough credits gets their GPA checked. Each '
                                                'deeper level is indented farther to show which decision it '
                                                'belongs to. If the first check fails, the inner check is '
                                                'skipped completely.',
                        'expected_output': 'Honor roll',
                        'introduction': 'A nested if is an if inside another decision. Python checks the '
                                        'outside rule first and reaches the inside rule only if the outer '
                                        'path allows it.',
                        'learning_objectives': ['Understand putting an if inside another if.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'credits = 64', 'explanation': 'Store the number 64 in credits.'}, {'line': '2', 'code': 'gpa = 3.7', 'explanation': 'Store the number 3.7 in gpa.'}, {'line': '3', 'code': 'if credits >= 60:', 'explanation': 'Check whether credits is at least 60. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '4', 'code': '    if gpa >= 3.5:', 'explanation': 'Check whether gpa is at least 3.5. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '5', 'code': '        print("Honor roll")', 'explanation': "Show the text 'Honor roll' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Two school checks',
                                                'code': 'credits = 64\n'
                                                        'gpa = 3.7\n'
                                                        'if credits >= 60:\n'
                                                        '    if gpa >= 3.5:\n'
                                                        '        print("Honor roll")',
                                                'explanation': 'The credit check passes, so Python then '
                                                               'checks the GPA.',
                                                'output': 'Honor roll'},
                                               {'title': 'Example 2: First check fails',
                                                'code': 'credits = 40\n'
                                                        'gpa = 4.0\n'
                                                        'if credits >= 60:\n'
                                                        '    if gpa >= 3.5:\n'
                                                        '        print("Honor roll")\n'
                                                        'else:\n'
                                                        '    print("Earn more credits")',
                                                'explanation': 'The outside rule fails, so Python never '
                                                               'enters the GPA check.',
                                                'output': 'Earn more credits'},
                                               {'title': 'Example 3: ATM safety',
                                                'code': 'card_ok = True\n'
                                                        'pin_ok = False\n'
                                                        'if card_ok:\n'
                                                        '    if pin_ok:\n'
                                                        '        print("Cash ready")\n'
                                                        '    else:\n'
                                                        '        print("Check PIN")',
                                                'explanation': 'The card is accepted, then the inner PIN '
                                                               'check fails.',
                                                'output': 'Check PIN'}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'A nested if is an if inside another decision. Python checks the outside '
                                   'rule first and reaches the inside rule only if the outer path allows it. '
                                   'credits = 64 The indented lines belong to their decision.',
                        'syntax_breakdown': 'credits = 64\n'
                                            'gpa = 3.7\n'
                                            'if credits >= 60:\n'
                                            '    if gpa >= 3.5:\n'
                                            '        print("Honor roll")\n'
                                            '    else:\n'
                                            '        print("Raise GPA")\n'
                                            'else:\n'
                                            '    print("Earn credits")',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 36,
             'quizzes': [{'question': 'What does this nested if code print?\n'
                                      '\n'
                                      'coins = 15\n'
                                      'if coins >= 10:\n'
                                      '    if coins >= 20:\n'
                                      "        print('Bonus')\n"
                                      '    else:\n'
                                      "        print('Prize')\n"
                                      'else:\n'
                                      "    print('Try again')",
                          'explanation': '15 passes the outer check but not the inner check, so the inner '
                                         'else prints Prize.',
                          'options': [{'text': 'Prize',
                                       'is_correct': True,
                                       'explanation': 'Correct. The outer if is True, then the inner if is '
                                                      'False and its else runs.'},
                                      {'text': 'Bonus',
                                       'is_correct': False,
                                       'explanation': '15 is less than 20, so the inner condition is False.'},
                                      {'text': 'Try again',
                                       'is_correct': False,
                                       'explanation': '15 is at least 10, so the outer else is skipped.'},
                                      {'text': 'Prize and Try again',
                                       'is_correct': False,
                                       'explanation': 'Only one nested path runs.'}]},
                         {'question': 'You may enter a game if your pass is valid. A bonus is given only if '
                                      'you also have 5 stars. What prints here?\n'
                                      '\n'
                                      'pass_valid = False\n'
                                      'stars = 5\n'
                                      'if pass_valid:\n'
                                      '    if stars >= 5:\n'
                                      "        print('Bonus entry')\n"
                                      "    print('Enter')\n"
                                      'else:\n'
                                      "    print('Check your pass')",
                          'explanation': 'The outer condition is False, so Python skips both indented lines '
                                         'inside it and runs the outer else.',
                          'options': [{'text': 'Check your pass',
                                       'is_correct': True,
                                       'explanation': 'Correct. The invalid pass makes the outer if False, '
                                                      'so its else runs.'},
                                      {'text': 'Bonus entry',
                                       'is_correct': False,
                                       'explanation': 'The inner check is never reached because the outer '
                                                      'condition is False.'},
                                      {'text': 'Enter',
                                       'is_correct': False,
                                       'explanation': 'Enter is inside the outer if, which is skipped.'},
                                      {'text': 'Bonus entry and Enter',
                                       'is_correct': False,
                                       'explanation': 'Both lines are skipped with the outer if block.'}]}],
             'title': 'Putting an if Inside Another if'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read has_key, knows_code, and alarm_on as True/False on separate lines.\n2. Unlock only with the key and code when the alarm is off.\n3. Otherwise print Door stays locked.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['Join the first two checks with and and require not alarm_on.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'has_key = input() == "True"\n'
                                       'knows_code = input() == "True"\n'
                                       'alarm_on = input() == "True"\n'
                                       'if has_key and knows_code and not alarm_on:\n'
                                       '    print("Door unlocked")\n'
                                       'else:\n'
                                       '    print("Door stays locked")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read has_key, knows_code, and alarm_on as True/False on '
                                             'separate lines. Unlock only with the key and code when the '
                                             'alarm is off. Otherwise print Door stays locked.',
                             'solution_code': 'has_key = input() == "True"\n'
                                              'knows_code = input() == "True"\n'
                                              'alarm_on = input() == "True"\n'
                                              'if has_key and knows_code and not alarm_on:\n'
                                              '    print("Door unlocked")\n'
                                              'else:\n'
                                              '    print("Door stays locked")',
                             'test_cases': [{'input_data': 'True\nTrue\nFalse\n',
                                             'expected_output': 'Door unlocked',
                                             'is_hidden': False},
                                            {'input_data': 'True\nTrue\nTrue\n',
                                             'expected_output': 'Door stays locked',
                                             'is_hidden': False},
                                            {'input_data': 'False\nTrue\nFalse\n',
                                             'expected_output': 'Door stays locked',
                                             'is_hidden': False}],
                             'title': 'Three-Part Door Check',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read height as a whole number, then adult and medical_warning as True/False.\n2. Allow the ride if height is at least 140 or the rider is an adult, and there is no medical warning.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Group (height >= 140 or adult) in parentheses, then require not '
                                       'medical_warning.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'height = int(input())\n'
                                       'adult = input() == "True"\n'
                                       'medical_warning = input() == "True"\n'
                                       'if (height >= 140 or adult) and not medical_warning:\n'
                                       '    print("Ride allowed")\n'
                                       'else:\n'
                                       '    print("Ride not allowed")'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read height as a whole number, then adult and medical_warning '
                                             'as True/False. Allow the ride if height is at least 140 or the '
                                             'rider is an adult, and there is no medical warning.',
                             'solution_code': 'height = int(input())\n'
                                              'adult = input() == "True"\n'
                                              'medical_warning = input() == "True"\n'
                                              'if (height >= 140 or adult) and not medical_warning:\n'
                                              '    print("Ride allowed")\n'
                                              'else:\n'
                                              '    print("Ride not allowed")',
                             'test_cases': [{'input_data': '140\nFalse\nFalse\n',
                                             'expected_output': 'Ride allowed',
                                             'is_hidden': False},
                                            {'input_data': '120\nTrue\nFalse\n',
                                             'expected_output': 'Ride allowed',
                                             'is_hidden': False},
                                            {'input_data': '150\nFalse\nTrue\n',
                                             'expected_output': 'Ride not allowed',
                                             'is_hidden': False},
                                            {'input_data': '120\nFalse\nFalse\n',
                                             'expected_output': 'Ride not allowed',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Ride Safety Check',
                             'xp_reward': 150}],
             'description': 'and requires every part. or accepts either part. not reverses a True/False '
                            'answer. Parentheses group a rule so it is easier to read.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'Think of each comparison as a True/False answer. and joins '
                                                'answers where every part must be True. or joins choices '
                                                'where either side can be True. not flips one answer: not '
                                                'False is True, and not True is False. Parentheses make '
                                                'related checks easier to see. In the ride example, height '
                                                'or adult is one group, and no warning is an additional rule '
                                                'that must also pass.',
                        'expected_output': 'Enter',
                        'introduction': 'and requires every part. or accepts either part. not reverses a '
                                        'True/False answer. Parentheses group a rule so it is easier to '
                                        'read.',
                        'learning_objectives': ['Understand combining conditions with and, or, and not.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'ticket = True', 'explanation': 'Store True in ticket. This variable records a yes-or-no answer.'}, {'line': '2', 'code': 'age_ok = True', 'explanation': 'Store True in age_ok. This variable records a yes-or-no answer.'}, {'line': '3', 'code': 'if ticket and age_ok:', 'explanation': 'Check whether ticket and age_ok. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '4', 'code': '    print("Enter")', 'explanation': "Show the text 'Enter' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: and needs both',
                                                'code': 'ticket = True\n'
                                                        'age_ok = True\n'
                                                        'if ticket and age_ok:\n'
                                                        '    print("Enter")',
                                                'explanation': 'Both requirements are true, so entry is '
                                                               'allowed.',
                                                'output': 'Enter'},
                                               {'title': 'Example 2: or accepts either',
                                                'code': 'weekend = False\n'
                                                        'holiday = True\n'
                                                        'if weekend or holiday:\n'
                                                        '    print("No school")',
                                                'explanation': 'The holiday is true, so the or rule '
                                                               'succeeds.',
                                                'output': 'No school'},
                                               {'title': 'Example 3: not reverses',
                                                'code': 'locked = False\n'
                                                        'if not locked:\n'
                                                        '    print("You may enter")',
                                                'explanation': 'not False becomes True, so the message '
                                                               'appears.',
                                                'output': 'You may enter'}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'and requires every part. or accepts either part. not reverses a '
                                   'True/False answer. Parentheses group a rule so it is easier to read. '
                                   'tall = True The indented lines belong to their decision.',
                        'syntax_breakdown': 'tall = True\n'
                                            'adult = False\n'
                                            'warning = False\n'
                                            'if (tall or adult) and not warning:\n'
                                            '    print("Ride allowed")\n'
                                            'else:\n'
                                            '    print("Ride not allowed")',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 37,
             'quizzes': [{'question': 'Both checks must pass to print Safe. What is printed?\n'
                                      '\n'
                                      'wind_ok = True\n'
                                      'rain_ok = False\n'
                                      'if wind_ok and not rain_ok:\n'
                                      "    print('Safe')\n"
                                      'else:\n'
                                      "    print('Wait')",
                          'explanation': 'not rain_ok is True because rain_ok is False. Both sides of and '
                                         'are then True.',
                          'options': [{'text': 'Safe',
                                       'is_correct': True,
                                       'explanation': 'Correct. wind_ok is True and not False is True, so '
                                                      'the full condition is True.'},
                                      {'text': 'Wait',
                                       'is_correct': False,
                                       'explanation': 'The condition is True, so the else branch is '
                                                      'skipped.'},
                                      {'text': 'Safe and Wait',
                                       'is_correct': False,
                                       'explanation': 'Python runs only one branch.'},
                                      {'text': 'SyntaxError',
                                       'is_correct': False,
                                       'explanation': 'not can be used in a Boolean condition like this.'}]},
                         {'question': 'A ride needs height from 120 up to but not including 190. Does height '
                                      '150 pass this check?\n'
                                      '\n'
                                      'height = 150\n'
                                      'print(120 <= height < 190)',
                          'explanation': '150 is at least 120 and less than 190, so both parts of the '
                                         'chained comparison are True.',
                          'options': [{'text': 'True',
                                       'is_correct': True,
                                       'explanation': 'Correct. 120 <= 150 and 150 < 190 are both True.'},
                                      {'text': 'False',
                                       'is_correct': False,
                                       'explanation': '150 is inside the allowed range.'},
                                      {'text': '150',
                                       'is_correct': False,
                                       'explanation': 'The code prints the comparison result, not height '
                                                      'itself.'},
                                      {'text': 'An error',
                                       'is_correct': False,
                                       'explanation': 'Python supports chained comparisons such as 120 <= '
                                                      'height < 190.'}]}],
             'title': 'Combining Conditions with and, or, and not'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a whole number.\n2. Print You found ten only when the number is exactly 10 otherwise print Try again.\n3. Use a comparison in the condition.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['Use == to compare the number with 10. Use else for every other '
                                       'number.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'number = int(input())\n'
                                       'if number == 10:\n'
                                       '    print("You found ten")\n'
                                       'else:\n'
                                       '    print("Try again")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read a whole number. Print You found ten only when the number '
                                             'is exactly 10; otherwise print Try again. Use a comparison in '
                                             'the condition.',
                             'solution_code': 'number = int(input())\n'
                                              'if number == 10:\n'
                                              '    print("You found ten")\n'
                                              'else:\n'
                                              '    print("Try again")',
                             'test_cases': [{'input_data': '10\n',
                                             'expected_output': 'You found ten',
                                             'is_hidden': False},
                                            {'input_data': '9\n',
                                             'expected_output': 'Try again',
                                             'is_hidden': False},
                                            {'input_data': '11\n',
                                             'expected_output': 'Try again',
                                             'is_hidden': False}],
                             'title': 'Fix the Equality Check',
                             'xp_reward': 30},
                            {'description': 'Your task, step by step:\n1. Read a line of text.\n2. Print Python found if the lowercase text python appears in the line.\n3. Otherwise print Python not found.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Use "python" in text to check whether that piece of text appears in '
                                       'the line.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'text = input()\n'
                                       'if "python" in text:\n'
                                       '    print("Python found")\n'
                                       'else:\n'
                                       '    print("Python not found")'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read a line of text. Print Python found if the lowercase text '
                                             'python appears in the line. Otherwise print Python not found.',
                             'solution_code': 'text = input()\n'
                                              'if "python" in text:\n'
                                              '    print("Python found")\n'
                                              'else:\n'
                                              '    print("Python not found")',
                             'test_cases': [{'input_data': 'I like python\n',
                                             'expected_output': 'Python found',
                                             'is_hidden': False},
                                            {'input_data': 'python is fun\n',
                                             'expected_output': 'Python found',
                                             'is_hidden': False},
                                            {'input_data': 'I like Java\n',
                                             'expected_output': 'Python not found',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Search for a Word',
                             'xp_reward': 150}],
             'description': 'A single = stores a value; == compares two values. Indentation shows which '
                            'lines belong to a branch. In an elif chain, a broad rule placed too early can '
                            'hide a more specific answer.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'A conditional bug can come from a tiny difference. Use one '
                                                'equals sign in a line such as answer = input() to save a '
                                                'value. Use two equals signs in answer == "yes" to ask '
                                                'whether it matches. Indent only the lines that belong to '
                                                'the decision. For an elif chain, put a narrow/high score '
                                                'rule before a wide/lower score rule because the first match '
                                                'wins. The in operator checks whether one piece of text '
                                                'occurs inside another.',
                        'expected_output': 'Correct',
                        'introduction': 'A single = stores a value; == compares two values. Indentation '
                                        'shows which lines belong to a branch. In an elif chain, a broad '
                                        'rule placed too early can hide a more specific answer.',
                        'learning_objectives': ['Understand avoiding common if statement mistakes.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'answer = "yes"', 'explanation': 'Store the text "yes" in answer.'}, {'line': '2', 'code': 'if answer == "yes":', 'explanation': 'Check whether answer is the same as "yes". If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '3', 'code': '    print("Correct")', 'explanation': "Show the text 'Correct' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Compare text',
                                                'code': 'answer = "yes"\n'
                                                        'if answer == "yes":\n'
                                                        '    print("Correct")',
                                                'explanation': '== asks whether the values match; it does '
                                                               'not change answer.',
                                                'output': 'Correct'},
                                               {'title': 'Example 2: Find a word',
                                                'code': 'sentence = "I am learning Python"\n'
                                                        'if "Python" in sentence:\n'
                                                        '    print("Found")',
                                                'explanation': 'in checks whether the smaller text appears '
                                                               'inside the sentence.',
                                                'output': 'Found'},
                                               {'title': 'Example 3: Order checks',
                                                'code': 'score = 92\n'
                                                        'if score >= 90:\n'
                                                        '    print("Excellent")\n'
                                                        'elif score >= 70:\n'
                                                        '    print("Passing")',
                                                'explanation': 'The high score is checked first. If >= 70 '
                                                               'came first, 92 would only print Passing.',
                                                'output': 'Excellent'}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'A single = stores a value; == compares two values. Indentation shows '
                                   'which lines belong to a branch. In an elif chain, a broad rule placed '
                                   'too early can hide a more specific answer. answer = input() The indented '
                                   'lines belong to their decision.',
                        'syntax_breakdown': 'answer = input()\n'
                                            'if answer == "yes":\n'
                                            '    print("You said yes")\n'
                                            'else:\n'
                                            '    print("Not yes")\n'
                                            '\n'
                                            'message = "learn Python"\n'
                                            'if "Python" in message:\n'
                                            '    print("Word found")',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 38,
             'quizzes': [{'question': 'Which message prints? The first condition is broad, so check what '
                                      'Python does when it finds a match.\n'
                                      '\n'
                                      'score = 95\n'
                                      'if score >= 60:\n'
                                      "    print('Pass')\n"
                                      'elif score >= 90:\n'
                                      "    print('High score')",
                          'explanation': 'Python checks top to bottom and stops at the first True condition. '
                                         'score >= 60 matches first.',
                          'options': [{'text': 'Pass',
                                       'is_correct': True,
                                       'explanation': 'Correct. The first condition is already True, so '
                                                      'Python skips the later elif.'},
                                      {'text': 'High score',
                                       'is_correct': False,
                                       'explanation': 'This elif is never checked after the first if '
                                                      'condition matches.'},
                                      {'text': 'Pass and High score',
                                       'is_correct': False,
                                       'explanation': 'Only the first matching branch runs.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'The first condition is True, so a message prints.'}]},
                         {'question': 'What is the mistake in this code, and what should replace the single '
                                      'equals sign?\n'
                                      '\n'
                                      "answer = 'yes'\n"
                                      "if answer = 'yes':\n"
                                      "    print('Correct')",
                          'explanation': 'Use == to compare two values. A single = assigns a value and '
                                         'cannot be used for this if comparison.',
                          'options': [{'text': 'Replace = with ==',
                                       'is_correct': True,
                                       'explanation': 'Correct. == checks whether answer matches the text '
                                                      'yes.'},
                                      {'text': 'Replace = with !=',
                                       'is_correct': False,
                                       'explanation': '!= means the values should be different, which is not '
                                                      'the intended check.'},
                                      {'text': 'Remove the colon',
                                       'is_correct': False,
                                       'explanation': 'The colon is required at the end of an if line.'},
                                      {'text': 'Indent the answer line',
                                       'is_correct': False,
                                       'explanation': 'The comparison syntax must be fixed; the answer '
                                                      'assignment can stay where it is.'}]}],
             'title': 'Avoiding Common if Statement Mistakes'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a whole number.\n2. Print FizzBuzz if divisible by both 3 and 5, Fizz if only by 3, Buzz if only by 5, or the number otherwise.\n3. Check both divisors first.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['Use % to check remainders. Put the combined and check first so 15 is '
                                       'not caught by the 3-only branch.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'number = int(input())\n'
                                       'if number % 3 == 0 and number % 5 == 0:\n'
                                       '    print("FizzBuzz")\n'
                                       'elif number % 3 == 0:\n'
                                       '    print("Fizz")\n'
                                       'elif number % 5 == 0:\n'
                                       '    print("Buzz")\n'
                                       'else:\n'
                                       '    print(number)'],
                             'initial_code': '',
                             'is_boss': True,
                             'requirements': 'Read a whole number. Print FizzBuzz if divisible by both 3 and '
                                             '5, Fizz if only by 3, Buzz if only by 5, or the number '
                                             'otherwise. Check both divisors first.',
                             'solution_code': 'number = int(input())\n'
                                              'if number % 3 == 0 and number % 5 == 0:\n'
                                              '    print("FizzBuzz")\n'
                                              'elif number % 3 == 0:\n'
                                              '    print("Fizz")\n'
                                              'elif number % 5 == 0:\n'
                                              '    print("Buzz")\n'
                                              'else:\n'
                                              '    print(number)',
                             'test_cases': [{'input_data': '15\n',
                                             'expected_output': 'FizzBuzz',
                                             'is_hidden': False},
                                            {'input_data': '9\n',
                                             'expected_output': 'Fizz',
                                             'is_hidden': False},
                                            {'input_data': '10\n',
                                             'expected_output': 'Buzz',
                                             'is_hidden': False},
                                            {'input_data': '7\n', 'expected_output': '7', 'is_hidden': False},
                                            {'input_data': '0\n',
                                             'expected_output': 'FizzBuzz',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Classic FizzBuzz',
                             'xp_reward': 150},
                            {'description': 'Your task, step by step:\n1. Read account balance then withdrawal amount, each as a whole number.\n2. Reject amounts 0 or less with Withdrawal must be positive.\n3. Otherwise approve if it is within the balance print Not enough money if it exceeds the balance.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['Check amount > 0 first. Inside that branch, check amount <= balance.',
                                       'Write the condition first. Then indent only the message that belongs '
                                       'to that choice.',
                                       'balance = int(input())\n'
                                       'amount = int(input())\n'
                                       'if amount > 0:\n'
                                       '    if amount <= balance:\n'
                                       '        print("Withdrawal approved")\n'
                                       '    else:\n'
                                       '        print("Not enough money")\n'
                                       'else:\n'
                                       '    print("Withdrawal must be positive")'],
                             'initial_code': '',
                             'is_boss': False,
                             'requirements': 'Read account balance then withdrawal amount, each as a whole '
                                             'number. Reject amounts 0 or less with Withdrawal must be '
                                             'positive. Otherwise approve if it is within the balance; print '
                                             'Not enough money if it exceeds the balance.',
                             'solution_code': 'balance = int(input())\n'
                                              'amount = int(input())\n'
                                              'if amount > 0:\n'
                                              '    if amount <= balance:\n'
                                              '        print("Withdrawal approved")\n'
                                              '    else:\n'
                                              '        print("Not enough money")\n'
                                              'else:\n'
                                              '    print("Withdrawal must be positive")',
                             'test_cases': [{'input_data': '100\n40\n',
                                             'expected_output': 'Withdrawal approved',
                                             'is_hidden': False},
                                            {'input_data': '100\n120\n',
                                             'expected_output': 'Not enough money',
                                             'is_hidden': False},
                                            {'input_data': '100\n0\n',
                                             'expected_output': 'Withdrawal must be positive',
                                             'is_hidden': False},
                                            {'input_data': '100\n-5\n',
                                             'expected_output': 'Withdrawal must be positive',
                                             'is_hidden': False}],
                             'title': 'ATM Withdrawal Check',
                             'xp_reward': 50}],
             'description': 'Use if for a special case, if/else for two outcomes, elif for several choices, '
                            'and combined conditions when a rule has multiple parts. Test boundary inputs '
                            'too.',
             'lesson': {'common_mistakes': [{'mistake': 'Using = when you mean to compare.',
                                             'why': '= stores a value; == checks whether values match.',
                                             'fix': 'Use == in a comparison.'},
                                            {'mistake': 'Forgetting the colon or indentation.',
                                             'why': 'Python needs these to identify the decision block.',
                                             'fix': 'Add a colon and indent the block by four spaces.'},
                                            {'mistake': 'Putting a broad elif before a specific one.',
                                             'why': 'Python stops at the first true condition.',
                                             'fix': 'Check high or specific thresholds first.'}],
                        'detailed_explanation': 'This review combines the choices from earlier levels. An '
                                                'if/else can approve or refuse one withdrawal. An elif chain '
                                                'can pick one label from several options. FizzBuzz has an '
                                                'overlap: 15 is divisible by 3 and by 5, so test that '
                                                'combined case before checking either divisor on its own. '
                                                'Use a remainder of zero to recognize values that divide '
                                                'evenly. Try boundary values such as 0, 3, 5, and 15 to '
                                                'catch ordering mistakes.',
                        'expected_output': 'Approved',
                        'introduction': 'Use if for a special case, if/else for two outcomes, elif for '
                                        'several choices, and combined conditions when a rule has multiple '
                                        'parts. Test boundary inputs too.',
                        'learning_objectives': ['Understand world 4 review: conditional decisions.',
                                                'Explain what each condition checks and why it is used.',
                                                'Predict which lines run for different example values.'],
                        'line_by_line': [{'line': '1', 'code': 'balance = 40', 'explanation': 'Store the number 40 in balance.'}, {'line': '2', 'code': 'amount = 25', 'explanation': 'Store the number 25 in amount.'}, {'line': '3', 'code': 'if amount <= balance:', 'explanation': 'Check whether amount is at most balance. If that is true, run the indented lines below; otherwise, skip them.'}, {'line': '4', 'code': '    print("Approved")', 'explanation': "Show the text 'Approved' on the screen."}, {'line': '5', 'code': 'else:', 'explanation': 'Run the indented lines below only when the earlier if check was false.'}, {'line': '6', 'code': '    print("Not enough money")', 'explanation': "Show the text 'Not enough money' on the screen."}],
                        'practical_examples': [{'title': 'Example 1: Withdrawal decision',
                                                'code': 'balance = 40\n'
                                                        'amount = 25\n'
                                                        'if amount <= balance:\n'
                                                        '    print("Approved")\n'
                                                        'else:\n'
                                                        '    print("Not enough money")',
                                                'explanation': 'The amount is within the balance, so the '
                                                               'first path runs.',
                                                'output': 'Approved'},
                                               {'title': 'Example 2: Several outcomes',
                                                'code': 'score = 76\n'
                                                        'if score >= 90:\n'
                                                        '    print("A")\n'
                                                        'elif score >= 70:\n'
                                                        '    print("C or better")\n'
                                                        'else:\n'
                                                        '    print("Practice")',
                                                'explanation': 'The score is below 90 but at least 70.',
                                                'output': 'C or better'},
                                               {'title': 'Example 3: Both divisors',
                                                'code': 'number = 15\n'
                                                        'if number % 3 == 0 and number % 5 == 0:\n'
                                                        '    print("FizzBuzz")',
                                                'explanation': 'Both remainders are zero, so the combined '
                                                               'condition succeeds.',
                                                'output': 'FizzBuzz'}],
                        'practice_questions': ['Which condition is Python checking?',
                                               'Change an example value: which message will appear, and '
                                               'why?'],
                        'prerequisites': 'No Python experience is required. World 3 comparisons such as == '
                                         'and >= are useful; the examples explain them again.',
                        'real_world_apps': 'Everyday examples include game access, school reports, online '
                                           'discounts, weather alerts, traffic lights, and ATM safety '
                                           'checks.',
                        'summary': 'Use if for a special case, if/else for two outcomes, elif for several '
                                   'choices, and combined conditions when a rule has multiple parts. Test '
                                   'boundary inputs too. number = 15 The indented lines belong to their '
                                   'decision.',
                        'syntax_breakdown': 'number = 15\n'
                                            'if number % 3 == 0 and number % 5 == 0:\n'
                                            '    print("FizzBuzz")\n'
                                            'elif number % 3 == 0:\n'
                                            '    print("Fizz")\n'
                                            'elif number % 5 == 0:\n'
                                            '    print("Buzz")\n'
                                            'else:\n'
                                            '    print(number)',
                        'terminology': [{'term': 'condition',
                                         'definition': 'A question Python answers with True or False.'},
                                        {'term': 'branch',
                                         'definition': 'One possible path a program can follow.'},
                                        {'term': 'indentation',
                                         'definition': 'Spaces at the start of a line that show which '
                                                       'instructions belong together.'}]},
             'number': 39,
             'quizzes': [{'question': 'A game gives access only when the player is level 10 or higher and '
                                      'has the Master rank. What prints?\n'
                                      '\n'
                                      'level = 15\n'
                                      "rank = 'Master'\n"
                                      "if level >= 10 and rank == 'Master':\n"
                                      "    print('Access granted')\n"
                                      'else:\n'
                                      "    print('Access denied')",
                          'explanation': 'Both checks are True: level is at least 10 and rank matches '
                                         'Master.',
                          'options': [{'text': 'Access granted',
                                       'is_correct': True,
                                       'explanation': 'Correct. Both sides of and are True, so the if branch '
                                                      'runs.'},
                                      {'text': 'Access denied',
                                       'is_correct': False,
                                       'explanation': 'The else runs only when the combined condition is '
                                                      'False.'},
                                      {'text': '15 Master',
                                       'is_correct': False,
                                       'explanation': 'The code prints the chosen message, not the variable '
                                                      'values.'},
                                      {'text': 'An error',
                                       'is_correct': False,
                                       'explanation': 'The comparisons and and condition are valid '
                                                      'Python.'}]},
                         {'question': 'An emergency kit should be used when health is 0 or lower and a '
                                      'potion is available. What prints?\n'
                                      '\n'
                                      'health = 0\n'
                                      'has_potion = True\n'
                                      'if health <= 0 and has_potion:\n'
                                      "    print('Use potion')\n"
                                      'else:\n'
                                      "    print('Keep going')",
                          'explanation': 'At zero health the first check is True, and a potion is available, '
                                         'so both parts of and are True.',
                          'options': [{'text': 'Use potion',
                                       'is_correct': True,
                                       'explanation': 'Correct. health <= 0 and has_potion are both True.'},
                                      {'text': 'Keep going',
                                       'is_correct': False,
                                       'explanation': 'The else branch runs only when the combined condition '
                                                      'is False.'},
                                      {'text': 'Use potion and Keep going',
                                       'is_correct': False,
                                       'explanation': 'Python runs only one branch.'},
                                      {'text': 'Nothing',
                                       'is_correct': False,
                                       'explanation': 'The condition is True, so a message prints.'}]}],
             'title': 'World 4 Review: Conditional Decisions'}],
 'number': 4,
 'title': 'Conditional Decisions'}
