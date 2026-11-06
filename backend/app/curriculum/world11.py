"""
Curriculum module: WORLD_11
Upgraded with pedagogical question scenarios and scaffolded starter code.
"""

WORLD_11 = {'description': 'Deep dive into comprehensions, iterators, generators, closures, decorators, recursion, and '
                'regular expressions.',
 'final_project_desc': 'Architect a streaming log and data transformation pipeline using generators, custom '
                       'decorators, and regular expression parsing.',
 'final_project_title': 'Advanced Data Processing Application',
 'goal': 'Master idiomatic, high-performance, and advanced Python metaprogramming constructs.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Read whole numbers on one line.\n2. Make a new list containing the square of each even number, leaving out odd numbers.\n3. Print the list.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['nums = [int(x) for x in input().split()]\n'
                                       'res = [x * x for x in nums if x % 2 == 0]\n'
                                       'print(res)'],
                             'initial_code': '# Advanced Comprehensions: Mapping and Filtering\n'
                                             '# Step 1: Read numbers:\n'
                                             'nums = [int(x) for x in input().split()]\n'
                                             '\n'
                                             '# Step 2: Compute res = [x * x for x in nums if x % 2 == 0] '
                                             'and print below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'nums = [int(x) for x in input().split()]\n'
                                              'even_squares = [x * x for x in nums if x % 2 == 0]\n'
                                              'print(even_squares)',
                             'test_cases': [{'challenge_id': 1510,
                                             'expected_output': '[4, 16, 36]',
                                             'explanation': '',
                                             'id': 2471,
                                             'input_data': '1 2 3 4 5 6\n',
                                             'is_hidden': 0},
                                            {'challenge_id': 1510,
                                             'expected_output': '[]',
                                             'explanation': '',
                                             'id': 2472,
                                             'input_data': '7 9 11\n',
                                             'is_hidden': 0}],
                             'title': 'Square Evens Comprehension',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use a dictionary comprehension to map every word to its length.\n2. Read the words and print the dictionary.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['words = input().split()\n'
                                       'lengths = {word: len(word) for word in words}\n'
                                       'print(lengths)'],
                             'initial_code': '# ⚔️ Boss Challenge: Dictionary Comprehension\n'
                                             '# Step 1: Read words:\n'
                                             'words = input().split()\n'
                                             '\n'
                                             '# Step 2: d = {w: len(w) for w in words} and print(d) below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'words = input().split()\n'
                                              'lengths = {word: len(word) for word in words}\n'
                                              'print(lengths)',
                             'test_cases': [{'expected_output': "{'cat': 3, 'python': 6}",
                                             'input_data': 'cat python\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Word Length Dictionary',
                             'xp_reward': 150}],
             'description': 'Write concise, expressive, and high-performance collection transformations '
                            'using comprehension syntax.',
             'lesson': {'common_mistakes': [{'fix': 'Limit comprehensions to at most 1 or 2 clauses.',
                                             'mistake': 'Nesting 4 levels of comprehensions into an '
                                                        'unreadable 100-character line',
                                             'why': 'Readability counts! If a comprehension cannot be '
                                                    'understood in 5 seconds, use a standard loop.'}],
                        'detailed_explanation': 'Comprehension Syntax Anatomy:\n'
                                                '`[expression for item in iterable if condition]`\n'
                                                '\n'
                                                '1. List Comprehensions: `[x * 2 for x in nums if x > 0]`\n'
                                                '2. Set Comprehensions: `{x.lower() for x in words}` '
                                                '(automatically deduplicates)\n'
                                                '3. Dictionary Comprehensions: `{k: len(v) for k, v in '
                                                'data.items()}`\n'
                                                '\n'
                                                'Why Comprehensions are Faster:\n'
                                                'Under the hood, Python compiles comprehensions into a '
                                                'specialized bytecode instruction (`LIST_APPEND`) executed '
                                                'directly in C without calling the Python-level `.append()` '
                                                'method lookups repeatedly.',
                        'expected_output': "['alice', 'carol']",
                        'introduction': 'In Python, creating a new list by transforming or filtering an '
                                        'existing one using an explicit 5-line `for` loop with `.append()` '
                                        'is considered unpythonic. Python provides comprehensions — a '
                                        'concise, declarative syntax that expresses the entire operation in '
                                        'a single elegant line that runs faster in C-bytecode.',
                        'learning_objectives': ['Construct list comprehensions with transformation '
                                                'expressions and filtering conditions',
                                                'Build dictionary comprehensions {k: v for ...} and set '
                                                'comprehensions {x for ...}',
                                                'Understand how comprehensions run faster in C-bytecode than '
                                                'equivalent append loops'],
                        'line_by_line': [{'code': 'raw_prices = [10.0, 25.5, 8.0, 50.0]',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': 'discounted = [p * 0.9 for p in raw_prices if p >= 20.0]',
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': "print('Discounted items (>= $20):', discounted)",
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'}],
                        'practical_examples': [{'code': 'raw_prices = [10.0, 25.5, 8.0, 50.0]\n'
                                                        'discounted = [p * 0.9 for p in raw_prices if p >= '
                                                        '20.0]\n'
                                                        "print('Discounted items (>= $20):', discounted)",
                                                'explanation': 'Selects catalog prices >= 20 and applies 10% '
                                                               'discount in a single expression.',
                                                'output': 'Discounted items (>= $20): [22.95, 45.0]',
                                                'title': 'Example 1: Filtering and transforming prices with '
                                                         'list comprehension'},
                                               {'code': "role_to_user = {'admin': 'Alex', 'editor': 'Sam'}\n"
                                                        'user_to_role = {v: k for k, v in '
                                                        'role_to_user.items()}\n'
                                                        "print('Inverted mapping:', user_to_role)",
                                                'explanation': 'Swaps keys and values efficiently using a '
                                                               'dictionary comprehension.',
                                                'output': "Inverted mapping: {'Alex': 'admin', 'Sam': "
                                                          "'editor'}",
                                                'title': 'Example 2: Inverting a dictionary mapping with '
                                                         'dict comprehension'},
                                               {'code': "words = ['cat', 'car', 'dog', 'deer', 'duck']\n"
                                                        'initials = {w[0].upper() for w in words}\n'
                                                        "print('Distinct initial letters:', "
                                                        'sorted(list(initials)))',
                                                'explanation': 'Extracts unique first letters and '
                                                               'automatically discards duplicate entries.',
                                                'output': "Distinct initial letters: ['C', 'D']",
                                                'title': 'Example 3: Extracting first characters with set '
                                                         'comprehension'}],
                        'practice_questions': ['What brackets are used for a dictionary comprehension?',
                                               'Why are list comprehensions faster than standard for-loops '
                                               'with .append()?'],
                        'prerequisites': 'World 10: Object-Oriented Programming',
                        'real_world_apps': 'Data cleaning pipelines, database query result mapping, text '
                                           'tokenization, matrix transpositions.',
                        'summary': 'Comprehensions provide declarative, high-speed construction of lists, '
                                   'sets, and dicts using [expr for item in iter if cond].',
                        'syntax_breakdown': '# Comprehensions: Compact syntax for creating collections:\n'
                                            '# 1. List Comprehension: [expression for item in iterable if '
                                            'condition]\n'
                                            'evens = [x * 2 for x in range(5) if x % 2 == 0]\n'
                                            "print('Even multiples:', evens)\n"
                                            '\n'
                                            '# 2. Dict Comprehension: {k_expr: v_expr for item in iterable}\n'
                                            'squares_map = {n: n**2 for n in range(1, 4)}\n'
                                            "print('Squares map:', squares_map)\n"
                                            '\n'
                                            '# 3. Set Comprehension: {expression for item in iterable}\n'
                                            "unique_lengths = {len(w) for w in ['apple', 'pear', 'banana', "
                                            "'fig']}\n"
                                            "print('Unique word lengths:', unique_lengths)",
                        'terminology': [{'definition': 'A concise syntax for creating collections (lists, '
                                                       'sets, dicts) based on existing iterables.',
                                         'term': 'Comprehension'},
                                        {'definition': 'Specifying WHAT data you want produced rather than '
                                                       'detailing every step of HOW to build it.',
                                         'term': 'Declarative Syntax'},
                                        {'definition': 'An optimized internal Python C-level instruction '
                                                       'powering fast comprehension execution.',
                                         'term': 'LIST_APPEND Bytecode'}]},
             'number': 106,
             'quizzes': [{'explanation': 'Calculates x % 3: 1%3=1, 2%3=2, 3%3=0, 4%3=1, 5%3=2, 6%3=0. The '
                                         'set of unique results is {0, 1, 2}.',
                          'options': [{'explanation': 'Correct! The set comprehension collects the unique '
                                                      'remainders: 0, 1, 2.',
                                       'is_correct': True,
                                       'text': '{0, 1, 2}'},
                                      {'explanation': 'Incorrect. Set comprehension produces a set with '
                                                      'duplicates removed.',
                                       'is_correct': False,
                                       'text': '[1, 2, 0, 1, 2, 0]'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '{1, 2, 3}'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '{0, 1}'}],
                          'question': 'What is the result of `{x % 3 for x in [1, 2, 3, 4, 5, 6]}`?'},
                         {'explanation': 'Maps each number to its square: {2: 4, 3: 9}.',
                          'options': [{'explanation': 'Correct! 2**2 = 4 and 3**2 = 9.',
                                       'is_correct': True,
                                       'text': '{2: 4, 3: 9}'},
                                      {'explanation': 'Incorrect. That is a list comprehension.',
                                       'is_correct': False,
                                       'text': '[4, 9]'},
                                      {'explanation': 'Incorrect. That is a set comprehension.',
                                       'is_correct': False,
                                       'text': '{4, 9}'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '{2: 2, 3: 3}'}],
                          'question': 'What will this dictionary comprehension produce?\n'
                                      '\n'
                                      'print({x: x ** 2 for x in [2, 3]})'}],
             'title': 'List, Dict, and Set Comprehensions'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create an iterator from the words and call next() twice.\n2. Print the first and second word.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['words = input().split()\n'
                                       'iterator = iter(words)\n'
                                       "print(f'First: {next(iterator)}')\n"
                                       "print(f'Second: {next(iterator)}')"],
                             'initial_code': '# Iterators: iter() and next()\n'
                                             '# Step 1: Read words and get iterator:\n'
                                             'words = input().split()\n'
                                             'it = iter(words)\n'
                                             '\n'
                                             '# Step 2: Print next(it) twice below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'words = input().split()\n'
                                              'iterator = iter(words)\n'
                                              "print(f'First: {next(iterator)}')\n"
                                              "print(f'Second: {next(iterator)}')",
                             'test_cases': [{'expected_output': 'First: alpha\nSecond: beta',
                                             'input_data': 'alpha beta gamma\n',
                                             'is_hidden': False}],
                             'title': 'Read an Iterator Step by Step',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Implement an iterator that returns start down to 1.\n2. Convert Countdown(3) to a list and print it.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Countdown:\n'
                                       '    def __init__(self, start):\n'
                                       '        self.current = start\n'
                                       '    def __iter__(self):\n'
                                       '        return self\n'
                                       '    def __next__(self):\n'
                                       '        if self.current <= 0:\n'
                                       '            raise StopIteration\n'
                                       '        value = self.current\n'
                                       '        self.current -= 1\n'
                                       '        return value\n'
                                       'print(list(Countdown(3)))'],
                             'initial_code': '# ⚔️ Boss Challenge: Custom Countdown Iterator Class\n'
                                             '# Step 1: Define Countdown with __iter__ and __next__:\n'
                                             '\n'
                                             '# Step 2: Print list(Countdown(3)) below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Countdown:\n'
                                              '    def __init__(self, start):\n'
                                              '        self.current = start\n'
                                              '    def __iter__(self):\n'
                                              '        return self\n'
                                              '    def __next__(self):\n'
                                              '        if self.current <= 0:\n'
                                              '            raise StopIteration\n'
                                              '        value = self.current\n'
                                              '        self.current -= 1\n'
                                              '        return value\n'
                                              'print(list(Countdown(3)))',
                             'test_cases': [{'expected_output': '[3, 2, 1]',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Countdown Iterator',
                             'xp_reward': 150}],
             'description': 'Understand the inner workings of Python loops with iter(), next(), and the '
                            'StopIteration exception.',
             'lesson': {'common_mistakes': [{'fix': 'Create a fresh iterator by calling iter(collection) '
                                                    'again.',
                                             'mistake': 'Expecting an exhausted iterator to restart '
                                                        'automatically',
                                             'why': 'Iterators are one-way streams. Once exhausted, calling '
                                                    'next() continues raising StopIteration.'}],
                        'detailed_explanation': 'Iterable vs Iterator:\n'
                                                '- Iterable: Any object that can produce an iterator '
                                                '(implements `__iter__()`, like lists, dicts, strings, '
                                                'files).\n'
                                                '- Iterator: The stateful stream object that actually '
                                                'produces values one at a time via `__next__()`.\n'
                                                '\n'
                                                'The Protocol in Action:\n'
                                                '1. Python calls `it = iter(my_list)` to obtain the '
                                                'iterator.\n'
                                                '2. In a loop, it calls `val = next(it)` repeatedly.\n'
                                                '3. When no more items remain, `next(it)` raises the '
                                                '`StopIteration` exception.\n'
                                                '4. The `for` loop catches `StopIteration` and terminates '
                                                'gracefully.\n'
                                                '\n'
                                                'You can provide a default fallback to `next(it, default)` '
                                                'to avoid raising StopIteration.',
                        'expected_output': 'Item: a\nItem: b\nItem: c',
                        'introduction': 'When you write `for item in sequence:`, what is Python actually '
                                        "doing behind the scenes? It doesn't use a numeric index counter! "
                                        'Python uses the universal Iteration Protocol: converting the '
                                        'collection into an Iterator and pulling items one by one with '
                                        '`next()`.',
                        'learning_objectives': ['Distinguish between an Iterable and an Iterator',
                                                'Manually advance iterators using iter() and next()',
                                                'Understand how for loops intercept StopIteration behind the '
                                                'scenes'],
                        'line_by_line': [{'code': "items = ['Alpha', 'Beta']",
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': 'it = iter(items)',
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': 'try:',
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'},
                                         {'code': '    print(next(it))',
                                          'explanation': 'Line 4 instruction execution',
                                          'line': '4'},
                                         {'code': '    print(next(it))',
                                          'explanation': 'Line 5 instruction execution',
                                          'line': '5'},
                                         {'code': '    print(next(it))',
                                          'explanation': 'Line 6 instruction execution',
                                          'line': '6'},
                                         {'code': 'except StopIteration:',
                                          'explanation': 'Line 7 instruction execution',
                                          'line': '7'},
                                         {'code': "    print('Iteration finished.')",
                                          'explanation': 'Line 8 instruction execution',
                                          'line': '8'}],
                        'practical_examples': [{'code': "items = ['Alpha', 'Beta']\n"
                                                        'it = iter(items)\n'
                                                        'try:\n'
                                                        '    print(next(it))\n'
                                                        '    print(next(it))\n'
                                                        '    print(next(it))\n'
                                                        'except StopIteration:\n'
                                                        "    print('Iteration finished.')",
                                                'explanation': 'Demonstrates the underlying mechanism of '
                                                               'Python for loops.',
                                                'output': 'Alpha\nBeta\nIteration finished.',
                                                'title': 'Example 1: Manual traversal using next() and '
                                                         'StopIteration'},
                                               {'code': 'class Countdown:\n'
                                                        '    def __init__(self, start):\n'
                                                        '        self.val = start\n'
                                                        '    def __iter__(self):\n'
                                                        '        return self\n'
                                                        '    def __next__(self):\n'
                                                        '        if self.val <= 0:\n'
                                                        '            raise StopIteration\n'
                                                        '        curr = self.val\n'
                                                        '        self.val -= 1\n'
                                                        '        return curr\n'
                                                        'print(list(Countdown(3)))',
                                                'explanation': 'Implements __iter__ and __next__ directly to '
                                                               'build an iterable class.',
                                                'output': '[3, 2, 1]',
                                                'title': 'Example 2: Custom Countdown Iterator class'},
                                               {'code': "s = 'Quest'\n"
                                                        "print('String is iterable:', hasattr(s, "
                                                        "'__iter__'))",
                                                'explanation': 'Checks for the presence of the __iter__ '
                                                               'magic method.',
                                                'output': 'String is iterable: True',
                                                'title': 'Example 3: Inspecting iterable nature with '
                                                         'hasattr'}],
                        'practice_questions': ['What exception signals that an iterator has no more '
                                               'elements?',
                                               'How do you get an iterator from a list `my_list`?'],
                        'prerequisites': 'Level 106: List, Dict, and Set Comprehensions',
                        'real_world_apps': 'Streaming data chunks from AWS S3, reading database cursors '
                                           'row-by-row, infinite sequence generators.',
                        'summary': 'Iterables produce iterators with iter(). Iterators produce elements with '
                                   'next() until raising StopIteration.',
                        'syntax_breakdown': '# Iterators and the Iteration Protocol:\n'
                                            '# 1. An iterable implements __iter__() (e.g. list, tuple, '
                                            'string)\n'
                                            '# 2. An iterator implements __next__()\n'
                                            'numbers = [10, 20, 30]\n'
                                            'it = iter(numbers)\n'
                                            '\n'
                                            "print('First item:', next(it))\n"
                                            "print('Second item:', next(it))\n"
                                            "print('Third item:', next(it))\n"
                                            '# Calling next(it) again raises StopIteration to signal the '
                                            'end!',
                        'terminology': [{'definition': 'An object capable of returning its members one at a '
                                                       'time, implementing the __iter__() method.',
                                         'term': 'Iterable'},
                                        {'definition': 'An object representing a stream of data that returns '
                                                       'successive items via __next__().',
                                         'term': 'Iterator'},
                                        {'definition': "The built-in exception raised by an iterator's "
                                                       '__next__() method to signal that no further items '
                                                       'remain.',
                                         'term': 'StopIteration'}]},
             'number': 107,
             'quizzes': [{'explanation': 'iter() returns an iterator; successive next() calls yield 10 then '
                                         '20.',
                          'options': [{'explanation': 'Correct! next() steps through the iterator elements.',
                                       'is_correct': True,
                                       'text': '10 20'},
                                      {'explanation': 'Incorrect. Iterators advance with each next() call.',
                                       'is_correct': False,
                                       'text': '10 10'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '20 10'},
                                      {'explanation': 'Incorrect. Elements exist for both calls.',
                                       'is_correct': False,
                                       'text': 'StopIteration'}],
                          'question': 'What is the output of the iterator protocol functions?\n'
                                      '\n'
                                      'it = iter([10, 20])\n'
                                      'print(next(it), next(it))'},
                         {'explanation': 'When an iterator is exhausted, next() raises a StopIteration '
                                         'exception.',
                          'options': [{'explanation': 'Correct! StopIteration signals completion of '
                                                      'iteration.',
                                       'is_correct': True,
                                       'text': 'It raises a StopIteration exception'},
                                      {'explanation': 'Incorrect. Unless a default is passed like next(it, '
                                                      'None).',
                                       'is_correct': False,
                                       'text': 'It returns None'},
                                      {'explanation': 'Incorrect. Iterators are one-way streams.',
                                       'is_correct': False,
                                       'text': 'It loops back to the beginning'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It raises IndexError'}],
                          'question': 'What happens when you call `next(it)` on an iterator that has reached '
                                      'the end of its data?'}],
             'title': 'Iterators and the Iteration Protocol'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use yield to produce even numbers up to a limit.\n2. Print the list of values from the generator.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def even_numbers(limit):\n'
                                       '    for number in range(2, limit + 1, 2):\n'
                                       '        yield number\n'
                                       'print(list(even_numbers(int(input()))))'],
                             'initial_code': '# Generators and yield\n'
                                             '# Step 1: Define generator even_numbers(max_limit):\n'
                                             '\n'
                                             '# Step 2: Print list(even_numbers(int(input()))) below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def even_numbers(limit):\n'
                                              '    for number in range(2, limit + 1, 2):\n'
                                              '        yield number\n'
                                              'print(list(even_numbers(int(input()))))',
                             'test_cases': [{'expected_output': '[2, 4, 6]',
                                             'input_data': '6\n',
                                             'is_hidden': False}],
                             'title': 'Collect Values from a Generator',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Generate Fibonacci numbers lazily.\n2. Read how many values to show and print those values as a list.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def fibonacci():\n'
                                       '    first, second = 0, 1\n'
                                       '    while True:\n'
                                       '        yield first\n'
                                       '        first, second = second, first + second\n'
                                       'count = int(input())\n'
                                       'sequence = fibonacci()\n'
                                       'print([next(sequence) for _ in range(count)])'],
                             'initial_code': '# ⚔️ Boss Challenge: Infinite Fibonacci Stream\n'
                                             '# Step 1: Define infinite fibonacci_stream():\n'
                                             '\n'
                                             '# Step 2: Fetch n elements using next(gen):\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def fibonacci():\n'
                                              '    first, second = 0, 1\n'
                                              '    while True:\n'
                                              '        yield first\n'
                                              '        first, second = second, first + second\n'
                                              'count = int(input())\n'
                                              'sequence = fibonacci()\n'
                                              'print([next(sequence) for _ in range(count)])',
                             'test_cases': [{'expected_output': '[0, 1, 1, 2, 3, 5, 8]',
                                             'input_data': '7\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Fibonacci Generator',
                             'xp_reward': 150}],
             'description': 'Produce lazy, memory-efficient streams of data using generator functions and '
                            'yield.',
             'lesson': {'common_mistakes': [{'fix': 'Create gen = my_gen() once, then advance gen.',
                                             'mistake': 'Calling the generator function inside a loop: for x '
                                                        'in my_gen():',
                                             'why': 'If you re-call my_gen() inside a while loop, you create '
                                                    'a brand-new generator each iteration rather than '
                                                    'advancing the existing one.'}],
                        'detailed_explanation': 'The Magic of `yield`:\n'
                                                'When a function contains the `yield` keyword, it becomes a '
                                                'Generator Function. Calling it does NOT run the code; it '
                                                'returns a generator object.\n'
                                                '\n'
                                                'How Execution Pauses and Resumes:\n'
                                                '1. When `next(gen)` is called, execution starts and runs '
                                                'until it hits `yield value`.\n'
                                                '2. It hands `value` back to the caller and FREEZES its '
                                                'execution state (all local variables and instruction '
                                                'pointer are preserved in memory!).\n'
                                                '3. When `next(gen)` is called again, execution unfreezes '
                                                'right on the line after `yield` and continues until the '
                                                'next `yield`.\n'
                                                '4. When the function returns, it automatically raises '
                                                '`StopIteration`.',
                        'expected_output': 'ID_100\nID_101',
                        'introduction': 'What if you need to calculate the first 10,000,000 Fibonacci '
                                        'numbers? Generating a list of 10 million numbers requires gigabytes '
                                        'of RAM and takes seconds to compute before you can even look at the '
                                        'first number. A Generator creates numbers on demand, one at a time, '
                                        'consuming virtually zero memory!',
                        'learning_objectives': ['Define generator functions using the yield keyword',
                                                'Understand execution pausing and resumption in generators',
                                                'Leverage lazy evaluation to process massive data with '
                                                'near-zero memory footprint'],
                        'line_by_line': [{'code': 'def even_numbers(limit):',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': '    n = 0',
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': '    while n < limit:',
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'},
                                         {'code': '        yield n',
                                          'explanation': 'Line 4 instruction execution',
                                          'line': '4'},
                                         {'code': '        n += 2',
                                          'explanation': 'Line 5 instruction execution',
                                          'line': '5'},
                                         {'code': 'for e in even_numbers(6):',
                                          'explanation': 'Line 6 instruction execution',
                                          'line': '6'},
                                         {'code': "    print('Even:', e)",
                                          'explanation': 'Line 7 instruction execution',
                                          'line': '7'}],
                        'practical_examples': [{'code': 'def even_numbers(limit):\n'
                                                        '    n = 0\n'
                                                        '    while n < limit:\n'
                                                        '        yield n\n'
                                                        '        n += 2\n'
                                                        'for e in even_numbers(6):\n'
                                                        "    print('Even:', e)",
                                                'explanation': 'Generates even numbers lazily without '
                                                               'allocating a temporary list.',
                                                'output': 'Even: 0\nEven: 2\nEven: 4',
                                                'title': 'Example 1: Lazy infinite-style sequence generator'},
                                               {'code': 'def fib(n):\n'
                                                        '    a, b = 0, 1\n'
                                                        '    for _ in range(n):\n'
                                                        '        yield a\n'
                                                        '        a, b = b, a + b\n'
                                                        "print('First 5 Fib numbers:', list(fib(5)))",
                                                'explanation': 'yield generates sequential terms of the '
                                                               'Fibonacci recurrence.',
                                                'output': 'First 5 Fib numbers: [0, 1, 1, 2, 3]',
                                                'title': 'Example 2: Fibonacci generator stream'},
                                               {'code': 'def read_logs():\n'
                                                        "    yield 'LOG: System boot'\n"
                                                        "    yield 'LOG: Engine check OK'\n"
                                                        'for entry in read_logs():\n'
                                                        '    print(entry)',
                                                'explanation': 'Yields log strings one by one to keep memory '
                                                               'footprint flat.',
                                                'output': 'LOG: System boot\nLOG: Engine check OK',
                                                'title': 'Example 3: Streaming large simulated log records'}],
                        'practice_questions': ['What keyword turns a normal Python function into a '
                                               'generator?',
                                               'What happens to local variables in a generator function when '
                                               '`yield` is reached?'],
                        'prerequisites': 'Level 107: Iterators and the Iteration Protocol',
                        'real_world_apps': 'Reading multi-gigabyte log files line by line, stream processing '
                                           'real-time IoT sensor readings, generating infinite math '
                                           'sequences.',
                        'summary': 'yield turns functions into generators. They emit values lazily and pause '
                                   'execution, preserving memory.',
                        'syntax_breakdown': "# Generators and the 'yield' Keyword:\n"
                                            '# Generators produce values ONE AT A TIME on demand (lazy '
                                            'evaluation).\n'
                                            '# Saves immense memory compared to building large lists in '
                                            'RAM!\n'
                                            'def countdown_gen(start):\n'
                                            '    while start > 0:\n'
                                            '        yield start  # Pauses execution and yields value to '
                                            'caller\n'
                                            '        start -= 1\n'
                                            '\n'
                                            'for count in countdown_gen(3):\n'
                                            "    print('Countdown:', count)",
                        'terminology': [{'definition': 'A function that uses yield to produce a sequence of '
                                                       'values lazily on demand.',
                                         'term': 'Generator Function'},
                                        {'definition': 'A Python keyword that pauses function execution, '
                                                       'emits a value to the caller, and remembers the '
                                                       'execution state.',
                                         'term': 'yield'},
                                        {'definition': 'An evaluation strategy that delays the computation '
                                                       'of a value until it is actually needed.',
                                         'term': 'Lazy Evaluation'}]},
             'number': 108,
             'quizzes': [{'explanation': 'Calling gen() returns a generator object. list() consumes the '
                                         'yielded values: [1, 2].',
                          'options': [{'explanation': 'Correct! list() consumes the generator yields into a '
                                                      'list.',
                                       'is_correct': True,
                                       'text': '[1, 2]'},
                                      {'explanation': 'Incorrect. list() returns a list.',
                                       'is_correct': False,
                                       'text': '(1, 2)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '[None, None]'},
                                      {'explanation': 'Incorrect. list(...) consumes the generator.',
                                       'is_correct': False,
                                       'text': '<generator object gen...>'}],
                          'question': 'What is the output of this generator function?\n'
                                      '\n'
                                      'def gen():\n'
                                      '    yield 1\n'
                                      '    yield 2\n'
                                      '\n'
                                      'print(list(gen()))'},
                         {'explanation': 'yield pauses function execution, saves its state, and yields the '
                                         'value to the caller until next() is called again.',
                          'options': [{'explanation': 'Correct! Execution pauses and resumes on the next() '
                                                      'call.',
                                       'is_correct': True,
                                       'text': 'It yields the value and pauses execution, preserving its '
                                               'local state'},
                                      {'explanation': 'Incorrect. yield pauses rather than terminates.',
                                       'is_correct': False,
                                       'text': 'It permanently terminates the function like return'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It converts the function into a list'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It clears all local variables'}],
                          'question': 'What happens when a generator function encounters a `yield` '
                                      'statement?'}],
             'title': 'Generators and the yield Keyword'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a limit.\n2. Use a generator expression to make the squares from 1 up to that limit as sum needs them, then print their total.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['limit = int(input())\n'
                                       'total = sum(x * x for x in range(1, limit + 1))\n'
                                       'print(total)'],
                             'initial_code': '# Generator Expressions for Memory Efficiency\n'
                                             '# Step 1: Read limit:\n'
                                             'limit = int(input())\n'
                                             '\n'
                                             '# Step 2: Compute sum(x * x for x in range(1, limit + 1)) and '
                                             'print:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'limit = int(input())\n'
                                              'total = sum(x * x for x in range(1, limit + 1))\n'
                                              "print(f'Sum of Squares: {total}')",
                             'test_cases': [{'challenge_id': 1516,
                                             'expected_output': 'Sum of Squares: 55',
                                             'explanation': '',
                                             'id': 2483,
                                             'input_data': '5\n',
                                             'is_hidden': 0},
                                            {'challenge_id': 1516,
                                             'expected_output': 'Sum of Squares: 385',
                                             'explanation': '',
                                             'id': 2484,
                                             'input_data': '10\n',
                                             'is_hidden': 0}],
                             'title': 'Lazy Sum of Squares',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use any() with a generator expression to check whether any entered number is negative.\n\nInput for this example: The Input box shows 4 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['count = int(input())\n'
                                       'numbers = [int(input()) for _ in range(count)]\n'
                                       'contains_negative = any(number < 0 for number in numbers)\n'
                                       "print(f'Contains negative: {contains_negative}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Short-Circuiting Stream Validator\n'
                                             '# Step 1: Read numbers:\n'
                                             'count = int(input())\n'
                                             'nums = [int(input()) for _ in range(count)]\n'
                                             '\n'
                                             '# Step 2: Check any(x < 0 for x in nums) and print:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'count = int(input())\n'
                                              'numbers = [int(input()) for _ in range(count)]\n'
                                              'contains_negative = any(number < 0 for number in numbers)\n'
                                              "print(f'Contains negative: {contains_negative}')",
                             'test_cases': [{'expected_output': 'Contains negative: False',
                                             'input_data': '3\n2\n4\n6\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Contains negative: True',
                                             'input_data': '3\n2\n-4\n5\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Check for Negative Numbers',
                             'xp_reward': 150}],
             'description': 'Choose between eager list allocation with [] and lazy generator evaluation with '
                            '().',
             'lesson': {'common_mistakes': [{'fix': 'Remember () = Generator expression; tuple() = Tuple.',
                                             'mistake': 'Thinking (x for x in items) creates a tuple',
                                             'why': 'Parentheses in comprehensions create a GENERATOR, not a '
                                                    'tuple! To create a tuple, use tuple(x for x in '
                                                    'items).'}],
                        'detailed_explanation': 'List Comprehension vs Generator Expression:\n'
                                                '- List Comprehension: `[x * 2 for x in range(1000000)]`\n'
                                                '  EAGER: Allocates a 1,000,000-element list in RAM '
                                                'immediately (~8 MB of memory).\n'
                                                '- Generator Expression: `(x * 2 for x in range(1000000))`\n'
                                                '  LAZY: Allocates only a lightweight generator object in '
                                                'RAM (~100 bytes of memory). Numbers are calculated one at a '
                                                'time as requested.\n'
                                                '\n'
                                                'Aggregator Optimization:\n'
                                                'When passing a generator expression as the ONLY argument to '
                                                'a function like `sum()` or `any()`, you can omit the outer '
                                                'parentheses:\n'
                                                '`total = sum(x**2 for x in range(1000))`.',
                        'expected_output': 'List memory: 8856 bytes\n'
                                           'Gen memory:  104 bytes\n'
                                           'Gen is smaller: True',
                        'introduction': 'Did you know that changing square brackets `[]` to parentheses `()` '
                                        'turns a list comprehension into a generator expression? This simple '
                                        "syntax difference can reduce your program's memory consumption from "
                                        '800 Megabytes down to 100 Bytes!',
                        'learning_objectives': ['Construct generator expressions using parentheses: (x for x '
                                                'in iterable)',
                                                'Compare memory usage between eager list comprehensions and '
                                                'lazy generator expressions using sys.getsizeof()',
                                                'Pass generator expressions directly into aggregators like '
                                                'sum(), min(), max()'],
                        'line_by_line': [{'code': 'total_squares = sum(x**2 for x in range(1, 5))',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': "print('Sum of 1^2 + 2^2 + 3^2 + 4^2:', total_squares)",
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'}],
                        'practical_examples': [{'code': 'total_squares = sum(x**2 for x in range(1, 5))\n'
                                                        "print('Sum of 1^2 + 2^2 + 3^2 + 4^2:', "
                                                        'total_squares)',
                                                'explanation': 'Omitting enclosing brackets inside sum() '
                                                               'feeds items lazily without creating a list.',
                                                'output': 'Sum of 1^2 + 2^2 + 3^2 + 4^2: 30',
                                                'title': 'Example 1: Passing generator expressions directly '
                                                         'into sum()'},
                                               {'code': "data = ['cat', 'apple', 'banana']\n"
                                                        'first_a = next(w for w in data if '
                                                        "w.startswith('a'))\n"
                                                        'print(\'First word starting with "a":\', first_a)',
                                                'explanation': 'Halts evaluation the moment the predicate '
                                                               'matches, avoiding scanning the rest.',
                                                'output': 'First word starting with "a": apple',
                                                'title': 'Example 2: Finding first matching item with '
                                                         'next()'},
                                               {'code': 'gen = (n for n in range(5))\n'
                                                        "print('Type:', type(gen).__name__)\n"
                                                        "print('First value:', next(gen))",
                                                'explanation': 'Shows generator expression type and '
                                                               'on-demand item extraction.',
                                                'output': 'Type: generator\nFirst value: 0',
                                                'title': 'Example 3: Memory comparison between list and '
                                                         'generator'}],
                        'practice_questions': ['What type of object does `(x for x in range(5))` create?',
                                               'When can you omit the outer parentheses of a generator '
                                               'expression?'],
                        'prerequisites': 'Level 108: Generators and the yield Keyword',
                        'real_world_apps': 'Calculating sums of massive CSV datasets, checking any()/all() '
                                           'condition matches that terminate early on first True.',
                        'summary': 'Use [] when you need indexing, sorting, or multiple passes. Use () for '
                                   'lazy, single-pass stream processing with minimal memory.',
                        'syntax_breakdown': '# Generator Expressions vs List Comprehensions:\n'
                                            '# List comprehension: [x for x in data] -> builds FULL list '
                                            'immediately in memory\n'
                                            '# Generator expression: (x for x in data) -> returns a '
                                            'generator object (lazy!)\n'
                                            'import sys\n'
                                            '\n'
                                            'list_comp = [x * 2 for x in range(1000)]\n'
                                            'gen_exp = (x * 2 for x in range(1000))\n'
                                            '\n'
                                            "print('List comp size in bytes:', sys.getsizeof(list_comp))\n"
                                            "print('Gen exp size in bytes:  ', sys.getsizeof(gen_exp))",
                        'terminology': [{'definition': 'A high-performance generator constructed using '
                                                       'comprehension syntax enclosed in parentheses ().',
                                         'term': 'Generator Expression'},
                                        {'definition': 'Computing and storing all results in memory '
                                                       'immediately upfront.',
                                         'term': 'Eager Evaluation'},
                                        {'definition': 'A standard library function that returns the size of '
                                                       'an object in memory in bytes.',
                                         'term': 'sys.getsizeof()'}]},
             'number': 109,
             'quizzes': [{'explanation': 'Parentheses surrounding a comprehension create a generator '
                                         'expression, not a tuple.',
                          'options': [{'explanation': 'Correct! Parentheses form a lazy generator '
                                                      'expression.',
                                       'is_correct': True,
                                       'text': 'A generator expression object'},
                                      {'explanation': 'Incorrect. To create a tuple, use tuple(...).',
                                       'is_correct': False,
                                       'text': 'A tuple of 10 integers'},
                                      {'explanation': 'Incorrect. Lists use square brackets [].',
                                       'is_correct': False,
                                       'text': 'A list comprehension'},
                                      {'explanation': 'Incorrect. Generator expressions are valid syntax.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What is created by the expression `gen = (x * 2 for x in '
                                      'range(10))`?'},
                         {'explanation': 'The generator expression evaluates lazily and short-circuits on '
                                         'the first match without building a full list in memory.',
                          'options': [{'explanation': 'Correct! Lazy evaluation stops immediately when any() '
                                                      'finds a match.',
                                       'is_correct': True,
                                       'text': 'The generator evaluates lazily and short-circuits on the '
                                               'first True without allocating the entire list'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Generators run on the GPU'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'The square bracket syntax causes an overflow error'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'List comprehensions cannot be passed to any()'}],
                          'question': 'Why is `any(x > 100 for x in stream)` faster than `any([x > 100 for x '
                                      'in stream])` on large data?'}],
             'title': 'Generator Expressions vs List Comprehensions'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Write make_power(exponent), which returns a function remembering the exponent.\n2. Use it to print the square and cube of 3.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def make_power(exponent):\n'
                                       '    def power(number):\n'
                                       '        return number ** exponent\n'
                                       '    return power\n'
                                       'square = make_power(2)\n'
                                       'cube = make_power(3)\n'
                                       'print(square(3))\n'
                                       'print(cube(3))'],
                             'initial_code': '# Function Factories and Closures\n'
                                             '# Step 1: Define make_power(exponent):\n'
                                             '\n'
                                             '# Step 2: Create square and cube closures and test below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def make_power(exponent):\n'
                                              '    def power(number):\n'
                                              '        return number ** exponent\n'
                                              '    return power\n'
                                              'square = make_power(2)\n'
                                              'cube = make_power(3)\n'
                                              'print(square(3))\n'
                                              'print(cube(3))',
                             'test_cases': [{'expected_output': '9\n27',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Make Square and Cube Closures',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use nonlocal so the returned counter remembers its value.\n2. Start at 5, call it three times, and print each value.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def make_counter(start):\n'
                                       '    value = start\n'
                                       '    def next_value():\n'
                                       '        nonlocal value\n'
                                       '        value += 1\n'
                                       '        return value\n'
                                       '    return next_value\n'
                                       'counter = make_counter(5)\n'
                                       'print(counter())\n'
                                       'print(counter())\n'
                                       'print(counter())'],
                             'initial_code': '# ⚔️ Boss Challenge: Stateful Counter Closure\n'
                                             '# Step 1: Define make_counter with nonlocal count:\n'
                                             '\n'
                                             '# Step 2: Call counter 3 times and print results:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def make_counter(start):\n'
                                              '    value = start\n'
                                              '    def next_value():\n'
                                              '        nonlocal value\n'
                                              '        value += 1\n'
                                              '        return value\n'
                                              '    return next_value\n'
                                              'counter = make_counter(5)\n'
                                              'print(counter())\n'
                                              'print(counter())\n'
                                              'print(counter())',
                             'test_cases': [{'expected_output': '6\n7\n8',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Remember a Counter Value',
                             'xp_reward': 150}],
             'description': 'Capture enclosing lexical state using nested functions and closures.',
             'lesson': {'common_mistakes': [{'fix': 'Return the function reference without parentheses: '
                                                    'return inner_func.',
                                             'mistake': 'Returning log() with parentheses instead of log',
                                             'why': 'Calling the function immediately executes it rather '
                                                    'than returning the closure function object.'}],
                        'detailed_explanation': 'What is a Closure?\n'
                                                'A closure is an inner function that retains access to '
                                                'variables from its enclosing outer scope, even after the '
                                                'outer function has finished executing.\n'
                                                '\n'
                                                'Criteria for a Closure:\n'
                                                '1. Must have a nested (inner) function.\n'
                                                '2. The inner function must reference a variable from the '
                                                'outer (enclosing) scope.\n'
                                                '3. The outer function must return the inner function object '
                                                'itself.\n'
                                                '\n'
                                                "Python packages the referenced variable into a 'cell' "
                                                'attached to the function '
                                                '(`fn.__closure__[0].cell_contents`). This allows you to '
                                                'generate customized, specialized functions on the fly '
                                                '(function factories).',
                        'expected_output': '[INFO] Server started\n[ERROR] Connection timeout',
                        'introduction': 'Can a function remember a variable even after the outer function '
                                        'that created it has completely finished running and exited? Yes! In '
                                        'Python, this phenomenon is called a Closure. Closures are the '
                                        'conceptual foundation of decorators.',
                        'learning_objectives': ['Understand nested (inner) functions',
                                                'Understand what a Closure is in Python (a function '
                                                'retaining its enclosing scope)',
                                                'Inspect captured closure state using __closure__ and '
                                                'cell_contents'],
                        'line_by_line': [{'code': 'def create_taxer(rate):',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': '    def calculate(subtotal):',
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': '        return subtotal * (1 + rate)',
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'},
                                         {'code': '    return calculate',
                                          'explanation': 'Line 4 instruction execution',
                                          'line': '4'},
                                         {'code': 'calc_state_tax = create_taxer(0.08)',
                                          'explanation': 'Line 5 instruction execution',
                                          'line': '5'},
                                         {'code': "print('Price with 8% tax: $', calc_state_tax(100))",
                                          'explanation': 'Line 6 instruction execution',
                                          'line': '6'}],
                        'practical_examples': [{'code': 'def create_taxer(rate):\n'
                                                        '    def calculate(subtotal):\n'
                                                        '        return subtotal * (1 + rate)\n'
                                                        '    return calculate\n'
                                                        'calc_state_tax = create_taxer(0.08)\n'
                                                        "print('Price with 8% tax: $', calc_state_tax(100))",
                                                'explanation': 'create_taxer locks in rate inside the '
                                                               'enclosed calculate function.',
                                                'output': 'Price with 8% tax: $ 108.0',
                                                'title': 'Example 1: Configurable tax rate calculator '
                                                         'closure'},
                                               {'code': 'def apply_op(a, b, op_func):\n'
                                                        '    return op_func(a, b)\n'
                                                        "print('Addition:', apply_op(10, 5, lambda x, y: x + "
                                                        'y))\n'
                                                        "print('Multiplication:', apply_op(10, 5, lambda x, "
                                                        'y: x * y))',
                                                'explanation': 'Passes callable operation functions '
                                                               'dynamically into apply_op.',
                                                'output': 'Addition: 15\nMultiplication: 50',
                                                'title': 'Example 2: Passing functions as arguments '
                                                         '(Higher-order functions)'},
                                               {'code': 'def make_counter():\n'
                                                        '    count = 0\n'
                                                        '    def inc():\n'
                                                        '        nonlocal count\n'
                                                        '        count += 1\n'
                                                        '        return count\n'
                                                        '    return inc\n'
                                                        'c = make_counter()\n'
                                                        "print('Tick:', c())\n"
                                                        "print('Tick:', c())",
                                                'explanation': 'nonlocal allows the closure to update state '
                                                               'in the outer enclosing function.',
                                                'output': 'Tick: 1\nTick: 2',
                                                'title': 'Example 3: Tracking state with non-local variable '
                                                         'in closure'}],
                        'practice_questions': ['What three criteria define a Python closure?',
                                               'What happens if an outer function returns `inner()` with '
                                               'parentheses instead of `inner`?'],
                        'prerequisites': 'Level 109: Generator Expressions vs List Comprehensions',
                        'real_world_apps': 'Creating customized event listeners, configuring API request '
                                           'wrappers, powering Python decorators.',
                        'summary': 'Closures are inner functions that capture and retain their enclosing '
                                   'scope. They enable function factories and decorators.',
                        'syntax_breakdown': '# Closures and First-Class Functions:\n'
                                            '# 1. Functions are first-class citizens: can be passed as '
                                            'arguments & returned!\n'
                                            '# 2. A closure is an inner function that remembers variables '
                                            'from its enclosing scope:\n'
                                            'def make_multiplier(factor):\n'
                                            '    def multiplier(number):\n'
                                            "        return number * factor  # 'factor' is remembered from "
                                            'enclosing scope!\n'
                                            '    return multiplier\n'
                                            '\n'
                                            'double = make_multiplier(2)\n'
                                            'triple = make_multiplier(3)\n'
                                            "print('Double 5:', double(5))\n"
                                            "print('Triple 5:', triple(5))",
                        'terminology': [{'definition': 'A function object that remembers values in enclosing '
                                                       'scopes even if they are not present in memory.',
                                         'term': 'Closure'},
                                        {'definition': 'The local scope of an outer function enclosing a '
                                                       'nested function.',
                                         'term': 'Enclosing Scope'},
                                        {'definition': 'A pattern where a function creates and returns '
                                                       'customized, specialized function instances.',
                                         'term': 'Function Factory'}]},
             'number': 110,
             'quizzes': [{'explanation': 'adder closes over n = 5. add5(10) returns 10 + 5 = 15.',
                          'options': [{'explanation': 'Correct! The closure retains n = 5 from the enclosing '
                                                      'scope.',
                                       'is_correct': True,
                                       'text': '15'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '10'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '5'},
                                      {'explanation': 'Incorrect. Closures retain enclosing variables.',
                                       'is_correct': False,
                                       'text': 'NameError: n is not defined'}],
                          'question': 'What is the output of the closure snippet?\n'
                                      '\n'
                                      'def make_adder(n):\n'
                                      '    def adder(x):\n'
                                      '        return x + n\n'
                                      '    return adder\n'
                                      '\n'
                                      'add5 = make_adder(5)\n'
                                      'print(add5(10))'},
                         {'explanation': "'nonlocal' allows rebinding of variables in enclosing function "
                                         'scopes.',
                          'options': [{'explanation': "Correct! 'nonlocal' rebinds outer enclosing function "
                                                      'variables.',
                                       'is_correct': True,
                                       'text': 'nonlocal'},
                                      {'explanation': "Incorrect. 'global' binds to module level.",
                                       'is_correct': False,
                                       'text': 'global'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'enclosing'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'outer'}],
                          'question': 'Which Python keyword allows an inner function to modify a variable in '
                                      'its enclosing (outer non-global) scope?'}],
             'title': 'Closures and First-Class Functions'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use @uppercase_result above greet.\n2. The decorator should change the returned text to uppercase.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def uppercase_result(function):\n'
                                       '    def wrapper(name):\n'
                                       '        return function(name).upper()\n'
                                       '    return wrapper\n'
                                       '@uppercase_result\n'
                                       'def greet(name):\n'
                                       "    return f'Hello, {name}!'\n"
                                       'print(greet(input().strip()))'],
                             'initial_code': '# Function Decorators (@decorator)\n'
                                             'from functools import wraps\n'
                                             '# Step 1: Define uppercase_result decorator:\n'
                                             '\n'
                                             '# Step 2: Apply to greet(name) and print greet(input()):\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def uppercase_result(function):\n'
                                              '    def wrapper(name):\n'
                                              '        return function(name).upper()\n'
                                              '    return wrapper\n'
                                              '@uppercase_result\n'
                                              'def greet(name):\n'
                                              "    return f'Hello, {name}!'\n"
                                              'print(greet(input().strip()))',
                             'test_cases': [{'expected_output': 'HELLO, ADA!',
                                             'input_data': 'Ada\n',
                                             'is_hidden': False}],
                             'title': 'Decorate a Function to Uppercase Its Result',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Write a decorator that prints [CALL] compute before calling compute(x).\n2. Print the returned value after the call.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def trace_calls(function):\n'
                                       '    def wrapper(value):\n'
                                       "        print(f'[CALL] {function.__name__}')\n"
                                       '        return function(value)\n'
                                       '    return wrapper\n'
                                       '@trace_calls\n'
                                       'def compute(value):\n'
                                       '    return value * 2\n'
                                       "print('Result:', compute(int(input())))"],
                             'initial_code': '# ⚔️ Boss Challenge: Execution Trace and Metric Logger\n'
                                             'from functools import wraps\n'
                                             '# Step 1: Define trace_calls decorator:\n'
                                             '\n'
                                             '# Step 2: Decorate compute(x) and test below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def trace_calls(function):\n'
                                              '    def wrapper(value):\n'
                                              "        print(f'[CALL] {function.__name__}')\n"
                                              '        return function(value)\n'
                                              '    return wrapper\n'
                                              '@trace_calls\n'
                                              'def compute(value):\n'
                                              '    return value * 2\n'
                                              "print('Result:', compute(int(input())))",
                             'test_cases': [{'expected_output': '[CALL] compute\nResult: 12',
                                             'input_data': '6\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Trace a Function Call',
                             'xp_reward': 150}],
             'description': 'Extend and modify function behavior transparently using decorators and '
                            'functools.wraps.',
             'lesson': {'common_mistakes': [{'fix': 'Always capture and return: result = func(*args, '
                                                    '**kwargs); return result.',
                                             'mistake': 'Forgetting to return the result of func(*args, '
                                                        '**kwargs) inside wrapper',
                                             'why': 'The decorated function will return None to the caller '
                                                    'instead of its actual return value!'}],
                        'detailed_explanation': 'What is a Decorator?\n'
                                                'A decorator is simply a function that takes another '
                                                'function as an argument, extends its behavior by wrapping '
                                                'it inside an inner function, and returns the wrapper.\n'
                                                '\n'
                                                'The Syntactic Sugar:\n'
                                                'Writing:\n'
                                                '```python\n'
                                                '@timer\n'
                                                'def calculate(): ...\n'
                                                '```\n'
                                                'Is 100% equivalent to:\n'
                                                '```python\n'
                                                'def calculate(): ...\n'
                                                'calculate = timer(calculate)\n'
                                                '```\n'
                                                '\n'
                                                'Preserving Metadata with `functools.wraps`:\n'
                                                'Without `@wraps(func)`, the decorated function loses its '
                                                "identity (its `__name__` becomes `'wrapper'`). Decorating "
                                                'the inner wrapper with `@wraps(func)` preserves the '
                                                "original function's name and docstring.",
                        'expected_output': 'Calling deploy...\nDeploying server container\ndeploy finished.',
                        'introduction': 'What if you need to measure the execution time of 20 different '
                                        'functions, or ensure that only logged-in users can access 15 web '
                                        'routes? Copy-pasting timing or authentication code into every '
                                        'single function creates bloated, unmaintainable code. Decorators '
                                        'let you wrap existing functions with reusable behavior in a single '
                                        'line: `@my_decorator`.',
                        'learning_objectives': ['Understand decorators as higher-order functions wrapping '
                                                'target functions',
                                                'Use the @decorator syntactic sugar',
                                                'Preserve function metadata (name, docstring) using '
                                                'functools.wraps'],
                        'line_by_line': [{'code': 'def benchmark(func):',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': '    def wrapper(*args, **kwargs):',
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': "        print(f'Starting {func.__name__}')",
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'},
                                         {'code': '        return func(*args, **kwargs)',
                                          'explanation': 'Line 4 instruction execution',
                                          'line': '4'},
                                         {'code': '    return wrapper',
                                          'explanation': 'Line 5 instruction execution',
                                          'line': '5'},
                                         {'code': '@benchmark',
                                          'explanation': 'Line 6 instruction execution',
                                          'line': '6'},
                                         {'code': 'def load_data():',
                                          'explanation': 'Line 7 instruction execution',
                                          'line': '7'},
                                         {'code': "    return 'Data loaded'",
                                          'explanation': 'Line 8 instruction execution',
                                          'line': '8'},
                                         {'code': 'print(load_data())',
                                          'explanation': 'Line 9 instruction execution',
                                          'line': '9'}],
                        'practical_examples': [{'code': 'def benchmark(func):\n'
                                                        '    def wrapper(*args, **kwargs):\n'
                                                        "        print(f'Starting {func.__name__}')\n"
                                                        '        return func(*args, **kwargs)\n'
                                                        '    return wrapper\n'
                                                        '@benchmark\n'
                                                        'def load_data():\n'
                                                        "    return 'Data loaded'\n"
                                                        'print(load_data())',
                                                'explanation': 'Wraps load_data with startup announcements '
                                                               'transparently.',
                                                'output': 'Starting load_data\nData loaded',
                                                'title': 'Example 1: Execution timer decorator'},
                                               {'code': 'def require_auth(func):\n'
                                                        '    def wrapper(user, *args, **kwargs):\n'
                                                        "        if not user.get('authenticated', False):\n"
                                                        "            return 'Access Denied: Please log in'\n"
                                                        '        return func(user, *args, **kwargs)\n'
                                                        '    return wrapper\n'
                                                        '@require_auth\n'
                                                        'def view_dashboard(user):\n'
                                                        "    return f'Welcome to VIP Dashboard, "
                                                        '{user["name"]}!\'\n'
                                                        "print(view_dashboard({'name': 'Sam', "
                                                        "'authenticated': False}))\n"
                                                        "print(view_dashboard({'name': 'Sam', "
                                                        "'authenticated': True}))",
                                                'explanation': 'Intercepts unauthorized function calls '
                                                               'before execution occurs.',
                                                'output': 'Access Denied: Please log in\n'
                                                          'Welcome to VIP Dashboard, Sam!',
                                                'title': 'Example 2: Authentication permission gate '
                                                         'decorator'},
                                               {'code': 'def make_uppercase(func):\n'
                                                        '    def wrapper():\n'
                                                        '        return func().upper()\n'
                                                        '    return wrapper\n'
                                                        '@make_uppercase\n'
                                                        'def get_title():\n'
                                                        "    return 'quest master'\n"
                                                        "print('Decorated Title:', get_title())",
                                                'explanation': 'Transforms the return value of get_title to '
                                                               'uppercase automatically.',
                                                'output': 'Decorated Title: QUEST MASTER',
                                                'title': 'Example 3: Output formatting decorator'}],
                        'practice_questions': ['What is `@my_decorator` shorthand for?',
                                               'Why should you use `functools.wraps` inside your wrapper '
                                               'function?'],
                        'prerequisites': 'Level 110: Closures and First-Class Functions',
                        'real_world_apps': 'Flask route decorators (@app.route), authentication verification '
                                           '(@login_required), caching (@lru_cache), execution profiling.',
                        'summary': 'Decorators wrap functions with reusable pre/post behavior using '
                                   '@decorator. Always use @wraps(func) to preserve metadata.',
                        'syntax_breakdown': '# Function Decorators (@decorator syntax):\n'
                                            '# A decorator wraps another function to modify or extend its '
                                            'behavior\n'
                                            "# without modifying the original function's source code!\n"
                                            'def my_logger(func):\n'
                                            '    def wrapper(*args, **kwargs):\n'
                                            "        print(f'[LOG] Calling {func.__name__}...')\n"
                                            '        result = func(*args, **kwargs)\n'
                                            "        print(f'[LOG] {func.__name__} finished.')\n"
                                            '        return result\n'
                                            '    return wrapper\n'
                                            '\n'
                                            '@my_logger\n'
                                            'def greet(name):\n'
                                            "    print(f'Hello, {name}!')\n"
                                            '\n'
                                            "greet('Alex')",
                        'terminology': [{'definition': 'A higher-order function that takes another function '
                                                       'as input, extends its behavior, and returns a '
                                                       'modified function.',
                                         'term': 'Decorator'},
                                        {'definition': 'Syntax within a programming language that is '
                                                       'designed to make things easier to read or to express '
                                                       'without adding new capabilities.',
                                         'term': 'Syntactic Sugar'},
                                        {'definition': 'A decorator that copies attributes like __name__ and '
                                                       '__doc__ from the original function to the wrapper '
                                                       'function.',
                                         'term': 'functools.wraps'}]},
             'number': 111,
             'quizzes': [{'explanation': "@tag wraps greet() so it executes wrapper(), returning '[Hello]'.",
                          'options': [{'explanation': 'Correct! The decorator wraps greet in brackets.',
                                       'is_correct': True,
                                       'text': '[Hello]'},
                                      {'explanation': 'Incorrect. @tag wrapped the return value.',
                                       'is_correct': False,
                                       'text': 'Hello'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'tag'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the decorator syntax?\n'
                                      '\n'
                                      'def tag(f):\n'
                                      '    def wrapper():\n'
                                      "        return '[' + f() + ']'\n"
                                      '    return wrapper\n'
                                      '\n'
                                      '@tag\n'
                                      'def greet():\n'
                                      "    return 'Hello'\n"
                                      '\n'
                                      'print(greet())'},
                         {'explanation': "It preserves the original function's metadata, such as its "
                                         '__name__ and docstring.',
                          'options': [{'explanation': 'Correct! wraps copies __name__, __doc__, and '
                                                      'signature metadata.',
                                       'is_correct': True,
                                       'text': "To preserve the original function's name (__name__) and "
                                               'docstring'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To make the decorator run 10x faster'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To prevent recursion errors'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To compile the function into bytecode'}],
                          'question': 'Why is `@functools.wraps(func)` applied to inner wrapper functions in '
                                      'custom decorators?'}],
             'title': 'Function Decorators (@decorator syntax)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use @repeat(times=3) to make ping print the word ping three times.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def repeat(times):\n'
                                       '    def decorate(function):\n'
                                       '        def wrapper():\n'
                                       '            for _ in range(times):\n'
                                       '                function()\n'
                                       '        return wrapper\n'
                                       '    return decorate\n'
                                       '@repeat(times=3)\n'
                                       'def ping():\n'
                                       "    print('ping')\n"
                                       'ping()'],
                             'initial_code': '# Decorators Accepting Arguments\n'
                                             'from functools import wraps\n'
                                             '# Step 1: Define repeat(times) returning decorator:\n'
                                             '\n'
                                             '# Step 2: Apply @repeat(times=3) to ping():\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def repeat(times):\n'
                                              '    def decorate(function):\n'
                                              '        def wrapper():\n'
                                              '            for _ in range(times):\n'
                                              '                function()\n'
                                              '        return wrapper\n'
                                              '    return decorate\n'
                                              '@repeat(times=3)\n'
                                              'def ping():\n'
                                              "    print('ping')\n"
                                              'ping()',
                             'test_cases': [{'expected_output': 'ping\nping\nping',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Repeat a Function with a Decorator Argument',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Create with_prefix(category), then decorate log_message so it adds [SEC] before the returned message.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def with_prefix(category):\n'
                                       '    def decorate(function):\n'
                                       '        def wrapper(message):\n'
                                       "            return f'[{category}] {function(message)}'\n"
                                       '        return wrapper\n'
                                       '    return decorate\n'
                                       "@with_prefix('SEC')\n"
                                       'def log_message(message):\n'
                                       '    return message\n'
                                       "print(log_message('System breach neutralized'))"],
                             'initial_code': '# ⚔️ Boss Challenge: Tagged Prefix Formatter\n'
                                             'from functools import wraps\n'
                                             '# Step 1: Define with_prefix(category):\n'
                                             '\n'
                                             '# Step 2: Decorate log_sec and print output:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def with_prefix(category):\n'
                                              '    def decorate(function):\n'
                                              '        def wrapper(message):\n'
                                              "            return f'[{category}] {function(message)}'\n"
                                              '        return wrapper\n'
                                              '    return decorate\n'
                                              "@with_prefix('SEC')\n"
                                              'def log_message(message):\n'
                                              '    return message\n'
                                              "print(log_message('System breach neutralized'))",
                             'test_cases': [{'expected_output': '[SEC] System breach neutralized',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Add a Prefix with a Decorator',
                             'xp_reward': 150}],
             'description': 'Build parameterized decorators using a three-tier nested function architecture.',
             'lesson': {'common_mistakes': [{'fix': 'Always use 3 levels: factory(args) -> decorator(func) '
                                                    '-> wrapper(*a, **kw).',
                                             'mistake': 'Writing only 2 levels of nesting for a decorator '
                                                        'with arguments',
                                             'why': 'Python will pass the argument to func instead of the '
                                                    'target function, raising TypeError.'}],
                        'detailed_explanation': 'The 3-Tier Architecture for Decorators with Arguments:\n'
                                                "1. Outer Function (Factory): Accepts the decorator's "
                                                'configuration arguments (`max_attempts`).\n'
                                                '2. Middle Function (Decorator): Accepts the target function '
                                                '(`func`).\n'
                                                "3. Inner Function (Wrapper): Accepts the target function's "
                                                'arguments (`*args, **kwargs`).\n'
                                                '\n'
                                                '```python\n'
                                                'def repeat(num_times):\n'
                                                '    def decorator(func):\n'
                                                '        def wrapper(*args, **kwargs):\n'
                                                '            for _ in range(num_times):\n'
                                                '                res = func(*args, **kwargs)\n'
                                                '            return res\n'
                                                '        return wrapper\n'
                                                '    return decorator\n'
                                                '```',
                        'expected_output': '[AUDIT] User logged in',
                        'introduction': 'What if you want to configure your decorator — for instance, '
                                        'specifying how many times to retry an API call '
                                        '`@retry(max_attempts=3)` or setting a rate limit '
                                        '`@rate_limit(calls=60)`? Because you are passing arguments to the '
                                        'decorator itself, you need a Decorator Factory.',
                        'learning_objectives': ['Understand why decorators with arguments require a 3-tier '
                                                'nested architecture',
                                                'Build parameterized decorators like @repeat(num_times=3)',
                                                'Understand how decorator factories work'],
                        'line_by_line': [{'code': 'def repeat_count(n):',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': '    def dec(fn):',
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': '        def wrap(*args, **kwargs):',
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'},
                                         {'code': '            for i in range(n):',
                                          'explanation': 'Line 4 instruction execution',
                                          'line': '4'},
                                         {'code': "                print(f'Run #{i+1}:', fn(*args, "
                                                  '**kwargs))',
                                          'explanation': 'Line 5 instruction execution',
                                          'line': '5'},
                                         {'code': '        return wrap',
                                          'explanation': 'Line 6 instruction execution',
                                          'line': '6'},
                                         {'code': '    return dec',
                                          'explanation': 'Line 7 instruction execution',
                                          'line': '7'},
                                         {'code': '@repeat_count(2)',
                                          'explanation': 'Line 8 instruction execution',
                                          'line': '8'},
                                         {'code': 'def announce():',
                                          'explanation': 'Line 9 instruction execution',
                                          'line': '9'},
                                         {'code': "    return 'Signal pulse'",
                                          'explanation': 'Line 10 instruction execution',
                                          'line': '10'},
                                         {'code': 'announce()',
                                          'explanation': 'Line 11 instruction execution',
                                          'line': '11'}],
                        'practical_examples': [{'code': 'def repeat_count(n):\n'
                                                        '    def dec(fn):\n'
                                                        '        def wrap(*args, **kwargs):\n'
                                                        '            for i in range(n):\n'
                                                        "                print(f'Run #{i+1}:', fn(*args, "
                                                        '**kwargs))\n'
                                                        '        return wrap\n'
                                                        '    return dec\n'
                                                        '@repeat_count(2)\n'
                                                        'def announce():\n'
                                                        "    return 'Signal pulse'\n"
                                                        'announce()',
                                                'explanation': 'n sets how many times the wrapped function '
                                                               'will be invoked.',
                                                'output': 'Run #1: Signal pulse\nRun #2: Signal pulse',
                                                'title': 'Example 1: Configurable repetition decorator'},
                                               {'code': 'def allow_role(role_name):\n'
                                                        '    def dec(fn):\n'
                                                        '        def wrap(user):\n'
                                                        "            if user.get('role') != role_name:\n"
                                                        "                return 'Forbidden'\n"
                                                        '            return fn(user)\n'
                                                        '        return wrap\n'
                                                        '    return dec\n'
                                                        "@allow_role('Admin')\n"
                                                        'def delete_account(user):\n'
                                                        "    return 'Account deleted.'\n"
                                                        "print(delete_account({'role': 'Guest'}))\n"
                                                        "print(delete_account({'role': 'Admin'}))",
                                                'explanation': 'Parameterizes permission checks cleanly at '
                                                               'decoration time.',
                                                'output': 'Forbidden\nAccount deleted.',
                                                'title': 'Example 2: Role-based access decorator with '
                                                         'allowed role parameter'},
                                               {'code': 'from functools import wraps\n'
                                                        'def doc_wrap(prefix):\n'
                                                        '    def dec(fn):\n'
                                                        '        @wraps(fn)\n'
                                                        '        def wrap(*args, **kwargs):\n'
                                                        "            return f'{prefix}: {fn(*args, "
                                                        "**kwargs)}'\n"
                                                        '        return wrap\n'
                                                        '    return dec\n'
                                                        "@doc_wrap('LOG')\n"
                                                        'def status():\n'
                                                        "    return 'OK'\n"
                                                        'print(status())\n'
                                                        "print('Function name preserved:', status.__name__)",
                                                'explanation': '@wraps preserves original docstrings and '
                                                               '__name__ attributes.',
                                                'output': 'LOG: OK\nFunction name preserved: status',
                                                'title': 'Example 3: Preserving metadata with '
                                                         'functools.wraps'}],
                        'practice_questions': ['How many levels of function nesting are required for a '
                                               'decorator that takes arguments?',
                                               'What does the outermost function in a parameterized '
                                               'decorator accept?'],
                        'prerequisites': 'Level 111: Function Decorators (@decorator)',
                        'real_world_apps': "Flask route decorators (@app.route('/login', methods=['POST'])), "
                                           'pytest parametrization (@pytest.mark.parametrize).',
                        'summary': 'Decorators that accept arguments require 3 tiers: factory(config) -> '
                                   'decorator(func) -> wrapper(*args, **kwargs).',
                        'syntax_breakdown': '# Decorators with Arguments:\n'
                                            '# To accept arguments in a decorator, create a 3-tier function '
                                            'factory:\n'
                                            'def repeat(times):\n'
                                            '    def decorator(func):\n'
                                            '        def wrapper(*args, **kwargs):\n'
                                            '            for _ in range(times):\n'
                                            '                result = func(*args, **kwargs)\n'
                                            '            return result\n'
                                            '        return wrapper\n'
                                            '    return decorator\n'
                                            '\n'
                                            '@repeat(times=3)\n'
                                            'def ping():\n'
                                            "    print('Ping packet transmitted.')\n"
                                            '\n'
                                            'ping()',
                        'terminology': [{'definition': 'A function that takes configuration parameters and '
                                                       'returns a custom decorator function.',
                                         'term': 'Decorator Factory'},
                                        {'definition': 'The architectural pattern (factory -> decorator -> '
                                                       'wrapper) required for parameterized decorators.',
                                         'term': '3-Tier Function Nesting'}]},
             'number': 112,
             'quizzes': [{'explanation': "repeat(3) configures n = 3. echo('A') returns 'A' * 3 = 'AAA'.",
                          'options': [{'explanation': "Correct! 'A' is multiplied by 3.",
                                       'is_correct': True,
                                       'text': 'AAA'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'A'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '3'},
                                      {'explanation': 'Incorrect. String multiplication produces a string.',
                                       'is_correct': False,
                                       'text': "['A', 'A', 'A']"}],
                          'question': 'What is the output of the parameterized decorator?\n'
                                      '\n'
                                      'def repeat(n):\n'
                                      '    def decorator(fn):\n'
                                      '        def wrapper(x):\n'
                                      '            return fn(x) * n\n'
                                      '        return wrapper\n'
                                      '    return decorator\n'
                                      '\n'
                                      '@repeat(3)\n'
                                      'def echo(s):\n'
                                      '    return s\n'
                                      '\n'
                                      "print(echo('A'))"},
                         {'explanation': 'repeat(5) is evaluated as a function call, returning the decorator '
                                         'function that receives the decorated target.',
                          'options': [{'explanation': 'Correct! The arguments function executes first to '
                                                      'produce the decorator.',
                                       'is_correct': True,
                                       'text': 'repeat(5) is called, returning the actual decorator '
                                               'function'},
                                      {'explanation': 'Incorrect. Decorators are applied at definition time.',
                                       'is_correct': False,
                                       'text': 'The target function is executed immediately'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Python creates a thread'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Nothing runs until the function is invoked'}],
                          'question': 'In `@repeat(5)`, what is executed first by Python when loading the '
                                      'module?'}],
             'title': 'Decorators with Arguments'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Write factorial using recursion, which means the function calls itself with a smaller number.\n2. A number’s factorial is that number multiplied by the factorial before it, and 0! is 1.\n3. Read a whole number and print its factorial.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def factorial(n):\n'
                                       '    if n <= 1:\n'
                                       '        return 1\n'
                                       '    return n * factorial(n - 1)\n'
                                       '\n'
                                       'print(factorial(int(input())))'],
                             'initial_code': '# Recursion and Call Stacks\n'
                                             '# Step 1: Define recursive factorial(n):\n'
                                             '\n'
                                             '# Step 2: Read int and print factorial below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def factorial(n):\n'
                                              '    if n <= 1:\n'
                                              '        return 1\n'
                                              '    return n * factorial(n - 1)\n'
                                              '\n'
                                              'num = int(input())\n'
                                              "print(f'Factorial({num}) = {factorial(num)}')",
                             'test_cases': [{'challenge_id': 1524,
                                             'expected_output': 'Factorial(5) = 120',
                                             'explanation': '',
                                             'id': 2498,
                                             'input_data': '5\n',
                                             'is_hidden': 0},
                                            {'challenge_id': 1524,
                                             'expected_output': 'Factorial(3) = 6',
                                             'explanation': '',
                                             'id': 2499,
                                             'input_data': '3\n',
                                             'is_hidden': 0}],
                             'title': 'Recursive Factorial',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use recursion to flatten nested lists into one list.\n2. Print the flattened result.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def flatten(items):\n'
                                       '    result = []\n'
                                       '    for item in items:\n'
                                       '        if isinstance(item, list):\n'
                                       '            result.extend(flatten(item))\n'
                                       '        else:\n'
                                       '            result.append(item)\n'
                                       '    return result\n'
                                       'print(flatten([1, [2, [3, 4]], 5]))'],
                             'initial_code': '# ⚔️ Boss Challenge: Nested Structure Flattener\n'
                                             '# Step 1: Define flatten_tree(node):\n'
                                             '\n'
                                             '# Step 2: Print flatten_tree([1, [2, [3, 4]], 5]) below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def flatten(items):\n'
                                              '    result = []\n'
                                              '    for item in items:\n'
                                              '        if isinstance(item, list):\n'
                                              '            result.extend(flatten(item))\n'
                                              '        else:\n'
                                              '            result.append(item)\n'
                                              '    return result\n'
                                              'print(flatten([1, [2, [3, 4]], 5]))',
                             'test_cases': [{'expected_output': '[1, 2, 3, 4, 5]',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Flatten a Nested List',
                             'xp_reward': 150}],
             'description': 'Solve self-similar algorithmic problems using base cases, recursive calls, and '
                            'call stack management.',
             'lesson': {'common_mistakes': [{'fix': 'Always verify your base case executes and your '
                                                    'recursive argument shrinks.',
                                             'mistake': 'RecursionError: maximum recursion depth exceeded',
                                             'why': 'Missing base case or recursive step does not make '
                                                    'progress toward the base case.'}],
                        'detailed_explanation': 'The 2 Mandatory Rules of Recursion:\n'
                                                '1. Base Case: The terminating condition that stops '
                                                'recursion and returns a direct answer without making any '
                                                'further recursive calls (e.g. `if n <= 1: return 1`). '
                                                'WITHOUT A BASE CASE, THE FUNCTION WILL RECURSE INFINITELY!\n'
                                                '2. Recursive Step: The branch where the function calls '
                                                'itself with a strictly smaller or simpler input (`return n '
                                                '* factorial(n - 1)`), progressing steadily toward the base '
                                                'case.\n'
                                                '\n'
                                                'The Call Stack & Recursion Limit:\n'
                                                "Every recursive call pushes a new frame onto Python's call "
                                                'stack. Python has a safety guard (default: 1,000 frames) to '
                                                'prevent crashing the OS. Exceeding this raises '
                                                '`RecursionError: maximum recursion depth exceeded`.',
                        'expected_output': '10',
                        'introduction': 'To understand recursion, you must first understand recursion! In '
                                        'computer science, recursion is an elegant technique where a '
                                        'function solves a problem by breaking it down into smaller '
                                        'instances of the exact same problem until it reaches a trivial '
                                        'baseline.',
                        'learning_objectives': ['Understand how a function can call itself (Recursion)',
                                                'Identify the two mandatory components: Base Case and '
                                                'Recursive Step',
                                                'Understand the call stack and prevent RecursionError (Stack '
                                                'Overflow)'],
                        'line_by_line': [{'code': 'def countdown(n):',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': '    if n == 0:',
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': "        print('Blastoff!')",
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'},
                                         {'code': '        return',
                                          'explanation': 'Line 4 instruction execution',
                                          'line': '4'},
                                         {'code': '    print(n)',
                                          'explanation': 'Line 5 instruction execution',
                                          'line': '5'},
                                         {'code': '    countdown(n - 1)',
                                          'explanation': 'Line 6 instruction execution',
                                          'line': '6'},
                                         {'code': 'countdown(3)',
                                          'explanation': 'Line 7 instruction execution',
                                          'line': '7'}],
                        'practical_examples': [{'code': 'def countdown(n):\n'
                                                        '    if n == 0:\n'
                                                        "        print('Blastoff!')\n"
                                                        '        return\n'
                                                        '    print(n)\n'
                                                        '    countdown(n - 1)\n'
                                                        'countdown(3)',
                                                'explanation': 'Executes down to 0 base case, printing '
                                                               'values as stack frames build.',
                                                'output': '3\n2\n1\nBlastoff!',
                                                'title': 'Example 1: Countdown recursion simulation'},
                                               {'code': 'def sum_list(nums):\n'
                                                        '    if not nums:\n'
                                                        '        return 0\n'
                                                        '    return nums[0] + sum_list(nums[1:])\n'
                                                        "print('Recursive sum:', sum_list([10, 20, 30]))",
                                                'explanation': 'Adds head of list to recursive sum of the '
                                                               'tail until empty.',
                                                'output': 'Recursive sum: 60',
                                                'title': 'Example 2: Summing list numbers recursively'},
                                               {'code': "fs = {'src': {'app': ['main.py', 'routes.py']}}\n"
                                                        'def list_files(d):\n'
                                                        '    files = []\n'
                                                        '    for k, v in d.items():\n'
                                                        '        if isinstance(v, dict):\n'
                                                        '            files.extend(list_files(v))\n'
                                                        '        else:\n'
                                                        '            files.extend(v)\n'
                                                        '    return files\n'
                                                        "print('Discovered files:', list_files(fs))",
                                                'explanation': 'Recursively explores directory tree '
                                                               'dictionaries of arbitrary depth.',
                                                'output': "Discovered files: ['main.py', 'routes.py']",
                                                'title': 'Example 3: Traversing nested folder hierarchies '
                                                         'recursively'}],
                        'practice_questions': ['What two components must every recursive function have?',
                                               'What error occurs if a recursive function lacks a base '
                                               'case?'],
                        'prerequisites': 'Level 112: Decorators with Arguments',
                        'real_world_apps': 'Navigating nested directory filesystems, parsing JSON/XML '
                                           'hierarchical AST trees, divide-and-conquer algorithms '
                                           '(QuickSort, MergeSort).',
                        'summary': 'Recursion requires a base case to terminate and a recursive step moving '
                                   'toward the base case. Avoid unbounded recursion to prevent stack '
                                   'overflow.',
                        'syntax_breakdown': '# Recursion and the Call Stack:\n'
                                            '# A recursive function is a function that calls ITSELF:\n'
                                            '# Essential rules:\n'
                                            '# 1. Base case: terminates recursion (prevents infinite loop & '
                                            'RecursionError!)\n'
                                            '# 2. Recursive step: moves closer to the base case\n'
                                            'def factorial(n):\n'
                                            '    if n <= 1:\n'
                                            '        return 1  # Base Case!\n'
                                            '    return n * factorial(n - 1)  # Recursive Step!\n'
                                            '\n'
                                            "print('Factorial of 5 (5 * 4 * 3 * 2 * 1):', factorial(5))",
                        'terminology': [{'definition': 'A programming technique in which a function calls '
                                                       'itself directly or indirectly to solve a problem.',
                                         'term': 'Recursion'},
                                        {'definition': 'The condition that stops recursive execution by '
                                                       'returning a concrete value without further '
                                                       'recursion.',
                                         'term': 'Base Case'},
                                        {'definition': 'A stack data structure maintained by the runtime '
                                                       'storing information about the active subroutines of '
                                                       'a program.',
                                         'term': 'Call Stack'}]},
             'number': 113,
             'quizzes': [{'explanation': 'fact(4) = 4 * 3 * 2 * 1 = 24.',
                          'options': [{'explanation': 'Correct! 4 * 3 * 2 * 1 = 24.',
                                       'is_correct': True,
                                       'text': '24'},
                                      {'explanation': 'Incorrect. Factorial multiplies rather than adds.',
                                       'is_correct': False,
                                       'text': '10'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '12'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '1'}],
                          'question': 'What is the output of the recursive factorial function?\n'
                                      '\n'
                                      'def fact(n):\n'
                                      '    if n <= 1:\n'
                                      '        return 1\n'
                                      '    return n * fact(n - 1)\n'
                                      '\n'
                                      'print(fact(4))'},
                         {'explanation': "Python's default recursion limit (typically 1,000) prevents call "
                                         'stack overflow by raising RecursionError.',
                          'options': [{'explanation': 'Correct! Python raises RecursionError to protect '
                                                      'against stack exhaustion.',
                                       'is_correct': True,
                                       'text': 'RecursionError: maximum recursion depth exceeded'},
                                      {'explanation': 'Incorrect. Python catches deep recursion with '
                                                      'RecursionError.',
                                       'is_correct': False,
                                       'text': 'MemoryError'},
                                      {'explanation': 'Incorrect. That is Java/.NET terminology.',
                                       'is_correct': False,
                                       'text': 'StackOverflowException'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It completes with no error'}],
                          'question': 'What exception is raised if a recursive function recurses 2,000 times '
                                      'in default Python?'}],
             'title': 'Recursion and the Call Stack'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use re.findall with the pattern r\\d+ to find every group of digits in the text.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ["import re\ntext = input()\nprint(re.findall(r'\\d+', text))"],
                             'initial_code': '# Regular Expressions: re.findall\n'
                                             'import re\n'
                                             '# Step 1: Read text:\n'
                                             'text = input().strip()\n'
                                             '\n'
                                             '# Step 2: Extract numbers and print list below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "import re\ntext = input()\nprint(re.findall(r'\\d+', text))",
                             'test_cases': [{'expected_output': "['104', '3']",
                                             'input_data': 'User 104 bought 3 items\n',
                                             'is_hidden': False}],
                             'title': 'Find Digit Groups with a Regular Expression',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Use regular expressions to find unique email addresses and phone numbers.\n2. Print both sorted lists.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import re\n'
                                       'count = int(input())\n'
                                       'lines = [input() for _ in range(count)]\n'
                                       "text = '\\n'.join(lines)\n"
                                       "emails = sorted(set(re.findall(r'[\\w.+-]+@[\\w.-]+\\.[A-Za-z]{2,}', "
                                       'text)))\n'
                                       "phones = sorted(set(re.findall(r'\\d{3}-\\d{3}-\\d{4}', text)))\n"
                                       "print('Emails:', emails)\n"
                                       "print('Phones:', phones)"],
                             'initial_code': '# ⚔️ Boss Challenge: Contact Data Scraper\n'
                                             'import re\n'
                                             '# Step 1: Read n lines and extract emails and phones:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import re\n'
                                              'count = int(input())\n'
                                              'lines = [input() for _ in range(count)]\n'
                                              "text = '\\n'.join(lines)\n"
                                              'emails = '
                                              "sorted(set(re.findall(r'[\\w.+-]+@[\\w.-]+\\.[A-Za-z]{2,}', "
                                              'text)))\n'
                                              "phones = sorted(set(re.findall(r'\\d{3}-\\d{3}-\\d{4}', "
                                              'text)))\n'
                                              "print('Emails:', emails)\n"
                                              "print('Phones:', phones)",
                             'test_cases': [{'expected_output': "Emails: ['help@example.com']\n"
                                                                "Phones: ['555-123-4567']",
                                             'input_data': '1\nMail help@example.com or call 555-123-4567\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Find Emails and Phone Numbers',
                             'xp_reward': 150}],
             'description': "Pattern match, extract, and sanitize complex text using Python's regular "
                            'expressions engine.',
             'lesson': {'common_mistakes': [{'fix': "Always use raw strings for regex patterns: r'\\d+'.",
                                             'mistake': "Writing '\\d+' without the raw string r prefix: "
                                                        "'\\\\d+'",
                                             'why': 'Without r, Python string escaping interferes with regex '
                                                    'backslashes.'}],
                        'detailed_explanation': "Python's `re` Module:\n"
                                                '1. Common Patterns:\n'
                                                '   - `\\d`: Any digit (0-9).\n'
                                                '   - `\\w`: Any word character (letters, numbers, '
                                                'underscore).\n'
                                                '   - `\\s`: Any whitespace character.\n'
                                                '   - `+`: One or more occurrences.\n'
                                                '   - `*`: Zero or more occurrences.\n'
                                                '   - `?`: Zero or one occurrence (optional).\n'
                                                '   - `[a-z]`: Character class (any lowercase letter).\n'
                                                '2. Core Functions:\n'
                                                '   - `re.search(pattern, text)`: Scans entire string for '
                                                'first match (returns Match object or None).\n'
                                                '   - `re.findall(pattern, text)`: Finds ALL non-overlapping '
                                                'occurrences (returns list of strings).\n'
                                                '   - `re.sub(pattern, replacement, text)`: Substitutes '
                                                'matches with replacement string.\n'
                                                '\n'
                                                'Raw Strings: Always prefix regex patterns with `r` (e.g. '
                                                "`r'\\d+'`) so Python does not interpret backslashes as "
                                                'string escape sequences.',
                        'expected_output': 'Domain: pythonquest.org',
                        'introduction': 'How do you validate that an email address has a valid domain, '
                                        'extract every phone number from a 500-page document, or redact '
                                        'credit card numbers? Standard string methods like `.find()` or '
                                        '`.split()` are completely inadequate for complex pattern matching. '
                                        'Regular Expressions (regex) provide a mini-language for text '
                                        'patterns.',
                        'learning_objectives': ['Understand regular expressions (regex) syntax and special '
                                                'characters (\\d, \\w, +, *, ?)',
                                                'Search and match patterns using re.search(), re.match(), '
                                                'and re.findall()',
                                                'Substitute and clean text patterns using re.sub()'],
                        'line_by_line': [{'code': 'import re',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': "phone = '555-123-4567'",
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': "is_valid = bool(re.fullmatch(r'\\d{3}-\\d{3}-\\d{4}', "
                                                  'phone))',
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'},
                                         {'code': "print('Phone number format valid:', is_valid)",
                                          'explanation': 'Line 4 instruction execution',
                                          'line': '4'}],
                        'practical_examples': [{'code': 'import re\n'
                                                        "phone = '555-123-4567'\n"
                                                        'is_valid = '
                                                        "bool(re.fullmatch(r'\\d{3}-\\d{3}-\\d{4}', phone))\n"
                                                        "print('Phone number format valid:', is_valid)",
                                                'explanation': '\\d{3} matches exactly 3 digits; validates '
                                                               'full phone format.',
                                                'output': 'Phone number format valid: True',
                                                'title': 'Example 1: Validating phone number format with '
                                                         're.match'},
                                               {'code': 'import re\n'
                                                        "text = 'User ID 402, User ID 509'\n"
                                                        "anonymized = re.sub(r'\\d+', 'XXX', text)\n"
                                                        "print('Sanitized text:', anonymized)",
                                                'explanation': 're.sub() substitutes all occurrences of '
                                                               "digit patterns with 'XXX'.",
                                                'output': 'Sanitized text: User ID XXX, User ID XXX',
                                                'title': 'Example 2: Search and replace with re.sub'},
                                               {'code': 'import re\n'
                                                        "log = '2026-11-03 ERROR [AUTH] Token expired'\n"
                                                        "m = re.search(r'(\\d{4}-\\d{2}-\\d{2}) (\\w+)', "
                                                        'log)\n'
                                                        'if m:\n'
                                                        "    print('Date:', m.group(1), '| Severity:', "
                                                        'm.group(2))',
                                                'explanation': 'Parentheses create capture groups accessible '
                                                               'via .group(1), .group(2).',
                                                'output': 'Date: 2026-11-03 | Severity: ERROR',
                                                'title': 'Example 3: Extracting regex capture groups'}],
                        'practice_questions': ['What does the raw string prefix `r` prevent in Python '
                                               'strings?',
                                               'What function replaces regex matches with a substitute '
                                               'string?'],
                        'prerequisites': 'Level 113: Recursion and the Call Stack',
                        'real_world_apps': 'Validating phone numbers and postal codes, sanitizing user '
                                           'inputs against SQL injection, parsing log files.',
                        'summary': "The re module provides pattern matching. Use r'\\d+' raw strings, "
                                   're.search for finding, re.findall for lists of matches, and re.sub for '
                                   'substitutions.',
                        'syntax_breakdown': '# Regular Expressions (re module):\n'
                                            '# Powerful pattern matching for text validation and '
                                            'extraction:\n'
                                            'import re\n'
                                            '\n'
                                            "text = 'Contact support@pythonquest.io or admin@quest.org'\n"
                                            '# Regex pattern for email addresses:\n'
                                            "pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\n"
                                            '\n'
                                            'emails = re.findall(pattern, text)\n'
                                            "print('Extracted emails:', emails)",
                        'terminology': [{'definition': 'A sequence of characters that specifies a search '
                                                       'pattern in text.',
                                         'term': 'Regular Expression (Regex)'},
                                        {'definition': 'A string literal prefix that treats backslashes as '
                                                       'literal characters without interpreting escape '
                                                       'codes.',
                                         'term': "Raw String (r'...')"},
                                        {'definition': 'An object returned by re.search containing metadata '
                                                       'about the matched pattern.',
                                         'term': 'Match Object'}]},
             'number': 114,
             'quizzes': [{'explanation': "r'\\d+' matches one or more consecutive digits: ['42', '100'].",
                          'options': [{'explanation': 'Correct! findall extracts all matching digit '
                                                      'sequences.',
                                       'is_correct': True,
                                       'text': "['42', '100']"},
                                      {'explanation': 'Incorrect. + groups consecutive digits.',
                                       'is_correct': False,
                                       'text': "['4', '2', '1', '0', '0']"},
                                      {'explanation': 'Incorrect. findall returns a list.',
                                       'is_correct': False,
                                       'text': "'42 100'"},
                                      {'explanation': 'Incorrect. \\d matches digits, not letters.',
                                       'is_correct': False,
                                       'text': "['Level', 'XP']"}],
                          'question': 'What is the output of the regex pattern search?\n'
                                      '\n'
                                      'import re\n'
                                      "text = 'Level 42 gives 100 XP'\n"
                                      "print(re.findall(r'\\d+', text))"},
                         {'explanation': 're.sub(pattern, replacement, string) performs regex pattern '
                                         'substitution.',
                          'options': [{'explanation': 'Correct! re.sub replaces regex matches.',
                                       'is_correct': True,
                                       'text': 're.sub()'},
                                      {'explanation': 'Incorrect. str.replace is for literal strings, not '
                                                      'regex.',
                                       'is_correct': False,
                                       'text': 're.replace()'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 're.change()'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 're.swap()'}],
                          'question': 'Which `re` function replaces all occurrences of a pattern with a '
                                      'replacement string?'}],
             'title': 'Regular Expressions (re module)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use re.fullmatch with a pattern to split each [LEVEL] message into its level and message.\n2. Print both parts.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['import re\n'
                                       'count = int(input())\n'
                                       "pattern = r'\\[(\\w+)\\]\\s*(.*)'\n"
                                       'for _ in range(count):\n'
                                       '    match = re.fullmatch(pattern, input().strip())\n'
                                       '    if match:\n'
                                       '        level, message = match.groups()\n'
                                       "        print(f'LEVEL={level} MSG={message}')"],
                             'initial_code': '# World 11 Capstone: Log Parser Stream\n'
                                             'import re\n'
                                             '# Step 1: Read n:\n'
                                             'n = int(input())\n'
                                             '\n'
                                             '# Step 2: For each line, match regex and print:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import re\n'
                                              'count = int(input())\n'
                                              "pattern = r'\\[(\\w+)\\]\\s*(.*)'\n"
                                              'for _ in range(count):\n'
                                              '    match = re.fullmatch(pattern, input().strip())\n'
                                              '    if match:\n'
                                              '        level, message = match.groups()\n'
                                              "        print(f'LEVEL={level} MSG={message}')",
                             'test_cases': [{'expected_output': 'LEVEL=INFO MSG=Server running\n'
                                                                'LEVEL=ERROR MSG=Disk space low',
                                             'input_data': '2\n'
                                                           '[INFO] Server running\n'
                                                           '[ERROR] Disk space low\n',
                                             'is_hidden': False}],
                             'title': 'Parse Log Lines with a Regular Expression',
                             'xp_reward': 50},
                            {'description': 'Your task, step by step:\n1. Create a pipeline decorator that runs strip, lowercase, and slugify steps before printing the final text.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import re\n'
                                       'def pipeline(steps):\n'
                                       '    def decorate(function):\n'
                                       '        def wrapper(value):\n'
                                       '            for step in steps:\n'
                                       '                value = step(value)\n'
                                       '            return function(value)\n'
                                       '        return wrapper\n'
                                       '    return decorate\n'
                                       'def slugify(value):\n'
                                       "    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')\n"
                                       '@pipeline([str.strip, str.lower, slugify])\n'
                                       'def show_slug(value):\n'
                                       '    return value\n'
                                       'print(show_slug(input()))'],
                             'initial_code': '# ⚔️ Boss Challenge: Pipeline Transformation Decorator\n'
                                             'import re\n'
                                             'from functools import wraps\n'
                                             '\n'
                                             '# Step 1: Define pipeline decorator and transformation steps:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import re\n'
                                              'def pipeline(steps):\n'
                                              '    def decorate(function):\n'
                                              '        def wrapper(value):\n'
                                              '            for step in steps:\n'
                                              '                value = step(value)\n'
                                              '            return function(value)\n'
                                              '        return wrapper\n'
                                              '    return decorate\n'
                                              'def slugify(value):\n'
                                              "    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')\n"
                                              '@pipeline([str.strip, str.lower, slugify])\n'
                                              'def show_slug(value):\n'
                                              '    return value\n'
                                              'print(show_slug(input()))',
                             'test_cases': [{'expected_output': 'python-quest-level-up',
                                             'input_data': '  Python Quest: Level Up!  \n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Decorated Text Pipeline',
                             'xp_reward': 250}],
             'description': 'Synthesize comprehensions, generators, custom decorators, and regex into a '
                            'streaming pipeline application.',
             'lesson': {'common_mistakes': [{'fix': 'Keep intermediate stages as generator expressions until '
                                                    'final aggregation.',
                                             'mistake': 'Converting intermediate pipeline stages into lists '
                                                        '(list(stage1))',
                                             'why': 'Defeats the purpose of generators, loading all data '
                                                    'into RAM at once.'}],
                        'detailed_explanation': 'Pipeline Architecture:\n'
                                                '1. Ingestion Generator: Lazily streams log records line by '
                                                'line without buffering all in RAM.\n'
                                                '2. Regex Parser: Extracts timestamp, log level, module, and '
                                                'message payload.\n'
                                                '3. Decorator Layer: Injects auditing metrics across '
                                                'processing stages.\n'
                                                '4. Aggregator: Uses comprehensions and Counter to compute '
                                                'severity metrics and error alerts.',
                        'expected_output': '[0, 4, 16, 36, 64]',
                        'introduction': 'Welcome to the World 11 Capstone Examination! Real-world data '
                                        'engineering involves processing gigabytes of messy, unstructured '
                                        'log files. You will synthesize advanced Python features — generator '
                                        'stream pipelines, custom execution decorators, dictionary '
                                        'comprehensions, and regular expressions — to build an Advanced Data '
                                        'Processing Application.',
                        'learning_objectives': ['Integrate generator pipelines for memory-efficient '
                                                'streaming processing',
                                                'Apply custom performance and logging decorators to pipeline '
                                                'stages',
                                                'Parse and sanitize messy logs using regular expressions'],
                        'line_by_line': [{'code': 'def generate_stream():',
                                          'explanation': 'Line 1 instruction execution',
                                          'line': '1'},
                                         {'code': '    for n in range(5):',
                                          'explanation': 'Line 2 instruction execution',
                                          'line': '2'},
                                         {'code': '        yield n',
                                          'explanation': 'Line 3 instruction execution',
                                          'line': '3'},
                                         {'code': 'filtered = (x * 10 for x in generate_stream() if x % 2 == '
                                                  '0)',
                                          'explanation': 'Line 4 instruction execution',
                                          'line': '4'},
                                         {'code': "print('Processed items:', list(filtered))",
                                          'explanation': 'Line 5 instruction execution',
                                          'line': '5'}],
                        'practical_examples': [{'code': 'def generate_stream():\n'
                                                        '    for n in range(5):\n'
                                                        '        yield n\n'
                                                        'filtered = (x * 10 for x in generate_stream() if x '
                                                        '% 2 == 0)\n'
                                                        "print('Processed items:', list(filtered))",
                                                'explanation': 'Chains generator producer and consumer '
                                                               'pipelines together.',
                                                'output': 'Processed items: [0, 20, 40]',
                                                'title': 'Example 1: Streaming pipeline processing with '
                                                         'generator'},
                                               {'code': 'import re\n'
                                                        "raw_data = 'Item: Shield | Price: $45.00'\n"
                                                        "match = re.search(r'\\$(\\d+\\.\\d{2})', raw_data)\n"
                                                        'if match:\n'
                                                        "    print('Extracted Price: $', match.group(1))",
                                                'explanation': 'Captures decimal dollar amounts out of '
                                                               'unstructured text.',
                                                'output': 'Extracted Price: $ 45.00',
                                                'title': 'Example 2: Regex extraction benchmark'},
                                               {'code': 'def notify(fn):\n'
                                                        '    def wrap(*args):\n'
                                                        "        return f'[STATUS] {fn(*args)}'\n"
                                                        '    return wrap\n'
                                                        '@notify\n'
                                                        'def process(batch):\n'
                                                        "    return f'{len(batch)} records synced'\n"
                                                        'print(process([1, 2, 3]))',
                                                'explanation': 'Applies decorator notification to summary '
                                                               'pipeline functions.',
                                                'output': '[STATUS] 3 records synced',
                                                'title': 'Example 3: Composing decorators on stream '
                                                         'consumers'}],
                        'practice_questions': ['Why chain generators instead of intermediate lists in data '
                                               'pipelines?',
                                               'What makes regex ideal for log line parsing?'],
                        'prerequisites': 'Levels 106 through 114',
                        'real_world_apps': 'Big Data processing (Apache Spark/PySpark pipelines), security '
                                           'SIEM log parsers, financial high-frequency tick analyzers.',
                        'summary': 'Advanced Python enables high-performance streaming pipelines by '
                                   'combining generators, regex parsing, and decorators.',
                        'syntax_breakdown': '# World 11 Capstone: High-Throughput Log Stream Processing '
                                            'Engine\n'
                                            'import re\n'
                                            '\n'
                                            'log_stream = [\n'
                                            "    '2026-11-03 10:00:01 INFO User login: alex',\n"
                                            "    '2026-11-03 10:00:05 ERROR Database connection failed',\n"
                                            "    '2026-11-03 10:00:12 WARNING High memory usage: 88%'\n"
                                            ']\n'
                                            '\n'
                                            'def parse_logs(lines):\n'
                                            '    for line in lines:\n'
                                            "        match = re.search(r'(\\d{2}:\\d{2}:\\d{2}) (\\w+) "
                                            "(.+)', line)\n"
                                            '        if match:\n'
                                            "            yield {'time': match.group(1), 'level': "
                                            "match.group(2), 'msg': match.group(3)}\n"
                                            '\n'
                                            'parsed = list(parse_logs(log_stream))\n'
                                            "print('Parsed records:', len(parsed))\n"
                                            "print('Errors:', [r['msg'] for r in parsed if r['level'] == "
                                            "'ERROR'])",
                        'terminology': [{'definition': 'A chain of processing elements arranged so the '
                                                       'output of each element is the input of the next.',
                                         'term': 'Data Pipeline'},
                                        {'definition': 'A computer programming paradigm where data is '
                                                       'processed sequentially piece-by-piece rather than in '
                                                       'batch memory.',
                                         'term': 'Stream Processing'},
                                        {'definition': 'Extract, Transform, Load — the foundational data '
                                                       'engineering process of moving and converting data.',
                                         'term': 'ETL'}]},
             'number': 115,
             'quizzes': [{'explanation': "Only 'beta' has length 4. In uppercase, it yields ['BETA'].",
                          'options': [{'explanation': "Correct! 'beta' has len 4 and is converted to "
                                                      'uppercase.',
                                       'is_correct': True,
                                       'text': "['BETA']"},
                                      {'explanation': "Incorrect. 'alpha' and 'gamma' have length 5.",
                                       'is_correct': False,
                                       'text': "['ALPHA', 'BETA', 'GAMMA']"},
                                      {'explanation': 'Incorrect. w.upper() was applied.',
                                       'is_correct': False,
                                       'text': "['beta']"},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '[]'}],
                          'question': 'What is the output of the generator pipeline?\n'
                                      '\n'
                                      "words = ['alpha', 'beta', 'gamma']\n"
                                      'pipeline = (w.upper() for w in words if len(w) == 4)\n'
                                      'print(list(pipeline))'},
                         {'explanation': 're.compile() compiles the regex pattern once into a pattern '
                                         'object, eliminating redundant parsing overhead on each iteration.',
                          'options': [{'explanation': 'Correct! Pre-compiling improves performance in loops.',
                                       'is_correct': True,
                                       'text': 'It compiles the pattern once, avoiding redundant regex '
                                               'parsing overhead in repeated iterations'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It encrypts the regex pattern for security'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It allows multi-threading'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It converts the regex to machine code'}],
                          'question': 'What is the advantage of compiling a regex pattern with '
                                      '`re.compile()` before matching in a large loop?'}],
             'title': 'World 11 Examination & Capstone: Advanced Data Processing Application'}],
 'number': 11,
 'title': 'Advanced Python'}
