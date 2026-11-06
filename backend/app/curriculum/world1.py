WORLD_1 = {'number': 1,
 'title': 'Python Beginner',
 'goal': 'Introduce programming to someone who has never written code.',
 'description': 'Start your journey with fundamental programming concepts, syntax, text, and numbers.',
 'final_project_title': 'Personal Introduction Program',
 'final_project_desc': 'Build an interactive script that prints a formatted biography card with text, '
                       'calculations, and comments.',
 'is_unlocked_by_default': True,
 'levels': [{'number': 1,
             'title': 'What Is Programming?',
             'description': 'Understand what instructions are and write your very first print() command.',
             'lesson': {'learning_objectives': ['Understand what programming is: giving step-by-step '
                                                'instructions to a computer',
                                                'Learn your very first Python tool: the print() command',
                                                'Understand WHY we need print() to see anything on screen',
                                                'Learn WHAT Python does behind the scenes when reading your '
                                                'code'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'Welcome to Python Quest! Imagine you have a friendly helper robot '
                                        'in your room. This robot can move at lightning speed, but it is '
                                        'born with a totally blank mind. It knows nothing on its own! If you '
                                        "say 'make tea', it freezes because it doesn't know what tea is. You "
                                        'must give it clear, step-by-step instructions: 1. Boil water. 2. '
                                        'Put tea bag in mug. 3. Pour water into mug. That is all programming '
                                        'is: writing down simple, numbered steps so the computer knows '
                                        'exactly what to do.',
                        'detailed_explanation': '### In simple words\n'
                                                'A program is a list of instructions. Python follows them '
                                                'from top to bottom. `print()` is an instruction that shows '
                                                'something on the screen.\n'
                                                '\n'
                                                '### Try it step by step\n'
                                                '1. Write `print` in lowercase.\n'
                                                '2. Put `(` after it and `)` at the end.\n'
                                                '3. Put the words you want to show inside quotes: '
                                                "`print('Hello')`.\n"
                                                '4. Run the program. The screen should show `Hello`.\n'
                                                '\n'
                                                'The quotes mark the words as text. The parentheses show '
                                                'which value belongs to `print()`. Each new `print()` '
                                                'normally starts a new output line.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 WHY DO WE USE THE print() COMMAND?\n'
                                                'Computers are silent and invisible workers. If a computer '
                                                'does a calculation or runs a task, it keeps the result '
                                                "hidden inside its memory chip. You won't see anything on "
                                                'your monitor! To make the computer show words or numbers on '
                                                'your screen, Python created a special command called '
                                                '`print()`. Think of `print()` as giving your computer a '
                                                'mouth so it can speak to you!\n'
                                                '\n'
                                                '🤖 WHAT PYTHON DOES STEP-BY-STEP:\n'
                                                "When Python reads: `print('System Boot')`\n"
                                                "1. Python reads the word `print` &rarr; It realizes: 'Aha! "
                                                "The human wants me to display something on the screen!'\n"
                                                '2. Python opens the parentheses `(` and looks inside.\n'
                                                "3. Python spots the quotation marks `'...'` &rarr; It "
                                                "understands: 'These are human words to display, NOT code "
                                                "commands to execute!'\n"
                                                '4. Python takes the exact text `System Boot` and prints it '
                                                'onto your screen.\n'
                                                '5. Python automatically jumps down to a fresh line, ready '
                                                'for your next instruction!\n'
                                                '\n'
                                                '⚠️ CRUCIAL RULE — CAPITALIZATION MATTERS:\n'
                                                'Python is case-sensitive. That means lowercase `print` '
                                                'works, but capitalized `Print` or `PRINT` will fail with an '
                                                'error. Always write `print` in all-lowercase letters!',
                        'terminology': [{'term': 'Programming',
                                         'definition': 'Writing step-by-step instructions that tell a '
                                                       'computer what to do.'},
                                        {'term': 'print() Command',
                                         'definition': 'The built-in Python tool used to display words, '
                                                       'messages, and numbers on your screen.'},
                                        {'term': 'Parentheses ( )',
                                         'definition': 'The curved brackets that hold whatever message you '
                                                       'want to display on screen.'},
                                        {'term': "Quotation Marks ' '",
                                         'definition': "Speech bubbles around words that tell Python 'these "
                                                       "are words to display, not commands'."}],
                        'syntax_breakdown': '# 1. Built-in function name: print (MUST be strictly '
                                            'lowercase)\n'
                                            '# 2. Parentheses () enclose the data to display\n'
                                            "# 3. Quotation marks '' define text string\n"
                                            "print('Welcome to Python Quest!')\n"
                                            "print('Programming is giving instructions to the computer.')",
                        'practical_examples': [{'title': 'Example 1: Displaying a single message',
                                                'code': "print('System Boot')",
                                                'explanation': "Tells Python to display 'System Boot' on the "
                                                               'screen.',
                                                'output': 'System Boot'},
                                               {'title': 'Example 2: Sequential execution (line by line)',
                                                'code': "print('Step 1: Power On')\n"
                                                        "print('Step 2: Ready for Quest')",
                                                'explanation': "Python executes line 1 first, prints 'Step "
                                                               "1: Power On', then moves down to line 2 and "
                                                               "prints 'Step 2: Ready for Quest'.",
                                                'output': 'Step 1: Power On\nStep 2: Ready for Quest'},
                                               {'title': 'Example 3: Player Greeting Card',
                                                'code': "print('Player: Alex')\n"
                                                        "print('Level: 1')\n"
                                                        "print('Status: Active')",
                                                'explanation': 'Prints a three-line structured player '
                                                               'profile card.',
                                                'output': 'Player: Alex\nLevel: 1\nStatus: Active'}],
                        'line_by_line': [{'line': '1', 'code': "print('System Boot')", 'explanation': "Show the text 'System Boot' on the screen."}],
                        'expected_output': 'System Boot\nStep 1: Power On\nStep 2: Ready for Quest',
                        'common_mistakes': [{'mistake': "Print('Hello')",
                                             'why': 'Python is case-sensitive! It does not recognize capital '
                                                    "'P'. It must be lowercase 'print'.",
                                             'fix': "print('Hello')"},
                                            {'mistake': 'print(Hello)',
                                             'why': 'Missing quotes! Without quotation marks, Python thinks '
                                                    'Hello is a command rather than plain words.',
                                             'fix': "print('Hello')"},
                                            {'mistake': "print('Hello)",
                                             'why': 'Missing closing quote! You opened a quote at the start, '
                                                    'but forgot to close it before the bracket.',
                                             'fix': "print('Hello')"}],
                        'real_world_apps': 'Every app uses output: WhatsApp showing messages on your screen, '
                                           'Google Maps showing turn directions, and games showing game-over '
                                           'screens.',
                        'summary': "Programming is writing step-by-step instructions. In Python, print('Your "
                                   "text') shows words on screen. Always use lowercase 'print', wrap words "
                                   'in quotes, and close your parentheses!',
                        'practice_questions': ['What tool makes Python display words on the screen?',
                                               'Why must print always be written in lowercase letters?',
                                               'What happens when you write two print statements on two '
                                               'lines?']},
             'challenges': [{'title': 'Instruction Sequence',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Print two lines in this order.\n2. The first line should say System Boot.\n3. The second line should say Ready for Quest.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Write two print instructions. Keep the words and line order '
                                             'exactly as shown.',
                             'initial_code': '',
                             'solution_code': "print('System Boot')\nprint('Ready for Quest')",
                             'hints': ['Use the print instruction to show words.',
                                       'Put each requested message on its own output line.',
                                       'Check the spelling and the order of the two lines.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'System Boot\nReady for Quest',
                                             'is_hidden': False,
                                             'explanation': 'Both lines printed in exact sequence.'}]},
                            {'title': 'Boss Challenge: Mission Launch Sequence',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Print a four-step launch countdown, with one line for each step.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Show Countdown: 3, Countdown: 2, Countdown: 1, then Launch '
                                             'Python Quest! Put each message on its own line.',
                             'initial_code': '',
                             'solution_code': "print('Countdown: 3')\n"
                                              "print('Countdown: 2')\n"
                                              "print('Countdown: 1')\n"
                                              "print('Launch Python Quest!')",
                             'hints': ['A countdown has one message for each number.',
                                       'Print the messages from 3 down to 1.',
                                       'After 1, show the launch message on a new line.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Countdown: 3\n'
                                                                'Countdown: 2\n'
                                                                'Countdown: 1\n'
                                                                'Launch Python Quest!',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': 'In Python, what happens when you run two print() statements one after '
                                      'another?\n'
                                      '\n'
                                      "print('Step 1: System Boot')\n"
                                      "print('Step 2: Ready for Quest')",
                          'explanation': 'Python runs code from top to bottom. Each print() call '
                                         'automatically prints on its own fresh line.',
                          'options': [{'text': 'Step 1: System Boot\nStep 2: Ready for Quest',
                                       'is_correct': True,
                                       'explanation': 'Correct! Python executes line 1 first, then line 2 on '
                                                      'the next line.'},
                                      {'text': 'Step 1: System Boot Step 2: Ready for Quest (Both glued on a '
                                               'single line)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. In Python, each print() outputs onto a new '
                                                      'line by default.'},
                                      {'text': 'Step 2: Ready for Quest\nStep 1: System Boot (Reverse order)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Python executes from top to bottom, not in '
                                                      'reverse order.'},
                                      {'text': 'SyntaxError: print cannot be repeated',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. You can call print() as many times as you '
                                                      'like in a program.'}]},
                         {'question': 'Which of the following is the correct Python command to display the '
                                      'text: System Online?',
                          'explanation': 'Python is case-sensitive and requires lowercase print, parentheses '
                                         "(), and quotation marks '' around words.",
                          'options': [{'text': "print('System Online')",
                                       'is_correct': True,
                                       'explanation': 'Correct! Lowercase print, parentheses (), and single '
                                                      "quotes '' around the words."},
                                      {'text': "Print('System Online')",
                                       'is_correct': False,
                                       'explanation': "Incorrect. Capital 'Print' causes a NameError because "
                                                      'Python is strictly case-sensitive.'},
                                      {'text': 'print(System Online)',
                                       'is_correct': False,
                                       'explanation': "Incorrect. Without quotes, Python thinks 'System' is "
                                                      'a command name and crashes.'},
                                      {'text': "display 'System Online'",
                                       'is_correct': False,
                                       'explanation': "Incorrect. 'display' is not a built-in Python "
                                                      'command.'}]}]},
            {'number': 2,
             'title': 'What Is Python?',
             'description': 'Learn why quotes are like speech bubbles, single vs double quotes, and case '
                            'sensitivity.',
             'lesson': {'learning_objectives': ['Understand WHY Python requires quotation marks for human '
                                                'words',
                                                "Learn that single quotes 'hello' and double quotes "
                                                '"hello" work identically',
                                                "Master Python's strict case-sensitivity (print vs Print)",
                                                'Write your first Python statement declaring your new '
                                                'programming skill'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'Why is Python the most popular programming language on Earth? '
                                        'Because it was designed to read like clean, plain English! In older '
                                        'languages like Java or C++, displaying a single message takes 5 to '
                                        '7 complicated lines of boilerplate code. In Python, it is just one '
                                        'simple command! But to write Python, you need to understand how '
                                        'Python tells the difference between code and words.',
                        'detailed_explanation': '### In simple words\n'
                                                'Python code is made of instructions, while text is '
                                                'information that an instruction can use. Quotes tell '
                                                'Python, “these are words.” Without quotes, Python treats '
                                                'names and symbols as instructions or values.\n'
                                                '\n'
                                                '### Try it step by step\n'
                                                "`print('Hello')` shows the word Hello. The quote marks do "
                                                'not appear in the output. Single and double quotes both '
                                                'work, as long as the opening and closing marks match.\n'
                                                '\n'
                                                'Python also cares about capital letters in code: write '
                                                '`print`, not `Print`. The words inside quotes can use any '
                                                'capitalization you want.\n'
                                                '\n'
                                                '### More detail\n'
                                                "🎯 WHY DO WE USE QUOTATION MARKS '...' ?\n"
                                                "Imagine you tell a robot: 'RUN'. Does that mean *run across "
                                                "the room*, or does it mean *say the word 'RUN' out loud*? "
                                                "It's confusing!\n"
                                                'To solve this problem, programmers invented quotation marks '
                                                "`'...'`. Quotes act exactly like speech bubbles in a comic "
                                                'book:\n'
                                                "• When Python sees quotes `'...'`, it understands: 'These "
                                                "are plain human words to display. Don't try to execute them "
                                                "as code!'\n"
                                                '• If you forget quotes like `print(Hello)`, Python thinks '
                                                'Hello is a computer command name. It searches its memory, '
                                                'cannot find any command named Hello, and panics with an '
                                                'error called `NameError`!\n'
                                                '\n'
                                                '🔍 SINGLE QUOTES VS DOUBLE QUOTES:\n'
                                                "You can use single quotes `'Python'` or double quotes "
                                                '"Python". Both work 100% identically in Python! Just make '
                                                'sure whatever quote you start with, you close with the same '
                                                'quote.\n'
                                                '\n'
                                                '⚠️ CRUCIAL RULE — CASE SENSITIVITY:\n'
                                                'To Python, lowercase and uppercase letters are completely '
                                                'different symbols. `print` works, but `Print` or `PRINT` '
                                                'will crash. Always use lowercase!',
                        'terminology': [{'term': 'String',
                                         'definition': 'A piece of human text wrapped in quotation marks '
                                                       '(\'...\' or "...").'},
                                        {'term': 'Case Sensitivity',
                                         'definition': 'Treating uppercase and lowercase letters as '
                                                       'completely different symbols (print is NOT the same '
                                                       'as Print).'},
                                        {'term': 'NameError',
                                         'definition': 'An error that happens when you write a word without '
                                                       'quotes that Python does not recognize.'}],
                        'syntax_breakdown': '# Single quotes and double quotes work identically for text '
                                            'strings:\n'
                                            "print('Single quotes work great for short text')\n"
                                            'print("Double quotes let you safely use apostrophes like it\'s '
                                            'easy!")\n'
                                            '# Text inside quotes is called a String (str)',
                        'practical_examples': [{'title': 'Example 1: Quotes as speech bubbles',
                                                'code': "print('Greetings, adventurer!')",
                                                'explanation': 'Quotes tell Python to treat the characters '
                                                               'as literal human text rather than Python '
                                                               'commands.',
                                                'output': 'Greetings, adventurer!'},
                                               {'title': 'Example 2: Protecting apostrophes inside double '
                                                         'quotes',
                                                'code': 'print("It\'s dangerous to go alone! Take this.")',
                                                'explanation': 'Wrapping in double quotes prevents the '
                                                               'apostrophe in "It\'s" from prematurely '
                                                               'closing the string.',
                                                'output': "It's dangerous to go alone! Take this."},
                                               {'title': 'Example 3: Strict case-sensitivity',
                                                'code': "print('Python is case-sensitive')\n"
                                                        "print('HELLO != hello')",
                                                'explanation': 'In Python, uppercase and lowercase letters '
                                                               'are treated as completely different '
                                                               'characters.',
                                                'output': 'Python is case-sensitive\nHELLO != hello'}],
                        'line_by_line': [{'line': '1', 'code': "print('Greetings, adventurer!')", 'explanation': "Show the text 'Greetings, adventurer!' on the screen."}],
                        'expected_output': 'Python is clean and readable!\nDouble quotes work just as well!',
                        'common_mistakes': [{'mistake': 'print(Learning Python)',
                                             'why': 'Missing quotes! Without quotes, Python thinks Learning '
                                                    'is a command and throws a NameError.',
                                             'fix': "print('Learning Python')"},
                                            {'mistake': "Print('Hello')",
                                             'why': "Capital 'Print' causes NameError: name 'Print' is not "
                                                    'defined.',
                                             'fix': "print('Hello')"}],
                        'real_world_apps': 'NASA uses Python to control scientific equipment, Netflix uses '
                                           'it to recommend movies, and Google uses it for web '
                                           'infrastructure.',
                        'summary': "Quotes tell Python 'this is text to display, not a command.' Single "
                                   'quotes and double quotes both work. Python is strictly case-sensitive: '
                                   "always use lowercase 'print'!",
                        'practice_questions': ['Why must human words be enclosed in quotation marks?',
                                               'Can you use double quotes instead of single quotes in '
                                               'Python?',
                                               'What happens if you type Print with a capital P?']},
             'challenges': [{'title': 'Language Identity',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Print one line that says Learning Python with Python Quest.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Use one print instruction. Match the capital letters and '
                                             'spaces in the requested sentence.',
                             'initial_code': '',
                             'solution_code': "print('Learning Python with Python Quest')",
                             'hints': ['Use one output line.',
                                       'Keep the word Python capitalized as shown.',
                                       'Check that every word and space matches the request.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Learning Python with Python Quest',
                                             'is_hidden': False}]},
                            {'title': 'Boss Challenge: The Zen of Python Core',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Print two short Python principles on separate lines.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Line 1: Beautiful is better than ugly. Line 2: Simple is '
                                             'better than complex. Include the periods.',
                             'initial_code': '',
                             'solution_code': "print('Beautiful is better than ugly.')\n"
                                              "print('Simple is better than complex.')",
                             'hints': ['Print one sentence, then the next.',
                                       'Each sentence ends with a period.',
                                       'Keep the sentences in the requested order.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Beautiful is better than ugly.\n'
                                                                'Simple is better than complex.',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': 'Why must human words and sentences be enclosed in quotation marks '
                                      "'...' inside print()?",
                          'explanation': 'Without quotes, Python tries to execute words as programming '
                                         'commands or look for variables, resulting in an error.',
                          'options': [{'text': 'To tell Python the words are text to display, not '
                                               'programming commands to execute.',
                                       'is_correct': True,
                                       'explanation': 'Correct! Quotes define a string of text for humans.'},
                                      {'text': 'Because quotation marks make the computer processor run '
                                               'faster.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Quotes have no effect on processor speed.'},
                                      {'text': 'Quotation marks are optional in Python and have no meaning.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Without quotation marks, Python raises a '
                                                      'NameError or SyntaxError.'},
                                      {'text': 'To hide the text from the terminal screen.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. The text is printed directly to the '
                                                      'terminal.'}]},
                         {'question': 'What error occurs if you capitalize the print command like '
                                      "Print('Hello')?",
                          'explanation': "Python is strictly case-sensitive. 'Print' with a capital P is "
                                         "unrecognized and raises NameError: name 'Print' is not defined.",
                          'options': [{'text': "NameError: name 'Print' is not defined (Python is strictly "
                                               'case-sensitive)',
                                       'is_correct': True,
                                       'explanation': 'Correct! You must always write print in lowercase.'},
                                      {'text': "It prints 'Hello' in uppercase bold text.",
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Capitalizing the function name produces an '
                                                      'error, not styling.'},
                                      {'text': 'ZeroDivisionError: division by zero.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. ZeroDivisionError only happens in math '
                                                      'when dividing by 0.'},
                                      {'text': 'Python automatically fixes it to lowercase with no error.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Python will not automatically alter your '
                                                      'code.'}]}]},
            {'number': 3,
             'title': 'How Python Runs Code',
             'description': 'Learn how Python reads a saved program from top to bottom, and what comments '
                            'are for.',
             'lesson': {'learning_objectives': ['Understand that Python reads instructions from top to '
                                                'bottom.',
                                                'Learn what a .py file and Python interpreter do.',
                                                'Recognize comments that Python skips.'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'When you write code, you are not just writing for the computer—you '
                                        'are also writing for other humans and for future you! What if you '
                                        'want to leave a note in your code explaining what a line does? That '
                                        'is what comments are for.',
                        'detailed_explanation': '### In simple words\n'
                                                'A Python file is a saved set of instructions. The Python '
                                                'interpreter reads the file and carries out each instruction '
                                                'in order. You can run a file from a code editor or from a '
                                                'terminal with a command such as `python my_file.py`.\n'
                                                '\n'
                                                '### Try it step by step\n'
                                                '1. Save Python instructions in a file ending in `.py`, such '
                                                'as `hello.py`.\n'
                                                '2. Open that file in a Python editor, or open a terminal in '
                                                'its folder.\n'
                                                '3. Run the file. Python starts at the first instruction and '
                                                'moves downward.\n'
                                                '4. If an instruction prints text, that text appears in the '
                                                'output area.\n'
                                                '\n'
                                                'A comment starts with `#`. Python skips the comment; it is '
                                                'a note for people reading the file. Comments do not install '
                                                'Python or run a program.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 WHY DO WE USE COMMENTS (#)?\n'
                                                'What if you want to write a personal note to yourself '
                                                "inside your code, like 'This line prints player health'? If "
                                                'you write normal words in code, Python tries to run them '
                                                'and crashes. When you put a hash symbol `#` at the start of '
                                                'a line, you turn it into a **comment**. Python completely '
                                                'ignores it! It acts like an invisible sticky note for '
                                                'humans.\n'
                                                '\n'
                                                '🤖 WHAT PYTHON DOES:\n'
                                                'Python executes code sequentially: starting at Line 1, '
                                                'proceeding to Line 2, Line 3, and so forth until the end. '
                                                'But whenever Python spots a `#` symbol, it completely skips '
                                                'the rest of that line and does not print anything from it!',
                        'terminology': [{'term': 'Comment (#)',
                                         'definition': 'A note written in code for humans to read. Python '
                                                       'completely ignores comments during execution.'},
                                        {'term': 'Sequential Execution',
                                         'definition': 'Processing code line by line from top to bottom in '
                                                       'order.'},
                                        {'term': 'Script (.py)',
                                         'definition': 'A plain text file containing Python instructions '
                                                       'that can be saved and run.'}],
                        'syntax_breakdown': '# 1. The hash symbol (#) creates a comment that Python '
                                            'completely ignores\n'
                                            "print('Step 1: Initializing core engine...')\n"
                                            '\n'
                                            '# 2. Disabled debugging line (commented out):\n'
                                            "# print('Diagnostic mode: skipped')\n"
                                            '\n'
                                            '# 3. Active line runs normally:\n'
                                            "print('Step 2: Engine online!')",
                        'practical_examples': [{'title': 'Example 1: Sequential top-to-bottom pipeline',
                                                'code': "print('Downloading asset package')\n"
                                                        "print('Verifying digital signature')\n"
                                                        "print('Launch complete!')",
                                                'explanation': 'Python reads and runs each instruction from '
                                                               'line 1 downward in exact order.',
                                                'output': 'Downloading asset package\n'
                                                          'Verifying digital signature\n'
                                                          'Launch complete!'},
                                               {'title': 'Example 2: Commenting out debugging statements',
                                                'code': "# print('Debug: memory = 1024MB')\n"
                                                        "print('System ready for player.')",
                                                'explanation': 'Adding # before the debug print prevents it '
                                                               'from polluting the terminal output.',
                                                'output': 'System ready for player.'},
                                               {'title': 'Example 3: Documenting critical mission parameters',
                                                'code': '# Flight altitude target: 400km\n'
                                                        "print('Target Orbit: LEO (Low Earth Orbit)')\n"
                                                        "print('Trajectory: Nominal')",
                                                'explanation': 'Comments explain the context and goal of the '
                                                               'program to human teammates.',
                                                'output': 'Target Orbit: LEO (Low Earth Orbit)\n'
                                                          'Trajectory: Nominal'}],
                        'line_by_line': [{'line': '1', 'code': "print('Downloading asset package')", 'explanation': "Show the text 'Downloading asset package' on the screen."}, {'line': '2', 'code': "print('Verifying digital signature')", 'explanation': "Show the text 'Verifying digital signature' on the screen."}, {'line': '3', 'code': "print('Launch complete!')", 'explanation': "Show the text 'Launch complete!' on the screen."}],
                        'expected_output': 'System Online\nAll Systems Go',
                        'common_mistakes': [{'mistake': 'print(# Hello)',
                                             'why': 'Putting # inside the parentheses of print() will cause '
                                                    'a SyntaxError.',
                                             'fix': "# Print a hello message\nprint('Hello')"}],
                        'real_world_apps': 'Professional developers at Google and Microsoft use comments on '
                                           'almost every complex function to explain logic to team members.',
                        'summary': 'Comments start with # and are completely ignored by Python. Code '
                                   'executes sequentially from top to bottom.',
                        'practice_questions': ['What symbol creates a comment in Python?',
                                               'Does Python print comments to the terminal?',
                                               'Why are comments useful when debugging?'],
                        'title': 'How Python Runs Code'},
             'challenges': [{'title': 'Script Simulation',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Pretend you ran a file named app.py with Python 3.\n2. Print the message that confirms it started.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Print one line: Running app.py on Python 3.',
                             'initial_code': '',
                             'solution_code': "print('Running app.py on Python 3')",
                             'hints': ['The task asks for one confirmation message.',
                                       'A file name can be printed as ordinary text.',
                                       'Check the spelling of the file name and Python version.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Running app.py on Python 3',
                                             'is_hidden': False}]},
                            {'title': 'Boss Challenge: Console Diagnostics',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Pretend you ran a file named app.py with Python 3.\n2. Print the message that confirms it started.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Print these three lines in order: [INIT] Interpreter Online, '
                                             '[LOAD] Loading Scripts, [DONE] Ready for Commands.',
                             'initial_code': '',
                             'solution_code': "print('[INIT] Interpreter Online')\n"
                                              "print('[LOAD] Loading Scripts')\n"
                                              "print('[DONE] Ready for Commands')",
                             'hints': ['A start-up report has three stages.',
                                       'Put the stages in the order: start, load, ready.',
                                       'Each stage should appear on its own line.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': '[INIT] Interpreter Online\n'
                                                                '[LOAD] Loading Scripts\n'
                                                                '[DONE] Ready for Commands',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': 'What does Python do when a line begins with the hash symbol #?',
                          'explanation': 'Any line or text beginning with # is a comment. Python completely '
                                         'skips it during execution.',
                          'options': [{'text': 'Python completely ignores it; it is a comment meant for '
                                               'humans to read.',
                                       'is_correct': True,
                                       'explanation': 'Correct! Comments are notes for human developers.'},
                                      {'text': 'Python prints the comment in bright green text in the '
                                               'terminal.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Comments are never displayed on the '
                                                      'screen.'},
                                      {'text': 'Python crashes with a SyntaxError.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. The # symbol is completely valid Python '
                                                      'syntax.'},
                                      {'text': 'Python executes the line backwards.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Python does not run code backwards.'}]},
                         {'question': 'Given the code:\n'
                                      '\n'
                                      "print('Alpha')\n"
                                      "# print('Beta')\n"
                                      "print('Gamma')\n"
                                      '\n'
                                      'What will be displayed on the console?',
                          'explanation': "Line 2 is commented out with #, so Python ignores it. Only 'Alpha' "
                                         "and 'Gamma' execute.",
                          'options': [{'text': 'Alpha\nGamma',
                                       'is_correct': True,
                                       'explanation': 'Correct! Line 2 is commented out, so only Alpha and '
                                                      'Gamma are printed.'},
                                      {'text': 'Alpha\nBeta\nGamma',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Line 2 has a # symbol, which disables it.'},
                                      {'text': 'Beta',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Beta is commented out and will never '
                                                      'execute.'},
                                      {'text': 'None (the entire program crashes)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Comments do not cause crashes.'}]}]},
            {'number': 4,
             'title': 'Your First Python Program',
             'description': "Learn the big difference between text in quotes '5 + 5' and numbers 5 + 5.",
             'lesson': {'learning_objectives': ['Understand WHY numbers do NOT use quotation marks',
                                                "Learn Python's basic math symbols (+, -, *, /)",
                                                'Use Python as an instant calculator',
                                                'Print the historic programmer greeting: Hello, World!'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'In 1978, computer scientist Brian Kernighan wrote a tutorial that '
                                        "began with printing 'hello, world'. Since then, every programmer "
                                        'begins with this tradition! But computers were also built for '
                                        'calculations. Let us learn how Python handles numbers and math.',
                        'detailed_explanation': '### In simple words\n'
                                                'Text and numbers can look similar but mean different things '
                                                'to Python. Quotes make a value into text. A number without '
                                                'quotes can be used in arithmetic.\n'
                                                '\n'
                                                '### Try it step by step\n'
                                                "`print('5 + 5')` displays the characters `5 + 5`.\n"
                                                '`print(5 + 5)` calculates the sum and displays `10`.\n'
                                                '\n'
                                                'Try changing one number and running the program again. Keep '
                                                'quotes around words such as `Hello`, but leave quotes off '
                                                'numbers you want Python to calculate.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 WHY DO NUMBERS HAVE NO QUOTES?\n'
                                                'Notice this massive difference:\n'
                                                "1. When you put numbers inside quotes: `print('5 + 5')`\n"
                                                '   Python sees text. It displays literally: `5 + 5`\n'
                                                '2. When you omit quotes: `print(5 + 5)`\n'
                                                '   Python performs the calculation! It displays: `10`\n'
                                                '\n'
                                                "Quotes tell Python: 'Treat this as plain letters to "
                                                "display.' Leaving off quotes tells Python: 'Calculate this "
                                                "mathematically!'\n"
                                                '\n'
                                                "🤖 PYTHON'S BASIC MATH SYMBOLS:\n"
                                                '• Addition: `+` (e.g. `10 + 5 = 15`)\n'
                                                '• Subtraction: `-` (e.g. `20 - 4 = 16`)\n'
                                                '• Multiplication: `*` (the asterisk symbol, e.g. `25 * 4 = '
                                                '100`)\n'
                                                '• Division: `/` (forward slash, e.g. `10 / 2 = 5.0`)',
                        'terminology': [{'term': 'Integer',
                                         'definition': 'A whole number without a decimal point (e.g. 5, 42, '
                                                       '-10).'},
                                        {'term': 'Float',
                                         'definition': 'A number with a decimal point (e.g. 3.14, 0.5).'},
                                        {'term': 'Operator',
                                         'definition': 'A symbol that performs an operation, like + for '
                                                       'addition or * for multiplication.'}],
                        'syntax_breakdown': '# Text inside quotes is printed verbatim (literally as '
                                            'letters):\n'
                                            "print('10 + 20')  # Outputs text: 10 + 20\n"
                                            '\n'
                                            '# Numbers without quotes are evaluated mathematically by the '
                                            'CPU:\n'
                                            'print(10 + 20)    # Outputs calculation result: 30',
                        'practical_examples': [{'title': 'Example 1: Text vs Math arithmetic',
                                                'code': "print('5 * 4')\nprint(5 * 4)",
                                                'explanation': "Line 1 outputs the literal characters '5 * "
                                                               "4'. Line 2 calculates 5 multiplied by 4 and "
                                                               'outputs 20.',
                                                'output': '5 * 4\n20'},
                                               {'title': 'Example 2: Game score calculation',
                                                'code': "print('Total Game Score:')\nprint(100 + 50 + 25)",
                                                'explanation': 'Combines a text label with an arithmetic '
                                                               'expression calculating the final tally.',
                                                'output': 'Total Game Score:\n175'},
                                               {'title': 'Example 3: Shopping discount calculation',
                                                'code': "print('Original Price: 80')\n"
                                                        "print('Discounted Price:')\n"
                                                        'print(80 - 15)',
                                                'explanation': 'Computes the discounted price dynamically.',
                                                'output': 'Original Price: 80\nDiscounted Price:\n65'}],
                        'line_by_line': [{'line': '1', 'code': "print('5 * 4')", 'explanation': "Show the text '5 * 4' on the screen."}, {'line': '2', 'code': 'print(5 * 4)', 'explanation': 'Work out 5 * 4, then show the answer on the screen.'}],
                        'expected_output': 'Hello, World!\nMath calculation:\n100',
                        'common_mistakes': [{'mistake': 'print(25 x 4)',
                                             'why': 'Python uses the asterisk * for multiplication, not the '
                                                    "letter 'x'.",
                                             'fix': 'print(25 * 4)'}],
                        'real_world_apps': 'Video game score counters, banking balance calculators, and '
                                           'physics simulations all use basic numeric calculations.',
                        'summary': 'Numbers do not use quotes. Use * for multiplication and + for addition. '
                                   'Text uses quotes.',
                        'practice_questions': ['What will print(5 + 5) output?',
                                               "What will print('5 + 5') output?",
                                               'What symbol multiplies numbers in Python?']},
             'challenges': [{'title': 'Hello World Tradition',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Write the classic first-program greeting.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Print Hello, World! on one line. Keep the comma and '
                                             'exclamation mark.',
                             'initial_code': '',
                             'solution_code': "print('Hello, World!')",
                             'hints': ['This is the familiar first message many programmers write.',
                                       'Keep the comma and exclamation mark.',
                                       'Use one output line.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Hello, World!',
                                             'is_hidden': False}]},
                            {'title': 'Boss Challenge: Text or Calculation?',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Show the difference between text and arithmetic.\n2. First print 5 + 5 as words and symbols.\n3. Then calculate the sum and print the answer.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Print 5 + 5 on the first line and 10 on the second. The first '
                                             'line is text; the second is a calculation.',
                             'initial_code': '',
                             'solution_code': "print('5 + 5')\nprint(5 + 5)",
                             'hints': ['Quotes tell Python to display the characters as text.',
                                       'Without quotes, Python treats the plus sign as addition.',
                                       'The text line and the calculated line should look different.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': '5 + 5\n10',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': "What is the difference between print(5 + 5) and print('5 + 5') in "
                                      'Python?',
                          'explanation': 'Without quotes, Python evaluates the arithmetic expression (10). '
                                         "With quotes, it treats it as a string of characters ('5 + 5').",
                          'options': [{'text': "print(5 + 5) calculates 10, while print('5 + 5') prints the "
                                               'literal text 5 + 5.',
                                       'is_correct': True,
                                       'explanation': 'Correct! Without quotes Python does math; with quotes '
                                                      'it prints text.'},
                                      {'text': 'Both statements calculate 10.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Quotes prevent Python from doing '
                                                      'arithmetic.'},
                                      {'text': "Both statements print '5 + 5'.",
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Unquoted numbers are calculated.'},
                                      {'text': 'print(5 + 5) causes a syntax error.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Python calculates numbers easily.'}]},
                         {'question': 'Which symbol is used for multiplication in Python?',
                          'explanation': 'Python uses the asterisk symbol (*) for multiplication (e.g. 5 * '
                                         '2).',
                          'options': [{'text': '* (Asterisk)',
                                       'is_correct': True,
                                       'explanation': 'Correct! 5 * 2 calculates 10.'},
                                      {'text': 'x (The letter x)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. The letter x is treated as a variable '
                                                      'name.'},
                                      {'text': '× (Math cross symbol)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Standard keyboards and Python syntax use '
                                                      'the asterisk *.'},
                                      {'text': '^ (Caret)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. ^ is a bitwise operator in Python, not '
                                                      'multiplication.'}]}]},
            {'number': 5,
             'title': 'Understanding print()',
             'description': 'Master printing multiple items with commas, custom separators (sep), and end '
                            'parameters.',
             'lesson': {'learning_objectives': ['Print multiple items in a single print() statement using '
                                                'commas',
                                                'Understand how Python inserts spaces between '
                                                'comma-separated values',
                                                'Use the sep parameter to customize separators between items',
                                                'Use the end parameter to prevent jumping to a new line'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'So far, you have printed one piece of text at a time. But what if '
                                        'you want to print a word AND a calculated number together, like '
                                        "'Score: 100'? In Python, you can print multiple items in a single "
                                        'line simply by separating them with commas!',
                        'detailed_explanation': '### In simple words\n'
                                                '`print()` can show several values on one line. Separate the '
                                                'values with commas; Python puts a space between them by '
                                                'default. The `sep` setting changes that space, and `end` '
                                                'changes what print adds after its output.\n'
                                                '\n'
                                                '### Try it step by step\n'
                                                "`print('Score:', 10 + 5)` shows `Score: 15`.\n"
                                                "`print('A', 'B', sep='-')` shows `A-B`.\n"
                                                "`print('Loading', end='... ')` keeps the next print on the "
                                                'same line.\n'
                                                '\n'
                                                'The comma separates values for `print()`. The plus sign '
                                                'joins or calculates values, depending on their types.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 WHY DO WE USE COMMAS INSIDE print()?\n'
                                                'When you put commas between items inside `print()`, Python '
                                                'prints each item and automatically inserts a single space '
                                                'in between:\n'
                                                "`print('Score:', 50 + 50)` &rarr; outputs: `Score: 100`\n"
                                                '\n'
                                                '🔍 THE sep PARAMETER (CUSTOM SEPARATORS):\n'
                                                'By default, Python puts a space between comma items. If you '
                                                'want to separate them with a hyphen or dash instead, you '
                                                "tell Python: `sep='-'`!\n"
                                                "`print('Apple', 'Banana', 'Cherry', sep='-')` &rarr; "
                                                'outputs: `Apple-Banana-Cherry`\n'
                                                '\n'
                                                '🔍 THE end PARAMETER (CONTROLLING LINE ENDINGS):\n'
                                                'By default, after printing, Python presses Enter and starts '
                                                'the next line. If you want to stay on the same line, you '
                                                "pass `end='... '`!\n"
                                                "`print('Loading', end='... ')` &rarr; stays on the same "
                                                'line!',
                        'terminology': [{'term': 'Argument',
                                         'definition': 'A value passed into a function inside parentheses, '
                                                       'separated by commas.'},
                                        {'term': 'sep Parameter',
                                         'definition': 'A parameter in print() that specifies what symbol '
                                                       'goes between items (default is space).'},
                                        {'term': 'end Parameter',
                                         'definition': 'A parameter in print() that specifies what symbol '
                                                       'goes at the end of the line (default is newline).'}],
                        'syntax_breakdown': '# Pass multiple items separated by commas (default separator is '
                                            'a space):\n'
                                            "print('Health:', 100, 'Shield:', 50)\n"
                                            '\n'
                                            "# Custom separator between items with sep='...':\n"
                                            "print('2026', '11', '03', sep='-')\n"
                                            '\n'
                                            "# Custom ending instead of a new line with end='...':\n"
                                            "print('Loading', end='... ')\n"
                                            "print('Complete!')",
                        'practical_examples': [{'title': 'Example 1: Inventory list with custom separator',
                                                'code': "print('Sword', 'Shield', 'Potion', sep=' | ')",
                                                'explanation': "The sep=' | ' argument replaces the default "
                                                               'space with a clean divider between items.',
                                                'output': 'Sword | Shield | Potion'},
                                               {'title': "Example 2: Inline progress meter with end=''",
                                                'code': "print('Uploading data', end=' -> ')\n"
                                                        "print('Verified!')",
                                                'explanation': 'By default print() adds a newline at the '
                                                               "end. end=' -> ' keeps the next print on the "
                                                               'same line.',
                                                'output': 'Uploading data -> Verified!'},
                                               {'title': 'Example 3: Telemetry sensor log',
                                                'code': "print('Sensor 1', '24.5C', '1013hPa', sep=', ')",
                                                'explanation': 'Formats multiple variables into standard '
                                                               'comma-separated values (CSV).',
                                                'output': 'Sensor 1, 24.5C, 1013hPa'}],
                        'line_by_line': [{'line': '1', 'code': "print('Sword', 'Shield', 'Potion', sep=' | ')", 'explanation': 'Show the items on one line with the chosen separator between them.'}],
                        'expected_output': 'Red | Green | Blue\nStatus: 100 %',
                        'common_mistakes': [{'mistake': "print('A', 'B', sep - '-')",
                                             'why': "Parameter assignment uses equals sign: sep='-'.",
                                             'fix': "print('A', 'B', sep='-')"}],
                        'real_world_apps': "Formatting dates like '2026-11-02' and constructing progress "
                                           'bars.',
                        'summary': "Commas let you print multiple values. sep='-' changes the separator. "
                                   "end='' controls line ending.",
                        'practice_questions': ['What does Python place between comma-separated items by '
                                               'default?',
                                               'How do you separate items with a hyphen in print()?',
                                               "What does end='' do?"]},
             'challenges': [{'title': 'Custom Delimiters',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Print Apple, Banana, and Cherry on one line, with a hyphen between each fruit.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Use print with the sep setting. The output should be '
                                             'Apple-Banana-Cherry.',
                             'initial_code': '',
                             'solution_code': "print('Apple', 'Banana', 'Cherry', sep='-')",
                             'hints': ['Print all three fruit names together.',
                                       'The separator setting changes the spaces between the names.',
                                       'Check that the output has hyphens and no extra spaces.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Apple-Banana-Cherry',
                                             'is_hidden': False}]},
                            {'title': 'Boss Challenge: Continuous Status Bar',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Create a one-line loading message.\n2. Print Loading, keep the cursor on the same line, then print 100%.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'The final output should read Loading... 100% on one line.',
                             'initial_code': '',
                             'solution_code': "print('Loading', end='... ')\nprint('100%')",
                             'hints': ['The first print normally moves to a new line.',
                                       'Change what print adds at the end of the first message.',
                                       'The loading message and percentage should share one line.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Loading... 100%',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': 'What does Python insert between items by default when you separate '
                                      "them with commas in print('A', 'B')?",
                          'explanation': 'By default, print() places a single space character between '
                                         'comma-separated items.',
                          'options': [{'text': 'A single space: A B',
                                       'is_correct': True,
                                       'explanation': 'Correct! Python puts one space between '
                                                      'comma-separated arguments.'},
                                      {'text': 'Nothing at all: AB',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. A space is automatically inserted.'},
                                      {'text': 'A newline after every item',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Newlines only occur at the end of the '
                                                      'entire print statement.'},
                                      {'text': 'A literal comma: A,B',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Commas separate the arguments in code, but '
                                                      'are not printed.'}]},
                         {'question': 'Which parameter inside print() allows you to change the separator '
                                      'between items?',
                          'explanation': 'The sep parameter (short for separator) customizes the string '
                                         'inserted between items.',
                          'options': [{'text': "sep (e.g. sep='-')",
                                       'is_correct': True,
                                       'explanation': "Correct! sep='-' replaces spaces with dashes."},
                                      {'text': 'delimiter',
                                       'is_correct': False,
                                       'explanation': "Incorrect. Python uses 'sep', not 'delimiter'."},
                                      {'text': 'split',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. split is a string method, not a print '
                                                      'parameter.'},
                                      {'text': 'between',
                                       'is_correct': False,
                                       'explanation': "Incorrect. 'between' is not a valid parameter."}]}]},
            {'number': 6,
             'title': 'Understanding Text and Strings',
             'description': 'Learn string concatenation (+), joining text, and newlines (\\n).',
             'lesson': {'learning_objectives': ['Understand what strings are in programming',
                                                'Join text together using the concatenation operator (+)',
                                                "Understand why '5' + '5' equals '55' and not 10",
                                                'Use \\n to create newlines inside a single string'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'In programming, any sequence of characters (letters, numbers, '
                                        "spaces, symbols) wrapped in quotes is called a 'string'. Think of "
                                        'beads strung on a necklace. You can combine and manipulate strings '
                                        'in powerful ways.',
                        'detailed_explanation': '### In simple words\n'
                                                'A string is text inside matching quotes. The plus sign '
                                                'joins strings together. Python does not add a space for '
                                                "you, so include a space string (`' '`) when you want one.\n"
                                                '\n'
                                                '### Try it step by step\n'
                                                "`'Python' + 'Quest'` becomes `PythonQuest`.\n"
                                                "`'Python' + ' ' + 'Quest'` becomes `Python Quest`.\n"
                                                '\n'
                                                'You can also put `\\n` inside a string to start a new '
                                                'output line. It is a special two-character code in your '
                                                'program that becomes a line break when printed. Keep the '
                                                'whole message inside one matching pair of quotes.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 WHY DO WE USE THE PLUS (+) SIGN WITH STRINGS?\n'
                                                'When you put a plus sign `+` between two strings, Python '
                                                'glues them together end-to-end. This is called '
                                                '**concatenation**:\n'
                                                "`print('Python' + 'Quest')` &rarr; outputs: `PythonQuest`\n"
                                                '\n'
                                                '⚠️ CRUCIAL DIFFERENCE:\n'
                                                'Notice that `+` does NOT insert a space automatically! If '
                                                "you want a space, you must add it yourself: `'Python' + ' ' "
                                                "+ 'Quest'`.\n"
                                                "Also: `print('5' + '5')` outputs `55`, because quotes tell "
                                                'Python they are text characters, not numbers!',
                        'terminology': [{'term': 'String',
                                         'definition': 'A sequence of characters enclosed in quotation '
                                                       'marks.'},
                                        {'term': 'Concatenation',
                                         'definition': 'The operation of joining two or more strings '
                                                       'end-to-end using the + operator.'},
                                        {'term': 'Escape Sequence (\\n)',
                                         'definition': 'A special character combination representing a '
                                                       'newline.'}],
                        'syntax_breakdown': "# String concatenation joins strings together with '+':\n"
                                            "print('Super' + ' ' + 'Nova')\n"
                                            '\n'
                                            "# String repetition multiplies strings with '*':\n"
                                            "print('=' * 20)\n"
                                            '\n'
                                            '# Escape character \\n creates a new line inside a single '
                                            'string:\n'
                                            "print('Line 1\\nLine 2')",
                        'practical_examples': [{'title': 'Example 1: Personalized player welcome',
                                                'code': "print('Hello, ' + 'Captain ' + 'Reynolds' + '!')",
                                                'explanation': 'Concatenates title, name, and punctuation '
                                                               'into one cohesive message.',
                                                'output': 'Hello, Captain Reynolds!'},
                                               {'title': 'Example 2: Visual separator border',
                                                'code': "print('*' * 20)\n"
                                                        "print('  QUEST VICTORY  ')\n"
                                                        "print('*' * 20)",
                                                'explanation': "Repeats '*' 20 times to build neat visual "
                                                               'header borders without typing 20 stars '
                                                               'manually.',
                                                'output': '********************\n'
                                                          '  QUEST VICTORY  \n'
                                                          '********************'},
                                               {'title': 'Example 3: Multi-line invoice receipt with \\n',
                                                'code': "print('INVOICE:\\nItem: Laser Blaster\\nCost: 150 "
                                                        "Credits')",
                                                'explanation': 'Uses the \\n escape sequence to break a '
                                                               'single string across three distinct terminal '
                                                               'lines.',
                                                'output': 'INVOICE:\n'
                                                          'Item: Laser Blaster\n'
                                                          'Cost: 150 Credits'}],
                        'line_by_line': [{'line': '1', 'code': "print('Hello, ' + 'Captain ' + 'Reynolds' + '!')", 'explanation': "Work out 'Hello, ' + 'Captain ' + 'Reynolds' + '!', then show the answer on the screen."}],
                        'expected_output': 'Welcome to Python Quest!\nTop\nBottom',
                        'common_mistakes': [{'mistake': "print('Score: ' + 100)",
                                             'why': 'You cannot concatenate a string and a number with + '
                                                    'directly. Use commas or convert to string.',
                                             'fix': "print('Score:', 100)"}],
                        'real_world_apps': 'Constructing dynamic URLs, user welcome greetings, and '
                                           'generating email notifications.',
                        'summary': 'Strings are text in quotes. The + operator concatenates strings together '
                                   'without extra spaces. \\n creates a new line.',
                        'practice_questions': ["What will print('5' + '5') output?",
                                               'What does concatenation mean?',
                                               'What does \\n do in a string?']},
             'challenges': [{'title': 'String Concatenation',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Join the words Python and Quest with one space between them.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Use the plus sign to join the two words and a space. Print the '
                                             'result.',
                             'initial_code': '',
                             'solution_code': "print('Python' + ' ' + 'Quest')",
                             'hints': ['A string is text between matching quote marks.',
                                       'The plus sign joins strings together.',
                                       'Add a separate space between the two words.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Python Quest',
                                             'is_hidden': False}]},
                            {'title': 'Boss Challenge: Multiline Quest Dialogue',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Print a two-line conversation in one print instruction.\n2. The mentor speaks first the hero replies that they are ready to learn.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'The output should be Mentor: Welcome to the Citadel. followed '
                                             'by Hero: I am ready to learn. on the next line.',
                             'initial_code': '',
                             'solution_code': "print('Mentor: Welcome to the Citadel.\\nHero: I am ready to "
                                              "learn.')",
                             'hints': ['One print instruction can display two lines.',
                                       'A special newline marker moves the second part to a new line.',
                                       'The second line says the hero is ready to learn.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Mentor: Welcome to the Citadel.\n'
                                                                'Hero: I am ready to learn.',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': "What will be the result of print('5' + '5') in Python?",
                          'explanation': "Because '5' is in quotation marks, it is a string. The + operator "
                                         "concatenates them into '55'.",
                          'options': [{'text': '55 (The text is joined together)',
                                       'is_correct': True,
                                       'explanation': 'Correct! Strings are concatenated, not added '
                                                      'mathematically.'},
                                      {'text': '10 (Mathematical addition)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. For 10, write print(5 + 5) without '
                                                      'quotes.'},
                                      {'text': 'TypeError: cannot add text',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Concatenating strings with + is valid.'},
                                      {'text': '5 5 (with a space)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. The + operator does not insert spaces.'}]},
                         {'question': 'What does the escape sequence \\n do when written inside a string?',
                          'explanation': '\\n inserts a line break (newline), causing following text to '
                                         'start on the next line.',
                          'options': [{'text': 'It creates a newline, moving subsequent text to the next '
                                               'line.',
                                       'is_correct': True,
                                       'explanation': 'Correct! \\n acts like pressing Enter.'},
                                      {'text': 'It cancels the execution of the program.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. It is simply a newline character.'},
                                      {'text': 'It prints the literal letters backslash and n.',
                                       'is_correct': False,
                                       'explanation': "Incorrect. The backslash escapes the 'n' to mean "
                                                      'newline.'},
                                      {'text': 'It converts text to uppercase.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. It only creates a line break.'}]}]},
            {'number': 7,
             'title': 'Understanding Numbers',
             'description': 'Explore arithmetic calculations, multiplication, and order of operations.',
             'lesson': {'learning_objectives': ['Master order of operations in Python math',
                                                'Perform multi-step arithmetic calculations',
                                                'Combine descriptive text and calculated numbers in output'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'Computers were originally designed as calculation engines. In '
                                        'Python, solving math problems is clean and instant.',
                        'detailed_explanation': '### In simple words\n'
                                                'Python can calculate with numbers. Use `+` to add, `-` to '
                                                'subtract, `*` to multiply, and `/` to divide. Put a '
                                                'calculation inside `print()` to show its answer.\n'
                                                '\n'
                                                '### Try it step by step\n'
                                                '`print(25 * 4)` shows `100`.\n'
                                                'Python follows normal math order: multiplication happens '
                                                'before addition. Use parentheses when you want to choose '
                                                'what happens first: `(5 + 3) * 2`.\n'
                                                '\n'
                                                'Do not put quotes around numbers that you want Python to '
                                                'calculate. Quoted numbers are text.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 ORDER OF OPERATIONS IN PYTHON:\n'
                                                'Python obeys standard order of operations: parentheses '
                                                'first, multiplication and division next, addition and '
                                                'subtraction last.\n'
                                                '`print(10 + 5 * 2)` &rarr; evaluates `5 * 2 = 10`, then `10 '
                                                '+ 10 = 20`!\n'
                                                '\n'
                                                'You can print both descriptive text and calculated results '
                                                'together using commas:\n'
                                                "`print('Total:', 25 * 4)` &rarr; outputs: `Total: 100`",
                        'terminology': [{'term': 'Expression',
                                         'definition': 'A combination of numbers, operators, and variables '
                                                       'that Python evaluates to a single value.'},
                                        {'term': 'Order of Operations',
                                         'definition': 'The standard mathematical rules determining which '
                                                       'operations are evaluated first.'}],
                        'syntax_breakdown': '# Standard arithmetic operators in Python:\n'
                                            'print(20 + 5)   # Addition: 25\n'
                                            'print(20 - 5)   # Subtraction: 15\n'
                                            'print(20 * 5)   # Multiplication: 100\n'
                                            'print(20 / 4)   # Float division: 5.0 (always gives decimal)\n'
                                            'print((10 + 2) * 3) # Parentheses force execution order: 36',
                        'practical_examples': [{'title': 'Example 1: Item shop cost tally',
                                                'code': "print('Total item cost:')\nprint(3 * 15 + 10)",
                                                'explanation': 'Multiplication takes precedence over '
                                                               'addition: 3 * 15 is 45, then + 10 equals 55.',
                                                'output': 'Total item cost:\n55'},
                                               {'title': 'Example 2: PEMDAS order of operations with '
                                                         'parentheses',
                                                'code': 'print(5 + 3 * 2)\nprint((5 + 3) * 2)',
                                                'explanation': 'Without parentheses, 3 * 2 is evaluated '
                                                               'first (11). With parentheses, (5 + 3) '
                                                               'evaluates first (16).',
                                                'output': '11\n16'},
                                               {'title': 'Example 3: Splitting a dinner bill evenly',
                                                'code': "print('Total Bill: $120')\n"
                                                        "print('Per person share:')\n"
                                                        'print(120 / 4)',
                                                'explanation': 'Divides 120 among 4 people. Division '
                                                               'operator / always produces a floating-point '
                                                               'number.',
                                                'output': 'Total Bill: $120\nPer person share:\n30.0'}],
                        'line_by_line': [{'line': '1', 'code': "print('Total item cost:')", 'explanation': "Show the text 'Total item cost:' on the screen."}, {'line': '2', 'code': 'print(3 * 15 + 10)', 'explanation': 'Work out 3 * 15 + 10, then show the answer on the screen.'}],
                        'expected_output': '100\nSum: 150',
                        'common_mistakes': [{'mistake': "print('25 * 4')",
                                             'why': 'Quotes around math turn it into text instead of '
                                                    'calculating it.',
                                             'fix': 'print(25 * 4)'}],
                        'real_world_apps': 'E-commerce checkout totals, game damage formulas, and tax '
                                           'calculations.',
                        'summary': 'Python evaluates arithmetic expressions instantly. Use commas to combine '
                                   'text and numbers.',
                        'practice_questions': ['What will print(10 + 5 * 2) output?',
                                               'How do you print a label next to a calculated number?']},
             'challenges': [{'title': 'Python Math Calculator',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Calculate 25 multiplied by 4 and print the answer.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Keep the numbers outside quotation marks so Python calculates '
                                             'them. The output should be 100.',
                             'initial_code': '',
                             'solution_code': 'print(25 * 4)',
                             'hints': ['The star symbol means multiplication in Python.',
                                       'Use numbers, not quoted text, for a calculation.',
                                       'Check the multiplication result before running.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '',
                                             'expected_output': '100',
                                             'is_hidden': False}]},
                            {'title': 'Boss Challenge: Arithmetic Card',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Print a sum and a product on two separate lines.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'First show Sum: 150. Then show Product: 500.',
                             'initial_code': '',
                             'solution_code': "print('Sum:', 100 + 50)\nprint('Product:', 50 * 10)",
                             'hints': ['A sum uses addition.',
                                       'A product uses multiplication.',
                                       'Print the label and its calculated value on each line.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Sum: 150\nProduct: 500',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': 'What is the output of print(10 + 5 * 2) in Python?',
                          'explanation': 'Multiplication has higher precedence than addition, so 5 * 2 is '
                                         'evaluated first (10), then 10 + 10 = 20.',
                          'options': [{'text': '20 (Multiplication occurs before addition)',
                                       'is_correct': True,
                                       'explanation': 'Correct! 5 * 2 = 10, then 10 + 10 = 20.'},
                                      {'text': '30 (Addition occurs first: 15 * 2)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Python follows standard order of '
                                                      'operations: multiplication first.'},
                                      {'text': '100', 'is_correct': False, 'explanation': 'Incorrect.'},
                                      {'text': 'SyntaxError',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Numeric expressions are valid.'}]},
                         {'question': 'Which of the following lines correctly prints: Score: 100?',
                          'explanation': "Separating the text label 'Score:' and the number 100 with a comma "
                                         "outputs 'Score: 100'.",
                          'options': [{'text': "print('Score:', 50 + 50)",
                                       'is_correct': True,
                                       'explanation': "Correct! Evaluates 50 + 50 to 100 and prints 'Score: "
                                                      "100'."},
                                      {'text': "print('Score: + 50 + 50')",
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Everything inside quotes is printed '
                                                      'literally.'},
                                      {'text': 'print(Score:, 100)',
                                       'is_correct': False,
                                       'explanation': "Incorrect. 'Score:' without quotes causes a "
                                                      'SyntaxError.'},
                                      {'text': "print('Score:' 100)",
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Missing comma between items causes a '
                                                      'SyntaxError.'}]}]},
            {'number': 8,
             'title': 'Python Comments',
             'description': 'Document code clearly using single-line and multi-line comments.',
             'lesson': {'learning_objectives': ['Document code effectively with meaningful comments',
                                                'Temporarily disable problematic code by commenting it out',
                                                'Understand proper comment placement'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'Good code is self-explanatory, but great code includes helpful '
                                        'documentation for fellow engineers.',
                        'detailed_explanation': '### In simple words\n'
                                                'A comment is a note for a person reading your code. Start '
                                                'it with `#`. Python ignores everything from that symbol to '
                                                'the end of the line, so a commented-out instruction will '
                                                'not run.\n'
                                                '\n'
                                                '### Try it step by step\n'
                                                '`# show the score` is only a note.\n'
                                                '`print(15 * 6)` is an instruction and displays `90`.\n'
                                                'To temporarily stop a line from running, put `#` at the '
                                                'beginning of that line. Remove the `#` when you want it to '
                                                'run again.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 WHY DO WE USE COMMENTS?\n'
                                                'Comments allow you to:\n'
                                                '1. Explain what complex code is doing in simple human '
                                                'words.\n'
                                                '2. Provide section headers so your file is organized.\n'
                                                "3. Temporarily 'comment out' code during testing to prevent "
                                                'bugs without deleting it.',
                        'terminology': [{'term': 'Commenting Out',
                                         'definition': 'Adding # before a line of code so Python skips it '
                                                       'during execution.'}],
                        'syntax_breakdown': '# 1. Inline comment explaining units of measurement:\n'
                                            'speed_mph = 65  # Speed in miles per hour\n'
                                            '\n'
                                            '# 2. Block comment documenting calculation formula:\n'
                                            '# ---------------------------------------------\n'
                                            '# Total Fuel = (Distance / MPG) * Price_Per_Gal\n'
                                            '# ---------------------------------------------\n'
                                            "print('Calculating trip fuel requirements...')",
                        'practical_examples': [{'title': 'Example 1: Documenting formula context',
                                                'code': '# Convert 3 hours into total seconds: 3 * 60 * 60\n'
                                                        "print('Total seconds in 3 hours:')\n"
                                                        'print(3 * 60 * 60)',
                                                'explanation': 'Explains why the numbers 60 and 60 are being '
                                                               'multiplied so teammates understand the '
                                                               'formula.',
                                                'output': 'Total seconds in 3 hours:\n10800'},
                                               {'title': 'Example 2: Bug triage and isolating code',
                                                'code': "# print('Legacy physics engine running')\n"
                                                        "print('Next-gen physics engine online.')",
                                                'explanation': 'Temporarily disabling a line with a comment '
                                                               'lets you test new code without deleting the '
                                                               'old code.',
                                                'output': 'Next-gen physics engine online.'},
                                               {'title': 'Example 3: Step-by-step workflow documentation',
                                                'code': '# Step 1: Connect to flight telemetry\n'
                                                        "print('Telemetry: Connected')\n"
                                                        '# Step 2: Calibrate gyroscopes\n'
                                                        "print('Calibration: Complete')",
                                                'explanation': 'Separates logical execution stages with '
                                                               'clear comment markers.',
                                                'output': 'Telemetry: Connected\nCalibration: Complete'}],
                        'line_by_line': [{'line': '1', 'code': '# Convert 3 hours into total seconds: 3 * 60 * 60', 'explanation': 'This is a note for the person reading the code. Python skips comments, so this line does not run or print anything.'}, {'line': '2', 'code': "print('Total seconds in 3 hours:')", 'explanation': "Show the text 'Total seconds in 3 hours:' on the screen."}, {'line': '3', 'code': 'print(3 * 60 * 60)', 'explanation': 'Work out 3 * 60 * 60, then show the answer on the screen.'}],
                        'expected_output': 'System Online\nQuest Ready',
                        'common_mistakes': [{'mistake': "print('Hello' # comment)",
                                             'why': 'Do not put comments inside function calls.',
                                             'fix': "print('Hello')  # comment"}],
                        'real_world_apps': 'Documenting team repositories and API specifications on GitHub.',
                        'summary': 'Use # for single-line notes and to comment out code during testing.',
                        'practice_questions': ['What does commenting out code mean?',
                                               'Can you place a comment at the end of a code line?']},
             'challenges': [{'title': 'Documenting Code',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Write a note that says Calculate score.\n2. Then print the result of 15 multiplied by 6.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'The note must be a comment, so begin it with #. The output '
                                             'should be 90.',
                             'initial_code': '',
                             'solution_code': '# Calculate score\nprint(15 * 6)',
                             'hints': ['A comment begins with the # symbol.',
                                       'Python skips a comment when it runs the program.',
                                       'Only the calculation should produce output.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '', 'expected_output': '90', 'is_hidden': False}]},
                            {'title': 'Boss Challenge: Commenting Out Bugs',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Write three lines.\n2. Show System Online, add a commented-out error message in the middle, then show Quest Ready.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'The error line must begin with # so it does not run. Output '
                                             'only System Online and Quest Ready, each on its own line.',
                             'initial_code': '',
                             'solution_code': "print('System Online')\n"
                                              "# print('System Error: Broken Component')\n"
                                              "print('Quest Ready')",
                             'hints': ['A # at the start turns a line into a note that Python skips.',
                                       'Keep the first and last print instructions active.',
                                       'The output should contain two lines, with no error message.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'System Online\nQuest Ready',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': "What is 'commenting out' code?",
                          'explanation': 'Adding a # symbol at the start of a code line disables it without '
                                         'having to delete the text.',
                          'options': [{'text': 'Adding a # at the start of a line to temporarily disable it.',
                                       'is_correct': True,
                                       'explanation': 'Correct! It stops Python from running that line.'},
                                      {'text': 'Deleting the entire file permanently.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect.'},
                                      {'text': 'Translating code into another language.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect.'},
                                      {'text': 'Printing text to the console.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect.'}]},
                         {'question': 'What will be printed when this program runs?\n'
                                      '\n'
                                      "# print('Alpha')\n"
                                      "print('Beta')\n"
                                      "# print('Gamma')",
                          'explanation': 'Alpha and Gamma are commented out with #, so only Beta executes.',
                          'options': [{'text': 'Beta',
                                       'is_correct': True,
                                       'explanation': 'Correct! Only Beta is not commented out.'},
                                      {'text': 'Alpha\nBeta\nGamma',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Lines with # are skipped.'},
                                      {'text': 'Alpha', 'is_correct': False, 'explanation': 'Incorrect.'},
                                      {'text': 'Nothing at all',
                                       'is_correct': False,
                                       'explanation': 'Incorrect.'}]}]},
            {'number': 9,
             'title': 'Understanding Basic Syntax',
             'description': 'Master case sensitivity, indentation rules, and common syntax errors.',
             'lesson': {'learning_objectives': ['Recognize and fix common SyntaxError and NameError issues',
                                                'Understand Python indentation rules (no unexpected leading '
                                                'spaces)',
                                                'Write clean, error-free statement blocks'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'Every human language has grammar rules: spelling, punctuation, and '
                                        'capitalization. In programming, these rules are called syntax.',
                        'detailed_explanation': '### In simple words\n'
                                                'Python expects code to follow exact spelling and '
                                                'punctuation rules. A missing quote or parenthesis can stop '
                                                'the program before it runs. Capitalization matters for '
                                                'Python names such as `print`.\n'
                                                '\n'
                                                '### Try it step by step\n'
                                                'Before running a line, check that every opening quote has a '
                                                'matching closing quote, every `(` has a `)`, and names such '
                                                'as `print` use the correct lowercase letters.\n'
                                                '\n'
                                                'At the start of a program, write each top-level line from '
                                                'the left edge. Spaces at the start are used for grouping '
                                                'code inside blocks, which you will learn later.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 THE 3 MOST COMMON BEGINNER ERRORS AND HOW TO AVOID THEM:\n'
                                                "1. Unclosed quotes: `print('Hello)` &rarr; You opened `'` "
                                                "but forgot to close it with another `'` before the "
                                                'bracket!\n'
                                                "2. Unclosed parenthesis: `print('Hello'` &rarr; You opened "
                                                '`(` but forgot to close it with `)` at the end!\n'
                                                '3. Accidental leading spaces: In Python, you must not add '
                                                'random spaces at the very start of a line, or Python will '
                                                'raise an `IndentationError`!',
                        'terminology': [{'term': 'SyntaxError',
                                         'definition': 'An error raised when code violates the grammar rules '
                                                       'of Python.'},
                                        {'term': 'IndentationError',
                                         'definition': 'An error caused by improper leading whitespace or '
                                                       'tab characters.'}],
                        'syntax_breakdown': '# Top-level code must start flush against the left margin '
                                            '(column 0):\n'
                                            "print('Clean line 1: Zero extra indentation')\n"
                                            "print('Clean line 2: Matches column 0 exactly')\n"
                                            '\n'
                                            '# Python is strictly case-sensitive:\n'
                                            "# print('Valid')    <-- Correct\n"
                                            "# Print('Error')    <-- NameError: name 'Print' is not defined",
                        'practical_examples': [{'title': 'Example 1: Proper indentation flow',
                                                'code': "print('Alpha')\nprint('Beta')\nprint('Gamma')",
                                                'explanation': 'All three statements align precisely at '
                                                               'column 0. Unintentional spaces at the '
                                                               'beginning cause IndentationError.',
                                                'output': 'Alpha\nBeta\nGamma'},
                                               {'title': 'Example 2: Matching brackets and quotes',
                                                'code': "print('Total XP: ' + '500')",
                                                'explanation': "Every opening parenthesis '(' must have a "
                                                               "matching closing parenthesis ')'. Quotes "
                                                               'must pair up.',
                                                'output': 'Total XP: 500'},
                                               {'title': 'Example 3: Handling mixed quotes cleanly',
                                                'code': 'print(\'Captain said: "Shields up!"\')',
                                                'explanation': 'Enclosing the text in single quotes allows '
                                                               'double quotes inside the string without '
                                                               'errors.',
                                                'output': 'Captain said: "Shields up!"'}],
                        'line_by_line': [{'line': '1', 'code': "print('Alpha')", 'explanation': "Show the text 'Alpha' on the screen."}, {'line': '2', 'code': "print('Beta')", 'explanation': "Show the text 'Beta' on the screen."}, {'line': '3', 'code': "print('Gamma')", 'explanation': "Show the text 'Gamma' on the screen."}],
                        'expected_output': 'STATUS: ACTIVE\nSYNTAX: VERIFIED\nWORLD 1: NEARLY MASTERED',
                        'common_mistakes': [{'mistake': " print('Indented')",
                                             'why': 'Unnecessary leading spaces cause an IndentationError at '
                                                    'top level.',
                                             'fix': "print('Indented')"}],
                        'real_world_apps': 'Clean syntax is essential for automated code linting in '
                                           'continuous integration pipelines.',
                        'summary': 'Check matching quotes, matching parentheses, and ensure lines start '
                                   'without accidental leading spaces.',
                        'practice_questions': ['What causes an IndentationError?',
                                               'What should you check if you get a SyntaxError?']},
             'challenges': [{'title': 'Writing Valid Python Syntax',
                             'difficulty': 'easy',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Write a valid Python print instruction for the message Syntax Fixed: Ready to Code.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Check that print is lowercase and that the quotes and '
                                             'parentheses are complete.',
                             'initial_code': '',
                             'solution_code': "print('Syntax Fixed: Ready to Code')",
                             'hints': ['Python names are case-sensitive.',
                                       'Use matching opening and closing quote marks.',
                                       'Check that every opening parenthesis has a closing one.'],
                             'xp_reward': 30,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Syntax Fixed: Ready to Code',
                                             'is_hidden': False}]},
                            {'title': 'Boss Challenge: Clean Statement Block',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Print three status messages.\n2. Start every line at the far left with no spaces before it.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Print STATUS: ACTIVE, SYNTAX: VERIFIED, and WORLD 1: NEARLY '
                                             'MASTERED on separate lines.',
                             'initial_code': '',
                             'solution_code': "print('STATUS: ACTIVE')\n"
                                              "print('SYNTAX: VERIFIED')\n"
                                              "print('WORLD 1: NEARLY MASTERED')",
                             'hints': ['Start each instruction at the far left.',
                                       'Use one output line for each status message.',
                                       'Check spelling and order before running.'],
                             'xp_reward': 150,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'STATUS: ACTIVE\n'
                                                                'SYNTAX: VERIFIED\n'
                                                                'WORLD 1: NEARLY MASTERED',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': 'What happens if you accidentally add leading spaces at the very start '
                                      'of a line in Python?\n'
                                      '\n'
                                      "  print('Hello')",
                          'explanation': 'Python uses indentation to define code blocks. Unnecessary leading '
                                         'spaces at the top level raise an IndentationError.',
                          'options': [{'text': 'IndentationError: unexpected indent',
                                       'is_correct': True,
                                       'explanation': 'Correct! Top-level code must not have random leading '
                                                      'spaces.'},
                                      {'text': 'Python runs normally and ignores the spaces.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Python is very strict about indentation.'},
                                      {'text': 'The text prints in the middle of the screen.',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Spaces in code do not format terminal '
                                                      'positioning.'},
                                      {'text': 'ZeroDivisionError',
                                       'is_correct': False,
                                       'explanation': 'Incorrect.'}]},
                         {'question': 'Which of the following will cause a SyntaxError in Python?',
                          'explanation': "print('Hello) has an unclosed string literal (missing closing "
                                         'quote).',
                          'options': [{'text': "print('Hello)",
                                       'is_correct': True,
                                       'explanation': 'Correct! Missing closing quote raises SyntaxError: '
                                                      'unterminated string literal.'},
                                      {'text': "print('Hello')",
                                       'is_correct': False,
                                       'explanation': 'Incorrect. This is completely valid.'},
                                      {'text': 'print(100)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Printing numbers is completely valid.'},
                                      {'text': "print('A', 'B')",
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Comma-separated arguments are valid.'}]}]},
            {'number': 10,
             'title': 'World 1 Examination',
             'description': 'Synthesize all beginner concepts and build your first full program.',
             'lesson': {'learning_objectives': ['Synthesize print(), text, numbers, calculations, comments, '
                                                'and delimiters',
                                                'Build a complete multi-line Personal Profile Card program',
                                                'Pass the World 1 graduation requirements'],
                        'prerequisites': 'No prior Python knowledge is needed for this lesson.',
                        'introduction': 'Congratulations on reaching the World 1 Capstone! You have learned '
                                        'the foundational mechanics of Python: instructions, strings, '
                                        'numbers, comments, and syntax.',
                        'detailed_explanation': '### In simple words\n'
                                                'This level brings together the ideas from World 1: write '
                                                'instructions with `print()`, use quotes for text, let '
                                                'Python calculate unquoted numbers, and add comments when a '
                                                'note helps.\n'
                                                '\n'
                                                '### Build it one line at a time\n'
                                                '1. Decide what each output line should say.\n'
                                                '2. Put text inside quotes.\n'
                                                '3. Put any calculation outside quotes.\n'
                                                '4. Use commas when one print line needs both a label and a '
                                                'calculated value.\n'
                                                '5. Run the whole program and compare every line with the '
                                                'requested output.\n'
                                                '\n'
                                                'If Python reports a syntax error, check the spelling, '
                                                'matching quotes and parentheses, and the start of each '
                                                'line.\n'
                                                '\n'
                                                '### More detail\n'
                                                '🎯 BRINGING IT ALL TOGETHER:\n'
                                                'In this final project, you will build a complete developer '
                                                'card program: printing banners, identity text, calculated '
                                                'XP targets, and status declarations!\n'
                                                'Notice how every skill you learned works in harmony:\n'
                                                '• `print()` makes words appear.\n'
                                                "• Quotes `'...'` wrap your text.\n"
                                                '• Math without quotes calculates numbers.\n'
                                                '• Commas `,` combine words and calculations on the same '
                                                'line!',
                        'terminology': [{'term': 'Capstone',
                                         'definition': 'A comprehensive project that synthesizes all '
                                                       'knowledge acquired across a learning world.'}],
                        'syntax_breakdown': '# World 1 Capstone Synthesis:\n'
                                            "print('========================================')\n"
                                            "print('           PILOT MISSION LOG            ')\n"
                                            "print('========================================')\n"
                                            "print('Callsign:', 'Viper', sep=' ')\n"
                                            "print('Missions Flown:', 12 + 3)\n"
                                            "print('Status:', 'Flight Certified')",
                        'practical_examples': [{'title': 'Example 1: Pilot badge card',
                                                'code': "print('PILOT:', 'Alex Vance')\n"
                                                        "print('RANK:', 'Lieutenant')\n"
                                                        "print('MISSIONS:', 14)",
                                                'explanation': 'A complete 3-line identification badge '
                                                               'combining strings and integers.',
                                                'output': 'PILOT: Alex Vance\n'
                                                          'RANK: Lieutenant\n'
                                                          'MISSIONS: 14'},
                                               {'title': 'Example 2: Store checkout summary',
                                                'code': "print('--- STORE RECEIPT ---')\n"
                                                        "print('Subtotal:', 40 + 25)\n"
                                                        "print('Tax:', 5)\n"
                                                        "print('Total:', 40 + 25 + 5)",
                                                'explanation': 'Generates a clean itemized receipt with '
                                                               'mathematical totals.',
                                                'output': '--- STORE RECEIPT ---\n'
                                                          'Subtotal: 65\n'
                                                          'Tax: 5\n'
                                                          'Total: 70'},
                                               {'title': 'Example 3: Server health dashboard',
                                                'code': "print('--- SYSTEM METRICS ---')\n"
                                                        "print('Uptime:', 99.8, '%')\n"
                                                        "print('Active Users:', 150 + 75)\n"
                                                        "print('Status: OPERATIONAL')",
                                                'explanation': 'Combines strings, floats, expressions, and '
                                                               'headers into a professional status monitor.',
                                                'output': '--- SYSTEM METRICS ---\n'
                                                          'Uptime: 99.8 %\n'
                                                          'Active Users: 225\n'
                                                          'Status: OPERATIONAL'}],
                        'line_by_line': [{'line': '1', 'code': "print('PILOT:', 'Alex Vance')", 'explanation': "Show the text 'PILOT:', followed by the text 'Alex Vance'. Python puts a space between comma-separated print items."}, {'line': '2', 'code': "print('RANK:', 'Lieutenant')", 'explanation': "Show the text 'RANK:', followed by the text 'Lieutenant'. Python puts a space between comma-separated print items."}, {'line': '3', 'code': "print('MISSIONS:', 14)", 'explanation': "Show the text 'MISSIONS:', followed by the value 14. Python puts a space between comma-separated print items."}],
                        'expected_output': '=== PYTHON QUEST PROFILE ===\n'
                                           'Name: Quest Explorer\n'
                                           'Role: Python Apprentice\n'
                                           'XP Target: 500\n'
                                           'Status: Ready for World 2',
                        'common_mistakes': [{'mistake': "print('XP Target: 250 + 250')",
                                             'why': "Remember to calculate math outside quotes: print('XP "
                                                    "Target:', 250 + 250)",
                                             'fix': "print('XP Target:', 250 + 250)"}],
                        'real_world_apps': 'CLI administrative tools, data report generators, and onboarding '
                                           'greeting scripts.',
                        'summary': 'You have mastered the foundational building blocks of Python. You are '
                                   'ready to explore variables, conditionals, and logic in World 2!',
                        'practice_questions': ['What concepts did you master in World 1?',
                                               'How do you combine text labels and calculations in output?']},
             'challenges': [{'title': 'World 1 Capstone: Personal Introduction Program',
                             'difficulty': 'medium',
                             'is_boss': False,
                             'description': 'Your task, step by step:\n1. Print a five-line explorer profile.\n2. Include the title, name, role, an XP target calculated as 250 + 250, and the next-world status.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 5 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'Keep the five lines in the requested order. Use print to show '
                                             'text and calculate the XP total.',
                             'initial_code': '',
                             'solution_code': '# World 1 Capstone Project\n'
                                              "print('=== PYTHON QUEST PROFILE ===')\n"
                                              "print('Name: Quest Explorer')\n"
                                              "print('Role: Python Apprentice')\n"
                                              "print('XP Target:', 250 + 250)\n"
                                              "print('Status: Ready for World 2')",
                             'hints': ['Plan the five output lines before writing them.',
                                       'Use words for the name and role.',
                                       'Use a calculation for the XP target.'],
                             'xp_reward': 50,
                             'test_cases': [{'input_data': '',
                                             'expected_output': '=== PYTHON QUEST PROFILE ===\n'
                                                                'Name: Quest Explorer\n'
                                                                'Role: Python Apprentice\n'
                                                                'XP Target: 500\n'
                                                                'Status: Ready for World 2',
                                             'is_hidden': False}]},
                            {'title': 'Boss Challenge: World 1 Master Checkpoint',
                             'difficulty': 'boss',
                             'is_boss': True,
                             'description': 'Your task, step by step:\n1. Print three lines to celebrate finishing World 1.\n2. Include the calculated XP total and name the next topic.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'requirements': 'The output should say World 1 complete, then XP: 500, then '
                                             'Next: Variables. Calculate 250 + 250 for the XP line.',
                             'initial_code': '',
                             'solution_code': "print('World 1 complete')\n"
                                              "print('XP:', 250 + 250)\n"
                                              "print('Next: Variables')",
                             'hints': ['This task combines printed text and arithmetic.',
                                       'Keep the three messages in order.',
                                       'Calculate the XP amount, then print the next topic.'],
                             'xp_reward': 200,
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'World 1 complete\nXP: 500\nNext: Variables',
                                             'is_hidden': False}]}],
             'quizzes': [{'question': 'Which of the following lines correctly outputs: Status: OK with 50 XP '
                                      '(where 50 is calculated from 25 + 25)?',
                          'explanation': 'Separating the text label and the arithmetic expression with a '
                                         'comma allows Python to evaluate 25 + 25 and insert a space.',
                          'options': [{'text': "print('Status: OK with', 25 + 25, 'XP')",
                                       'is_correct': True,
                                       'explanation': "Correct! Evaluates 25 + 25 to 50 and prints 'Status: "
                                                      "OK with 50 XP'."},
                                      {'text': "print('Status: OK with 25 + 25 XP')",
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Inside quotes, 25 + 25 is printed '
                                                      'literally without calculating.'},
                                      {'text': 'print(Status: OK with, 50, XP)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Unquoted words cause a SyntaxError.'},
                                      {'text': "print('Status: OK with' + 50 + 'XP')",
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Direct string-number addition with + '
                                                      'raises a TypeError.'}]},
                         {'question': 'What is the expected output of this synthesis program?\n'
                                      '\n'
                                      '# Quest Completion Log\n'
                                      "print('Level', 10, sep=': ')\n"
                                      "print('World 1 Complete!')",
                          'explanation': "Line 2 prints 'Level: 10' because sep=': ' replaces the default "
                                         'space between arguments. Line 3 prints on a new line.',
                          'options': [{'text': 'Level: 10\nWorld 1 Complete!',
                                       'is_correct': True,
                                       'explanation': "Correct! sep=': ' joins 'Level' and 10 with a colon "
                                                      'and space.'},
                                      {'text': 'Level 10 World 1 Complete! (all on one line)',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Each print statement creates a newline.'},
                                      {'text': 'Level: 10',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Line 3 also executes.'},
                                      {'text': 'Quest Completion Log',
                                       'is_correct': False,
                                       'explanation': 'Incorrect. Line 1 is a comment and is skipped.'}]}]}]}
