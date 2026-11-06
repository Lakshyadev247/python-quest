"""Curriculum module: WORLD_6
Beginner-friendly lessons and challenges about strings and collections.
"""

WORLD_6 = {'description': 'Deep dive into strings, lists, tuples, sets, dictionaries, and nested data structures.',
 'final_project_desc': 'Build an in-memory student database application managing courses, grades, and GPA '
                       'calculations using nested collections.',
 'final_project_title': 'Student Records Management System',
 'goal': 'Master sequence data, mapping types, set theory, and composite nested structures.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Text has numbered positions.\n2. Read the text the user types.\n3. Print its first character, its last character, and the three characters starting at position 1.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['s[0]\ns[-1]\ns[1:4]',
                                       's = input().strip()\nprint(s[0])\nprint(s[-1])\nprint(s[1:4])'],
                             'initial_code': '# String Indexing and Slicing\n'
                                             '# Step 1: Read string:\n'
                                             's = input().strip()\n'
                                             '\n'
                                             '# Step 2: Print first char, last char, and slice [1:4] below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Try QUESTMASTER. Print Q, R, and UES, each on its own line.',
                             'solution_code': 's = input().strip()\nprint(s[0])\nprint(s[-1])\nprint(s[1:4])',
                             'test_cases': [{'input_data': 'QUESTMASTER\n',
                                             'expected_output': 'Q\nR\nUES',
                                             'is_hidden': False},
                                            {'input_data': 'ABCDEF123456\n',
                                             'expected_output': 'A\n6\nBCD',
                                             'is_hidden': False}],
                             'title': 'Secret Code Extractor',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. A palindrome reads the same from left to right and right to left, like radar.\n2. Read one word and print True if it is a palindrome.\n3. Otherwise, print False.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['s = input().strip()\nprint(s == s[::-1])'],
                             'initial_code': '# ⚔️ Boss Challenge: Palindrome Verifier\n'
                                             '# Step 1: Read input string:\n'
                                             's = input().strip()\n'
                                             '\n'
                                             '# Step 2: Print whether s == s[::-1] below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Try racecar (True) and python (False).',
                             'solution_code': 's = input().strip()\nprint(s == s[::-1])',
                             'test_cases': [{'input_data': 'racecar\n',
                                             'expected_output': 'True',
                                             'is_hidden': False},
                                            {'input_data': 'python\n',
                                             'expected_output': 'False',
                                             'is_hidden': False},
                                            {'input_data': 'madam\n',
                                             'expected_output': 'True',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Palindrome Verifier',
                             'xp_reward': 150}],
             'description': 'Find characters and pieces of text by position.',
             'lesson': {'common_mistakes': [{'mistake': 'Using text[1] for the first character.',
  'why': 'Index 1 means the second character because counting starts at 0.',
  'fix': 'Use text[0].'},
 {'mistake': 'Expecting the stop index in text[1:4] to appear.',
  'why': 'The start is included but the stop is excluded.',
  'fix': 'Use text[1:5] to include positions 1 through 4.'},
 {'mistake': 'Expecting text[99:100] to raise IndexError.',
  'why': 'A slice clips to the available range; direct indexing requires an existing position.',
  'fix': 'Use a slice for a range, and check length before a possibly invalid direct index.'}],
                        'detailed_explanation': ('A character is one letter, digit, space, or symbol in text. Its index is its position. Python '
 'starts indexes at 0: the first character is text[0], the second is text[1]. Negative indexes '
 'count backward, with -1 meaning the last character and -2 the one before it.\n'
 '\n'
 'Use text[index] for exactly one character. If that position does not exist, Python raises '
 "IndexError. For example, 'cat'[8] fails. A slice uses text[start:stop]. The start is included "
 "and stop is excluded: 'PYTHON'[1:4] includes positions 1, 2, and 3, giving YTH.\n"
 '\n'
 'Leave start empty to begin at the first character; leave stop empty to continue to the end. '
 'Slices that extend past the text are clipped to the available characters, unlike a direct index. '
 'A third part is the step: text[start:stop:step]. Step 2 takes every second character; step -1 '
 'walks backward, so text[::-1] reverses the string. Slicing returns new text and leaves the '
 'original unchanged.'),
                        'expected_output': 'P\nN',
                        'introduction': ('A game receives the code word PYTHON and needs its first and last letters. Direct indexing gets '
 'one character; a slice gets a piece such as YTH. Python assigns each character a position so you '
 'can ask for exactly what you need.'),
                        'learning_objectives': ['Read one character using a positive or negative index.',
 'Take a substring with a slice and explain its included start and excluded stop.',
 'Use omitted bounds, steps, and reverse slicing.',
 'Distinguish IndexError from a slice clipped at the end.'],
                        'line_by_line': [{'line': '1', 'code': "text = 'PYTHON'", 'explanation': 'Store the six-character string in text.'},
 {'line': '2',
  'code': 'print(text[0])',
  'explanation': 'Read index 0, the first character, and display it.'},
 {'line': '3',
  'code': 'print(text[-1])',
  'explanation': 'Read index -1, the last character, and display it.'}],
                        'practical_examples': [{'title': 'Get the first and last character',
  'code': "text = 'PYTHON'\nprint(text[0])\nprint(text[-1])",
  'explanation': 'Index 0 is the first character. Index -1 is always the last, even if the word '
                 'length changes.',
  'output': 'P\nN'},
 {'title': 'Slice, skip, and reverse',
  'code': "text = 'PYTHON'\n"
          'print(text[1:4])\n'
          'print(text[:2])\n'
          'print(text[4:])\n'
          'print(text[::2])\n'
          'print(text[::-1])',
  'explanation': 'The slice stops before its stop index. The step chooses every second character; '
                 '-1 walks backward.',
  'output': 'YTH\nPY\nON\nPTO\nNOHTYP'},
 {'title': 'A long slice is clipped safely',
  'code': "text = 'cat'\nprint(text[1:99])",
  'explanation': "The slice ends at the text's actual end. By contrast, text[99] raises "
                 'IndexError.',
  'output': 'at'}],
                        'practice_questions': ["Try word = 'robot': what is word[-1]? Check: t.",
 "What does 'planet'[1:4] return? Check: lan; stop 4 is excluded.",
 'Which slice reverses text? Check: text[::-1].',
 'Which can safely clip when text is short: text[100] or text[100:105]? Check: the slice.'],
                        'prerequisites': ('Know that quotes make a string and a variable can store it. Level 49 builds on variables; Level '
 '50 will clean strings.'),
                        'real_world_apps': ("Inspect a product code's first character, take an extension from the end of a filename, or "
 'extract a known section from a longer code. Use an index for one character and a slice for a '
 'range.'),
                        'summary': ('Indexes select one character: positive indexes start at 0 and negative indexes start at -1 from '
 'the end. Slices include start and exclude stop; they can use a step. Direct indexing can raise '
 'IndexError, while an overlong slice is clipped.'),
                        'syntax_breakdown': ('text[index]             # one character\n'
 'text[start:stop]        # start included, stop excluded\n'
 'text[start:stop:step]\n'
 'text[:3]                # from the start, before index 3\n'
 'text[3:]                # from index 3 through the end\n'
 'text[::2]               # every second character\n'
 'text[::-1]              # reverse the text'),
                        'terminology': [{'term': 'Character', 'definition': 'One letter, digit, space, or symbol in text.'},
 {'term': 'Index', 'definition': 'The zero-based position of one character; -1 is the last.'},
 {'term': 'Slice', 'definition': 'A selected range written with start, stop, and optionally step.'},
 {'term': 'IndexError',
  'definition': 'An error from asking for one character at a position that does not exist.'}]},
             'number': 49,
             'quizzes': [{'explanation': 'Slicing [1:4] extracts characters from index 1 up to index 3: '
                                         "'yth'.",
                          'options': [{'explanation': "Correct! Characters at indices 1, 2, 3 are 'y', 't', "
                                                      "'h'.",
                                       'is_correct': True,
                                       'text': "'yth'"},
                                      {'explanation': "Incorrect. Index 0 is 'P'; slice starts at 1.",
                                       'is_correct': False,
                                       'text': "'Pyt'"},
                                      {'explanation': 'Incorrect. Slicing is exclusive of stop index 4.',
                                       'is_correct': False,
                                       'text': "'ytho'"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': "'ythn'"}],
                          'question': "What does the expression 'Python'[1:4] return?"},
                         {'explanation': 'Negative indexing slices from second to last character to the end: '
                                         "'on'.",
                          'options': [{'explanation': "Correct! -2 is 'o', -1 is 'n'.",
                                       'is_correct': True,
                                       'text': 'on'},
                                      {'explanation': 'Incorrect. Slicing preserves order.',
                                       'is_correct': False,
                                       'text': 'no'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'hon'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'P'}],
                          'question': "What is the output of print('Python'[-2:])?"}],
             'title': 'String Slicing and Indexing'},
            {'challenges': [{'description': 'Your task, step by step:\n1. People may type extra spaces or use different capital letters.\n2. Read a phrase and print it three ways: lowercase, uppercase, then with spaces replaced by underscores.\n3. Remove extra spaces from the ends first.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['s = input().strip()\n'
                                       'print(s.lower())\n'
                                       'print(s.upper())\n'
                                       "print(s.replace(' ', '_'))"],
                             'initial_code': '# String Methods: lower(), upper(), replace()\n'
                                             '# Step 1: Read input:\n'
                                             's = input().strip()\n'
                                             '\n'
                                             '# Step 2: Print transformations below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Try “Python Quest”. The three lines should be python quest, '
                                             'PYTHON QUEST, and Python_Quest.',
                             'solution_code': 's = input().strip()\n'
                                              'print(s.lower())\n'
                                              'print(s.upper())\n'
                                              "print(s.replace(' ', '_'))",
                             'test_cases': [{'input_data': '  user access token  \n',
                                             'expected_output': 'user access token\n'
                                                                'USER ACCESS TOKEN\n'
                                                                'user_access_token',
                                             'is_hidden': False},
                                            {'input_data': 'Python Quest\n',
                                             'expected_output': 'python quest\nPYTHON QUEST\nPython_Quest',
                                             'is_hidden': False}],
                             'title': 'Data Sanitizer',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. A web address uses a short title with hyphens between words.\n2. Read a title, make it lowercase, and replace spaces between words with one hyphen.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["slug = title.strip().lower().replace(' ', '-')\nprint(slug)"],
                             'initial_code': '# ⚔️ Boss Challenge: URL Slug Generator\n'
                                             '# Step 1: Read title:\n'
                                             'title = input().strip()\n'
                                             '\n'
                                             '# Step 2: Generate slug and print below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Try “Mastering Python In 30 Days”. The result is '
                                             'mastering-python-in-30-days.',
                             'solution_code': 'title = input().strip().lower()\n'
                                              "slug = '-'.join(title.split())\n"
                                              'print(slug)',
                             'test_cases': [{'input_data': 'Mastering Python In 30 Days\n',
                                             'expected_output': 'mastering-python-in-30-days',
                                             'is_hidden': False},
                                            {'input_data': '  Advanced   Data   Structures   \n',
                                             'expected_output': 'advanced-data-structures',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: URL Slug Generator',
                             'xp_reward': 150}],
             'description': 'Clean and change text with string methods.',
             'lesson': {'common_mistakes': [{'mistake': 'Writing name.lower without parentheses.',
  'why': 'That refers to the method instead of calling it.',
  'fix': 'Write name.lower().'},
 {'mistake': 'Calling name.lower() and expecting name to change.',
  'why': 'Strings are immutable; lower() returns a new string.',
  'fix': 'Save the result: name = name.lower().'},
 {'mistake': 'Using strip() to remove spaces between words.',
  'why': 'strip() removes whitespace only at the two ends.',
  'fix': 'Use replace() or split() and join() for spaces inside text.'},
 {'mistake': 'Calling replace() with only one argument.',
  'why': 'It needs both what to find and what to put in its place.',
  'fix': "Use title.replace(' ', '-')."}],
                        'detailed_explanation': ('A method is an action called on a value. The dot connects the string to the method, and '
 'parentheses call it: name.lower(). strip() removes whitespace from the two ends, not between '
 'words. lower() and upper() return text with letters changed to one case. replace(old, new) '
 'returns text with matching pieces replaced.\n'
 '\n'
 'Strings are immutable: a method does not edit the original string in place. It returns a new '
 "string. If name is 'SAM', name.lower() produces 'sam', but name remains 'SAM' unless you save "
 'the result. Write cleaned = name.strip().lower() when you want to keep the cleaned value.\n'
 '\n'
 'Chaining runs methods left to right: name.strip().lower() first removes edge whitespace, then '
 'lowercases the returned string. Order matters. For a web slug, lowercase the title and replace '
 'spaces with hyphens. Use a method when its returned result is useful; otherwise it is easy to '
 'call it and accidentally discard the result.'),
                        'expected_output': 'sam',
                        'introduction': ('People can type a name with extra spaces or different capital letters. A program may need one '
 'consistent version before comparing or displaying it. String methods are built-in actions for '
 'cleaning and changing text.'),
                        'learning_objectives': ['Call strip(), lower(), upper(), and replace() with method syntax.',
 'Explain that string methods return new strings because strings are immutable.',
 'Save a returned string and chain methods in a useful order.',
 'Use methods to clean typed names or create a simple URL slug.'],
                        'line_by_line': [{'line': '1',
  'code': "raw_name = '  SAM  '",
  'explanation': 'Store the typed name, including its outside spaces.'},
 {'line': '2',
  'code': 'clean_name = raw_name.strip().lower()',
  'explanation': 'Remove edge spaces, lowercase the returned text, and save the final result.'},
 {'line': '3', 'code': 'print(clean_name)', 'explanation': 'Display the cleaned string sam.'}],
                        'practical_examples': [{'title': 'Clean a name',
  'code': "raw_name = '  SAM  '\nclean_name = raw_name.strip().lower()\nprint(clean_name)",
  'explanation': 'strip() removes outside spaces, then lower() changes the letters. The final new '
                 'string is saved in clean_name; raw_name is unchanged.',
  'output': 'sam'},
 {'title': 'Create a simple slug',
  'code': "title = 'Python Quest Guide'\nslug = title.lower().replace(' ', '-')\nprint(slug)",
  'explanation': 'lower() returns lowercase text; replace() changes each space to a hyphen.',
  'output': 'python-quest-guide'},
 {'title': 'See that the original stays the same',
  'code': "word = 'Cat'\nnew_word = word.lower()\nprint(word)\nprint(new_word)",
  'explanation': "lower() returns another string. The old variable still refers to 'Cat'.",
  'output': 'Cat\ncat'}],
                        'practice_questions': ['What does strip() remove? Check: whitespace at the start and end, not spaces between words.',
 'Why assign cleaned = text.lower()? Check: lower() returns new text and leaves text unchanged.',
 "What is '  Hi '.strip().upper()? Check: HI.",
 "How can you change spaces in 'red blue' to underscores? Check: text.replace(' ', '_')."],
                        'prerequisites': ('Know variables, strings, and print(). Level 49 taught how to select parts of text; this lesson '
 'returns cleaned versions of text.'),
                        'real_world_apps': ('Trim accidental spaces from a username before checking it. Compare lowercase names so '
 'capitalization does not create accidental differences. Turn a page title into a simple URL slug '
 'by replacing spaces with hyphens.'),
                        'summary': ('String methods use dot-and-parentheses syntax. strip(), lower(), upper(), and replace() return '
 'new strings rather than changing the original. Save returned text; chaining runs from left to '
 'right.'),
                        'syntax_breakdown': ('text.strip()                 # remove whitespace at the ends\n'
 'text.lower()                 # return lowercase text\n'
 'text.upper()                 # return uppercase text\n'
 'text.replace(old, new)       # replace matching text\n'
 'clean = text.strip().lower() # save the chained result'),
                        'terminology': [{'term': 'Method',
  'definition': 'An action called on a value with dot syntax, such as text.lower().'},
 {'term': 'Return value', 'definition': 'The new value a method gives back.'},
 {'term': 'Immutable', 'definition': 'Not changeable in place; string methods return new strings.'},
 {'term': 'Method chaining', 'definition': 'Calling a method on the result of another method.'},
 {'term': 'Whitespace',
  'definition': 'Spaces, tabs, or line breaks; strip() removes it from the ends.'}]},
             'number': 50,
             'quizzes': [{'question': 'Which method removes spaces at the start and end of text?',
                          'explanation': 'strip removes whitespace from both ends.',
                          'options': [{'text': 'strip()',
                                       'is_correct': True,
                                       'explanation': 'Correct. strip removes whitespace from both ends.'},
                                      {'text': 'split()',
                                       'is_correct': False,
                                       'explanation': 'Review the example. strip removes whitespace from '
                                                      'both ends.'},
                                      {'text': 'replace()',
                                       'is_correct': False,
                                       'explanation': 'Review the example. strip removes whitespace from '
                                                      'both ends.'},
                                      {'text': 'upper()',
                                       'is_correct': False,
                                       'explanation': 'Review the example. strip removes whitespace from '
                                                      'both ends.'}]},
                         {'question': "What does 'Cat'.lower() return?",
                          'explanation': 'lower changes letters to lowercase.',
                          'options': [{'text': 'cat',
                                       'is_correct': True,
                                       'explanation': 'Correct. lower changes letters to lowercase.'},
                                      {'text': 'CAT',
                                       'is_correct': False,
                                       'explanation': 'Review the example. lower changes letters to '
                                                      'lowercase.'},
                                      {'text': 'Cat',
                                       'is_correct': False,
                                       'explanation': 'Review the example. lower changes letters to '
                                                      'lowercase.'},
                                      {'text': 'cAT',
                                       'is_correct': False,
                                       'explanation': 'Review the example. lower changes letters to '
                                                      'lowercase.'}]}],
             'title': 'Essential String Methods'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Make a receipt line.\n2. Read an item name and a price.\n3. Print the name on the left and its price with two digits after the decimal.\n4. Leave enough room so the prices line up.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['item = input().strip()\n'
                                       'price = float(input())\n'
                                       "print(f'{item:<10} | ${price:>7.2f}')"],
                             'initial_code': '# Columnar Formatting with f-strings\n'
                                             '# Step 1: Read inputs:\n'
                                             'item = input().strip()\n'
                                             'price = float(input())\n'
                                             '\n'
                                             '# Step 2: Print formatted column below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Try Apple and 1.5. The price should appear as $   1.50.',
                             'solution_code': 'item = input().strip()\n'
                                              'price = float(input())\n'
                                              "print(f'{item:<10} | ${price:>7.2f}')",
                             'test_cases': [{'input_data': 'Apple\n1.5\n',
                                             'expected_output': 'Apple      | $   1.50',
                                             'is_hidden': False},
                                            {'input_data': 'Milk\n42\n',
                                             'expected_output': 'Milk       | $  42.00',
                                             'is_hidden': False}],
                             'title': 'Formatted Receipt Column',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read a decimal such as 0.125.\n2. Show it as a percentage with one digit after the decimal point.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["rate = float(input())\nprint(f'{rate:.1%}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Percentage Formatter\n'
                                             '# Step 1: Read rate:\n'
                                             'rate = float(input())\n'
                                             '\n'
                                             "# Step 2: Print f'{rate:.1%}' below:\n"
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Try 0.125. The result is 12.5%.',
                             'solution_code': "rate = float(input())\nprint(f'{rate:.1%}')",
                             'test_cases': [{'input_data': '0.125\n',
                                             'expected_output': '12.5%',
                                             'is_hidden': False},
                                            {'input_data': '1\n',
                                             'expected_output': '100.0%',
                                             'is_hidden': False},
                                            {'input_data': '0.04\n',
                                             'expected_output': '4.0%',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Percentage Formatter',
                             'xp_reward': 150}],
             'description': 'Put values into neat, readable messages with f-strings.',
             'lesson': {'common_mistakes': [{'mistake': 'Forgetting the f before the quote.',
  'why': 'Without f, braces are ordinary text and variables are not inserted.',
  'fix': "Write print(f'Hello, {name}')."},
 {'mistake': 'Putting a variable name in quotes inside its braces.',
  'why': 'That asks Python to insert the literal word rather than look up the variable.',
  'fix': "Use {name}, not {'name'}, when name is a variable."},
 {'mistake': 'Thinking .2f changes the stored number.',
  'why': 'The format spec changes only the text shown by the f-string.',
  'fix': 'Keep the numeric value for later calculations and format it when displaying it.'},
 {'mistake': 'Assuming a width truncates long text.',
  'why': 'Width is a minimum; longer values extend beyond it.',
  'fix': 'Choose enough width for typical values and handle unusually long labels separately.'}],
                        'detailed_explanation': ('An f-string begins with f immediately before its quote. Inside braces, Python evaluates an '
 'expression and inserts its value. For example, {name} looks up the current value of name; '
 '{quantity * price} calculates a total. Without the f prefix, braces are ordinary text.\n'
 '\n'
 'A colon inside braces starts a format specification. .2f means show a fixed-point number with '
 'two digits after the decimal, so 4.5 is displayed as 4.50. This changes the displayed text, not '
 'the number stored in the variable.\n'
 '\n'
 'A width reserves a minimum number of character spaces. In {item:<8}, < means left-align and 8 is '
 'the minimum field width. In {price:>7.2f}, > means right-align, 7 is the minimum width, and .2f '
 'controls decimals. Long text is not cut off; it may extend beyond its field. For literal braces, '
 "double them: f'{{ready}}' displays {ready}.\n"
 '\n'
 'Use f-strings to build messages, receipts, and reports. Keep the value as a number while '
 'calculating; format it when displaying it.'),
                        'expected_output': 'Mia scored 93 points.',
                        'introduction': ('A receipt needs to show an item name and price. Joining text by hand is awkward when values '
 'change or need fixed decimal places. An f-string lets Python place values into a sentence and '
 'format them for display.'),
                        'learning_objectives': ['Insert variables and calculations into text with an f-string.',
 'Use .2f to display two decimal places without changing the stored number.',
 'Align text and numbers with a field width.',
 'Print literal braces by doubling them.'],
                        'line_by_line': [{'line': '1',
  'code': "name = 'Mia'",
  'explanation': 'Store the name that the message will display.'},
 {'line': '2', 'code': 'score = 93', 'explanation': 'Store the score as a number.'},
 {'line': '3',
  'code': "print(f'{name} scored {score} points.')",
  'explanation': 'Evaluate both brace expressions, insert their current values, then display the '
                 'completed sentence.'}],
                        'practical_examples': [{'title': 'Insert variables into a message',
  'code': "name = 'Mia'\nscore = 93\nprint(f'{name} scored {score} points.')",
  'explanation': 'The f prefix tells Python to evaluate each expression in braces, then insert the '
                 'result into the sentence.',
  'output': 'Mia scored 93 points.'},
 {'title': 'Display a price to two decimal places',
  'code': "price = 4.5\nprint(f'Price: ${price:.2f}')",
  'explanation': '.2f displays two digits after the decimal. The value in price remains the number '
                 '4.5.',
  'output': 'Price: $4.50'},
 {'title': 'Align a name and a price',
  'code': "item = 'Tea'\nprice = 2.5\nprint(f'{item:<8}|${price:>6.2f}')",
  'explanation': 'The item is left-aligned in 8 spaces. The price is right-aligned in a minimum '
                 'width of 6 and displayed with two decimals.',
  'output': 'Tea     |$  2.50'},
 {'title': 'Calculate inside braces',
  'code': "quantity = 3\nprice = 2.5\nprint(f'Total: ${quantity * price:.2f}')",
  'explanation': 'Python multiplies the values inside the braces, then formats the result.',
  'output': 'Total: $7.50'}],
                        'practice_questions': ["Write an f-string that prints Level: 4 from level = 4. Check: print(f'Level: {level}').",
 'What does :.2f do to 3.5? Check: displays 3.50; the stored number is unchanged.',
 "Fix print('Hi {name}') so it inserts name. Check: add f before the opening quote.",
 "Format price = 6 as a dollar amount with two decimals. Check: f'${price:.2f}' displays $6.00."],
                        'prerequisites': ('Know variables, strings, numbers, and basic arithmetic. Level 50 covered string methods; an '
 'f-string assembles output from current values.'),
                        'real_world_apps': ("Receipts align product names and prices. Score reports insert a student's name and show an "
 'average with a consistent number of decimal places. Tables become easier to scan when columns '
 'line up.'),
                        'summary': ('Prefix text with f and put values or calculations in braces. A colon introduces display rules: '
 '.2f chooses two decimals, while < and > align within a minimum-width field. Formatting affects '
 'display, not the stored value.'),
                        'syntax_breakdown': ("name = 'Mia'\n"
 'price = 4.5\n'
 "print(f'{name} pays ${price:.2f}')\n"
 "# {name} inserts the variable's value.\n"
 '# :.2f displays two digits after the decimal.\n'
 '# {item:<8} left-aligns in a minimum width of 8.\n'
 '# {price:>7.2f} right-aligns in a minimum width of 7.'),
                        'terminology': [{'term': 'f-string',
  'definition': 'A string prefixed by f that evaluates expressions inside braces.'},
 {'term': 'Expression',
  'definition': 'Code that Python evaluates to produce a value, such as quantity * price.'},
 {'term': 'Format specification',
  'definition': 'Instructions after a colon that control how a value is displayed.'},
 {'term': 'Precision',
  'definition': 'The number of digits shown after a decimal point for fixed-point formatting.'},
 {'term': 'Field width and alignment',
  'definition': 'A minimum display width and where the value sits: < left, > right, ^ center.'}]},
             'number': 51,
             'quizzes': [{'explanation': ':.2f formats the floating-point number rounded to 2 decimal '
                                         "places: '12.35'.",
                          'options': [{'explanation': 'Correct! 12.3456 is rounded to 2 decimal places.',
                                       'is_correct': True,
                                       'text': '12.35'},
                                      {'explanation': 'Incorrect. 5 rounds up the 4 to 5.',
                                       'is_correct': False,
                                       'text': '12.34'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '12.3'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '12.3456'}],
                          'question': "What is the output of f'{12.3456:.2f}'?"},
                         {'explanation': ":>8 right-aligns the string 'Hero' (4 characters) in a field of "
                                         'width 8, adding 4 leading spaces.',
                          'options': [{'explanation': 'Correct! :>8 right-aligns with 4 leading spaces.',
                                       'is_correct': True,
                                       'text': "'    Hero'"},
                                      {'explanation': 'Incorrect. :<8 is left-align.',
                                       'is_correct': False,
                                       'text': "'Hero    '"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': "'Hero'"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What is the output of: print(f\'{"Hero":>8}\')?'}],
             'title': 'Format Text and Numbers'},
            {'challenges': [{'description': 'Your task, step by step:\n1. A list keeps related items together.\n2. Print each hero from the given list on its own line, in the same order.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["heroes = ['Warrior', 'Mage', 'Rogue']\n"
                                       'print(heroes[0])\n'
                                       'print(heroes[1])\n'
                                       'print(heroes[2])'],
                             'initial_code': '# Lists: Ordered Collections\n'
                                             '# Step 1: List defined:\n'
                                             "heroes = ['Warrior', 'Mage', 'Rogue']\n"
                                             '\n'
                                             '# Step 2: Print each element by index below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'The output is Warrior, Mage, then Rogue.',
                             'solution_code': "heroes = ['Warrior', 'Mage', 'Rogue']\n"
                                              'print(heroes[0])\n'
                                              'print(heroes[1])\n'
                                              'print(heroes[2])',
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Warrior\nMage\nRogue',
                                             'is_hidden': False}],
                             'title': 'Guild Party Roster',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read four test scores.\n2. Print the highest score, the lowest score, and the average to one digit after the decimal point.\n\nInput for this example: The Input box shows 4 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['scores = [int(input()) for _ in range(4)]\n'
                                       "print(f'Max: {max(scores)}')\n"
                                       "print(f'Min: {min(scores)}')\n"
                                       "print(f'Avg: {sum(scores)/len(scores):.1f}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Statistical Summary\n'
                                             '# Step 1: Read 4 scores:\n'
                                             'scores = [int(input()) for _ in range(4)]\n'
                                             '\n'
                                             '# Step 2: Print Max, Min, and Avg (.1f) below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'For 85, 92, 78, and 95, show Max: 95, Min: 78, and Avg: 87.5.',
                             'solution_code': 'scores = [int(input()) for _ in range(4)]\n'
                                              "print(f'Max: {max(scores)}')\n"
                                              "print(f'Min: {min(scores)}')\n"
                                              "print(f'Avg: {sum(scores) / len(scores):.1f}')",
                             'test_cases': [{'input_data': '85\n92\n78\n95\n',
                                             'expected_output': 'Max: 95\nMin: 78\nAvg: 87.5',
                                             'is_hidden': False},
                                            {'input_data': '100\n60\n80\n40\n',
                                             'expected_output': 'Max: 100\nMin: 40\nAvg: 70.0',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Statistical Summary',
                             'xp_reward': 150}],
             'description': 'Keep several ordered values together in a list.',
             'lesson': {'common_mistakes': [{'mistake': 'Using snacks[1] for the first item.',
  'why': 'Index 1 means the second item because counting begins at 0.',
  'fix': 'Use snacks[0].'},
 {'mistake': 'Confusing the length with the last index.',
  'why': 'A three-item list has length 3 but its final index is 2.',
  'fix': 'Use len(items) to count; use items[-1] to read the last item when the list is not '
         'empty.'},
 {'mistake': 'Reading index 0 from an empty list.',
  'why': 'An empty list has no items at any index.',
  'fix': 'Add an item first or check whether the list has items.'},
 {'mistake': 'Assuming a list cannot change.',
  'why': 'Lists are mutable collections.',
  'fix': 'Use items[index] = value to replace an existing item.'}],
                        'detailed_explanation': ('A list is an ordered, mutable collection. Write items between square brackets and separate them '
 "with commas: items = ['map', 'potion']. Each stored value is an item or element. Order matters "
 'because each item has a position.\n'
 '\n'
 'Use square brackets with an index to read one item. Indexes start at zero, so items[0] is the '
 'first item. Negative indexes count backward: items[-1] is the last. len(items) returns the '
 'number of items. An empty list is [] and has length 0.\n'
 '\n'
 'A for loop visits every item in order: for item in items: gives the current item to item on each '
 'pass. This works even if the list later grows or shrinks, unlike manually writing several print '
 'statements.\n'
 '\n'
 "Lists are mutable: you can replace an item with items[0] = 'torch'. Lists can also grow and "
 'shrink with methods, which Level 53 teaches. Use a list when order matters, repeated values are '
 'allowed, or the group will change. A set or dictionary fits different needs.'),
                        'expected_output': 'apple\n2',
                        'introduction': ('A game inventory may contain a map, a potion, and a key. Separate variables become awkward as '
 'the inventory grows. A list stores related items together, remembers their order, and lets a '
 'program visit or change them.'),
                        'learning_objectives': ['Create an ordered list and identify its items.',
 'Read an item by its zero-based index and count items with len().',
 'Use a for loop to visit items one by one.',
 'Change a list item and explain that lists are mutable.',
 'Create and use an empty list.'],
                        'line_by_line': [{'line': '1',
  'code': "snacks = ['apple', 'toast']",
  'explanation': 'Create an ordered list with two text items.'},
 {'line': '2',
  'code': 'print(snacks[0])',
  'explanation': 'Read index 0, the first item, and display apple.'},
 {'line': '3',
  'code': 'print(len(snacks))',
  'explanation': 'Count both items and display the result, 2.'}],
                        'practical_examples': [{'title': 'Create, read, and count',
  'code': "snacks = ['apple', 'toast']\nprint(snacks[0])\nprint(len(snacks))",
  'explanation': 'The list holds two strings in order. Index 0 selects apple, and len() counts two '
                 'items.',
  'output': 'apple\n2'},
 {'title': 'Visit every item',
  'code': "heroes = ['Aria', 'Boran', 'Cleo']\nfor hero in heroes:\n    print(hero)",
  'explanation': 'The loop gives each name to hero in turn and prints it. No separate index is '
                 'needed.',
  'output': 'Aria\nBoran\nCleo'},
 {'title': 'Change one item',
  'code': "inventory = ['map', 'key']\ninventory[0] = 'treasure map'\nprint(inventory)",
  'explanation': 'Assignment at index 0 replaces the first item in the existing mutable list.',
  'output': "['treasure map', 'key']"}],
                        'practice_questions': ["What is pets[0] when pets = ['cat', 'dog']? Check: cat.",
 'How many items are in [3, 5, 8]? Check: 3; len() returns the count.',
 "Replace the second color in ['red', 'blue'] with green. Check: colors[1] = 'green'.",
 'Why use a for loop instead of writing one statement for each item? Check: it handles the current '
 'items even when their number changes.'],
                        'prerequisites': ('Know variables, strings, numbers, and how a for loop repeats. Lists let one variable hold an '
 'ordered group of values.'),
                        'real_world_apps': ('A basket stores chosen products in order. A roster keeps player names together. A score list can '
 'be looped over to display or calculate results.'),
                        'summary': ('Lists store ordered items in square brackets. Indexes start at 0; len() counts items; a for loop '
 'visits them. Lists are mutable, so values can be replaced. Use [] for an empty list.'),
                        'syntax_breakdown': ("items = ['map', 'potion'] # create a list\n"
 'items[0]                 # read the first item\n'
 "items[0] = 'torch'       # replace an item\n"
 'len(items)               # count items\n'
 'for item in items:       # visit items in order\n'
 '    print(item)\n'
 'empty = []               # create an empty list'),
                        'terminology': [{'term': 'List', 'definition': 'An ordered collection written with square brackets.'},
 {'term': 'Item / element', 'definition': 'One value stored in a collection.'},
 {'term': 'Index', 'definition': 'A zero-based position used to read or replace one item.'},
 {'term': 'Length', 'definition': 'The item count returned by len(list_name).'},
 {'term': 'Mutable', 'definition': 'Able to change after creation.'},
 {'term': 'Iteration', 'definition': 'Visiting items one at a time, often with a for loop.'}]},
             'number': 52,
             'quizzes': [{'question': 'What is the first index in a Python list?',
                          'explanation': 'Python starts list indexes at zero.',
                          'options': [{'text': '0',
                                       'is_correct': True,
                                       'explanation': 'Correct. Python starts list indexes at zero.'},
                                      {'text': '1',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Python starts list indexes at '
                                                      'zero.'},
                                      {'text': '-1',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Python starts list indexes at '
                                                      'zero.'},
                                      {'text': 'It has no index',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Python starts list indexes at '
                                                      'zero.'}]},
                         {'question': "After a = ['red', 'blue'], what is a[1]?",
                          'explanation': 'Index 1 is the second item.',
                          'options': [{'text': 'blue',
                                       'is_correct': True,
                                       'explanation': 'Correct. Index 1 is the second item.'},
                                      {'text': 'red',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Index 1 is the second item.'},
                                      {'text': '1',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Index 1 is the second item.'},
                                      {'text': 'An error',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Index 1 is the second item.'}]}],
             'title': 'Introduction to Lists'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Change the third number in the given list to 99.\n2. Remember that Python starts counting list positions at 0.\n3. Print the updated list.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['nums = [10, 20, 30, 40, 50]\nnums[2] = 99\nprint(nums)'],
                             'initial_code': '# Mutating Lists in Place\n'
                                             '# Step 1: Initialize list:\n'
                                             'nums = [10, 20, 30, 40, 50]\n'
                                             '\n'
                                             '# Step 2: Mutate index 2 and print nums below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'The updated list is [10, 20, 99, 40, 50].',
                             'solution_code': 'nums = [10, 20, 30, 40, 50]\nnums[2] = 99\nprint(nums)',
                             'test_cases': [{'input_data': '',
                                             'expected_output': '[10, 20, 99, 40, 50]',
                                             'is_hidden': False}],
                             'title': 'Element Replacement',
                             'xp_reward': 35},
                            {'description': ('Your task, step by step:\n1. Start with the items map and potion.\n2. Add key to the end with append(), remove the first item with pop(0), then sort the remaining items alphabetically.\n3. Print the final list.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.'),
                             'difficulty': 'boss',
                             'hints': ["bag = ['map', 'potion']\nbag.append('key')\nbag.pop(0)\nbag.sort()\nprint(bag)"],
                             'initial_code': '# ⚔️ Boss Challenge: Middle Slice Trimmer\n'
                                             '# Step 1: Read items:\n'
                                             'items = input().split()\n'
                                             '\n'
                                             '# Step 2: Print middle slice items[1:-1] below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': "The final list should be ['key', 'potion'].",
                             'solution_code': "bag = ['map', 'potion']\nbag.append('key')\nbag.pop(0)\nbag.sort()\nprint(bag)",
                             'test_cases': [{'input_data': '', 'expected_output': "['key', 'potion']", 'is_hidden': False}],
                             'title': 'Boss Challenge: Pack and Sort the Backpack',
                             'xp_reward': 150}],
             'description': 'Add, remove, and sort list items.',
             'lesson': {'common_mistakes': [{'mistake': "Using append(['key', 'coin']) to add two separate items.",
  'why': 'append adds the entire provided list as one nested item.',
  'fix': "Use extend(['key', 'coin']) to add its items separately."},
 {'mistake': "Using pop('coin') to remove by value.",
  'why': 'pop takes a position; remove takes a value.',
  'fix': "Use items.remove('coin') or items.pop(index)."},
 {'mistake': 'Assigning items = items.sort().',
  'why': 'sort changes the list and returns None.',
  'fix': 'Call items.sort() without assigning its result, or use sorted(items) for a new list.'},
 {'mistake': 'Removing a value that may not be present without checking.',
  'why': 'remove() raises ValueError when no matching value exists.',
  'fix': 'Check value in items before removing when absence is possible.'}],
                        'detailed_explanation': ("Call a list method with a dot: bag.append('key'). append() adds its argument as one item at the "
 'end. extend() visits another collection and adds each of its items. insert(index, item) places '
 "one item before the given position. Item assignment, such as bag[0] = 'map', replaces one "
 'existing position rather than adding a new one.\n'
 '\n'
 'pop() removes and returns an item. With no index it removes the last item; pop(0) removes the '
 'first. Save the return value if it is needed. remove(value) searches for the first matching '
 'value and removes it; if the value is absent, Python raises ValueError.\n'
 '\n'
 'sort() rearranges the same list in ascending order and returns None. append(), extend(), '
 'insert(), remove(), and sort() also change the list and return None. Do not write bag = '
 'bag.sort(): that assigns None to bag. Call bag.sort() on its own. sorted(bag) is different: it '
 'returns a new sorted list and leaves bag unchanged.\n'
 '\n'
 'Choose a method based on the job: append one value, extend from several values, insert at a '
 'position, pop by position, remove by value, or sort the current list. Check indexes and values '
 'before trying to remove them.'),
                        'expected_output': "gem\n['coin', 'key', 'map', 'potion']",
                        'introduction': ('A game inventory changes as a player finds, uses, or reorganizes items. List methods are '
 'ready-made actions for those changes. The right method depends on whether you have one new item, '
 'several items, a position, or a value to remove.'),
                        'learning_objectives': ['Replace a list item by index.',
 'Add one item with append(), several with extend(), or one at a position with insert().',
 'Remove by position with pop() or by value with remove().',
 'Sort in place and explain which methods return a value versus None.'],
                        'line_by_line': [{'line': '1', 'code': "bag = ['map', 'potion']", 'explanation': 'Start with two ordered items.'},
 {'line': '2', 'code': "bag.append('key')", 'explanation': 'Add key as one item at the end.'},
 {'line': '3',
  'code': "bag.extend(['coin', 'gem'])",
  'explanation': 'Add coin and gem as separate items.'},
 {'line': '4',
  'code': "bag.insert(1, 'torch')",
  'explanation': 'Place torch before the item currently at index 1.'},
 {'line': '5',
  'code': 'removed = bag.pop()',
  'explanation': 'Remove the last item and save the returned value, gem.'},
 {'line': '6',
  'code': "bag.remove('torch')",
  'explanation': 'Find and remove the first item equal to torch.'},
 {'line': '7',
  'code': 'bag.sort()',
  'explanation': 'Sort the remaining list in place; this method returns None.'},
 {'line': '8', 'code': 'print(removed)', 'explanation': 'Display the item that pop() returned.'},
 {'line': '9', 'code': 'print(bag)', 'explanation': 'Display the final sorted list.'}],
                        'practical_examples': [{'title': 'Change a bag with several methods',
  'code': "bag = ['map', 'potion']\n"
          "bag.append('key')\n"
          "bag.extend(['coin', 'gem'])\n"
          "bag.insert(1, 'torch')\n"
          'removed = bag.pop()\n'
          "bag.remove('torch')\n"
          'bag.sort()\n'
          'print(removed)\n'
          'print(bag)',
  'explanation': 'append adds key as one item. extend adds coin and gem separately. insert puts '
                 'torch before index 1. pop removes and returns gem. remove deletes torch by '
                 'value. sort reorders the remaining items in the same list.',
  'output': "gem\n['coin', 'key', 'map', 'potion']"},
 {'title': 'append() and extend() are different',
  'code': "a = ['map']\n"
          "a.append(['key', 'coin'])\n"
          'print(a)\n'
          "b = ['map']\n"
          "b.extend(['key', 'coin'])\n"
          'print(b)',
  'explanation': 'append treats the provided list as one nested item. extend adds its two strings '
                 'separately.',
  'output': "['map', ['key', 'coin']]\n['map', 'key', 'coin']"},
 {'title': 'pop() returns the removed item',
  'code': "queue = ['Mia', 'Kai']\nnext_player = queue.pop(0)\nprint(next_player)\nprint(queue)",
  'explanation': 'pop(0) removes the first item and returns it, so next_player can use that value.',
  'output': "Mia\n['Kai']"}],
                        'practice_questions': ['What does x.append([2, 3]) add to x? Check: one nested list item.',
 'Which method adds 2 and 3 separately? Check: x.extend([2, 3]).',
 'Which call removes and returns the first item? Check: items.pop(0).',
 'Why is items = items.sort() a bug? Check: sort returns None; call items.sort() alone.'],
                        'prerequisites': ('Know list indexes, loops, and mutability. This lesson explains methods for changing a list; '
 'Level 54 covers slices and copies.'),
                        'real_world_apps': ('A cart can add a chosen product, extend with products from an order, remove one selection, and '
 'sort the list for display. A queue can pop its first waiting person.'),
                        'summary': ('append adds one item; extend adds each item from an iterable; insert places one before an index. '
 'pop removes and returns by position; remove removes by value. sort changes the same list and '
 'returns None; sorted() returns another list.'),
                        'syntax_breakdown': ('items[index] = value         # replace existing item\n'
 'items.append(value)          # add one at end\n'
 'items.extend(more_items)     # add each item\n'
 'items.insert(index, value)  # insert before index\n'
 'removed = items.pop()       # remove and return last\n'
 'items.remove(value)         # remove first matching value\n'
 'items.sort()                # reorder this list in place\n'
 'new_order = sorted(items)   # make a separate sorted list'),
                        'terminology': [{'term': 'In place',
  'definition': 'A method changes the existing list rather than returning a replacement list.'},
 {'term': 'append(item)', 'definition': 'Adds its argument as one item at the end.'},
 {'term': 'extend(items)', 'definition': 'Adds each item from another iterable.'},
 {'term': 'pop(index)',
  'definition': 'Removes and returns an item; with no index, removes the last.'},
 {'term': 'remove(value)', 'definition': 'Removes the first matching value.'},
 {'term': 'None',
  'definition': "Python's value meaning no result; in-place list methods return None."}]},
             'number': 53,
             'quizzes': [{'question': "What does items.append('pear') do?",
                          'explanation': 'append adds one item at the end.',
                          'options': [{'text': 'Adds pear to the end of the list',
                                       'is_correct': True,
                                       'explanation': 'Correct. append adds one item at the end.'},
                                      {'text': 'Removes pear',
                                       'is_correct': False,
                                       'explanation': 'Review the example. append adds one item at the end.'},
                                      {'text': 'Sorts the list',
                                       'is_correct': False,
                                       'explanation': 'Review the example. append adds one item at the end.'},
                                      {'text': 'Adds pear at the beginning',
                                       'is_correct': False,
                                       'explanation': 'Review the example. append adds one item at the '
                                                      'end.'}]},
                         {'question': 'What does items.pop(0) do?',
                          'explanation': 'Index 0 is the first item.',
                          'options': [{'text': 'Removes and returns the first item',
                                       'is_correct': True,
                                       'explanation': 'Correct. Index 0 is the first item.'},
                                      {'text': 'Removes the last item',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Index 0 is the first item.'},
                                      {'text': 'Adds an item',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Index 0 is the first item.'},
                                      {'text': 'Sorts the list',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Index 0 is the first item.'}]}],
             'title': 'List Operations and Methods'},
            {'challenges': [{'description': ('Your task, step by step:\n1. Read several words on one line.\n2. Use a slice to make a new list without the first or last word, then print it.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.'),
                             'difficulty': 'easy',
                             'hints': ['words = input().split()\ninside = words[1:-1]\nprint(inside)'],
                             'initial_code': '# Queue Simulation with append() and pop(0)\n'
                                             '# Step 1: Initialize q = []\n'
                                             '\n'
                                             "# Step 2: Append 'A', 'B', 'C', then pop(0), then print(q):\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'For red blue green gold, print [blue, green].',
                             'solution_code': 'words = input().split()\ninside = words[1:-1]\nprint(inside)',
                             'test_cases': [{'input_data': 'red blue green gold\n',
  'expected_output': "['blue', 'green']",
  'is_hidden': False},
 {'input_data': 'one two three\n', 'expected_output': "['two']", 'is_hidden': False}],
                             'title': 'Middle Slice Trimmer',
                             'xp_reward': 35},
                            {'description': ('Your task, step by step:\n1. Make a copy of the given color list.\n2. Add green to the copy, then print both lists to show that the original list stayed the same.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.'),
                             'difficulty': 'boss',
                             'hints': ["original = ['red', 'blue']\n"
 'copy = original.copy()\n'
 "copy.append('green')\n"
 'print(original)\n'
 'print(copy)'],
                             'initial_code': '# ⚔️ Boss Challenge: In-Place Alphabetical Sort\n'
                                             '# Step 1: Initialize lst = []\n'
                                             '# Step 2: Read 3 items, sort, and print:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': "Print ['red', 'blue'] first, then ['red', 'blue', 'green'].",
                             'solution_code': ("original = ['red', 'blue']\n"
 'copy = original.copy()\n'
 "copy.append('green')\n"
 'print(original)\n'
 'print(copy)'),
                             'test_cases': [{'input_data': '',
  'expected_output': "['red', 'blue']\n['red', 'blue', 'green']",
  'is_hidden': False}],
                             'title': 'Boss Challenge: Copy Without Changing the Original',
                             'xp_reward': 150}],
             'description': 'Understand when two names share a list and how to make a copy.',
             'lesson': {'common_mistakes': [{'mistake': 'Thinking second = first copies a list.',
  'why': 'Assignment creates another name for the same object.',
  'fix': 'Use first.copy() or first[:] for a shallow copy.'},
 {'mistake': 'Expecting items[1:3] to include index 3.',
  'why': 'The stop index is excluded.',
  'fix': 'Use items[1:4] to include positions 1, 2, and 3.'},
 {'mistake': 'Assuming copy() duplicates every nested list.',
  'why': 'copy() makes a shallow copy and keeps references to inner objects.',
  'fix': 'Remember that changing a shared inner list affects both outer lists.'}],
                        'detailed_explanation': ('A slice uses list[start:stop:step]. The start is included and stop is excluded. items[1:-1] '
 'therefore leaves off the first and last values. Leaving out a bound starts at the beginning or '
 'continues to the end. A slice creates a new outer list containing the selected items.\n'
 '\n'
 'Assignment does not copy a list. After second = first, both names refer to the same list. This '
 'is aliasing. An append or item assignment through either name is visible through both names.\n'
 '\n'
 'Use first.copy() or first[:] to make a shallow copy. The outer list is new, so adding or '
 'replacing a top-level item in the copy does not change the original outer list. A shallow copy '
 'does not copy nested mutable objects. If an item is another list, both outer lists still refer '
 'to that same inner list. Changing that inner list is visible through both. Deep copying is a '
 'separate tool and is outside this lesson.\n'
 '\n'
 'Use a slice to select a portion; use a shallow copy for a separate outer list; use simple '
 'assignment when shared changes are intended. Always consider whether the items themselves '
 'contain mutable objects.'),
                        'expected_output': "['blue', 'green']\n['red', 'blue', 'green', 'gold']",
                        'introduction': ('A program may need a few middle entries from a list, or a safe working version to edit without '
 'changing the saved one. Slicing selects a range. Copying separates the outer list. These tools '
 'help avoid surprising changes to shared data.'),
                        'learning_objectives': ['Slice a list with included start and excluded stop positions.',
 'Predict what happens when two names refer to the same list.',
 'Make a shallow copy with copy() or [:].',
 'Explain the shallow-copy limit when a list contains mutable inner lists.'],
                        'line_by_line': [{'line': '1',
  'code': "colors = ['red', 'blue', 'green', 'gold']",
  'explanation': 'Create a list with four ordered color names.'},
 {'line': '2',
  'code': 'inside = colors[1:-1]',
  'explanation': 'Take a new list beginning at index 1 and stopping before the last item.'},
 {'line': '3', 'code': 'print(inside)', 'explanation': 'Display the two selected middle items.'},
 {'line': '4',
  'code': 'print(colors)',
  'explanation': 'Display the original to show slicing did not remove any of its items.'}],
                        'practical_examples': [{'title': 'Take the middle items',
  'code': "colors = ['red', 'blue', 'green', 'gold']\n"
          'inside = colors[1:-1]\n'
          'print(inside)\n'
          'print(colors)',
  'explanation': 'The slice begins at index 1 and stops before index -1. It returns a new list '
                 'with blue and green; colors is unchanged.',
  'output': "['blue', 'green']\n['red', 'blue', 'green', 'gold']"},
 {'title': 'Assignment shares; copy() separates the outer list',
  'code': "original = ['red', 'blue']\n"
          'alias = original\n'
          'copy = original.copy()\n'
          "alias.append('gold')\n"
          "copy.append('green')\n"
          'print(original)\n'
          'print(copy)',
  'explanation': 'alias shares original, so gold appears in original. copy is a separate outer '
                 'list, so adding green to it does not change original.',
  'output': "['red', 'blue', 'gold']\n['red', 'blue', 'green']"},
 {'title': 'A shallow copy shares inner lists',
  'code': 'original = [[1], [2]]\n'
          'copy = original.copy()\n'
          'copy[0].append(9)\n'
          'print(original)\n'
          'print(copy)',
  'explanation': 'The two outer lists are separate, but their first item refers to the same inner '
                 'list. Appending 9 through copy is visible through original too.',
  'output': '[[1, 9], [2]]\n[[1, 9], [2]]'}],
                        'practice_questions': ['What is [10, 20, 30, 40][1:3]? Check: [20, 30].',
 'If b = a and b.append(4), does a change? Check: yes; they refer to the same list.',
 'Does a.copy() recursively copy nested lists? Check: no, it is shallow.',
 'Which creates a separate outer list, a[:] or b = a? Check: a[:].'],
                        'prerequisites': ('Know list indexing and methods. String slices from Level 49 use the same bounds; this lesson '
 'applies slicing to lists and explains copying.'),
                        'real_world_apps': ('A history screen can display only recent actions with a slice. A program can make a copy of a '
 'shopping list before proposing edits. Nested records require extra care because a shallow copy '
 'still shares inner lists or dictionaries.'),
                        'summary': ('Slices select ranges with an included start and excluded stop. Assignment shares a list. copy() '
 'and [:] create shallow copies: the outer list is new, but nested mutable items remain shared.'),
                        'syntax_breakdown': ('items[start:stop:step]\n'
 'items[1:-1]        # omit first and last\n'
 'second = first     # both names refer to the same list\n'
 'second = first.copy() # shallow copy\n'
 'second = first[:]     # another shallow-copy form\n'
 '# Inner lists are still shared by a shallow copy.'),
                        'terminology': [{'term': 'Slice', 'definition': 'A selected range; start is included and stop is excluded.'},
 {'term': 'Reference',
  'definition': 'The connection from a variable name to the object it refers to.'},
 {'term': 'Aliasing', 'definition': 'Two or more names refer to the same object.'},
 {'term': 'Shallow copy', 'definition': 'A new outer list whose nested objects are still shared.'},
 {'term': 'Mutation', 'definition': "Changing an existing object's contents."}]},
             'number': 54,
             'quizzes': [{'explanation': 'b = a assigns a reference to the same list. Mutating b also '
                                         'mutates a. len(a) is 3.',
                          'options': [{'explanation': 'Correct! b and a point to the exact same list in '
                                                      'memory.',
                                       'is_correct': True,
                                       'text': '3'},
                                      {'explanation': 'Incorrect. Assignment b = a does not copy the list.',
                                       'is_correct': False,
                                       'text': '2'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '1'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the following list reference snippet?\n'
                                      '\n'
                                      'a = [1, 2]\n'
                                      'b = a\n'
                                      'b.append(3)\n'
                                      'print(len(a))'},
                         {'explanation': 'nums.copy() or nums[:] creates a distinct new list object in '
                                         'memory.',
                          'options': [{'explanation': 'Correct! .copy() creates a new independent list.',
                                       'is_correct': True,
                                       'text': 'new_nums = nums.copy()'},
                                      {'explanation': 'Incorrect. This merely creates another reference to '
                                                      'the same list.',
                                       'is_correct': False,
                                       'text': 'new_nums = nums'},
                                      {'explanation': 'Incorrect. .clear() returns None.',
                                       'is_correct': False,
                                       'text': 'new_nums = list(nums).clear()'},
                                      {'explanation': 'Incorrect. Parentheses without commas do not create a '
                                                      'copy.',
                                       'is_correct': False,
                                       'text': 'new_nums = (nums)'}],
                          'question': 'Which of the following creates a genuine independent shallow copy of '
                                      '`nums`?'}],
             'title': 'List Slicing and Copying'},
            {'challenges': [{'description': ('Your task, step by step:\n1. Make a tuple that stores the point (10, 20).\n2. Unpack its two values into x and y, then print each label and value.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.'),
                             'difficulty': 'easy',
                             'hints': ["point = (10, 20)\nx, y = point\nprint(f'X: {x}')\nprint(f'Y: {y}')"],
                             'initial_code': '# List Comprehension: Squaring Elements\n'
                                             '# Step 1: Read numbers:\n'
                                             'nums = [int(x) for x in input().split()]\n'
                                             '\n'
                                             '# Step 2: Compute squares = [x * x for x in nums] and print '
                                             'below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Print X: 10 on the first line and Y: 20 on the second.',
                             'solution_code': "point = (10, 20)\nx, y = point\nprint(f'X: {x}')\nprint(f'Y: {y}')",
                             'test_cases': [{'input_data': '', 'expected_output': 'X: 10\nY: 20', 'is_hidden': False},
 {'input_data': '', 'expected_output': 'X: 10\nY: 20', 'is_hidden': False}],
                             'title': 'Coordinate Tuple',
                             'xp_reward': 35},
                            {'description': ('Your task, step by step:\n1. Read a name, a level, and a color on one line.\n2. Store the three values in a tuple, unpack them into separate names, and print each one with its label.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.'),
                             'difficulty': 'boss',
                             'hints': ['record = tuple(input().split())\n'
 'name, level, color = record\n'
 "print(f'Name: {name}')\n"
 "print(f'Level: {level}')\n"
 "print(f'Color: {color}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Even Filter Comprehension\n'
                                             '# Step 1: Read numbers:\n'
                                             'nums = [int(x) for x in input().split()]\n'
                                             '\n'
                                             '# Step 2: Filter evens = [x for x in nums if x % 2 == 0] and '
                                             'print below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'For Mia 8 red, print Name: Mia, Level: 8, and Color: red on separate lines.',
                             'solution_code': ('record = tuple(input().split())\n'
 'name, level, color = record\n'
 "print(f'Name: {name}')\n"
 "print(f'Level: {level}')\n"
 "print(f'Color: {color}')"),
                             'test_cases': [{'input_data': 'Mia 8 red\n',
  'expected_output': 'Name: Mia\nLevel: 8\nColor: red',
  'is_hidden': False},
 {'input_data': 'Kai 5 blue\n',
  'expected_output': 'Name: Kai\nLevel: 5\nColor: blue',
  'is_hidden': False}],
                             'title': 'Boss Challenge: Tuple Record Reader',
                             'xp_reward': 150}],
             'description': 'Group values in a tuple that cannot be changed.',
             'lesson': {'common_mistakes': [{'mistake': 'Writing one = (5) for a one-item tuple.',
  'why': 'Parentheses alone group the integer; they do not make a tuple.',
  'fix': 'Write one = (5,).'},
 {'mistake': 'Trying to assign point[0] = 9.',
  'why': 'Tuple positions cannot be reassigned.',
  'fix': 'Create a new tuple or use a list if the group must change.'},
 {'mistake': 'Assuming a tuple containing a list freezes that list.',
  'why': 'The tuple slot is fixed, but the list object is mutable.',
  'fix': 'Remember the difference between changing a tuple slot and changing an inner object.'}],
                        'detailed_explanation': ('A tuple is an ordered collection, often written with parentheses and commas: point = (4, 7). Its '
 'first value is at index 0 and its second at index 1, like a list. len(point) counts its values.\n'
 '\n'
 'Tuples are immutable as containers. You can read point[0], but assigning point[0] = 9 raises '
 'TypeError. Choose a tuple for a fixed coordinate or color; choose a list when items need to be '
 'added, removed, or replaced.\n'
 '\n'
 'The comma makes a tuple. (5) is the integer 5 in parentheses. (5,) is a one-item tuple. With '
 'several values, commas separate the items.\n'
 '\n'
 "Immutability applies to the tuple's slots, not recursively to every object inside. If a tuple "
 'contains a list, that inner list can still be changed. The tuple continues to refer to the same '
 'list object.'),
                        'expected_output': '4\n7',
                        'introduction': ('A map coordinate has an x and y value that belong together. If the pair should keep its order '
 'and not have one position replaced accidentally, a tuple is a suitable container.'),
                        'learning_objectives': ['Create a tuple and read values by index.',
 'Explain that a tuple is ordered but its positions cannot be reassigned.',
 'Create a one-item tuple using a trailing comma.',
 'Choose a tuple for a fixed group and a list for a group that changes.',
 'Recognize that a mutable object inside a tuple can still change.'],
                        'line_by_line': [{'line': '1',
  'code': 'point = (4, 7)',
  'explanation': 'Create a tuple with two coordinate values in order.'},
 {'line': '2',
  'code': 'print(point[0])',
  'explanation': 'Read and display the value at index 0, which is 4.'},
 {'line': '3',
  'code': 'print(point[1])',
  'explanation': 'Read and display the value at index 1, which is 7.'}],
                        'practical_examples': [{'title': 'Store and read a coordinate',
  'code': 'point = (4, 7)\nprint(point[0])\nprint(point[1])',
  'explanation': 'The tuple keeps x and y together in a fixed order. Index 0 is x and index 1 is '
                 'y.',
  'output': '4\n7'},
 {'title': 'Make a one-item tuple',
  'code': "choice = ('Start',)\nprint(choice)\nprint(len(choice))",
  'explanation': 'The comma makes choice a tuple. len() confirms it contains one item.',
  'output': "('Start',)\n1"},
 {'title': 'An inner list can still change',
  'code': "record = ('Mia', ['Python'])\nrecord[1].append('Art')\nprint(record)",
  'explanation': "The tuple's second slot still points to the same list, but that list's contents "
                 'can change.',
  'output': "('Mia', ['Python', 'Art'])"}],
                        'practice_questions': ['What is point[1] for point = (8, 3)? Check: 3.',
 'Which is a one-item tuple: (5) or (5,)? Check: (5,).',
 'Should a changing shopping basket use a tuple or a list? Check: a list.',
 'Can a list inside a tuple be changed? Check: yes; the tuple slot stays fixed, but the list is '
 'mutable.'],
                        'prerequisites': ('Know variables, lists, and indexes. A tuple resembles a list but is chosen when its positions '
 'should stay fixed.'),
                        'real_world_apps': ('Coordinates such as (x, y), screen sizes such as (width, height), and RGB colors are small fixed '
 'groups. A roster or inventory that changes is usually better stored in a list.'),
                        'summary': ('Tuples keep ordered values in fixed positions. Read them by index, but do not reassign a '
 'position. A one-item tuple needs a comma. A tuple may contain a mutable object whose contents '
 'can still change.'),
                        'syntax_breakdown': ('point = (4, 7)    # a two-item tuple\n'
 'point[0]          # read first item\n'
 'one = (5,)        # one-item tuple: comma is required\n'
 'not_tuple = (5)   # just the integer 5 in parentheses'),
                        'terminology': [{'term': 'Tuple',
  'definition': 'An ordered collection whose positions cannot be reassigned after creation.'},
 {'term': 'Immutable container',
  'definition': 'A container whose stored positions cannot be replaced, added, or removed.'},
 {'term': 'One-item tuple',
  'definition': 'A tuple with one value; its comma is required, as in (5,).'},
 {'term': 'Mutable object',
  'definition': 'An object whose contents can change, such as a list inside a tuple.'}]},
             'number': 55,
             'quizzes': [{'question': 'Can you replace an item in a tuple after creating it?',
                          'explanation': 'Tuples are immutable, so they cannot be changed.',
                          'options': [{'text': 'No, tuples cannot be changed',
                                       'is_correct': True,
                                       'explanation': 'Correct. Tuples are immutable, so they cannot be '
                                                      'changed.'},
                                      {'text': 'Yes, with index assignment',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Tuples are immutable, so they '
                                                      'cannot be changed.'},
                                      {'text': 'Only the first item',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Tuples are immutable, so they '
                                                      'cannot be changed.'},
                                      {'text': 'Only numbers',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Tuples are immutable, so they '
                                                      'cannot be changed.'}]},
                         {'question': 'How do you make a one-item tuple containing 5?',
                          'explanation': 'The comma makes it a tuple.',
                          'options': [{'text': '(5,)',
                                       'is_correct': True,
                                       'explanation': 'Correct. The comma makes it a tuple.'},
                                      {'text': '(5)',
                                       'is_correct': False,
                                       'explanation': 'Review the example. The comma makes it a tuple.'},
                                      {'text': '[5]',
                                       'is_correct': False,
                                       'explanation': 'Review the example. The comma makes it a tuple.'},
                                      {'text': '{5}',
                                       'is_correct': False,
                                       'explanation': 'Review the example. The comma makes it a tuple.'}]}],
             'title': 'Introduction to Tuples'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Make a tuple with the coordinates 10 and 20.\n2. Put them into the names x and y, then print the two values.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["pt = (10, 20)\nx, y = pt\nprint(f'X: {x}, Y: {y}')"],
                             'initial_code': '# Tuples: Immutable Sequences and Unpacking\n'
                                             '# Step 1: Define pt = (10, 20)\n'
                                             '\n'
                                             "# Step 2: Unpack x, y = pt and print f'X: {x}, Y: {y}' below:\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Print X: 10, Y: 20.',
                             'solution_code': "pt = (10, 20)\nx, y = pt\nprint(f'X: {x}, Y: {y}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'X: 10, Y: 20',
                                             'is_hidden': False}],
                             'title': 'Tuple Coordinate Unpacking',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read the given record tuple.\n2. Print how many items it contains, then print its second item.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["r = (1, 'Quest', 99.5)\nprint(len(r))\nprint(r[1])"],
                             'initial_code': '# ⚔️ Boss Challenge: Record Inspector\n'
                                             '# Step 1: Tuple defined:\n'
                                             "r = (1, 'Quest', 99.5)\n"
                                             '\n'
                                             '# Step 2: Print len(r) and r[1] below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Print 3, then Quest.',
                             'solution_code': "r = (1, 'Quest', 99.5)\nprint(len(r))\nprint(r[1])",
                             'test_cases': [{'input_data': '',
                                             'expected_output': '3\nQuest',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Record Inspector',
                             'xp_reward': 150}],
             'description': 'Pack values into a tuple and unpack them into names.',
             'lesson': {'common_mistakes': [{'mistake': 'Writing x, y = (4, 7, 9).',
  'why': 'There are three values but only two targets.',
  'fix': 'Make the number of targets match the number of values.'},
 {'mistake': 'Assuming unpacking sorts values.',
  'why': "Unpacking follows the tuple's order.",
  'fix': 'Put values in the intended order or choose meaningful target names.'},
 {'mistake': 'Swapping with left = right, then right = left.',
  'why': 'The first assignment overwrites the old left value.',
  'fix': 'Use left, right = right, left.'}],
                        'detailed_explanation': ('Packing puts several values into one tuple. point = (4, 7) packs two values; point = 4, 7 also '
 'works because commas make a tuple.\n'
 '\n'
 'Unpacking assigns tuple items to targets in order: x, y = point sends the first item to x and '
 'the second to y. There must be the same number of targets as values. If the counts differ, '
 'Python raises ValueError. Unpacking does not sort or search; it uses the existing order.\n'
 '\n'
 'Multiple assignment is useful for swapping: left, right = right, left. Python evaluates the '
 'right-hand values before assigning them, so neither old value is lost.\n'
 '\n'
 "A loop can unpack pairs too. In for name, score in records:, each record's first value goes to "
 'name and second to score. Use this when every item has the same shape and the order of each pair '
 'is meaningful.'),
                        'expected_output': '4\n7',
                        'introduction': ('A coordinate may arrive as a pair (4, 7), or a score report may contain a name and score. '
 'Instead of repeatedly reading positions, unpacking gives each value a clear variable name in one '
 'statement.'),
                        'learning_objectives': ['Pack values into a tuple, with or without parentheses.',
 'Unpack values into variables in matching order.',
 'Swap two values with multiple assignment.',
 'Predict the error when value count and target count differ.',
 'Unpack pairs in a for loop.'],
                        'line_by_line': [{'line': '1',
  'code': 'point = (4, 7)',
  'explanation': 'Pack the two coordinate values into a tuple.'},
 {'line': '2',
  'code': 'x, y = point',
  'explanation': 'Unpack the first tuple value into x and the second into y.'},
 {'line': '3',
  'code': 'print(x)',
  'explanation': 'Display the value that came from tuple position 0.'},
 {'line': '4',
  'code': 'print(y)',
  'explanation': 'Display the value that came from tuple position 1.'}],
                        'practical_examples': [{'title': 'Pack and unpack a coordinate',
  'code': 'point = (4, 7)\nx, y = point\nprint(x)\nprint(y)',
  'explanation': 'The tuple contains two values. Unpacking assigns the first to x and the second '
                 'to y.',
  'output': '4\n7'},
 {'title': 'Swap two values',
  'code': "left = 'red'\nright = 'blue'\nleft, right = right, left\nprint(left)\nprint(right)",
  'explanation': 'Python evaluates the right side first, then assigns both results, so the old '
                 'values exchange places.',
  'output': 'blue\nred'},
 {'title': 'Unpack pairs while looping',
  'code': "scores = [('Mia', 92), ('Kai', 85)]\n"
          'for name, score in scores:\n'
          "    print(f'{name}: {score}')",
  'explanation': "Each pair's first value goes to name and second goes to score on each loop pass.",
  'output': 'Mia: 92\nKai: 85'}],
                        'practice_questions': ['After x, y = (12, 5), what is y? Check: 5.',
 'Why does a, b = (1, 2, 3) fail? Check: there are three values but two targets.',
 'Swap a and b in one statement. Check: a, b = b, a.',
 "In for name, score in [('Ari', 90)], what goes into score? Check: 90, the pair's second value."],
                        'prerequisites': ('Know tuples, variables, and loops. Level 55 introduced fixed ordered groups; this lesson names '
 'tuple values as they are assigned.'),
                        'real_world_apps': ('Unpack coordinate pairs, name-score records, and pairs returned by other code. It makes the role '
 'of each position clearer than repeating point[0] or point[1].'),
                        'summary': ('Packing combines values into a tuple. Unpacking assigns values to targets in order, and their '
 'counts must match. Multiple assignment swaps safely. A loop can unpack each pair as it visits '
 'it.'),
                        'syntax_breakdown': ('point = (4, 7)          # pack\n'
 'x, y = point            # unpack in order\n'
 'left, right = right, left # swap\n'
 'for name, score in records:\n'
 '    print(name, score)  # unpack each pair'),
                        'terminology': [{'term': 'Packing', 'definition': 'Putting several values together in a tuple.'},
 {'term': 'Unpacking', 'definition': 'Assigning tuple values to several variables in order.'},
 {'term': 'Target', 'definition': 'A variable on the receiving side of an assignment.'},
 {'term': 'Multiple assignment',
  'definition': 'One statement assigning multiple values, including a safe swap.'},
 {'term': 'ValueError',
  'definition': 'An error raised when unpacking gets a different number of values than targets.'}]},
             'number': 56,
             'quizzes': [{'question': 'If point = (10, 20), what does x, y = point do?',
                          'explanation': 'Unpacking assigns tuple values in order.',
                          'options': [{'text': 'Sets x to 10 and y to 20',
                                       'is_correct': True,
                                       'explanation': 'Correct. Unpacking assigns tuple values in order.'},
                                      {'text': 'Sets x to (10, 20)',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Unpacking assigns tuple values in '
                                                      'order.'},
                                      {'text': 'Sets y to 10 and x to 20',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Unpacking assigns tuple values in '
                                                      'order.'},
                                      {'text': 'Causes an error',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Unpacking assigns tuple values in '
                                                      'order.'}]},
                         {'question': 'What does a, b = b, a do?',
                          'explanation': 'Python unpacks the right side into the names on the left.',
                          'options': [{'text': 'Swaps the values of a and b',
                                       'is_correct': True,
                                       'explanation': 'Correct. Python unpacks the right side into the names '
                                                      'on the left.'},
                                      {'text': 'Adds the values',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Python unpacks the right side '
                                                      'into the names on the left.'},
                                      {'text': 'Makes both equal to a',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Python unpacks the right side '
                                                      'into the names on the left.'},
                                      {'text': 'Creates a list',
                                       'is_correct': False,
                                       'explanation': 'Review the example. Python unpacks the right side '
                                                      'into the names on the left.'}]}],
             'title': 'Tuple Packing and Unpacking'},
            {'challenges': [{'description': 'Your task, step by step:\n1. A set keeps only one copy of each word.\n2. Read the words, remove duplicates, sort them alphabetically, and print the list.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['tags = set(input().split())\nprint(sorted(list(tags)))'],
                             'initial_code': '# Sets: Unordered Unique Collections\n'
                                             '# Step 1: Read words and convert to set:\n'
                                             'tags = set(input().split())\n'
                                             '\n'
                                             '# Step 2: Print sorted(list(tags)) below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'For python game python code, print [code, game, python].',
                             'solution_code': 'tags = set(input().split())\nprint(sorted(tags))',
                             'test_cases': [{'input_data': 'python game python code\n',
                                             'expected_output': "['code', 'game', 'python']",
                                             'is_hidden': False},
                                            {'input_data': 'red red blue\n',
                                             'expected_output': "['blue', 'red']",
                                             'is_hidden': False}],
                             'title': 'Unique Tag Filter',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Two friends have lists of skills.\n2. Read both lines and print only the skills they both have, in alphabetical order.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['skills_a = set(input().split())\n'
 'skills_b = set(input().split())\n'
 'print(sorted(skills_a & skills_b))'],
                             'initial_code': '# ⚔️ Boss Challenge: Set Intersection\n'
                                             '# Step 1: Read sets a and b:\n'
                                             'a = set(input().split())\n'
                                             'b = set(input().split())\n'
                                             '\n'
                                             '# Step 2: Print sorted(list(a & b)) below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'The example lines share python and sql, so print [python, '
                                             'sql].',
                             'solution_code': ('skills_a = set(input().split())\n'
 'skills_b = set(input().split())\n'
 'print(sorted(skills_a & skills_b))'),
                             'test_cases': [{'input_data': 'python git sql docker\npython java sql c++\n',
                                             'expected_output': "['python', 'sql']",
                                             'is_hidden': False},
                                            {'input_data': 'html css\npython django\n',
                                             'expected_output': '[]',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Set Intersection',
                             'xp_reward': 150}],
             'description': 'Use sets to keep unique values and check membership.',
             'lesson': {'common_mistakes': [{'mistake': 'Writing empty = {} for an empty set.',
  'why': 'Python uses {} for an empty dictionary.',
  'fix': 'Write empty = set().'},
 {'mistake': 'Trying tags[0].',
  'why': 'Sets do not have a positional order or indexes.',
  'fix': 'Use a loop to visit values or sorted(tags) to display them in order.'},
 {'mistake': 'Expecting a set to preserve the typed order.',
  'why': 'A set is not an ordered sequence.',
  'fix': 'Sort comparable items when display order matters.'},
 {'mistake': 'Adding a list to a set.',
  'why': 'Lists are mutable and unhashable.',
  'fix': 'Use individual hashable values or a tuple of hashable values.'}],
                        'detailed_explanation': ("A set stores unique hashable values. Braces can create one: tags = {'python', 'game'}. If a "
 'value appears twice, the set keeps one copy. Sets have no positional order, so tags[0] is '
 'invalid. Use a loop to visit items or sorted(tags) when you need a predictable display.\n'
 '\n'
 "The in operator asks whether a value is present: 'python' in tags returns True or False. This is "
 'a direct way to check whether an item has already been collected.\n'
 '\n'
 'Use set() for an empty set. Empty braces {} make an empty dictionary. Set elements must be '
 'hashable: strings and numbers are common examples. Lists can change, so they cannot be set '
 'elements; a tuple of hashable values can be.\n'
 '\n'
 'Use a list when order or repeated items matter. Use a set when you need distinct values and '
 'membership checks. Never rely on the order in which a set prints; sort comparable items when '
 'order matters to a person.'),
                        'expected_output': "['game', 'python']\nTrue\nFalse",
                        'introduction': ('A game records tags a player has collected, but the same tag can arrive more than once. A list '
 'keeps every repeat. A set keeps one copy of each distinct value, so it is useful for unique tags '
 'and membership checks.'),
                        'learning_objectives': ['Create sets and explain how they remove duplicate values.',
 'Test membership with in.',
 'Explain why sets have no positional indexes or promised display order.',
 'Create an empty set with set().',
 'Recognize that set elements must be hashable.'],
                        'line_by_line': [{'line': '1',
  'code': "tags = {'python', 'game', 'python'}",
  'explanation': 'Create a set; the repeated python value does not make a second copy.'},
 {'line': '2',
  'code': 'print(sorted(tags))',
  'explanation': 'Sort the distinct values so their displayed order is predictable.'},
 {'line': '3',
  'code': "print('python' in tags)",
  'explanation': 'Check whether python belongs to the set; this is True.'},
 {'line': '4',
  'code': "print('java' in tags)",
  'explanation': 'Check an absent value; this is False.'}],
                        'practical_examples': [{'title': 'Remove duplicates and check membership',
  'code': "tags = {'python', 'game', 'python'}\n"
          'print(sorted(tags))\n'
          "print('python' in tags)\n"
          "print('java' in tags)",
  'explanation': 'The repeated value is kept once. sorted() makes an ordered list for display. in '
                 'checks whether each word is present.',
  'output': "['game', 'python']\nTrue\nFalse"},
 {'title': 'Create an empty set',
  'code': "seen = set()\nseen.add('map')\nprint('map' in seen)\nprint(len(seen))",
  'explanation': 'set() creates an empty set; add() stores a value. {} would create a dictionary '
                 'instead.',
  'output': 'True\n1'},
 {'title': 'Use a tuple as a set element',
  'code': "locations = {('x', 3), ('y', 4)}\nprint(len(locations))",
  'explanation': 'The tuples contain hashable strings and numbers, so they can be set elements. A '
                 'list cannot be used because it is mutable.',
  'output': '2'}],
                        'practice_questions': ['How many values are in {2, 2, 5}? Check: 2.',
 'What does {} create? Check: an empty dictionary, not a set.',
 "What does 'key' in items return? Check: True or False.",
 'Why can a tuple be in a set while a list cannot? Check: a list can change and is unhashable.'],
                        'prerequisites': ('Know lists and duplicates. A set is a collection chosen for uniqueness and membership, not '
 'positional access.'),
                        'real_world_apps': ('A set can track unique course tags, product labels, or visited pages. Membership can check '
 'whether an item has already been collected. Use a list instead if order or repeats matter.'),
                        'summary': ('Sets remove duplicates and support membership checks with in. They have no indexes or guaranteed '
 'order. Use set() for an empty set. Values must be hashable; sorted() gives predictable display '
 'for comparable values.'),
                        'syntax_breakdown': ("tags = {'python', 'game', 'python'} # duplicate kept once\n"
 "'python' in tags                     # True or False\n"
 'empty = set()                        # empty set\n'
 'ordered = sorted(tags)               # predictable display\n'
 '# Sets do not support tags[0].'),
                        'terminology': [{'term': 'Set', 'definition': 'An unordered collection of unique hashable values.'},
 {'term': 'Membership', 'definition': 'Whether a value is present; test with value in collection.'},
 {'term': 'Hashable', 'definition': 'A value suitable as a stable set element or dictionary key.'},
 {'term': 'Empty set',
  'definition': 'A set with no values, created with set(); {} creates an empty dictionary.'}]},
             'number': 57,
             'quizzes': [{'explanation': 'Sets only store unique elements. {1, 2, 3} has length 3. Adding 3 '
                                         'again has no effect.',
                          'options': [{'explanation': 'Correct! Sets discard duplicate entries.',
                                       'is_correct': True,
                                       'text': '3'},
                                      {'explanation': 'Incorrect. Duplicates are never added to sets.',
                                       'is_correct': False,
                                       'text': '4'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '5'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of running this code?\n'
                                      '\n'
                                      's = {1, 2, 2, 3}\n'
                                      's.add(3)\n'
                                      'print(len(s))'},
                         {'explanation': 'Python sets are implemented using hash tables, offering O(1) '
                                         'constant average lookup time.',
                          'options': [{'explanation': 'Correct! Sets use hashing for O(1) average lookup.',
                                       'is_correct': True,
                                       'text': 'O(1) constant time'},
                                      {'explanation': 'Incorrect. Lists have O(N) lookup; sets have O(1).',
                                       'is_correct': False,
                                       'text': 'O(N) linear time'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'O(log N)'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'O(N^2)'}],
                          'question': 'What is the time complexity of checking `x in my_set` in Python on '
                                      'average?'}],
             'title': 'Introduction to Sets'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use the two sets in the code.\n2. First print all different numbers from either set in order.\n3. Then print the numbers that are only in the first set.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['set1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(sorted(set1 | set2))\nprint(sorted(set1 - set2))'],
                             'initial_code': '# Set Union (|) and Difference (-)\n'
                                             '# Step 1: Sets defined:\n'
                                             's1 = {1, 2, 3}\n'
                                             's2 = {3, 4, 5}\n'
                                             '\n'
                                             '# Step 2: Print union and difference below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Print [1, 2, 3, 4, 5], then [1, 2].',
                             'solution_code': 'set1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(sorted(set1 | set2))\nprint(sorted(set1 - set2))',
                             'test_cases': [{'input_data': '',
                                             'expected_output': '[1, 2, 3, 4, 5]\n[1, 2]',
                                             'is_hidden': False}],
                             'title': 'Union and Difference',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read two groups of names.\n2. Print the names that appear in one group but not both, in alphabetical order.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['group_a = set(input().split())\n'
                                       'group_b = set(input().split())\n'
                                       'print(sorted(group_a ^ group_b))'],
                             'initial_code': '# ⚔️ Boss Challenge: Symmetric Difference\n'
                                             '# Step 1: Read the two groups:\n'
                                             'group_a = set(input().split())\n'
                                             'group_b = set(input().split())\n'
                                             '\n'
                                             '# Step 2: Print the names that are in only one group.\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Names in both groups are left out of the result.',
                             'solution_code': 'group_a = set(input().split())\n'
                                              'group_b = set(input().split())\n'
                                              'print(sorted(group_a ^ group_b))',
                             'test_cases': [{'input_data': 'U1 U2 U3 U4\nU3 U4 U5 U6\n',
                                             'expected_output': "['U1', 'U2', 'U5', 'U6']",
                                             'is_hidden': False},
                                            {'input_data': 'Alice Bob\nCharlie David\n',
                                             'expected_output': "['Alice', 'Bob', 'Charlie', 'David']",
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Symmetric Difference',
                             'xp_reward': 150}],
             'description': 'Compare sets to find shared or different values.',
             'lesson': {'common_mistakes': [{'mistake': 'Using A - B to combine two groups.',
  'why': 'Minus keeps only values from the left that are absent on the right.',
  'fix': 'Use A | B for union.'},
 {'mistake': 'Assuming A - B equals B - A.',
  'why': 'Difference starts with the left set, so order changes the question.',
  'fix': "Read A - B as 'in A but not in B.'"},
 {'mistake': 'Using ^ for shared values.',
  'why': 'Symmetric difference excludes values in both sets.',
  'fix': 'Use & for the intersection.'},
 {'mistake': 'Expecting raw set output to be alphabetic.',
  'why': 'Sets do not guarantee display order.',
  'fix': 'Use sorted(result) when a predictable order matters.'}],
                        'detailed_explanation': ("Let A = {'red', 'blue'} and B = {'blue', 'green'}. Union, A | B, combines values from either set "
 'and keeps each once. Intersection, A & B, keeps only values in both. Difference, A - B, keeps '
 'values in A that are not in B. Difference is directional: A - B can differ from B - A.\n'
 '\n'
 'Symmetric difference, A ^ B, keeps values that appear in one set but not both. In this example, '
 'red and green remain; shared blue is excluded. Each operator returns a new set and leaves the '
 'original sets unchanged.\n'
 '\n'
 'Sets do not promise display order. sorted(result) returns a list in a predictable order when '
 'values can be compared. Choose by the question: everything means |; shared means &; from the '
 'first group only means -; in one group but not both means ^. Reading the operation in plain '
 'words prevents confusing difference with symmetric difference.'),
                        'expected_output': "['blue', 'green', 'red']\n['blue']\n['red']\n['green', 'red']",
                        'introduction': ('Two friends have game items. You may want everything they own, only the shared items, items only '
 'one friend owns, or items owned by exactly one friend. Set operations express each question '
 'directly.'),
                        'learning_objectives': ['Use | for union and & for intersection.',
 'Use - for directional difference and ^ for symmetric difference.',
 'Explain which values each operation keeps.',
 'Sort results for predictable display.'],
                        'line_by_line': [{'line': '1', 'code': "a = {'red', 'blue'}", 'explanation': 'Create the first group.'},
 {'line': '2',
  'code': "b = {'blue', 'green'}",
  'explanation': 'Create the second group; blue is shared.'},
 {'line': '3',
  'code': 'print(sorted(a | b))',
  'explanation': 'Combine all values, then sort the result for display.'},
 {'line': '4',
  'code': 'print(sorted(a & b))',
  'explanation': 'Keep only values present in both sets.'},
 {'line': '5',
  'code': 'print(sorted(a - b))',
  'explanation': 'Keep values from a that are absent from b.'},
 {'line': '6',
  'code': 'print(sorted(a ^ b))',
  'explanation': 'Keep values present in one set but not both.'}],
                        'practical_examples': [{'title': 'Compare two groups with all four operations',
  'code': "a = {'red', 'blue'}\n"
          "b = {'blue', 'green'}\n"
          'print(sorted(a | b))\n'
          'print(sorted(a & b))\n'
          'print(sorted(a - b))\n'
          'print(sorted(a ^ b))',
  'explanation': 'Union returns all colors. Intersection returns shared blue. Difference keeps red '
                 'from a. Symmetric difference keeps red and green, which occur in exactly one '
                 'set.',
  'output': "['blue', 'green', 'red']\n['blue']\n['red']\n['green', 'red']"},
 {'title': 'Difference depends on operand order',
  'code': 'a = {1, 2, 3}\nb = {2, 3, 4}\nprint(sorted(a - b))\nprint(sorted(b - a))',
  'explanation': 'A - B asks for values in a but not b. B - A asks the reverse question.',
  'output': '[1]\n[4]'},
 {'title': 'Union keeps a shared item once',
  'code': "a = {'map', 'key'}\nb = {'key', 'torch'}\nprint(sorted(a | b))",
  'explanation': 'key occurs in both sets, but a set contains only one copy.',
  'output': "['key', 'map', 'torch']"}],
                        'practice_questions': ['Which operator keeps only shared values? Check: &.',
 'If A = {1, 2} and B = {2, 3}, what is A - B? Check: {1}.',
 'Which operator keeps values in one set but not both? Check: ^.',
 'Why sort a set result before displaying it? Check: sets do not promise a predictable order.'],
                        'prerequisites': ('Know that sets keep unique values and have no indexes. Level 57 introduced set creation and '
 'membership.'),
                        'real_world_apps': ('Compare course registrations to find all offered courses, courses two students share, courses '
 'only one student has, or courses taken by exactly one student. Choose the operator from the '
 'question being asked.'),
                        'summary': ('Use | for union, & for intersection, - for left-side difference, and ^ for symmetric difference. '
 'Operations return new sets. Use sorted() for predictable display; A - B is directional.'),
                        'syntax_breakdown': ('A | B # union: all values from either\n'
 'A & B # intersection: only shared values\n'
 'A - B # in A, not in B\n'
 'A ^ B # in one set, not both\n'
 'sorted(A | B) # sort the result for display'),
                        'terminology': [{'term': 'Union |', 'definition': 'All distinct values from either set.'},
 {'term': 'Intersection &', 'definition': 'Only values found in both sets.'},
 {'term': 'Difference -',
  'definition': 'Values in the left set but not the right; direction matters.'},
 {'term': 'Symmetric difference ^',
  'definition': 'Values in exactly one set, excluding shared values.'},
 {'term': 'sorted()', 'definition': 'Returns an ordered list for predictable display.'}]},
             'number': 58,
             'quizzes': [{'explanation': 'Symmetric difference (^) returns elements that are in either set, '
                                         'but NOT in both: {1, 4}.',
                          'options': [{'explanation': 'Correct! 1 and 4 are unique to one set.',
                                       'is_correct': True,
                                       'text': '{1, 4}'},
                                      {'explanation': 'Incorrect. {2, 3} is the intersection (a & b).',
                                       'is_correct': False,
                                       'text': '{2, 3}'},
                                      {'explanation': 'Incorrect. That is the union (a | b).',
                                       'is_correct': False,
                                       'text': '{1, 2, 3, 4}'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '{1}'}],
                          'question': 'What is the output of the set symmetric difference?\n'
                                      '\n'
                                      'a = {1, 2, 3}\n'
                                      'b = {2, 3, 4}\n'
                                      'print(a ^ b)'},
                         {'explanation': 'The & operator performs set intersection, returning common '
                                         'elements: {2, 3}.',
                          'options': [{'explanation': 'Correct! 2 and 3 exist in both sets.',
                                       'is_correct': True,
                                       'text': '{2, 3}'},
                                      {'explanation': 'Incorrect. That is symmetric difference (^).',
                                       'is_correct': False,
                                       'text': '{1, 4}'},
                                      {'explanation': 'Incorrect. That is union (|).',
                                       'is_correct': False,
                                       'text': '{1, 2, 3, 4}'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'set()'}],
                          'question': 'What is the output of: print({1, 2, 3} & {2, 3, 4})?'}],
             'title': 'Set Operations (Union, Intersection, Difference)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. A dictionary stores details with labels.\n2. Use the given hero information to print the name, then the level.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["hero = {'name': 'Arthur', 'class': 'Knight', 'level': 5}\n"
                                       "print(hero['name'])\n"
                                       "print(hero['level'])"],
                             'initial_code': '# Dictionaries: Key-Value Stores\n'
                                             '# Step 1: Dictionary defined:\n'
                                             "hero = {'name': 'Arthur', 'class': 'Knight', 'level': 5}\n"
                                             '\n'
                                             '# Step 2: Print name and level below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Print Arthur, then 5.',
                             'solution_code': "hero = {'name': 'Arthur', 'class': 'Knight', 'level': 5}\n"
                                              "print(hero['name'])\n"
                                              "print(hero['level'])",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Arthur\n5',
                                             'is_hidden': False}],
                             'title': 'Key-Value Character Profile',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Build a small dictionary.\n2. Read three pairs of lines: a label, then its value.\n3. Add each pair and print the dictionary.\n\nInput for this example: The Input box shows 6 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['d = {}\n'
                                       'for _ in range(3):\n'
                                       '    k = input().strip()\n'
                                       '    v = input().strip()\n'
                                       '    d[k] = v\n'
                                       'print(d)'],
                             'initial_code': '# ⚔️ Boss Challenge: Interactive Dictionary Builder\n'
                                             '# Step 1: Initialize empty dictionary:\n'
                                             'd = {}\n'
                                             '\n'
                                             '# Step 2: Loop 3 times reading key and value:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'For the example, the dictionary contains name Arthur, class '
                                             'Knight, and rank 5.',
                             'solution_code': 'd = {}\n'
                                              'for _ in range(3):\n'
                                              '    key = input().strip()\n'
                                              '    value = input().strip()\n'
                                              '    d[key] = value\n'
                                              'print(d)',
                             'test_cases': [{'input_data': 'name\nArthur\nclass\nKnight\nrank\n5\n',
                                             'expected_output': "{'name': 'Arthur', 'class': 'Knight', "
                                                                "'rank': '5'}",
                                             'is_hidden': False},
                                            {'input_data': 'a\n1\nb\n2\nc\n3\n',
                                             'expected_output': "{'a': '1', 'b': '2', 'c': '3'}",
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Interactive Dictionary Builder',
                             'xp_reward': 150}],
             'description': 'Store labeled information as key-value pairs.',
             'lesson': {'common_mistakes': [{'mistake': 'Writing hero[name] when name is the literal key text.',
  'why': 'Without quotes Python looks for a variable called name.',
  'fix': "Write hero['name']."},
 {'mistake': 'Expecting a missing bracket lookup to return an empty value.',
  'why': 'A missing key raises KeyError.',
  'fix': 'Use get() when the key may be absent and a fallback is appropriate.'},
 {'mistake': 'Expecting another copy of a key when assigning it again.',
  'why': 'Keys are unique; the new value replaces the old one.',
  'fix': 'Store several values in a list under one key if that is the intended structure.'},
 {'mistake': 'Using a list as a key.',
  'why': 'Lists can change and are unhashable.',
  'fix': 'Use a string, number, or suitable tuple as a key.'}],
                        'detailed_explanation': ("A dictionary maps keys to values. Write pairs inside braces: hero = {'name': 'Mia', 'level': 3}. "
 "The key 'name' labels Mia; 'level' labels 3. A colon separates key and value, and commas "
 'separate pairs.\n'
 '\n'
 "Use hero['name'] to retrieve Mia. Assignment adds or updates: hero['level'] = 4 changes an "
 "existing value; hero['class'] = 'Ranger' creates a new pair. Keys are unique, so assigning to an "
 'existing key replaces its old value. Values may repeat.\n'
 '\n'
 'Keys must be hashable. Strings and numbers are common keys; lists are mutable and cannot be '
 'keys. Looking up a missing key with brackets raises KeyError. Level 60 introduces get() for '
 'cases where a key may be absent.\n'
 '\n'
 'Dictionaries preserve insertion order in modern Python, but use them as mappings rather than '
 'numbered sequences. A list is better for an ordered group of repeated records; each record can '
 'be a dictionary so its fields are labeled.'),
                        'expected_output': "Mia\n{'name': 'Mia', 'level': 4, 'class': 'Ranger'}",
                        'introduction': ('A student record may contain a name, class, and score. Separate numbered positions are hard to '
 'remember. A dictionary labels each value, so code can ask for the score by its key instead of '
 'remembering its position.'),
                        'learning_objectives': ['Create a dictionary of key-value pairs and retrieve a value by key.',
 'Add a new pair or update the value under an existing key.',
 'Explain unique keys and the hashable-key requirement.',
 'Predict the result of looking up a missing key with brackets.',
 'Choose a dictionary for labeled information rather than numbered positions.'],
                        'line_by_line': [{'line': '1',
  'code': "hero = {'name': 'Mia', 'level': 3}",
  'explanation': 'Create two key-value pairs in a dictionary.'},
 {'line': '2',
  'code': "print(hero['name'])",
  'explanation': 'Look up the value connected to name and display Mia.'},
 {'line': '3',
  'code': "hero['level'] = 4",
  'explanation': 'Replace the value under the existing level key.'},
 {'line': '4',
  'code': "hero['class'] = 'Ranger'",
  'explanation': 'Add class because that key was not present.'},
 {'line': '5',
  'code': 'print(hero)',
  'explanation': 'Display the dictionary after the update and addition.'}],
                        'practical_examples': [{'title': 'Read, update, and add details',
  'code': "hero = {'name': 'Mia', 'level': 3}\n"
          "print(hero['name'])\n"
          "hero['level'] = 4\n"
          "hero['class'] = 'Ranger'\n"
          'print(hero)',
  'explanation': 'The name key retrieves Mia. The level assignment updates an existing pair; class '
                 'adds a new pair.',
  'output': "Mia\n{'name': 'Mia', 'level': 4, 'class': 'Ranger'}"},
 {'title': 'A repeated key updates its value',
  'code': "settings = {'volume': 5}\nsettings['volume'] = 8\nprint(settings)",
  'explanation': 'A dictionary cannot keep two separate values for one key. The new assignment '
                 'replaces the old value.',
  'output': "{'volume': 8}"},
 {'title': 'Use a meaningful label',
  'code': "scores = {'math': 91, 'art': 86}\nprint(scores['art'])",
  'explanation': 'The label art retrieves its score. No position number has to be remembered.',
  'output': '86'}],
                        'practice_questions': ["What does player['level'] return for {'level': 4}? Check: 4.",
 'What happens when assigning to an existing key? Check: its value is replaced.',
 "Why might scores['history'] raise KeyError? Check: history may not exist.",
 'Choose a list or dictionary for one score under each subject name. Check: dictionary, because '
 'subjects are labels.'],
                        'prerequisites': ('Know variables, strings, numbers, and lists. A dictionary connects each value to a meaningful '
 'label such as name, level, or score.'),
                        'real_world_apps': ('A settings dictionary can map volume to 8 and language to English. A student record can map name '
 'to Mia and score to 91. Dictionaries fit information retrieved by meaningful labels.'),
                        'summary': ('Dictionaries map unique, hashable keys to values. Brackets retrieve, add, or update values; a '
 'missing key raises KeyError. Choose dictionaries for labeled information and lists for ordered '
 'sequences.'),
                        'syntax_breakdown': ("hero = {'name': 'Mia', 'level': 3}\n"
 "hero['name']             # retrieve a value\n"
 "hero['level'] = 4        # update a value\n"
 "hero['class'] = 'Ranger' # add a new pair\n"
 "# hero['score'] raises KeyError if score is missing"),
                        'terminology': [{'term': 'Dictionary', 'definition': 'A mapping that connects keys to values.'},
 {'term': 'Key', 'definition': 'A unique, hashable label used to retrieve a value.'},
 {'term': 'Value', 'definition': 'The information stored under a key.'},
 {'term': 'Key-value pair', 'definition': 'A label and the information connected to it.'},
 {'term': 'KeyError', 'definition': 'An error from bracket lookup when a key is absent.'}]},
             'number': 59,
             'quizzes': [{'explanation': 'Dictionary keys must be hashable/immutable. A list is mutable, so '
                                         'it cannot be a key.',
                          'options': [{'explanation': 'Correct! Lists are unhashable because they are '
                                                      'mutable.',
                                       'is_correct': True,
                                       'text': '[1, 2, 3] (a list)'},
                                      {'explanation': 'Strings are immutable and hashable.',
                                       'is_correct': False,
                                       'text': "'name' (a string)"},
                                      {'explanation': 'Integers are immutable and hashable.',
                                       'is_correct': False,
                                       'text': '42 (an integer)'},
                                      {'explanation': 'Tuples containing hashable items are hashable.',
                                       'is_correct': False,
                                       'text': '(1, 2) (a tuple of integers)'}],
                          'question': 'Which of the following CANNOT be used as a dictionary key in Python?'},
                         {'explanation': 'Python dictionaries use hash tables, providing O(1) average lookup '
                                         'time.',
                          'options': [{'explanation': 'Correct! Hash-table lookup is O(1) on average.',
                                       'is_correct': True,
                                       'text': 'O(1) constant time'},
                                      {'explanation': 'Incorrect. Lists require O(N), not dicts.',
                                       'is_correct': False,
                                       'text': 'O(N) linear time'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'O(log N)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'O(N log N)'}],
                          'question': 'What is the average time complexity of looking up a key in a Python '
                                      'dictionary?'}],
             'title': 'Introduction to Dictionaries'},
            {'challenges': [{'description': 'Your task, step by step:\n1. A score may not exist for every subject.\n2. Look up the music score safely.\n3. If it is missing, print Not enrolled.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["scores = {'math': 90, 'art': 85}\n"
                                       "print(scores.get('music', 'Not enrolled'))"],
                             'initial_code': '# Safe Dictionary Lookups with get()\n'
                                             '# Step 1: Dictionary defined:\n'
                                             "scores = {'math': 90, 'art': 85}\n"
                                             '\n'
                                             "# Step 2: Print scores.get('music', 'Not enrolled') below:\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'The given dictionary has no music score, so print Not '
                                             'enrolled.',
                             'solution_code': "scores = {'math': 90, 'art': 85}\n"
                                              "print(scores.get('music', 'Not enrolled'))",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Not enrolled',
                                             'is_hidden': False}],
                             'title': 'Safe Lookup with get()',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Print each label and its value from the given dictionary, one pair per line.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["d = {'a': 10, 'b': 20, 'c': 30}\n"
                                       'for k, v in d.items():\n'
                                       "    print(f'{k}: {v}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Dictionary Items Iteration\n'
                                             '# Step 1: Dictionary defined:\n'
                                             "d = {'a': 10, 'b': 20, 'c': 30}\n"
                                             '\n'
                                             "# Step 2: for k, v in d.items(): print f'{k}: {v}' below:\n"
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Print a, 10; then b, 20; then c, 30.',
                             'solution_code': "d = {'a': 10, 'b': 20, 'c': 30}\n"
                                              'for k, v in d.items():\n'
                                              "    print(f'{k}: {v}')",
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'a: 10\nb: 20\nc: 30',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Dictionary Items Iteration',
                             'xp_reward': 150}],
             'description': 'Safely read and update dictionary information.',
             'lesson': {'common_mistakes': [{'mistake': 'Thinking get() adds its fallback to the dictionary.',
  'why': 'get() returns a value but does not change the mapping.',
  'fix': 'Use settings[key] = value when you want to add a key.'},
 {'mistake': 'Looping over a dictionary directly and expecting pairs.',
  'why': 'A direct dictionary loop visits keys only.',
  'fix': 'Use for key, value in settings.items() when both values are needed.'},
 {'mistake': 'Writing settings = settings.update(other).',
  'why': 'update() changes the dictionary and returns None.',
  'fix': 'Call settings.update(other) without assignment.'},
 {'mistake': 'Using brackets for an optional key.',
  'why': 'A missing key raises KeyError.',
  'fix': 'Use get(key, fallback) when absence is expected.'}],
                        'detailed_explanation': ('get(key, default) returns the value when a key exists. If it is missing, get() returns the '
 'supplied default instead of raising KeyError. With no default it returns None. get() does not '
 'add the missing key; assign with brackets when you want to create it.\n'
 '\n'
 'keys() gives the keys, values() gives the values, and items() gives key-value pairs. A loop can '
 "unpack those pairs: for subject, score in scores.items():. Each pair's first value goes to "
 'subject and the second to score. Iteration follows dictionary insertion order.\n'
 '\n'
 'update(other) adds new pairs or replaces values for matching keys. It changes the original '
 'dictionary and returns None. pop(key) removes a pair and returns its value. You can pass a '
 "fallback to pop() for a missing key. Save pop()'s return when it matters; do not assign "
 "update()'s return to the dictionary.\n"
 '\n'
 'Use bracket lookup when the key is required and a missing key is a real problem. Use get() when '
 'absence is normal and the program should continue with a useful fallback.'),
                        'expected_output': "light\n{'volume': 8}",
                        'introduction': ('A settings screen may need to show a theme even when the user has never chosen one. The program '
 'needs a safe fallback. Dictionary methods help with missing keys and with processing many stored '
 'labels and values.'),
                        'learning_objectives': ['Use get() to return a fallback for a missing key without changing the dictionary.',
 'Visit keys, values, or key-value pairs with dictionary methods.',
 'Unpack each pair from items() inside a loop.',
 'Use update() and pop() and understand their side effects and return values.',
 'Choose brackets or get() based on whether a key must exist.'],
                        'line_by_line': [{'line': '1',
  'code': "settings = {'volume': 8}",
  'explanation': 'Create a dictionary with volume but no theme key.'},
 {'line': '2',
  'code': "theme = settings.get('theme', 'light')",
  'explanation': 'Ask for theme; because it is absent, get() returns light rather than raising '
                 'KeyError.'},
 {'line': '3', 'code': 'print(theme)', 'explanation': 'Display the fallback returned by get().'},
 {'line': '4',
  'code': 'print(settings)',
  'explanation': 'Show that get() did not add theme to the dictionary.'}],
                        'practical_examples': [{'title': 'Safely read an optional setting',
  'code': "settings = {'volume': 8}\n"
          "theme = settings.get('theme', 'light')\n"
          'print(theme)\n'
          'print(settings)',
  'explanation': 'theme is absent, so get() returns light. It does not insert theme into settings.',
  'output': "light\n{'volume': 8}"},
 {'title': 'Visit each key-value pair',
  'code': "scores = {'math': 91, 'art': 86}\n"
          'for subject, score in scores.items():\n'
          "    print(f'{subject}: {score}')",
  'explanation': 'items() supplies pairs. The loop unpacks each pair into subject and score.',
  'output': 'math: 91\nart: 86'},
 {'title': 'Update a value and remove another',
  'code': "settings = {'volume': 5, 'theme': 'dark'}\n"
          "settings.update({'volume': 8})\n"
          "old_theme = settings.pop('theme')\n"
          'print(old_theme)\n'
          'print(settings)',
  'explanation': 'update() changes volume. pop() removes theme and returns dark, which is saved in '
                 'old_theme.',
  'output': "dark\n{'volume': 8}"}],
                        'practice_questions': ["What does {'volume': 8}.get('theme', 'light') return? Check: light.",
 'Which method supplies pairs for a loop? Check: items().',
 'Does get() add a missing key? Check: no.',
 'Which method removes a key and returns its old value? Check: pop().'],
                        'prerequisites': ('Know how to create, retrieve, and update dictionary entries. Level 59 explained that a missing '
 'bracket lookup raises KeyError.'),
                        'real_world_apps': ('A game can read an optional sound setting with a default. A report can print every setting using '
 'items(). A program can update configuration or remove a temporary entry after use.'),
                        'summary': ('get() supplies a fallback without inserting a key. items() provides pairs for unpacking in a '
 'loop. update() changes a dictionary and returns None; pop() removes a pair and returns its '
 'value.'),
                        'syntax_breakdown': ("theme = settings.get('theme', 'light')\n"
 'for key, value in settings.items():\n'
 '    print(key, value)\n'
 "settings.update({'volume': 8}) # changes settings; returns None\n"
 "old = settings.pop('theme', 'light') # remove; fallback if absent"),
                        'terminology': [{'term': 'get(key, default)',
  'definition': 'Returns a present value or a fallback when the key is missing; does not insert '
                'the fallback.'},
 {'term': 'items()', 'definition': 'Provides key-value pairs for iteration.'},
 {'term': 'keys() and values()',
  'definition': "Provide the dictionary's keys or values for iteration."},
 {'term': 'update()', 'definition': 'Adds or replaces pairs in place and returns None.'},
 {'term': 'pop(key)', 'definition': 'Removes a key and returns its value.'}]},
             'number': 60,
             'quizzes': [{'explanation': "d.items() yields key-value tuples ('a', 1) and ('b', 2), printing "
                                         "'a:1 b:2 '.",
                          'options': [{'explanation': 'Correct! .items() unpacks both key and value.',
                                       'is_correct': True,
                                       'text': 'a:1 b:2 '},
                                      {'explanation': 'Incorrect. That is d.keys().',
                                       'is_correct': False,
                                       'text': 'a b '},
                                      {'explanation': 'Incorrect. That is d.values().',
                                       'is_correct': False,
                                       'text': '1 2 '},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What will be printed when running this dictionary loop?\n'
                                      '\n'
                                      "d = {'a': 1, 'b': 2}\n"
                                      'for k, v in d.items():\n'
                                      "    print(f'{k}:{v}', end=' ')"},
                         {'explanation': '.values() returns a view of values [10, 20].',
                          'options': [{'explanation': 'Correct! .values() extracts the dictionary values.',
                                       'is_correct': True,
                                       'text': '[10, 20]'},
                                      {'explanation': 'Incorrect. That is .keys().',
                                       'is_correct': False,
                                       'text': "['x', 'y']"},
                                      {'explanation': 'Incorrect. That is .items().',
                                       'is_correct': False,
                                       'text': "[('x', 10), ('y', 20)]"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '30'}],
                          'question': "What is the output of: print(list({'x': 10, 'y': 20}.values()))?"}],
             'title': 'Essential Dictionary Methods'},
            {'challenges': [{'description': 'Your task, step by step:\n1. A party is a list of hero records.\n2. Visit each hero and print their name and health on one line.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["party = [{'name': 'Aria', 'hp': 100}, {'name': 'Boran', 'hp': 85}]\n"
                                       'for m in party:\n'
                                       '    print(f"{m[\'name\']}: {m[\'hp\']} HP")'],
                             'initial_code': '# Nested Collections: List of Dictionaries\n'
                                             '# Step 1: Party list defined:\n'
                                             "party = [{'name': 'Aria', 'hp': 100}, {'name': 'Boran', 'hp': "
                                             '85}]\n'
                                             '\n'
                                             '# Step 2: Iterate and print name and HP below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Print Aria: 100 HP, then Boran: 85 HP.',
                             'solution_code': "party = [{'name': 'Aria', 'hp': 100}, {'name': 'Boran', 'hp': "
                                              '85}]\n'
                                              'for member in party:\n'
                                              '    print(f"{member[\'name\']}: {member[\'hp\']} HP")',
                             'test_cases': [{'input_data': '',
                                             'expected_output': 'Aria: 100 HP\nBoran: 85 HP',
                                             'is_hidden': False}],
                             'title': 'Party Health Monitor',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. A grid has rows, and each row has numbers.\n2. Print each row on its own line with a space between the numbers.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['matrix = [[1, 2], [3, 4]]\n'
 'for row in matrix:\n'
 "    print(' '.join([str(value) for value in row]))"],
                             'initial_code': '# ⚔️ Boss Challenge: 2D Matrix Grid Printer\n'
                                             '# Step 1: Matrix defined:\n'
                                             'matrix = [[1, 2], [3, 4]]\n'
                                             '\n'
                                             '# Step 2: Print each row space-separated below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Print 1 2, then 3 4.',
                             'solution_code': "matrix = [[1, 2], [3, 4]]\nfor row in matrix:\n    print(' '.join([str(value) for value in row]))",
                             'test_cases': [{'input_data': '',
                                             'expected_output': '1 2\n3 4',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: 2D Matrix Grid Printer',
                             'xp_reward': 150}],
             'description': 'Store and read groups inside other groups.',
             'lesson': {'common_mistakes': [{'mistake': 'Writing grid[1] when you want one cell.',
  'why': 'grid[1] returns the entire second row.',
  'fix': 'Use grid[1][1] to select the second row and its second cell.'},
 {'mistake': "Using students['name'] when students is a list.",
  'why': 'The outer list requires a numeric position before a record key can be used.',
  'fix': "Use students[0]['name']."},
 {'mistake': 'Calling any dictionary-like data JSON.',
  'why': 'JSON is serialized text; a Python dictionary is an in-memory Python object.',
  'fix': 'Call it a Python dictionary unless you are working with encoded JSON text.'}],
                        'detailed_explanation': ('A nested collection contains another collection as an item. A grid can be a list of lists: grid '
 "= [['A', 'B'], ['C', 'D']]. The outer list stores rows; each inner list stores its cells. To get "
 "B, Python first evaluates grid[0] and gets ['A', 'B']; then [1] selects B. So grid[0][1] means "
 'first row, second cell.\n'
 '\n'
 "A list of dictionaries stores ordered records. In students[0]['name'], the first bracket selects "
 'the first dictionary; the second asks that dictionary for the value under name. Read from the '
 'outside inward and keep track of what each expression returns.\n'
 '\n'
 'Lists are useful for ordered groups; dictionaries label the fields in a record. Nested '
 'structures combine those jobs. JSON is a text format for exchanging data. It resembles Python '
 'lists and dictionaries, but JSON text is not itself a Python dictionary; it must be parsed into '
 'Python values before normal dictionary access.\n'
 '\n'
 'An inner list is still mutable. Changing it changes the object stored inside the outer list. '
 'When a nested expression looks confusing, evaluate one bracket at a time and name the '
 'intermediate row or record.'),
                        'expected_output': 'B',
                        'introduction': ('A game board has rows and columns, while a class roster has records with names and scores. One '
 'flat sequence cannot clearly represent all of these layers. Nested collections keep related '
 'groups together and let you select one level at a time.'),
                        'learning_objectives': ['Read a cell from a list of lists one level at a time.',
 'Read a field from a dictionary inside a list.',
 'Explain the job of each nested layer.',
 'Distinguish a Python dictionary/list from serialized JSON text.',
 'Predict how an inner mutable list changes the containing structure.'],
                        'line_by_line': [{'line': '1',
  'code': "grid = [['A', 'B'], ['C', 'D']]",
  'explanation': 'Create an outer list with two inner row lists.'},
 {'line': '2',
  'code': 'print(grid[0][1])',
  'explanation': 'grid[0] selects the first row; [1] selects the second value in that row.'}],
                        'practical_examples': [{'title': 'Read one grid cell',
  'code': "grid = [['A', 'B'], ['C', 'D']]\nprint(grid[0][1])",
  'explanation': "grid[0] returns the first row ['A', 'B']; [1] then selects that row's second "
                 'cell, B.',
  'output': 'B'},
 {'title': 'Read fields from student records',
  'code': 'students = [\n'
          "    {'name': 'Mia', 'score': 92},\n"
          "    {'name': 'Kai', 'score': 85}\n"
          ']\n'
          "print(students[0]['name'])\n"
          "print(students[1]['score'])",
  'explanation': 'The list index selects a record. The dictionary key inside that record selects a '
                 'labeled field.',
  'output': 'Mia\n85'},
 {'title': 'Visit each cell row by row',
  'code': 'grid = [[1, 2], [3, 4]]\nfor row in grid:\n    for cell in row:\n        print(cell)',
  'explanation': 'The outer loop selects a row; the inner loop visits each value in that row '
                 'before the next row begins.',
  'output': '1\n2\n3\n4'}],
                        'practice_questions': ["What is board[1][0] for [['A', 'B'], ['C', 'D']]? Check: C.",
 "In students[0]['score'], what does 0 select? Check: the first record.",
 'Why place dictionaries inside a list of student records? Check: the list orders records; keys '
 "label each record's fields.",
 'Is JSON text automatically a Python dictionary? Check: no; it must be parsed.'],
                        'prerequisites': ('Know lists, indexes, dictionaries, and keys. A nested collection stores a familiar list or '
 'dictionary inside another collection.'),
                        'real_world_apps': ('A board game can store rows in a list of lists. A roster can store student dictionaries in an '
 'outer list. A web service may send JSON text that gets parsed into Python lists and '
 'dictionaries.'),
                        'summary': ('Nested collections put familiar structures inside other structures. Select the outer row or '
 'record first, then its inner value. Lists hold ordered groups; dictionaries label fields. Python '
 'dictionaries are not the same thing as JSON text.'),
                        'syntax_breakdown': ('grid[row_index][column_index]\n'
 "students[record_index]['name']\n"
 '# First choose a row or record.\n'
 '# Then choose an item or labeled field inside it.\n'
 'for row in grid:\n'
 '    for cell in row:\n'
 '        print(cell)'),
                        'terminology': [{'term': 'Nested collection', 'definition': 'A collection stored inside another collection.'},
 {'term': '2D list',
  'definition': 'A list of row lists; one index selects a row and another selects a cell.'},
 {'term': 'Record', 'definition': 'Related fields, often stored in a dictionary under clear keys.'},
 {'term': 'Outer collection', 'definition': 'The first container selected during nested access.'},
 {'term': 'JSON',
  'definition': 'A text format for structured data, distinct from a live Python dictionary.'}]},
             'number': 61,
             'quizzes': [{'explanation': "data['players'][1] selects the second player dict {'name': 'Sam', "
                                         "...}, and ['name'] returns 'Sam'.",
                          'options': [{'explanation': 'Correct! Index 1 corresponds to Sam.',
                                       'is_correct': True,
                                       'text': 'Sam'},
                                      {'explanation': 'Incorrect. Alex is at index 0.',
                                       'is_correct': False,
                                       'text': 'Alex'},
                                      {'explanation': "Incorrect. That is ['score'].",
                                       'is_correct': False,
                                       'text': '95'},
                                      {'explanation': 'Incorrect. All keys and indices exist.',
                                       'is_correct': False,
                                       'text': 'KeyError'}],
                          'question': 'What is the output of the nested structure lookup?\n'
                                      '\n'
                                      "data = {'players': [{'name': 'Alex', 'score': 90}, {'name': 'Sam', "
                                      "'score': 95}]}\n"
                                      "print(data['players'][1]['name'])"},
                         {'explanation': "The 'players' list contains 2 dictionary elements.",
                          'options': [{'explanation': 'Correct! There are 2 player dicts in the list.',
                                       'is_correct': True,
                                       'text': '2'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '4'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '1'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': "What will be printed by: print(len(data['players']))?"}],
             'title': 'Nested Collections (2D Data & JSON Models)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a line of menu choices.\n2. Use enumerate() to print each choice with a number, starting at 1.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['choices = input().split()\n'
 'for number, choice in enumerate(choices, start=1):\n'
 "    print(f'{number}. {choice}')"],
                             'initial_code': '# Frequency Counting with collections.Counter\n'
                                             'from collections import Counter\n'
                                             '# Step 1: Read words:\n'
                                             'words = input().split()\n'
                                             '\n'
                                             '# Step 2: Find and print most common word below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'For Start Settings Quit, print 1. Start, 2. Settings, and 3. Quit on separate lines.',
                             'solution_code': ('choices = input().split()\n'
 'for number, choice in enumerate(choices, start=1):\n'
 "    print(f'{number}. {choice}')"),
                             'test_cases': [{'input_data': 'Start Settings Quit\n',
  'expected_output': '1. Start\n2. Settings\n3. Quit',
  'is_hidden': False},
 {'input_data': 'Play Help\n', 'expected_output': '1. Play\n2. Help', 'is_hidden': False}],
                             'title': 'Numbered Menu with enumerate()',
                             'xp_reward': 35},
                            {'description': ('Your task, step by step:\n1. Read names on the first line and matching scores on the second.\n2. Use zip() to pair items in the same positions, then print each name with its score.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.'),
                             'difficulty': 'boss',
                             'hints': ['names = input().split()\n'
 'scores = input().split()\n'
 'for name, score in zip(names, scores):\n'
 "    print(f'{name}: {score}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Grouping with defaultdict\n'
                                             'from collections import defaultdict\n'
                                             '# Step 1: Initialize d = defaultdict(list)\n'
                                             '# Step 2: Read n pairs and group:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'For Mia Kai and 8 10, print Mia: 8 and Kai: 10 on separate lines.',
                             'solution_code': ('names = input().split()\n'
 'scores = input().split()\n'
 'for name, score in zip(names, scores):\n'
 "    print(f'{name}: {score}')"),
                             'test_cases': [{'input_data': 'Mia Kai\n8 10\n', 'expected_output': 'Mia: 8\nKai: 10', 'is_hidden': False},
 {'input_data': 'Ada Bo Lin\n7 9 8\n',
  'expected_output': 'Ada: 7\nBo: 9\nLin: 8',
  'is_hidden': False}],
                             'title': 'Boss Challenge: Pair Names and Scores with zip()',
                             'xp_reward': 150}],
             'description': 'Loop through items with their positions or pair matching lists.',
             'lesson': {'common_mistakes': [{'mistake': 'Expecting enumerate(items) to begin at 1.',
  'why': 'The default start is 0.',
  'fix': 'Use enumerate(items, start=1) for human-facing numbering.'},
 {'mistake': 'Pairing lists that are in different orders.',
  'why': 'zip matches positions and cannot know which values belong together.',
  'fix': 'Keep both lists aligned or store each record together.'},
 {'mistake': 'Expecting zip() to reject lists of different lengths.',
  'why': 'zip stops quietly at the shortest iterable.',
  'fix': 'Compare lengths first when matching counts are required.'},
 {'mistake': 'Using pair[0] and pair[1] everywhere in the loop.',
  'why': 'The code hides what each value means.',
  'fix': 'Unpack with for name, score in zip(names, scores).'}],
                        'detailed_explanation': ('A for loop visits items one by one. enumerate(items) pairs each item with a count: by default '
 'the first count is 0. Use enumerate(items, start=1) when people expect numbering to begin at 1. '
 'The loop can unpack each pair: for number, choice in enumerate(choices, start=1):.\n'
 '\n'
 'zip(names, scores) pairs values by position: first name with first score, second with second, '
 'and so on. for name, score in zip(names, scores): unpacks each pair. The lists must be in '
 'corresponding order for the pairing to make sense.\n'
 '\n'
 'zip() stops when the shortest input runs out. If there are three names and two scores, it makes '
 'two pairs and leaves the extra name unused. It does not warn or raise an error. Compare lengths '
 'first if equal counts are required.\n'
 '\n'
 'Use enumerate when one collection needs a count. Use zip when separate collections contain '
 'matching values in the same order. If the order is not trustworthy, keep related values together '
 'in records instead of pairing by position.'),
                        'expected_output': '1. Start\n2. Settings\n3. Quit',
                        'introduction': ('A menu needs numbers beside each choice, and a report needs to match each person with a score. A '
 'loop can visit items, but manual counters and indexes can be easy to misalign. enumerate() and '
 'zip() provide the needed pairs as the loop runs.'),
                        'learning_objectives': ['Use a for loop to visit each item.',
 'Use enumerate() to receive both an item and its count.',
 "Set enumerate()'s starting count with start=.",
 'Use zip() to pair values at matching positions and unpack the pair.',
 'Explain that zip() stops at the shortest input and does not check equal lengths.'],
                        'line_by_line': [{'line': '1',
  'code': "choices = ['Start', 'Settings', 'Quit']",
  'explanation': 'Store menu labels in the order they should appear.'},
 {'line': '2',
  'code': 'for number, choice in enumerate(choices, start=1):',
  'explanation': 'enumerate returns a count beginning at 1 and the current item; unpack the pair '
                 'into number and choice.'},
 {'line': '3',
  'code': "    print(f'{number}. {choice}')",
  'explanation': 'Display one numbered menu line during each loop pass.'}],
                        'practical_examples': [{'title': 'Number menu choices from 1',
  'code': "choices = ['Start', 'Settings', 'Quit']\n"
          'for number, choice in enumerate(choices, start=1):\n'
          "    print(f'{number}. {choice}')",
  'explanation': 'enumerate supplies the count and the choice on each pass. start=1 changes the '
                 'first count from 0 to 1.',
  'output': '1. Start\n2. Settings\n3. Quit'},
 {'title': 'Match names with scores',
  'code': "names = ['Mia', 'Kai']\n"
          'scores = [92, 85]\n'
          'for name, score in zip(names, scores):\n'
          "    print(f'{name}: {score}')",
  'explanation': 'zip matches values in the same positions. Unpacking gives each pair clear names.',
  'output': 'Mia: 92\nKai: 85'},
 {'title': 'zip() stops at the shorter input',
  'code': "names = ['Mia', 'Kai', 'Bo']\n"
          'scores = [92, 85]\n'
          'for name, score in zip(names, scores):\n'
          "    print(f'{name}: {score}')",
  'explanation': 'There are three names but two scores. zip creates two pairs and stops; it does '
                 'not include Bo or report the mismatch.',
  'output': 'Mia: 92\nKai: 85'}],
                        'practice_questions': ['What is the first count from enumerate(names)? Check: 0 unless start is changed.',
 'How do you number from 1? Check: enumerate(menu, start=1).',
 'What pairs come from zip([1, 2, 3], [4, 5])? Check: (1, 4), (2, 5).',
 'What must be true for zip(names, scores) to pair the intended people? Check: both lists must be '
 'in corresponding order.'],
                        'prerequisites': ('Know lists, for loops, and tuple unpacking. Level 56 explained how two values can be assigned to '
 'two loop variables.'),
                        'real_world_apps': ('enumerate() numbers menu options, search results, and report rows. zip() matches names and '
 'scores or products and prices when both collections are in the same order.'),
                        'summary': ('enumerate() adds a count to each item; its default starts at 0. zip() pairs items at matching '
 'positions. Unpack pairs into clear loop variables. zip() stops at the shortest input and does '
 'not validate lengths.'),
                        'syntax_breakdown': ('for number, choice in enumerate(choices, start=1):\n'
 '    print(number, choice)\n'
 '\n'
 'for name, score in zip(names, scores):\n'
 '    print(name, score)\n'
 '# zip stops when the shortest input runs out.'),
                        'terminology': [{'term': 'Iteration', 'definition': 'Repeating an action once for each item in a collection.'},
 {'term': 'enumerate(iterable, start=0)',
  'definition': 'Pairs every item with a count; the default count begins at 0.'},
 {'term': 'zip(a, b)', 'definition': 'Pairs items from several iterables by matching positions.'},
 {'term': 'Unpacking',
  'definition': 'Assigning the parts of each pair to separate loop variables.'},
 {'term': 'Alignment',
  'definition': 'Keeping related values at matching positions in separate collections.'}]},
             'number': 62,
             'quizzes': [{'explanation': "zip pairs elements into ('a', 1) and ('b', 2). dict() converts "
                                         "pairs into {'a': 1, 'b': 2}.",
                          'options': [{'explanation': 'Correct! zip pairs matching index elements into '
                                                      'key-value pairs.',
                                       'is_correct': True,
                                       'text': "{'a': 1, 'b': 2}"},
                                      {'explanation': 'Incorrect. dict() wraps the pairs into a dictionary.',
                                       'is_correct': False,
                                       'text': "[('a', 1), ('b', 2)]"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "{'a': 'b', 1: 2}"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of zip on lists?\n'
                                      '\n'
                                      "keys = ['a', 'b']\n"
                                      'vals = [1, 2]\n'
                                      'print(dict(zip(keys, vals)))'},
                         {'explanation': 'By default, zip() stops at the end of the shortest iterable. It '
                                         "outputs [(1, 'x'), (2, 'y')].",
                          'options': [{'explanation': 'Correct! zip stops when the shortest sequence is '
                                                      'exhausted.',
                                       'is_correct': True,
                                       'text': "[(1, 'x'), (2, 'y')]"},
                                      {'explanation': 'Incorrect. That requires itertools.zip_longest().',
                                       'is_correct': False,
                                       'text': "[(1, 'x'), (2, 'y'), (3, None)]"},
                                      {'explanation': 'Incorrect. zip truncates silently by default.',
                                       'is_correct': False,
                                       'text': 'ValueError: unequal length'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '[]'}],
                          'question': 'What happens when zip() is called on lists of unequal lengths?\n'
                                      '\n'
                                      "print(list(zip([1, 2, 3], ['x', 'y'])))"}],
             'title': 'Iterating Over Collections (enumerate & zip)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Words can repeat and use different capital letters.\n2. Read them, make them lowercase, remove duplicates, sort alphabetically, and print the list.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['words = input().split()\n'
                                       'clean = [w.lower() for w in words]\n'
                                       'unique = sorted(set(clean))\n'
                                       'print(unique)'],
                             'initial_code': '# World 6 Capstone: Vocabulary Deduplicator\n'
                                             '# Step 1: Read words:\n'
                                             'words = input().split()\n'
                                             '\n'
                                             '# Step 2: Lowercase, set(), sorted(), and print below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'For Python python QUEST code quest, print [code, python, '
                                             'quest].',
                             'solution_code': 'words = [word.lower() for word in input().split()]\n'
                                              'print(sorted(set(words)))',
                             'test_cases': [{'input_data': 'Python python QUEST code quest\n',
                                             'expected_output': "['code', 'python', 'quest']",
                                             'is_hidden': False},
                                            {'input_data': 'Apple banana APPLE\n',
                                             'expected_output': "['apple', 'banana']",
                                             'is_hidden': False}],
                             'title': 'World 6 Capstone: Vocabulary Deduplicator',
                             'xp_reward': 50},
                            {'description': 'Your task, step by step:\n1. Read a sentence.\n2. Count each letter, ignoring capital letters and skipping spaces and punctuation.\n3. Print the letter counts in alphabetical order.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['text = input().lower()\n'
 'counts = {}\n'
 'for letter in text:\n'
 "    if letter in 'abcdefghijklmnopqrstuvwxyz':\n"
 '        counts[letter] = counts.get(letter, 0) + 1\n'
 'for letter in sorted(counts):\n'
 "    print(f'{letter}: {counts[letter]}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Character Frequency Histogram\n'
                                             'from collections import Counter\n'
                                             '# Step 1: Read text:\n'
                                             'text = input().strip().lower()\n'
                                             '\n'
                                             '# Step 2: Filter letters, count with Counter, and print sorted '
                                             'items:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'For Hello!, print e: 1, h: 1, l: 2, o: 1.',
                             'solution_code': ('text = input().lower()\n'
 'counts = {}\n'
 'for letter in text:\n'
 "    if letter in 'abcdefghijklmnopqrstuvwxyz':\n"
 '        counts[letter] = counts.get(letter, 0) + 1\n'
 'for letter in sorted(counts):\n'
 "    print(f'{letter}: {counts[letter]}')"),
                             'test_cases': [{'input_data': 'Hello!\n',
                                             'expected_output': 'e: 1\nh: 1\nl: 2\no: 1',
                                             'is_hidden': False},
                                            {'input_data': 'A-bba\n',
                                             'expected_output': 'a: 2\nb: 2',
                                             'is_hidden': False}],
                             'title': 'Character Frequency Histogram',
                             'xp_reward': 250}],
             'description': 'Combine World 6 collections to organize and report information.',
             'lesson': {'common_mistakes': [{'mistake': "Using students['name'] when students is the outer list.",
  'why': 'A list needs an index before a record dictionary can be selected.',
  'fix': "Use students[0]['name'] for the first student's name."},
 {'mistake': 'Using a list for unique course names and expecting repeats to disappear.',
  'why': 'Lists keep duplicates.',
  'fix': 'Gather names in a set, then sort it for display.'},
 {'mistake': 'Dividing by a fixed score count.',
  'why': "A student's number of scores can change.",
  'fix': 'Use len(scores) to count the current scores.'},
 {'mistake': 'Assuming a set prints alphabetically.',
  'why': 'Sets do not promise display order.',
  'fix': 'Use sorted(all_courses).'},
 {'mistake': 'Calling this Python structure JSON.',
  'why': 'The code creates in-memory Python objects; JSON is serialized text with its own syntax.',
  'fix': 'Call it a list of dictionaries unless you encode or decode JSON text.'}],
                        'detailed_explanation': ("Plan the shape of the data first. One student record is a dictionary: the key 'name' labels the "
 "student's name, 'scores' labels a list of scores, and 'courses' labels a list of course names. "
 'The outer students list stores several records in order. Each structure has one job: a list '
 'keeps an ordered group; a dictionary makes fields readable by name; a set removes duplicate '
 'course names.\n'
 '\n'
 'Stage 1: Read one nested value. students[0] selects the first dictionary from the outer list. '
 "students[0]['name'] then selects that dictionary's name. Read one bracket at a time to avoid "
 'mixing up the outer list index and inner dictionary key.\n'
 '\n'
 "Stage 2: Update a record. students[0]['scores'] reaches Mia's score list. append(96) changes "
 'that list by adding one score. The record is a dictionary, and its scores value is a list, so '
 'the nested access follows those two layers.\n'
 '\n'
 'Stage 3: Collect unique courses. set() creates an empty set. The nested loops visit each student '
 "and then each course in that student's course list. add(course) stores each course; if Art "
 'appears again, the set still keeps one Art. A set has no display order, so sorted(all_courses) '
 'creates a predictable ordered list for the report.\n'
 '\n'
 'Stage 4: Calculate and report. enumerate(students, start=1) pairs each student with a count for '
 'the printed report. sum(scores) adds the numbers; len(scores) counts them; dividing the total by '
 'the count gives the average. The program stores intermediate values in names so the final '
 'f-string stays readable. The .1f format displays one digit after the decimal; it does not change '
 'the average variable. join() combines course names with comma-space separators.\n'
 '\n'
 'The complete program stays in memory. It does not save a file or connect to a database. The '
 'dictionaries and lists are Python objects, not JSON text. A real student system would need input '
 'checks, saved storage, privacy protection, and access controls; those topics are beyond World 6. '
 'The small program here teaches how collections can fit together to solve one coherent problem.'),
                        'expected_output': ("Unique courses: ['Art', 'Python', 'Science']\n"
 'Student report:\n'
 '1. Mia - Average: 92.0\n'
 '   Courses: Python, Art\n'
 '2. Kai - Average: 80.0\n'
 '   Courses: Art, Science'),
                        'introduction': ('A teacher wants a small program that stores several student records, adds a score, finds all '
 'courses taught, and prints a readable report. Different parts of the information have different '
 "needs: students stay in order, each student's fields need labels, scores and courses can contain "
 'several values, and course names should be unique in the final catalog. This capstone combines '
 'the right collection for each job.'),
                        'learning_objectives': ['Design a student record as a dictionary with meaningful keys.',
 'Store many records in a list and retrieve nested values from the outside inward.',
 "Update a student's score and calculate an average using sum() and len().",
 'Collect unique course names in a set and sort them for display.',
 'Use enumerate() and f-strings to print a numbered report.',
 'Explain why each collection fits its job and distinguish Python data from JSON text.'],
                        'line_by_line': [{'line': '1',
  'code': 'students = [',
  'explanation': 'Start the outer list that stores records in order.'},
 {'line': '2',
  'code': "    {'name': 'Mia', 'scores': [88, 92], 'courses': ['Python', 'Art']},",
  'explanation': 'The first list item is a dictionary. Its keys label the name, score list, and '
                 'course list.'},
 {'line': '3',
  'code': "    {'name': 'Kai', 'scores': [75, 85], 'courses': ['Art', 'Science']}",
  'explanation': 'The second record uses the same keys, so one report loop can process both '
                 'students.'},
 {'line': '4',
  'code': ']',
  'explanation': 'Close the outer list; it now contains two student dictionaries.'},
 {'line': '5',
  'code': "students[0]['scores'].append(96)",
  'explanation': 'Select the first record, then its scores list, and add 96 to that inner list.'},
 {'line': '6',
  'code': 'all_courses = set()',
  'explanation': 'Create an empty set for course names; repeats will be removed.'},
 {'line': '7',
  'code': 'for student in students:',
  'explanation': 'Visit each student dictionary in the outer list.'},
 {'line': '8',
  'code': "    for course in student['courses']:",
  'explanation': 'For this student, visit each name in the inner courses list.'},
 {'line': '9',
  'code': '        all_courses.add(course)',
  'explanation': 'Add the current course to the set; an existing course is not duplicated.'},
 {'line': '10',
  'code': "print('Unique courses:', sorted(all_courses))",
  'explanation': 'Sort the unique course names and display a predictable list.'},
 {'line': '11',
  'code': "print('Student report:')",
  'explanation': 'Print a heading before the student rows.'},
 {'line': '12',
  'code': 'for number, student in enumerate(students, start=1):',
  'explanation': 'Pair each record with a count beginning at 1, then unpack the pair into number '
                 'and student.'},
 {'line': '13',
  'code': "    scores = student['scores']",
  'explanation': "Retrieve this record's scores list into a short variable name."},
 {'line': '14',
  'code': '    average = sum(scores) / len(scores)',
  'explanation': 'Add the scores, count them, then divide total by count.'},
 {'line': '15',
  'code': "    name = student['name']",
  'explanation': "Retrieve the current student's name from its dictionary."},
 {'line': '16',
  'code': "    course_text = ', '.join(student['courses'])",
  'explanation': 'Join course names into a readable string separated by comma and space.'},
 {'line': '17',
  'code': "    print(f'{number}. {name} - Average: {average:.1f}')",
  'explanation': 'Insert the count and name, and display average with one decimal place.'},
 {'line': '18',
  'code': "    print(f'   Courses: {course_text}')",
  'explanation': 'Display the course string for the same student.'}],
                        'practical_examples': [{'title': 'Complete project: Student Records Management System',
  'code': 'students = [\n'
          "    {'name': 'Mia', 'scores': [88, 92], 'courses': ['Python', 'Art']},\n"
          "    {'name': 'Kai', 'scores': [75, 85], 'courses': ['Art', 'Science']}\n"
          ']\n'
          '\n'
          "# Add a new score to Mia's existing scores list.\n"
          "students[0]['scores'].append(96)\n"
          '\n'
          '# Gather course names; the set keeps each course only once.\n'
          'all_courses = set()\n'
          'for student in students:\n'
          "    for course in student['courses']:\n"
          '        all_courses.add(course)\n'
          '\n'
          "print('Unique courses:', sorted(all_courses))\n"
          "print('Student report:')\n"
          'for number, student in enumerate(students, start=1):\n'
          "    scores = student['scores']\n"
          '    average = sum(scores) / len(scores)\n'
          "    name = student['name']\n"
          "    course_text = ', '.join(student['courses'])\n"
          "    print(f'{number}. {name} - Average: {average:.1f}')\n"
          "    print(f'   Courses: {course_text}')",
  'explanation': "The outer list keeps students ordered. Each dictionary labels one record's "
                 'fields. Scores and courses are inner lists because one student can have several. '
                 'The first nested assignment adds a score to Mia. The nested loops gather each '
                 'course into a set, removing repeats. sorted() makes course output predictable. '
                 'The final loop numbers each student, calculates the average, joins course names, '
                 'and formats each line.',
  'output': "Unique courses: ['Art', 'Python', 'Science']\n"
            'Student report:\n'
            '1. Mia - Average: 92.0\n'
            '   Courses: Python, Art\n'
            '2. Kai - Average: 80.0\n'
            '   Courses: Art, Science'},
 {'title': 'Read and update one student record',
  'code': "student = {'name': 'Mia', 'scores': [88, 92]}\n"
          "print(student['name'])\n"
          "student['scores'].append(96)\n"
          "print(student['scores'])",
  'explanation': 'The name key retrieves Mia. The scores key retrieves an inner list, and append() '
                 'changes that list by adding a score.',
  'output': 'Mia\n[88, 92, 96]'}],
                        'practice_questions': ['Add a third student with name, scores, and courses. Check: use a dictionary with the same three '
 'keys and append it to students.',
 "How do you read Kai's scores in this data? Check: students[1]['scores'].",
 'What average does Mia have after the new score? Check: (88 + 92 + 96) / 3 = 92.0.',
 'The unique course list shows Art twice. What should you inspect? Check: collect names in a set, '
 'then print sorted(all_courses).',
 'Why use both a list and dictionaries? Check: the list orders many records; each dictionary '
 "labels one record's fields.",
 'Extension: Add a new course to Kai and predict how the sorted unique list changes. Check: add it '
 "to Kai's courses list; the set includes it once."],
                        'prerequisites': ('This project uses strings, lists, tuples, sets, dictionaries, nested access, loops, enumerate(), '
 'and f-strings from World 6, plus basic addition, division, sum(), and len(). The steps recap '
 'each tool as it appears.'),
                        'real_world_apps': ('A small gradebook, club roster, or course tracker can store people as a list of records. Each '
 "record's dictionary labels fields; inner lists store multiple scores or courses; a set can build "
 'a unique course catalog. A real school system would also need safe storage and privacy controls.'),
                        'summary': ('A list keeps student records in order; dictionaries label each record; inner lists hold repeated '
 'scores and courses; a set removes duplicate course names. enumerate() numbers the report, '
 'sum()/len() calculate averages, and f-strings format readable output.'),
                        'syntax_breakdown': ('students = [\n'
 "    {'name': 'Mia', 'scores': [88, 92], 'courses': ['Python', 'Art']}\n"
 ']\n'
 '# Outer list -> student dictionary -> inner scores/courses list\n'
 "students[0]['scores'].append(96)\n"
 '\n'
 'for number, student in enumerate(students, start=1):\n'
 "    scores = student['scores']\n"
 '    average = sum(scores) / len(scores)\n'
 '    print(f\'{number}. {student["name"]}: {average:.1f}\')'),
                        'terminology': [{'term': 'Student record',
  'definition': 'A dictionary describing one student with labeled fields.'},
 {'term': 'Nested collection',
  'definition': 'A list or dictionary stored inside another collection.'},
 {'term': 'Unique course',
  'definition': 'A course name included once even if several students take it.'},
 {'term': 'Average', 'definition': 'The sum of scores divided by the number of scores.'},
 {'term': 'Report', 'definition': 'Readable output assembled from stored records.'},
 {'term': 'JSON',
  'definition': 'A text format for exchanging structured data; it is different from the live '
                'Python dictionaries used here.'}]},
             'number': 63,
             'quizzes': [{'explanation': "Maps the first letter w[0] to string length: {'a': 5, 'b': 6, 'c': "
                                         '6}.',
                          'options': [{'explanation': 'Correct! Keys are first letters; values are word '
                                                      'lengths.',
                                       'is_correct': True,
                                       'text': "{'a': 5, 'b': 6, 'c': 6}"},
                                      {'explanation': 'Incorrect. The key expression was w[0].',
                                       'is_correct': False,
                                       'text': "{'apple': 5, 'banana': 6, 'cherry': 6}"},
                                      {'explanation': 'Incorrect. Curly braces produce a dict.',
                                       'is_correct': False,
                                       'text': '[5, 6, 6]'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "{'a', 'b', 'c'}"}],
                          'question': 'What will this dictionary comprehension produce?\n'
                                      '\n'
                                      "words = ['apple', 'banana', 'cherry']\n"
                                      'res = {w[0]: len(w) for w in words}\n'
                                      'print(res)'},
                         {'explanation': 'Calculates frequency counts for each unique element: {1: 1, 2: 2, '
                                         '3: 3}.',
                          'options': [{'explanation': 'Correct! Counts occurrences of each item in the '
                                                      'original list.',
                                       'is_correct': True,
                                       'text': '{1: 1, 2: 2, 3: 3}'},
                                      {'explanation': 'Incorrect. 2 appears twice and 3 appears thrice.',
                                       'is_correct': False,
                                       'text': '{1: 1, 2: 1, 3: 1}'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '[1, 2, 3]'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '6'}],
                          'question': 'What is the output of running this code?\n'
                                      '\n'
                                      'items = [1, 2, 2, 3, 3, 3]\n'
                                      'print({x: items.count(x) for x in set(items)})'}],
             'title': 'World 6 Examination & Capstone: Student Records Management System'}],
 'number': 6,
 'title': 'Strings and Collections'}
