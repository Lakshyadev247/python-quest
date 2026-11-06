"""
Curriculum module: WORLD_10
Upgraded with pedagogical question scenarios and scaffolded starter code.
"""

WORLD_10 = {'description': 'Master classes, objects, __init__, self, encapsulation, inheritance, polymorphism, and '
                'dunder methods.',
 'final_project_desc': 'Architect an enterprise-grade banking engine with account hierarchies, interest '
                       'calculation, encapsulation, and transaction logging.',
 'final_project_title': 'Banking Management System',
 'goal': 'Model complex real-world entities and enterprise architectures using object-oriented principles.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Create an empty class named QuestHero.\n2. Make one QuestHero object and print its class name.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class QuestHero:\n'
                                       '    pass\n'
                                       'h = QuestHero()\n'
                                       'print(type(h).__name__)'],
                             'initial_code': '# Object-Oriented Programming: Classes and Instances\n'
                                             '# Step 1: Define class QuestHero: pass\n'
                                             '\n'
                                             '# Step 2: Instantiate h and print type(h).__name__ below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class QuestHero:\n'
                                              '    pass\n'
                                              '\n'
                                              'hero = QuestHero()\n'
                                              'print(type(hero).__name__)',
                             'test_cases': [{'expected_output': 'QuestHero',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'First Class Blueprint',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Create the three empty classes Warrior, Mage, and Archer.\n2. Make one object from each and print their class names, one per line.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Warrior:\n'
                                       '    pass\n'
                                       'class Mage:\n'
                                       '    pass\n'
                                       'class Archer:\n'
                                       '    pass\n'
                                       'w, m, a = Warrior(), Mage(), Archer()\n'
                                       "print(f'{type(w).__name__}, {type(m).__name__}, "
                                       "{type(a).__name__}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Entity Type Classifier\n'
                                             '# Step 1: Define Warrior, Mage, Archer classes:\n'
                                             '\n'
                                             '# Step 2: Instantiate and print formatted type names:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Warrior:\n'
                                              '    pass\n'
                                              '\n'
                                              'class Mage:\n'
                                              '    pass\n'
                                              '\n'
                                              'class Archer:\n'
                                              '    pass\n'
                                              '\n'
                                              'for character in [Warrior(), Mage(), Archer()]:\n'
                                              '    print(type(character).__name__)',
                             'test_cases': [{'expected_output': 'Warrior\nMage\nArcher',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Entity Type Classifier',
                             'xp_reward': 150}],
             'description': 'Understand the paradigm shift from procedural code to modeling entities with '
                            'state and behavior.',
             'lesson': {'common_mistakes': [{'fix': 'A class is a blueprint; an instance is one real object '
                                                    'made from it.',
                                             'mistake': 'a class is a definition, not an object; procedural '
                                                        'code can still be the simpler choice',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Related data and actions are easier '
                                                'to manage together for some programs. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: A class describes a kind of object; an '
                                                'instance is one particular object with state and behavior. '
                                                'Python uses this idea to create instances from a class and '
                                                'call their methods; OOP organizes related data and actions\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: A class is a definition, not an object; '
                                                'procedural code can still be the simpler choice. If you '
                                                'change the example’s input or value, check this rule again '
                                                'because it can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Rover is a Dog: True\nSpot is distinct from Rover: True',
                        'id': 95,
                        'introduction': 'Why learn this? Related data and actions are easier to manage '
                                        'together for some programs. In this lesson, we will see a class '
                                        'describes a kind of object; an instance is one particular object '
                                        'with state and behavior, follow how Python handles it, and practice '
                                        'a small example you can change yourself.',
                        'learning_objectives': ['Explain a class describes a kind of object; an instance is '
                                                'one particular object with state and behavior in your own '
                                                'words.',
                                                'Trace a small What Is Object-Oriented Programming? example '
                                                'and predict what Python does next.',
                                                'Use the concept safely, including this important rule: a '
                                                'class is a definition, not an object; procedural code can '
                                                'still be the simpler choice.'],
                        'level_id': 95,
                        'line_by_line': [{'code': 'class Dog:',
                                          'explanation': 'Define the class Dog. This is the blueprint for '
                                                         'instances; the indented lines below describe its '
                                                         'data or behavior.',
                                          'line': '1'},
                                         {'code': '    pass',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '2'},
                                         {'code': 'rover = Dog()',
                                          'explanation': 'Store Dog() in rover so later instructions can use '
                                                         'it.',
                                          'line': '3'},
                                         {'code': 'spot = Dog()',
                                          'explanation': 'Store Dog() in spot so later instructions can use '
                                                         'it.',
                                          'line': '4'},
                                         {'code': "print('Rover is a Dog:', isinstance(rover, Dog))",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '5'},
                                         {'code': "print('Spot is distinct from Rover:', rover is not spot)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '6'}],
                        'practical_examples': [{'code': 'class Dog:\n'
                                                        '    pass\n'
                                                        'rover = Dog()\n'
                                                        'spot = Dog()\n'
                                                        "print('Rover is a Dog:', isinstance(rover, Dog))\n"
                                                        "print('Spot is distinct from Rover:', rover is not "
                                                        'spot)',
                                                'explanation': 'Purpose: Example 1: Blueprint concept: Class '
                                                               'vs Object shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Dog:\n'
                                                               'Define the class Dog. This is the blueprint '
                                                               'for instances; the indented lines below '
                                                               'describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: rover = Dog()\n'
                                                               'Store Dog() in rover so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 4: spot = Dog()\n'
                                                               'Store Dog() in spot so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               "Line 5: print('Rover is a Dog:', "
                                                               'isinstance(rover, Dog))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               "Line 6: print('Spot is distinct from "
                                                               "Rover:', rover is not spot)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Rover is a Dog: True\n'
                                                               'Spot is distinct from Rover: True',
                                                'output': 'Rover is a Dog: True\n'
                                                          'Spot is distinct from Rover: True',
                                                'title': 'Example 1: Blueprint concept: Class vs Object'},
                                               {'code': 'class Inventory:\n'
                                                        '    pass\n'
                                                        'bag = Inventory()\n'
                                                        "print('Object type name:', type(bag).__name__)",
                                                'explanation': 'Purpose: Example 2: Inspecting object types '
                                                               'with type() shows the current lesson idea in '
                                                               'a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Inventory:\n'
                                                               'Define the class Inventory. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: bag = Inventory()\n'
                                                               'Store Inventory() in bag so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 4: print('Object type name:', "
                                                               'type(bag).__name__)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Object type name: Inventory',
                                                'output': 'Object type name: Inventory',
                                                'title': 'Example 2: Inspecting object types with type()'},
                                               {'code': 'class BankAccount:\n'
                                                        '    pass\n'
                                                        'acct = BankAccount()\n'
                                                        "print('Account object allocated in memory.')",
                                                'explanation': 'Purpose: Example 3: Modeling real-world '
                                                               'entities shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class BankAccount:\n'
                                                               'Define the class BankAccount. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: acct = BankAccount()\n'
                                                               'Store BankAccount() in acct so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 4: print('Account object allocated in "
                                                               "memory.')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Account object allocated in '
                                                               'memory.',
                                                'output': 'Account object allocated in memory.',
                                                'title': 'Example 3: Modeling real-world entities'}],
                        'practice_questions': [{'answer': 'A class describes a kind of object; an instance '
                                                          'is one particular object with state and behavior.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Related data and actions are easier to manage '
                                                          'together for some programs.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'A class is a definition, not an object; '
                                                          'procedural code can still be the simpler choice.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is separate game characters '
                                           'that each have a name and health. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: A class is a blueprint; an instance is one real object made '
                                   'from it. A class is a definition, not an object; procedural code can '
                                   'still be the simpler choice The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'class Dog:\n'
                                            '    pass\n'
                                            'rover = Dog()\n'
                                            'spot = Dog()\n'
                                            "print('Rover is a Dog:', isinstance(rover, Dog))\n"
                                            "print('Spot is distinct from Rover:', rover is not spot)",
                        'terminology': [{'definition': 'A definition describing the data and behavior of a '
                                                       'kind of object.',
                                         'term': 'Class'},
                                        {'definition': 'One particular object created from a class.',
                                         'term': 'Instance'},
                                        {'definition': 'The data currently stored by an object.',
                                         'term': 'State'}],
                        'title': 'What Is Object-Oriented Programming?'},
             'number': 95,
             'quizzes': [{'explanation': 'h is an instance of Hero. Its hp attribute is initialized to 100 '
                                         'and printed.',
                          'options': [{'explanation': 'Correct! h.hp is 100.',
                                       'is_correct': True,
                                       'text': '100'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect. Printing h.hp accesses the attribute.',
                                       'is_correct': False,
                                       'text': '<Hero object at 0x...>'},
                                      {'explanation': 'Incorrect. hp is set in __init__.',
                                       'is_correct': False,
                                       'text': 'AttributeError'}],
                          'question': 'What is the output of this class instantiation code?\n'
                                      '\n'
                                      'class Hero:\n'
                                      '    def __init__(self, hp):\n'
                                      '        self.hp = hp\n'
                                      '\n'
                                      'h = Hero(100)\n'
                                      'print(h.hp)'},
                         {'explanation': 'The 4 pillars are Encapsulation, Abstraction, Inheritance, and '
                                         'Polymorphism. Compilation is a translation phase.',
                          'options': [{'explanation': 'Correct! The 4 pillars are Encapsulation, '
                                                      'Abstraction, Inheritance, and Polymorphism.',
                                       'is_correct': True,
                                       'text': 'Compilation'},
                                      {'explanation': 'A core OOP pillar.',
                                       'is_correct': False,
                                       'text': 'Encapsulation'},
                                      {'explanation': 'A core OOP pillar.',
                                       'is_correct': False,
                                       'text': 'Inheritance'},
                                      {'explanation': 'A core OOP pillar.',
                                       'is_correct': False,
                                       'text': 'Polymorphism'}],
                          'question': 'Which of the following is NOT one of the 4 core pillars of '
                                      'Object-Oriented Programming?'}],
             'title': 'What Is Object-Oriented Programming?'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create two separate CloudInstance objects.\n2. Use is not to check whether they are different objects, then print the result.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class CloudInstance:\n'
                                       '    pass\n'
                                       's1 = CloudInstance()\n'
                                       's2 = CloudInstance()\n'
                                       'print(s1 is not s2)'],
                             'initial_code': '# Object Identity in Memory\n'
                                             '# Step 1: Define CloudInstance:\n'
                                             '\n'
                                             '# Step 2: Create s1 and s2 and print(s1 is not s2):\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class CloudInstance:\n'
                                              '    pass\n'
                                              '\n'
                                              's1 = CloudInstance()\n'
                                              's2 = CloudInstance()\n'
                                              'print(s1 is not s2)',
                             'test_cases': [{'expected_output': 'True',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Server Node Instantiator',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Make a1 an Artifact object.\n2. Set a2 to refer to that same object, then make a3 as a new Artifact.\n3. Print whether a1 and a2 are the same object, then whether a1 and a3 are the same object.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Artifact:\n'
                                       '    pass\n'
                                       'a1 = Artifact()\n'
                                       'a2 = a1\n'
                                       'a3 = Artifact()\n'
                                       'print(a1 is a2)\n'
                                       'print(a1 is a3)'],
                             'initial_code': '# ⚔️ Boss Challenge: Memory Identity Verifier\n'
                                             'class Artifact:\n'
                                             '    pass\n'
                                             '\n'
                                             '# Step 1: a1 = Artifact(), a2 = a1, a3 = Artifact()\n'
                                             '\n'
                                             '# Step 2: Print a1 is a2 and a1 is a3 below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Artifact:\n'
                                              '    pass\n'
                                              '\n'
                                              'a1 = Artifact()\n'
                                              'a2 = a1\n'
                                              'a3 = Artifact()\n'
                                              'print(a1 is a2)\n'
                                              'print(a1 is a3)',
                             'test_cases': [{'expected_output': 'True\nFalse',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Memory Identity Verifier',
                             'xp_reward': 150}],
             'description': 'Define custom classes with PascalCase naming and instantiate live objects.',
             'lesson': {'common_mistakes': [{'fix': 'Create each object by calling the class, then set or '
                                                    'inspect its attributes.',
                                             'mistake': 'two instances of one class are separate objects '
                                                        'even if their attribute values match',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A class can make many objects with '
                                                'the same shape but independent state. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: Instantiation means calling a class to make '
                                                'an instance. Python uses this idea to each instance can '
                                                'store its own attributes; type() and isinstance() inspect '
                                                'its class relationship\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Two instances of one class are separate '
                                                'objects even if their attribute values match. If you change '
                                                'the example’s input or value, check this rule again because '
                                                'it can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Aria has 100 HP',
                        'id': 96,
                        'introduction': 'Why learn this? A class can make many objects with the same shape '
                                        'but independent state. In this lesson, we will see instantiation '
                                        'means calling a class to make an instance, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain instantiation means calling a class to make an '
                                                'instance in your own words.',
                                                'Trace a small Creating Classes and Instantiating Objects '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: two '
                                                'instances of one class are separate objects even if their '
                                                'attribute values match.'],
                        'level_id': 96,
                        'line_by_line': [{'code': 'class Hero:',
                                          'explanation': 'Define the class Hero. This is the blueprint for '
                                                         'instances; the indented lines below describe its '
                                                         'data or behavior.',
                                          'line': '1'},
                                         {'code': '    pass',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '2'},
                                         {'code': 'h1 = Hero()',
                                          'explanation': 'Store Hero() in h1 so later instructions can use '
                                                         'it.',
                                          'line': '3'},
                                         {'code': "h1.name = 'Aria'",
                                          'explanation': "Store 'Aria' in h1.name so later instructions can "
                                                         'use it.',
                                          'line': '4'},
                                         {'code': 'h1.hp = 100',
                                          'explanation': 'Store 100 in h1.hp so later instructions can use '
                                                         'it.',
                                          'line': '5'},
                                         {'code': "print(f'{h1.name} has {h1.hp} HP')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '6'}],
                        'practical_examples': [{'code': 'class Hero:\n'
                                                        '    pass\n'
                                                        'h1 = Hero()\n'
                                                        "h1.name = 'Aria'\n"
                                                        'h1.hp = 100\n'
                                                        "print(f'{h1.name} has {h1.hp} HP')",
                                                'explanation': 'Purpose: Example 1: Setting attributes '
                                                               'directly on instances shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Hero:\n'
                                                               'Define the class Hero. This is the blueprint '
                                                               'for instances; the indented lines below '
                                                               'describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: h1 = Hero()\n'
                                                               'Store Hero() in h1 so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               "Line 4: h1.name = 'Aria'\n"
                                                               "Store 'Aria' in h1.name so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: h1.hp = 100\n'
                                                               'Store 100 in h1.hp so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               "Line 6: print(f'{h1.name} has {h1.hp} HP')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Aria has 100 HP',
                                                'output': 'Aria has 100 HP',
                                                'title': 'Example 1: Setting attributes directly on '
                                                         'instances'},
                                               {'code': 'class Enemy:\n'
                                                        '    pass\n'
                                                        'e1 = Enemy()\n'
                                                        "e1.kind = 'Goblin'\n"
                                                        'e2 = Enemy()\n'
                                                        "e2.kind = 'Orc'\n"
                                                        "print('Enemies:', e1.kind, 'and', e2.kind)",
                                                'explanation': 'Purpose: Example 2: Multiple independent '
                                                               'instances shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Enemy:\n'
                                                               'Define the class Enemy. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: e1 = Enemy()\n'
                                                               'Store Enemy() in e1 so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               "Line 4: e1.kind = 'Goblin'\n"
                                                               "Store 'Goblin' in e1.kind so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: e2 = Enemy()\n'
                                                               'Store Enemy() in e2 so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               "Line 6: e2.kind = 'Orc'\n"
                                                               "Store 'Orc' in e2.kind so later instructions "
                                                               'can use it.\n'
                                                               '\n'
                                                               "Line 7: print('Enemies:', e1.kind, 'and', "
                                                               'e2.kind)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Enemies: Goblin and Orc',
                                                'output': 'Enemies: Goblin and Orc',
                                                'title': 'Example 2: Multiple independent instances'},
                                               {'code': 'class Weapon:\n'
                                                        '    pass\n'
                                                        'sword = Weapon()\n'
                                                        "print('Is sword a Weapon?', isinstance(sword, "
                                                        'Weapon))',
                                                'explanation': 'Purpose: Example 3: Checking class identity '
                                                               'with isinstance shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Weapon:\n'
                                                               'Define the class Weapon. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: sword = Weapon()\n'
                                                               'Store Weapon() in sword so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 4: print('Is sword a Weapon?', "
                                                               'isinstance(sword, Weapon))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Is sword a Weapon? True',
                                                'output': 'Is sword a Weapon? True',
                                                'title': 'Example 3: Checking class identity with '
                                                         'isinstance'}],
                        'practice_questions': [{'answer': 'Instantiation means calling a class to make an '
                                                          'instance.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A class can make many objects with the same shape '
                                                          'but independent state.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Two instances of one class are separate objects '
                                                          'even if their attribute values match.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is several game items each '
                                           'with their own name and durability. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Create each object by calling the class, then set or inspect '
                                   'its attributes. Two instances of one class are separate objects even if '
                                   'their attribute values match The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'class Hero:\n'
                                            '    pass\n'
                                            'h1 = Hero()\n'
                                            "h1.name = 'Aria'\n"
                                            'h1.hp = 100\n'
                                            "print(f'{h1.name} has {h1.hp} HP')",
                        'terminology': [{'definition': 'Call a class to create an instance.',
                                         'term': 'Instantiate'},
                                        {'definition': 'A value stored on an object or class.',
                                         'term': 'Attribute'},
                                        {'definition': 'Whether two references point to the same object.',
                                         'term': 'Identity'}],
                        'title': 'Creating Classes and Instantiating Objects'},
             'number': 96,
             'quizzes': [{'explanation': 'd1 and d2 are two distinct instances stored in different memory '
                                         'locations. d1 is d2 evaluates to False.',
                          'options': [{'explanation': 'Correct! Each instantiation creates a separate object '
                                                      'in memory.',
                                       'is_correct': True,
                                       'text': 'False'},
                                      {'explanation': 'Incorrect. They are separate instances.',
                                       'is_correct': False,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the identity operator comparison between two '
                                      'distinct instances?\n'
                                      '\n'
                                      'class Dog: pass\n'
                                      '\n'
                                      'd1 = Dog()\n'
                                      'd2 = Dog()\n'
                                      'print(d1 is d2)'},
                         {'explanation': 'PEP 8 specifies PascalCase (CapWords) for class names: e.g. '
                                         'GameCharacter, BankAccount.',
                          'options': [{'explanation': 'Correct! PascalCase / CapWords is the standard for '
                                                      'classes.',
                                       'is_correct': True,
                                       'text': 'PascalCase (e.g. BankAccount)'},
                                      {'explanation': 'Incorrect. snake_case is for functions and variables.',
                                       'is_correct': False,
                                       'text': 'snake_case (e.g. bank_account)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'camelCase (e.g. bankAccount)'},
                                      {'explanation': 'Incorrect. Used for constants.',
                                       'is_correct': False,
                                       'text': 'SCREAMING_SNAKE_CASE'}],
                          'question': 'What is the PEP 8 naming convention for class names in Python?'}],
             'title': 'Creating Classes and Instantiating Objects'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create a Player class that saves a name and score when an object is made.\n2. Read the name and score, make the player, and print them in the format shown.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class Player:\n'
                                       '    def __init__(self, name, score):\n'
                                       '        self.name = name\n'
                                       '        self.score = score\n'
                                       'p = Player(input().strip(), int(input()))\n'
                                       "print(f'{p.name}: {p.score}')"],
                             'initial_code': '# The __init__ Constructor Method\n'
                                             '# Step 1: Define class Player with __init__:\n'
                                             '\n'
                                             '# Step 2: Read inputs, instantiate p, and print below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Player:\n'
                                              '    def __init__(self, name, score):\n'
                                              '        self.name = name\n'
                                              '        self.score = int(score)\n'
                                              '\n'
                                              'name = input().strip()\n'
                                              'score = int(input())\n'
                                              'player = Player(name, score)\n'
                                              "print(f'{player.name}: {player.score}')",
                             'test_cases': [{'expected_output': 'Ada: 250',
                                             'input_data': 'Ada\n250\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Linus: 999',
                                             'input_data': 'Linus\n999\n',
                                             'is_hidden': False}],
                             'title': 'Player Stats Initializer',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Create a Book class whose page count is 100 when no count is given.\n2. Make one book with the default and another with 500 pages.\n3. Print each title and page count as shown.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Book:\n'
                                       '    def __init__(self, title, pages=100):\n'
                                       '        self.title = title\n'
                                       '        self.pages = pages\n'
                                       "b1 = Book('Short Tale')\n"
                                       "b2 = Book('Epic Saga', 500)\n"
                                       "print(f'{b1.title} ({b1.pages}p)')\n"
                                       "print(f'{b2.title} ({b2.pages}p)')"],
                             'initial_code': '# ⚔️ Boss Challenge: Constructor with Default Arguments\n'
                                             '# Step 1: Define Book with default pages=100:\n'
                                             '\n'
                                             '# Step 2: Instantiate b1 and b2 and print info below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Book:\n'
                                              '    def __init__(self, title, pages=100):\n'
                                              '        self.title = title\n'
                                              '        self.pages = pages\n'
                                              '\n'
                                              "short_tale = Book('Short Tale')\n"
                                              "epic_saga = Book('Epic Saga', 500)\n"
                                              "print(f'{short_tale.title} ({short_tale.pages}p)')\n"
                                              "print(f'{epic_saga.title} ({epic_saga.pages}p)')",
                             'test_cases': [{'expected_output': 'Short Tale (100p)\nEpic Saga (500p)',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Constructor with Default Arguments',
                             'xp_reward': 150}],
             'description': 'Initialize object state upon creation using the __init__ dunder method and the '
                            'self reference.',
             'lesson': {'common_mistakes': [{'fix': 'Use __init__ to put each new instance into a useful '
                                                    'starting state.',
                                             'mistake': '__init__ does not allocate the object; __new__ '
                                                        'handles object creation',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: New objects often need valid starting '
                                                'values. This is the practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: __init__ initializes an already-created '
                                                'instance; self refers to that instance by convention. '
                                                'Python uses this idea to className(args) creates an object '
                                                'and Python calls __init__(self, args) to initialize it\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: __init__ does not allocate the object; '
                                                '__new__ handles object creation. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Vehicle: Tesla Model 3',
                        'id': 97,
                        'introduction': 'Why learn this? New objects often need valid starting values. In '
                                        'this lesson, we will see __init__ initializes an already-created '
                                        'instance; self refers to that instance by convention, follow how '
                                        'Python handles it, and practice a small example you can change '
                                        'yourself.',
                        'learning_objectives': ['Explain __init__ initializes an already-created instance; '
                                                'self refers to that instance by convention in your own '
                                                'words.',
                                                'Trace a small The Constructor (__init__) and self example '
                                                'and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                '__init__ does not allocate the object; __new__ handles '
                                                'object creation.'],
                        'level_id': 97,
                        'line_by_line': [{'code': 'class Car:',
                                          'explanation': 'Define the class Car. This is the blueprint for '
                                                         'instances; the indented lines below describe its '
                                                         'data or behavior.',
                                          'line': '1'},
                                         {'code': '    def __init__(self, make, model):',
                                          'explanation': 'Define a function named __init__. Its parameters '
                                                         '(self, make, model) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '2'},
                                         {'code': '        self.make = make',
                                          'explanation': 'Store make in self.make so later instructions can '
                                                         'use it.',
                                          'line': '3'},
                                         {'code': '        self.model = model',
                                          'explanation': 'Store model in self.model so later instructions '
                                                         'can use it.',
                                          'line': '4'},
                                         {'code': "my_car = Car('Tesla', 'Model 3')",
                                          'explanation': "Store Car('Tesla', 'Model 3') in my_car so later "
                                                         'instructions can use it.',
                                          'line': '5'},
                                         {'code': "print(f'Vehicle: {my_car.make} {my_car.model}')",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '6'}],
                        'practical_examples': [{'code': 'class Car:\n'
                                                        '    def __init__(self, make, model):\n'
                                                        '        self.make = make\n'
                                                        '        self.model = model\n'
                                                        "my_car = Car('Tesla', 'Model 3')\n"
                                                        "print(f'Vehicle: {my_car.make} {my_car.model}')",
                                                'explanation': 'Purpose: Example 1: Initializing car objects '
                                                               'with constructor shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Car:\n'
                                                               'Define the class Car. This is the blueprint '
                                                               'for instances; the indented lines below '
                                                               'describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, make, model):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, make, model) are local '
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.make = make\n'
                                                               'Store make in self.make so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: self.model = model\n'
                                                               'Store model in self.model so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 5: my_car = Car('Tesla', 'Model 3')\n"
                                                               "Store Car('Tesla', 'Model 3') in my_car so "
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               "Line 6: print(f'Vehicle: {my_car.make} "
                                                               "{my_car.model}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Vehicle: Tesla Model 3',
                                                'output': 'Vehicle: Tesla Model 3',
                                                'title': 'Example 1: Initializing car objects with '
                                                         'constructor'},
                                               {'code': 'class Account:\n'
                                                        '    def __init__(self, owner, balance=0.0):\n'
                                                        '        self.owner = owner\n'
                                                        '        self.balance = balance\n'
                                                        "acct = Account('Sarah Connor', 500.0)\n"
                                                        "print(f'Account: {acct.owner} | Balance: "
                                                        "${acct.balance}')",
                                                'explanation': 'Purpose: Example 2: Initializing bank '
                                                               'account with default zero balance shows the '
                                                               'current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Account:\n'
                                                               'Define the class Account. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, owner, '
                                                               'balance=0.0):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, owner, balance=0.0) are '
                                                               'local names that receive values when the '
                                                               'function is called. The colon starts the '
                                                               'indented body; defining it does not run it '
                                                               'yet.\n'
                                                               '\n'
                                                               'Line 3: self.owner = owner\n'
                                                               'Store owner in self.owner so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: self.balance = balance\n'
                                                               'Store balance in self.balance so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 5: acct = Account('Sarah Connor', "
                                                               '500.0)\n'
                                                               "Store Account('Sarah Connor', 500.0) in acct "
                                                               'so later instructions can use it.\n'
                                                               '\n'
                                                               "Line 6: print(f'Account: {acct.owner} | "
                                                               "Balance: ${acct.balance}')\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Account: Sarah Connor | '
                                                               'Balance: $500.0',
                                                'output': 'Account: Sarah Connor | Balance: $500.0',
                                                'title': 'Example 2: Initializing bank account with default '
                                                         'zero balance'},
                                               {'code': 'class Party:\n'
                                                        '    def __init__(self, leader):\n'
                                                        '        self.leader = leader\n'
                                                        '        self.members = []\n'
                                                        "p = Party('Alex')\n"
                                                        "p.members.append('Sam')\n"
                                                        "print('Party size:', len(p.members) + 1)",
                                                'explanation': 'Purpose: Example 3: Initializing collections '
                                                               'inside __init__ shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Party:\n'
                                                               'Define the class Party. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, leader):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, leader) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.leader = leader\n'
                                                               'Store leader in self.leader so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: self.members = []\n'
                                                               'Create the list shown and store it in '
                                                               'self.members. The list keeps items in order '
                                                               'and can be processed one item at a time.\n'
                                                               '\n'
                                                               "Line 5: p = Party('Alex')\n"
                                                               "Store Party('Alex') in p so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 6: p.members.append('Sam')\n"
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 7: print('Party size:', len(p.members) "
                                                               '+ 1)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Party size: 2',
                                                'output': 'Party size: 2',
                                                'title': 'Example 3: Initializing collections inside '
                                                         '__init__'}],
                        'practice_questions': [{'answer': '__init__ initializes an already-created instance; '
                                                          'self refers to that instance by convention.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'New objects often need valid starting values.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': '__init__ does not allocate the object; __new__ '
                                                          'handles object creation.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is setting a new account’s '
                                           'owner and starting cents balance. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Use __init__ to put each new instance into a useful starting '
                                   'state. __init__ does not allocate the object; __new__ handles object '
                                   'creation The practical example and its line-by-line walkthrough show the '
                                   'idea in action.',
                        'syntax_breakdown': 'class Car:\n'
                                            '    def __init__(self, make, model):\n'
                                            '        self.make = make\n'
                                            '        self.model = model\n'
                                            "my_car = Car('Tesla', 'Model 3')\n"
                                            "print(f'Vehicle: {my_car.make} {my_car.model}')",
                        'terminology': [{'definition': 'The initializer Python calls to set up a new '
                                                       'instance.',
                                         'term': '__init__'},
                                        {'definition': 'The conventional first parameter referring to the '
                                                       'current instance.',
                                         'term': 'self'},
                                        {'definition': 'The lower-level method responsible for creating an '
                                                       'instance.',
                                         'term': '__new__'}],
                        'title': 'The Constructor (__init__) and self'},
             'number': 97,
             'quizzes': [{'explanation': '`self` represents the specific instance on which the method was '
                                         'called.',
                          'options': [{'explanation': 'Correct! self binds method calls to the caller '
                                                      'instance.',
                                       'is_correct': True,
                                       'text': 'The specific instance of the class being acted upon'},
                                      {'explanation': 'Incorrect. That is cls in class methods.',
                                       'is_correct': False,
                                       'text': 'The class definition itself'},
                                      {'explanation': 'Incorrect. That is super().',
                                       'is_correct': False,
                                       'text': 'The parent superclass'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'A global namespace pointer'}],
                          'question': 'What does `self` represent inside an instance method in a Python '
                                      'class?'},
                         {'explanation': "__init__ assigns 'Alex' to self.name, which is retrieved via "
                                         'p.name.',
                          'options': [{'explanation': 'Correct! p.name accesses the initialized attribute.',
                                       'is_correct': True,
                                       'text': 'Alex'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'name'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'AttributeError'}],
                          'question': 'What will be printed when running this code?\n'
                                      '\n'
                                      'class Player:\n'
                                      '    def __init__(self, name):\n'
                                      '        self.name = name\n'
                                      '\n'
                                      "p = Player('Alex')\n"
                                      'print(p.name)'}],
             'title': 'The Constructor (__init__) and self'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Each pet has its own name.\n2. Every pet shares the same species label stored on the class.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class Pet:\n'
                                       "    species = 'cat'\n"
                                       '    def __init__(self, name):\n'
                                       '        self.name = name\n'
                                       "first = Pet('Mia')\n"
                                       "second = Pet('Bo')\n"
                                       'print(first.name, first.species)\n'
                                       'print(second.name, second.species)'],
                             'initial_code': '# Instance Methods and State Mutation\n'
                                             '# Step 1: Define BankAccount class:\n'
                                             '\n'
                                             '# Step 2: Test deposit and print balance below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Pet:\n'
                                              "    species = 'cat'\n"
                                              '    def __init__(self, name):\n'
                                              '        self.name = name\n'
                                              "first = Pet('Mia')\n"
                                              "second = Pet('Bo')\n"
                                              'print(first.name, first.species)\n'
                                              'print(second.name, second.species)',
                             'test_cases': [{'expected_output': 'Mia cat\nBo cat',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Compare Instance and Class Attributes',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Change the shared tax rate once, then use it to calculate totals for two products.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Product:\n'
                                       '    tax_rate = 0.05\n'
                                       '    def __init__(self, price):\n'
                                       '        self.price = price\n'
                                       '    def total(self):\n'
                                       '        return self.price * (1 + Product.tax_rate)\n'
                                       'Product.tax_rate = 0.10\n'
                                       'for product in (Product(100), Product(200)):\n'
                                       "    print(f'{product.total():.2f}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Stateful Counter Machine\n'
                                             '# Step 1: Define Counter with increment, decrement, reset:\n'
                                             '\n'
                                             '# Step 2: Perform sequence and print results:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Product:\n'
                                              '    tax_rate = 0.05\n'
                                              '    def __init__(self, price):\n'
                                              '        self.price = price\n'
                                              '    def total(self):\n'
                                              '        return self.price * (1 + Product.tax_rate)\n'
                                              'Product.tax_rate = 0.10\n'
                                              'for product in (Product(100), Product(200)):\n'
                                              "    print(f'{product.total():.2f}')",
                             'test_cases': [{'expected_output': '110.00\n220.00',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Shared Class Setting',
                             'xp_reward': 150}],
             'description': 'Distinguish between data belonging to an individual object versus data shared '
                            'across all instances.',
             'lesson': {'common_mistakes': [{'fix': 'Put personal state on instances and truly shared '
                                                    'constants on the class.',
                                             'mistake': 'a mutable class list is shared by every instance '
                                                        'unless intentionally managed',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Some facts belong to one object while '
                                                'others belong to the class as a whole. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: Instance attributes live on one instance; '
                                                'class attributes live on the class. Python uses this idea '
                                                'to lookup checks the instance first, then the class; '
                                                'assigning an instance value can shadow a class value\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: A mutable class list is shared by every '
                                                'instance unless intentionally managed. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Total users registered: 2',
                        'id': 98,
                        'introduction': 'Why learn this? Some facts belong to one object while others belong '
                                        'to the class as a whole. In this lesson, we will see instance '
                                        'attributes live on one instance; class attributes live on the '
                                        'class, follow how Python handles it, and practice a small example '
                                        'you can change yourself.',
                        'learning_objectives': ['Explain instance attributes live on one instance; class '
                                                'attributes live on the class in your own words.',
                                                'Trace a small Instance Attributes vs Class Attributes '
                                                'example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: a '
                                                'mutable class list is shared by every instance unless '
                                                'intentionally managed.'],
                        'level_id': 98,
                        'line_by_line': [{'code': 'class User:',
                                          'explanation': 'Define the class User. This is the blueprint for '
                                                         'instances; the indented lines below describe its '
                                                         'data or behavior.',
                                          'line': '1'},
                                         {'code': '    user_count = 0',
                                          'explanation': 'Store 0 in user_count so later instructions can '
                                                         'use it.',
                                          'line': '2'},
                                         {'code': '    def __init__(self, username):',
                                          'explanation': 'Define a function named __init__. Its parameters '
                                                         '(self, username) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '3'},
                                         {'code': '        self.username = username',
                                          'explanation': 'Store username in self.username so later '
                                                         'instructions can use it.',
                                          'line': '4'},
                                         {'code': '        User.user_count += 1',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '5'},
                                         {'code': "u1 = User('Alice')",
                                          'explanation': "Store User('Alice') in u1 so later instructions "
                                                         'can use it.',
                                          'line': '6'},
                                         {'code': "u2 = User('Bob')",
                                          'explanation': "Store User('Bob') in u2 so later instructions can "
                                                         'use it.',
                                          'line': '7'},
                                         {'code': "print('Total users registered:', User.user_count)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '8'}],
                        'practical_examples': [{'code': 'class User:\n'
                                                        '    user_count = 0\n'
                                                        '    def __init__(self, username):\n'
                                                        '        self.username = username\n'
                                                        '        User.user_count += 1\n'
                                                        "u1 = User('Alice')\n"
                                                        "u2 = User('Bob')\n"
                                                        "print('Total users registered:', User.user_count)",
                                                'explanation': 'Purpose: Example 1: Tracking total instances '
                                                               'created using class variable shows the '
                                                               'current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class User:\n'
                                                               'Define the class User. This is the blueprint '
                                                               'for instances; the indented lines below '
                                                               'describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: user_count = 0\n'
                                                               'Store 0 in user_count so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 3: def __init__(self, username):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, username) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 4: self.username = username\n'
                                                               'Store username in self.username so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: User.user_count += 1\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 6: u1 = User('Alice')\n"
                                                               "Store User('Alice') in u1 so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 7: u2 = User('Bob')\n"
                                                               "Store User('Bob') in u2 so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 8: print('Total users registered:', "
                                                               'User.user_count)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Total users registered: 2',
                                                'output': 'Total users registered: 2',
                                                'title': 'Example 1: Tracking total instances created using '
                                                         'class variable'},
                                               {'code': 'class Server:\n'
                                                        "    status = 'MAINTENANCE'\n"
                                                        's1 = Server()\n'
                                                        's2 = Server()\n'
                                                        "Server.status = 'ONLINE'\n"
                                                        "print('S1 status:', s1.status, '| S2 status:', "
                                                        's2.status)',
                                                'explanation': 'Purpose: Example 2: Modifying class '
                                                               'attribute for all instances shows the '
                                                               'current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Server:\n'
                                                               'Define the class Server. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               "Line 2: status = 'MAINTENANCE'\n"
                                                               "Store 'MAINTENANCE' in status so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 3: s1 = Server()\n'
                                                               'Store Server() in s1 so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 4: s2 = Server()\n'
                                                               'Store Server() in s2 so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               "Line 5: Server.status = 'ONLINE'\n"
                                                               "Store 'ONLINE' in Server.status so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 6: print('S1 status:', s1.status, '| S2 "
                                                               "status:', s2.status)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: S1 status: ONLINE | S2 status: '
                                                               'ONLINE',
                                                'output': 'S1 status: ONLINE | S2 status: ONLINE',
                                                'title': 'Example 2: Modifying class attribute for all '
                                                         'instances'},
                                               {'code': 'class Drone:\n'
                                                        '    battery = 100\n'
                                                        'd1 = Drone()\n'
                                                        'd2 = Drone()\n'
                                                        'd1.battery = 80  # Shadows class attribute on d1 '
                                                        'only!\n'
                                                        "print('D1 battery:', d1.battery, '| D2 battery:', "
                                                        'd2.battery)',
                                                'explanation': 'Purpose: Example 3: Instance attribute '
                                                               'shadowing class attribute shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Drone:\n'
                                                               'Define the class Drone. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: battery = 100\n'
                                                               'Store 100 in battery so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 3: d1 = Drone()\n'
                                                               'Store Drone() in d1 so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 4: d2 = Drone()\n'
                                                               'Store Drone() in d2 so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 5: d1.battery = 80  # Shadows class '
                                                               'attribute on d1 only!\n'
                                                               'Store 80  # Shadows class attribute on d1 '
                                                               'only! in d1.battery so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               "Line 6: print('D1 battery:', d1.battery, '| "
                                                               "D2 battery:', d2.battery)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: D1 battery: 80 | D2 battery: '
                                                               '100',
                                                'output': 'D1 battery: 80 | D2 battery: 100',
                                                'title': 'Example 3: Instance attribute shadowing class '
                                                         'attribute'}],
                        'practice_questions': [{'answer': 'Instance attributes live on one instance; class '
                                                          'attributes live on the class.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Some facts belong to one object while others '
                                                          'belong to the class as a whole.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'A mutable class list is shared by every instance '
                                                          'unless intentionally managed.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a shared game rule with '
                                           'separate player scores. The same pattern helps a larger program '
                                           'stay clear when it handles the same kind of task repeatedly.',
                        'summary': 'Remember: Put personal state on instances and truly shared constants on '
                                   'the class. A mutable class list is shared by every instance unless '
                                   'intentionally managed The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'class User:\n'
                                            '    user_count = 0\n'
                                            '    def __init__(self, username):\n'
                                            '        self.username = username\n'
                                            '        User.user_count += 1\n'
                                            "u1 = User('Alice')\n"
                                            "u2 = User('Bob')\n"
                                            "print('Total users registered:', User.user_count)",
                        'terminology': [{'definition': 'A value stored on one particular object.',
                                         'term': 'Instance attribute'},
                                        {'definition': 'A value looked up on the class and potentially '
                                                       'shared.',
                                         'term': 'Class attribute'},
                                        {'definition': 'An instance attribute taking precedence over a class '
                                                       'attribute of the same name.',
                                         'term': 'Shadowing'}],
                        'title': 'Instance Attributes vs Class Attributes'},
             'number': 98,
             'quizzes': [{'explanation': 'Modifying the class attribute on Config updates the shared '
                                         "attribute for all instances that haven't shadowed it: 2.5 2.5.",
                          'options': [{'explanation': 'Correct! Class attributes are shared across all '
                                                      'instances.',
                                       'is_correct': True,
                                       'text': '2.5 2.5'},
                                      {'explanation': 'Incorrect. Modifying Config.rate affects instances.',
                                       'is_correct': False,
                                       'text': '1.0 1.0'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '2.5 1.0'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'AttributeError'}],
                          'question': 'What is the output of class attribute versus instance attribute?\n'
                                      '\n'
                                      'class Config:\n'
                                      '    rate = 1.0\n'
                                      '\n'
                                      'c1 = Config()\n'
                                      'c2 = Config()\n'
                                      'Config.rate = 2.5\n'
                                      'print(c1.rate, c2.rate)'},
                         {'explanation': 'Assigning to c1.rate creates an instance attribute on c1, '
                                         'shadowing the class attribute without affecting c2.',
                          'options': [{'explanation': 'Correct! Assignment via instance binds a local '
                                                      'instance attribute.',
                                       'is_correct': True,
                                       'text': 'It creates an instance attribute on c1, leaving c2 '
                                               'unaffected'},
                                      {'explanation': 'Incorrect. Modifying through an instance does not '
                                                      'change the class attribute.',
                                       'is_correct': False,
                                       'text': 'It updates Config.rate globally'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It raises an AttributeError'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It changes c2.rate to 5.0 as well'}],
                          'question': 'What happens if you assign `c1.rate = 5.0` in the previous snippet?'}],
             'title': 'Instance Attributes vs Class Attributes'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Define a method that uses self to add points to one player.\n2. Create a player, add points, and print the score.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class Player:\n'
                                       '    def __init__(self, name):\n'
                                       '        self.name = name\n'
                                       '        self.score = 0\n'
                                       '    def add_points(self, points):\n'
                                       '        self.score += points\n'
                                       "player = Player('Mia')\n"
                                       'player.add_points(25)\n'
                                       "print(f'{player.name}: {player.score}')"],
                             'initial_code': '# Class Variables: Shared Across Instances\n'
                                             '# Step 1: Define Robot with population class variable:\n'
                                             '\n'
                                             '# Step 2: Create 3 robots and print Robot.population:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Player:\n'
                                              '    def __init__(self, name):\n'
                                              '        self.name = name\n'
                                              '        self.score = 0\n'
                                              '    def add_points(self, points):\n'
                                              '        self.score += points\n'
                                              "player = Player('Mia')\n"
                                              'player.add_points(25)\n'
                                              "print(f'{player.name}: {player.score}')",
                             'test_cases': [{'expected_output': 'Mia: 25',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Use an Instance Method',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Add a method that changes the player score and another that returns it.\n2. Call both methods.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Player:\n'
                                       '    def __init__(self, name):\n'
                                       '        self.name = name\n'
                                       '        self.score = 0\n'
                                       '    def add_points(self, points):\n'
                                       '        self.score += points\n'
                                       '    def get_score(self):\n'
                                       '        return self.score\n'
                                       "player = Player('Ari')\n"
                                       'player.add_points(10)\n'
                                       'player.add_points(5)\n'
                                       'print(player.get_score())'],
                             'initial_code': '# ⚔️ Boss Challenge: Global Tax Policy\n'
                                             '# Step 1: Define Product with tax_rate class variable:\n'
                                             '\n'
                                             '# Step 2: Instantiate p1 and p2 and print totals (.2f):\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Player:\n'
                                              '    def __init__(self, name):\n'
                                              '        self.name = name\n'
                                              '        self.score = 0\n'
                                              '    def add_points(self, points):\n'
                                              '        self.score += points\n'
                                              '    def get_score(self):\n'
                                              '        return self.score\n'
                                              "player = Player('Ari')\n"
                                              'player.add_points(10)\n'
                                              'player.add_points(5)\n'
                                              'print(player.get_score())',
                             'test_cases': [{'expected_output': '15', 'input_data': '', 'is_hidden': False}],
                             'title': 'Boss Challenge: Player Score Methods',
                             'xp_reward': 150}],
             'description': 'Define behavior and business logic that operates on instance state.',
             'lesson': {'common_mistakes': [{'fix': 'Methods combine an object’s data with actions that use '
                                                    'that data.',
                                             'mistake': 'self is the conventional first parameter and must '
                                                        'be present in the definition',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Objects need actions that read or '
                                                'change their own state. This is the practical problem the '
                                                'feature solves.\n'
                                                '\n'
                                                'What it means: A method is a function defined in a class; '
                                                'an instance method receives self. Python uses this idea to '
                                                'python binds the instance when calling obj.method(args); '
                                                'return can give a result back\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Self is the conventional first parameter '
                                                'and must be present in the definition. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Balance: $ 80',
                        'id': 99,
                        'introduction': 'Why learn this? Objects need actions that read or change their own '
                                        'state. In this lesson, we will see a method is a function defined '
                                        'in a class; an instance method receives self, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain a method is a function defined in a class; an '
                                                'instance method receives self in your own words.',
                                                'Trace a small Methods (Instance Methods) example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: self '
                                                'is the conventional first parameter and must be present in '
                                                'the definition.'],
                        'level_id': 99,
                        'line_by_line': [{'code': 'class Wallet:',
                                          'explanation': 'Define the class Wallet. This is the blueprint for '
                                                         'instances; the indented lines below describe its '
                                                         'data or behavior.',
                                          'line': '1'},
                                         {'code': '    def __init__(self, initial=0):',
                                          'explanation': 'Define a function named __init__. Its parameters '
                                                         '(self, initial=0) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '2'},
                                         {'code': '        self.balance = initial',
                                          'explanation': 'Store initial in self.balance so later '
                                                         'instructions can use it.',
                                          'line': '3'},
                                         {'code': '    def deposit(self, amt):',
                                          'explanation': 'Define a function named deposit. Its parameters '
                                                         '(self, amt) are local names that receive values '
                                                         'when the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '4'},
                                         {'code': '        self.balance += amt',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '5'},
                                         {'code': '    def get_balance(self):',
                                          'explanation': 'Define a function named get_balance. Its '
                                                         'parameters (self) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '6'},
                                         {'code': '        return self.balance',
                                          'explanation': 'Send self.balance back to the caller and end this '
                                                         'function call.',
                                          'line': '7'},
                                         {'code': 'w = Wallet(50)',
                                          'explanation': 'Store Wallet(50) in w so later instructions can '
                                                         'use it.',
                                          'line': '8'},
                                         {'code': 'w.deposit(30)',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '9'},
                                         {'code': "print('Balance: $', w.get_balance())",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '10'}],
                        'practical_examples': [{'code': 'class Wallet:\n'
                                                        '    def __init__(self, initial=0):\n'
                                                        '        self.balance = initial\n'
                                                        '    def deposit(self, amt):\n'
                                                        '        self.balance += amt\n'
                                                        '    def get_balance(self):\n'
                                                        '        return self.balance\n'
                                                        'w = Wallet(50)\n'
                                                        'w.deposit(30)\n'
                                                        "print('Balance: $', w.get_balance())",
                                                'explanation': 'Purpose: Example 1: Bank deposit and '
                                                               'withdrawal methods shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Wallet:\n'
                                                               'Define the class Wallet. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, initial=0):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, initial=0) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.balance = initial\n'
                                                               'Store initial in self.balance so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: def deposit(self, amt):\n'
                                                               'Define a function named deposit. Its '
                                                               'parameters (self, amt) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 5: self.balance += amt\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 6: def get_balance(self):\n'
                                                               'Define a function named get_balance. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 7: return self.balance\n'
                                                               'Send self.balance back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 8: w = Wallet(50)\n'
                                                               'Store Wallet(50) in w so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 9: w.deposit(30)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 10: print('Balance: $', "
                                                               'w.get_balance())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Balance: $ 80',
                                                'output': 'Balance: $ 80',
                                                'title': 'Example 1: Bank deposit and withdrawal methods'},
                                               {'code': 'class Book:\n'
                                                        '    def __init__(self, title, author):\n'
                                                        '        self.title = title\n'
                                                        '        self.author = author\n'
                                                        '    def describe(self):\n'
                                                        '        return f\'"{self.title}" by '
                                                        "{self.author}'\n"
                                                        "b = Book('1984', 'George Orwell')\n"
                                                        'print(b.describe())',
                                                'explanation': 'Purpose: Example 2: Formatted presentation '
                                                               'method shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Book:\n'
                                                               'Define the class Book. This is the blueprint '
                                                               'for instances; the indented lines below '
                                                               'describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, title, author):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, title, author) are local '
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.title = title\n'
                                                               'Store title in self.title so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: self.author = author\n'
                                                               'Store author in self.author so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: def describe(self):\n'
                                                               'Define a function named describe. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 6: return f\'"{self.title}" by '
                                                               "{self.author}'\n"
                                                               'Send f\'"{self.title}" by {self.author}\' '
                                                               'back to the caller and end this function '
                                                               'call.\n'
                                                               '\n'
                                                               "Line 7: b = Book('1984', 'George Orwell')\n"
                                                               "Store Book('1984', 'George Orwell') in b so "
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               'Line 8: print(b.describe())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: "1984" by George Orwell',
                                                'output': '"1984" by George Orwell',
                                                'title': 'Example 2: Formatted presentation method'},
                                               {'code': 'class Counter:\n'
                                                        '    def __init__(self):\n'
                                                        '        self.val = 0\n'
                                                        '    def inc(self):\n'
                                                        '        self.val += 1\n'
                                                        '        return self\n'
                                                        'c = Counter().inc().inc()\n'
                                                        "print('Value:', c.val)",
                                                'explanation': 'Purpose: Example 3: Method chaining pattern '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Counter:\n'
                                                               'Define the class Counter. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.val = 0\n'
                                                               'Store 0 in self.val so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 4: def inc(self):\n'
                                                               'Define a function named inc. Its parameters '
                                                               '(self) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               'Line 5: self.val += 1\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 6: return self\n'
                                                               'Send self back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 7: c = Counter().inc().inc()\n'
                                                               'Store Counter().inc().inc() in c so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 8: print('Value:', c.val)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Value: 2',
                                                'output': 'Value: 2',
                                                'title': 'Example 3: Method chaining pattern'}],
                        'practice_questions': [{'answer': 'A method is a function defined in a class; an '
                                                          'instance method receives self.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Objects need actions that read or change their '
                                                          'own state.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Self is the conventional first parameter and must '
                                                          'be present in the definition.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a wallet object with '
                                           'deposit and balance actions. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Methods combine an object’s data with actions that use that '
                                   'data. Self is the conventional first parameter and must be present in '
                                   'the definition The practical example and its line-by-line walkthrough '
                                   'show the idea in action.',
                        'syntax_breakdown': 'class Wallet:\n'
                                            '    def __init__(self, initial=0):\n'
                                            '        self.balance = initial\n'
                                            '    def deposit(self, amt):\n'
                                            '        self.balance += amt\n'
                                            '    def get_balance(self):\n'
                                            '        return self.balance\n'
                                            'w = Wallet(50)\n'
                                            'w.deposit(30)\n'
                                            "print('Balance: $', w.get_balance())",
                        'terminology': [{'definition': 'A function defined in a class.', 'term': 'Method'},
                                        {'definition': 'A method whose first parameter receives the '
                                                       'instance.',
                                         'term': 'Instance method'},
                                        {'definition': 'A method accessed through an instance with that '
                                                       'instance already supplied.',
                                         'term': 'Bound method'}],
                        'title': 'Methods (Instance Methods)'},
             'number': 99,
             'quizzes': [{'explanation': 'c.inc() increases val to 1, then the second call increases val to '
                                         '2 and returns 2.',
                          'options': [{'explanation': 'Correct! The method modifies self.val across calls: 0 '
                                                      '-> 1 -> 2.',
                                       'is_correct': True,
                                       'text': '2'},
                                      {'explanation': 'Incorrect. inc() was called twice.',
                                       'is_correct': False,
                                       'text': '1'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '0'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'}],
                          'question': 'What is the output of this method call?\n'
                                      '\n'
                                      'class Counter:\n'
                                      '    def __init__(self):\n'
                                      '        self.val = 0\n'
                                      '    def inc(self):\n'
                                      '        self.val += 1\n'
                                      '        return self.val\n'
                                      '\n'
                                      'c = Counter()\n'
                                      'c.inc()\n'
                                      'print(c.inc())'},
                         {'explanation': 'Using `self.method_name()` enables instance methods to call peer '
                                         'methods.',
                          'options': [{'explanation': 'Correct! Methods on the same instance are called '
                                                      'through self.',
                                       'is_correct': True,
                                       'text': 'self.other_method()'},
                                      {'explanation': 'Incorrect. Without self, Python searches for a '
                                                      'standalone function in global scope.',
                                       'is_correct': False,
                                       'text': 'other_method() directly without self'},
                                      {'explanation': 'Incorrect. Python uses self, not this.',
                                       'is_correct': False,
                                       'text': 'this.other_method()'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'super.other_method()'}],
                          'question': 'How does an instance method call another instance method on the same '
                                      'object in Python?'}],
             'title': 'Methods (Instance Methods)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Store the balance in a name-mangled private attribute.\n2. Expose it through a method and print the balance.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class Account:\n'
                                       '    def __init__(self, balance):\n'
                                       '        self.__balance = balance\n'
                                       '    def get_balance(self):\n'
                                       '        return self.__balance\n'
                                       'account = Account(250)\n'
                                       'print(account.get_balance())'],
                             'initial_code': '# Inheritance: Reusing and Extending Classes\n'
                                             '# Step 1: Define Animal and Dog(Animal):\n'
                                             '\n'
                                             '# Step 2: Instantiate Dog and print speak() below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Account:\n'
                                              '    def __init__(self, balance):\n'
                                              '        self.__balance = balance\n'
                                              '    def get_balance(self):\n'
                                              '        return self.__balance\n'
                                              'account = Account(250)\n'
                                              'print(account.get_balance())',
                             'test_cases': [{'expected_output': '250', 'input_data': '', 'is_hidden': False}],
                             'title': 'Hide an Account Balance',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Keep the balance private.\n2. Add a deposit method that refuses negative amounts and keeps the old balance.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Account:\n'
                                       '    def __init__(self, balance):\n'
                                       '        self.__balance = balance\n'
                                       '    def deposit(self, amount):\n'
                                       '        if amount < 0:\n'
                                       "            return 'Deposit must not be negative'\n"
                                       '        self.__balance += amount\n'
                                       "        return 'Deposit accepted'\n"
                                       '    def get_balance(self):\n'
                                       '        return self.__balance\n'
                                       'account = Account(100)\n'
                                       'print(account.deposit(-5))\n'
                                       'print(account.get_balance())'],
                             'initial_code': '# ⚔️ Boss Challenge: Specialized Vehicle Hierarchy\n'
                                             '# Step 1: Define Vehicle and Car(Vehicle):\n'
                                             '\n'
                                             '# Step 2: Call c.move() and c.drive() below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Account:\n'
                                              '    def __init__(self, balance):\n'
                                              '        self.__balance = balance\n'
                                              '    def deposit(self, amount):\n'
                                              '        if amount < 0:\n'
                                              "            return 'Deposit must not be negative'\n"
                                              '        self.__balance += amount\n'
                                              "        return 'Deposit accepted'\n"
                                              '    def get_balance(self):\n'
                                              '        return self.__balance\n'
                                              'account = Account(100)\n'
                                              'print(account.deposit(-5))\n'
                                              'print(account.get_balance())',
                             'test_cases': [{'expected_output': 'Deposit must not be negative\n100',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Reject an Invalid Deposit',
                             'xp_reward': 150}],
             'description': 'Protect internal invariants using public, protected (_single_underscore), and '
                            'private (__dunder) attributes.',
             'lesson': {'common_mistakes': [{'fix': 'Use a clear interface and validation; underscores are '
                                                    'conventions, not locks.',
                                             'mistake': 'Python does not enforce private access; mangling is '
                                                        'not encryption or security',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Object state should be changed '
                                                'through rules the class can check. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: Encapsulation groups state with methods that '
                                                'control how it is used. Python uses this idea to public '
                                                'names are ordinary; _name signals internal use; __name '
                                                'triggers name mangling\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Python does not enforce private access; '
                                                'mangling is not encryption or security. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Verified Balance: 150',
                        'id': 100,
                        'introduction': 'Why learn this? Object state should be changed through rules the '
                                        'class can check. In this lesson, we will see encapsulation groups '
                                        'state with methods that control how it is used, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain encapsulation groups state with methods that '
                                                'control how it is used in your own words.',
                                                'Trace a small Encapsulation and Data Hiding example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'Python does not enforce private access; mangling is not '
                                                'encryption or security.'],
                        'level_id': 100,
                        'line_by_line': [{'code': 'class BankAcct:',
                                          'explanation': 'Define the class BankAcct. This is the blueprint '
                                                         'for instances; the indented lines below describe '
                                                         'its data or behavior.',
                                          'line': '1'},
                                         {'code': '    def __init__(self, initial):',
                                          'explanation': 'Define a function named __init__. Its parameters '
                                                         '(self, initial) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '2'},
                                         {'code': '        self.__balance = initial',
                                          'explanation': 'Store initial in self.__balance so later '
                                                         'instructions can use it.',
                                          'line': '3'},
                                         {'code': '    def get_balance(self):',
                                          'explanation': 'Define a function named get_balance. Its '
                                                         'parameters (self) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '4'},
                                         {'code': '        return self.__balance',
                                          'explanation': 'Send self.__balance back to the caller and end '
                                                         'this function call.',
                                          'line': '5'},
                                         {'code': '    def deposit(self, amount):',
                                          'explanation': 'Define a function named deposit. Its parameters '
                                                         '(self, amount) are local names that receive values '
                                                         'when the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '6'},
                                         {'code': '        if amount > 0:',
                                          'explanation': 'Check whether amount > 0 is true. If it is, run '
                                                         'the indented block; otherwise Python skips that '
                                                         'block.',
                                          'line': '7'},
                                         {'code': '            self.__balance += amount',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '8'},
                                         {'code': 'a = BankAcct(100)',
                                          'explanation': 'Store BankAcct(100) in a so later instructions can '
                                                         'use it.',
                                          'line': '9'},
                                         {'code': 'a.deposit(50)',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '10'},
                                         {'code': "print('Verified Balance:', a.get_balance())",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '11'}],
                        'practical_examples': [{'code': 'class BankAcct:\n'
                                                        '    def __init__(self, initial):\n'
                                                        '        self.__balance = initial\n'
                                                        '    def get_balance(self):\n'
                                                        '        return self.__balance\n'
                                                        '    def deposit(self, amount):\n'
                                                        '        if amount > 0:\n'
                                                        '            self.__balance += amount\n'
                                                        'a = BankAcct(100)\n'
                                                        'a.deposit(50)\n'
                                                        "print('Verified Balance:', a.get_balance())",
                                                'explanation': 'Purpose: Example 1: Protecting bank account '
                                                               'balance from direct tampering shows the '
                                                               'current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class BankAcct:\n'
                                                               'Define the class BankAcct. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, initial):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, initial) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.__balance = initial\n'
                                                               'Store initial in self.__balance so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: def get_balance(self):\n'
                                                               'Define a function named get_balance. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 5: return self.__balance\n'
                                                               'Send self.__balance back to the caller and '
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 6: def deposit(self, amount):\n'
                                                               'Define a function named deposit. Its '
                                                               'parameters (self, amount) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 7: if amount > 0:\n'
                                                               'Check whether amount > 0 is true. If it is, '
                                                               'run the indented block; otherwise Python '
                                                               'skips that block.\n'
                                                               '\n'
                                                               'Line 8: self.__balance += amount\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 9: a = BankAcct(100)\n'
                                                               'Store BankAcct(100) in a so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 10: a.deposit(50)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 11: print('Verified Balance:', "
                                                               'a.get_balance())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Verified Balance: 150',
                                                'output': 'Verified Balance: 150',
                                                'title': 'Example 1: Protecting bank account balance from '
                                                         'direct tampering'},
                                               {'code': 'class Secret:\n'
                                                        '    def __init__(self):\n'
                                                        '        self.__code = 42\n'
                                                        's = Secret()\n'
                                                        '# Access via mangled name _ClassName__attr:\n'
                                                        "print('Mangled attribute value:', s._Secret__code)",
                                                'explanation': 'Purpose: Example 2: Demonstrating Python '
                                                               'name-mangling shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Secret:\n'
                                                               'Define the class Secret. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.__code = 42\n'
                                                               'Store 42 in self.__code so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: s = Secret()\n'
                                                               'Store Secret() in s so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 5: # Access via mangled name '
                                                               '_ClassName__attr:\n'
                                                               'This comment is a note for the reader. '
                                                               'Python skips it; it does not run.\n'
                                                               '\n'
                                                               "Line 6: print('Mangled attribute value:', "
                                                               's._Secret__code)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Mangled attribute value: 42',
                                                'output': 'Mangled attribute value: 42',
                                                'title': 'Example 2: Demonstrating Python name-mangling'},
                                               {'code': 'class Worker:\n'
                                                        '    def do_work(self):\n'
                                                        '        self._validate_queue()\n'
                                                        "        return 'Work complete'\n"
                                                        '    def _validate_queue(self):\n'
                                                        '        pass\n'
                                                        'print(Worker().do_work())',
                                                'explanation': 'Purpose: Example 3: Protected internal '
                                                               'helper methods shows the current lesson idea '
                                                               'in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Worker:\n'
                                                               'Define the class Worker. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def do_work(self):\n'
                                                               'Define a function named do_work. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self._validate_queue()\n'
                                                               'Call self._validate_queue now. Python runs '
                                                               'its body, and any returned result is '
                                                               'available to the caller.\n'
                                                               '\n'
                                                               "Line 4: return 'Work complete'\n"
                                                               "Send 'Work complete' back to the caller and "
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 5: def _validate_queue(self):\n'
                                                               'Define a function named _validate_queue. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 6: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 7: print(Worker().do_work())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Work complete',
                                                'output': 'Work complete',
                                                'title': 'Example 3: Protected internal helper methods'}],
                        'practice_questions': [{'answer': 'Encapsulation groups state with methods that '
                                                          'control how it is used.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Object state should be changed through rules the '
                                                          'class can check.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Python does not enforce private access; mangling '
                                                          'is not encryption or security.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is rejecting an invalid '
                                           'account balance update through a method. The same pattern helps '
                                           'a larger program stay clear when it handles the same kind of '
                                           'task repeatedly.',
                        'summary': 'Remember: Use a clear interface and validation; underscores are '
                                   'conventions, not locks. Python does not enforce private access; mangling '
                                   'is not encryption or security The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'class BankAcct:\n'
                                            '    def __init__(self, initial):\n'
                                            '        self.__balance = initial\n'
                                            '    def get_balance(self):\n'
                                            '        return self.__balance\n'
                                            '    def deposit(self, amount):\n'
                                            '        if amount > 0:\n'
                                            '            self.__balance += amount\n'
                                            'a = BankAcct(100)\n'
                                            'a.deposit(50)\n'
                                            "print('Verified Balance:', a.get_balance())",
                        'terminology': [{'definition': 'Managing data through an object’s clear interface.',
                                         'term': 'Encapsulation'},
                                        {'definition': 'A convention that a name is intended for internal '
                                                       'use.',
                                         'term': 'Single underscore'},
                                        {'definition': 'A name rewrite for double-underscore attributes; it '
                                                       'is not security.',
                                         'term': 'Name mangling'}],
                        'title': 'Encapsulation and Data Hiding'},
             'number': 100,
             'quizzes': [{'explanation': 'Attributes with leading double underscores are mangled to '
                                         '_Bank__balance. b.__balance does not exist directly.',
                          'options': [{'explanation': 'Correct! Name mangling renames it to _Bank__balance.',
                                       'is_correct': True,
                                       'text': 'False'},
                                      {'explanation': 'Incorrect. __balance is mangled to _Bank__balance.',
                                       'is_correct': False,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect. hasattr returns a boolean.',
                                       'is_correct': False,
                                       'text': '500'},
                                      {'explanation': 'Incorrect. hasattr catches AttributeError.',
                                       'is_correct': False,
                                       'text': 'AttributeError'}],
                          'question': 'What is the output of Python name mangling for private attributes?\n'
                                      '\n'
                                      'class Bank:\n'
                                      '    def __init__(self):\n'
                                      '        self.__balance = 500\n'
                                      '\n'
                                      'b = Bank()\n'
                                      "print(hasattr(b, '__balance'))"},
                         {'explanation': 'Python prefixes mangled variables with an underscore and the class '
                                         'name: `_Vault__secret`.',
                          'options': [{'explanation': 'Correct! _ClassName__attributeName.',
                                       'is_correct': True,
                                       'text': '_Vault__secret'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '__Vault_secret'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '__secret_Vault'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'private_secret'}],
                          'question': "Under Python's name mangling mechanism, what name does `__secret` "
                                      'become in a class named `Vault`?'}],
             'title': 'Encapsulation and Data Hiding'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Use @property and a setter to keep a person’s age at zero or above.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class Person:\n'
                                       '    def __init__(self, age):\n'
                                       '        self._age = age\n'
                                       '    @property\n'
                                       '    def age(self):\n'
                                       '        return self._age\n'
                                       '    @age.setter\n'
                                       '    def age(self, value):\n'
                                       '        if value < 0:\n'
                                       "            raise ValueError('Age cannot be negative')\n"
                                       '        self._age = value\n'
                                       'person = Person(10)\n'
                                       'person.age = 12\n'
                                       'print(person.age)'],
                             'initial_code': '# Calling Parent Constructors with super()\n'
                                             '# Step 1: Define Person and Employee with super().__init__:\n'
                                             '\n'
                                             "# Step 2: Instantiate Employee('Alice', 101) and print:\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Person:\n'
                                              '    def __init__(self, age):\n'
                                              '        self._age = age\n'
                                              '    @property\n'
                                              '    def age(self):\n'
                                              '        return self._age\n'
                                              '    @age.setter\n'
                                              '    def age(self, value):\n'
                                              '        if value < 0:\n'
                                              "            raise ValueError('Age cannot be negative')\n"
                                              '        self._age = value\n'
                                              'person = Person(10)\n'
                                              'person.age = 12\n'
                                              'print(person.age)',
                             'test_cases': [{'expected_output': '12', 'input_data': '', 'is_hidden': False}],
                             'title': 'Validate a Value with a Property',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Create a rectangle with a read-only area property.\n2. Print its area.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Rectangle:\n'
                                       '    def __init__(self, width, height):\n'
                                       '        self.width = width\n'
                                       '        self.height = height\n'
                                       '    @property\n'
                                       '    def area(self):\n'
                                       '        return self.width * self.height\n'
                                       'print(Rectangle(5, 4).area)'],
                             'initial_code': '# ⚔️ Boss Challenge: Geometric Shape Hierarchy\n'
                                             '# Step 1: Define Shape and Circle(Shape):\n'
                                             '\n'
                                             '# Step 2: Print c.info() below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Rectangle:\n'
                                              '    def __init__(self, width, height):\n'
                                              '        self.width = width\n'
                                              '        self.height = height\n'
                                              '    @property\n'
                                              '    def area(self):\n'
                                              '        return self.width * self.height\n'
                                              'print(Rectangle(5, 4).area)',
                             'test_cases': [{'expected_output': '20', 'input_data': '', 'is_hidden': False}],
                             'title': 'Boss Challenge: Computed Property',
                             'xp_reward': 150}],
             'description': 'Create pythonic getters, setters, and computed attributes with @property.',
             'lesson': {'common_mistakes': [{'fix': 'Properties keep a convenient attribute interface while '
                                                    'checking values.',
                                             'mistake': 'invalid values can raise ValueError; a property '
                                                        'does not make data secure',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: An attribute can look simple to '
                                                'callers while being computed or validated. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: @property lets a method be read like an '
                                                'attribute; a setter controls assignment. Python uses this '
                                                'idea to the getter runs on reading and the setter runs on '
                                                'assignment\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Invalid values can raise valueerror; a '
                                                'property does not make data secure. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Calculated Area property: 20',
                        'id': 101,
                        'introduction': 'Why learn this? An attribute can look simple to callers while being '
                                        'computed or validated. In this lesson, we will see @property lets a '
                                        'method be read like an attribute; a setter controls assignment, '
                                        'follow how Python handles it, and practice a small example you can '
                                        'change yourself.',
                        'learning_objectives': ['Explain @property lets a method be read like an attribute; '
                                                'a setter controls assignment in your own words.',
                                                'Trace a small Property Decorators (@property) example and '
                                                'predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'invalid values can raise ValueError; a property does not '
                                                'make data secure.'],
                        'level_id': 101,
                        'line_by_line': [{'code': 'class Rectangle:',
                                          'explanation': 'Define the class Rectangle. This is the blueprint '
                                                         'for instances; the indented lines below describe '
                                                         'its data or behavior.',
                                          'line': '1'},
                                         {'code': '    def __init__(self, w, h):',
                                          'explanation': 'Define a function named __init__. Its parameters '
                                                         '(self, w, h) are local names that receive values '
                                                         'when the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '2'},
                                         {'code': '        self.w = w',
                                          'explanation': 'Store w in self.w so later instructions can use '
                                                         'it.',
                                          'line': '3'},
                                         {'code': '        self.h = h',
                                          'explanation': 'Store h in self.h so later instructions can use '
                                                         'it.',
                                          'line': '4'},
                                         {'code': '    @property',
                                          'explanation': 'This decorator makes the next method behave like a '
                                                         'readable attribute.',
                                          'line': '5'},
                                         {'code': '    def area(self):',
                                          'explanation': 'Define a function named area. Its parameters '
                                                         '(self) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '6'},
                                         {'code': '        return self.w * self.h',
                                          'explanation': 'Send self.w * self.h back to the caller and end '
                                                         'this function call.',
                                          'line': '7'},
                                         {'code': 'r = Rectangle(4, 5)',
                                          'explanation': 'Store Rectangle(4, 5) in r so later instructions '
                                                         'can use it.',
                                          'line': '8'},
                                         {'code': "print('Calculated Area property:', r.area)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '9'}],
                        'practical_examples': [{'code': 'class Rectangle:\n'
                                                        '    def __init__(self, w, h):\n'
                                                        '        self.w = w\n'
                                                        '        self.h = h\n'
                                                        '    @property\n'
                                                        '    def area(self):\n'
                                                        '        return self.w * self.h\n'
                                                        'r = Rectangle(4, 5)\n'
                                                        "print('Calculated Area property:', r.area)",
                                                'explanation': 'Purpose: Example 1: Read-only computed '
                                                               'property shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Rectangle:\n'
                                                               'Define the class Rectangle. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, w, h):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, w, h) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.w = w\n'
                                                               'Store w in self.w so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 4: self.h = h\n'
                                                               'Store h in self.h so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 5: @property\n'
                                                               'This decorator makes the next method behave '
                                                               'like a readable attribute.\n'
                                                               '\n'
                                                               'Line 6: def area(self):\n'
                                                               'Define a function named area. Its parameters '
                                                               '(self) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               'Line 7: return self.w * self.h\n'
                                                               'Send self.w * self.h back to the caller and '
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 8: r = Rectangle(4, 5)\n'
                                                               'Store Rectangle(4, 5) in r so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 9: print('Calculated Area property:', "
                                                               'r.area)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Calculated Area property: 20',
                                                'output': 'Calculated Area property: 20',
                                                'title': 'Example 1: Read-only computed property'},
                                               {'code': 'class Player:\n'
                                                        '    def __init__(self, score=0):\n'
                                                        '        self._score = score\n'
                                                        '    @property\n'
                                                        '    def score(self):\n'
                                                        '        return self._score\n'
                                                        '    @score.setter\n'
                                                        '    def score(self, val):\n'
                                                        '        if val >= 0:\n'
                                                        '            self._score = val\n'
                                                        'p = Player()\n'
                                                        'p.score = 50\n'
                                                        "print('Valid Score set:', p.score)",
                                                'explanation': 'Purpose: Example 2: Validating attribute '
                                                               'assignment with setter shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Player:\n'
                                                               'Define the class Player. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, score=0):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, score=0) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self._score = score\n'
                                                               'Store score in self._score so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: @property\n'
                                                               'This decorator makes the next method behave '
                                                               'like a readable attribute.\n'
                                                               '\n'
                                                               'Line 5: def score(self):\n'
                                                               'Define a function named score. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 6: return self._score\n'
                                                               'Send self._score back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 7: @score.setter\n'
                                                               'This decorator marks the next method for a '
                                                               'special class behavior: score.setter.\n'
                                                               '\n'
                                                               'Line 8: def score(self, val):\n'
                                                               'Define a function named score. Its '
                                                               'parameters (self, val) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 9: if val >= 0:\n'
                                                               'Check whether val >= 0 is true. If it is, '
                                                               'run the indented block; otherwise Python '
                                                               'skips that block.\n'
                                                               '\n'
                                                               'Line 10: self._score = val\n'
                                                               'Store val in self._score so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 11: p = Player()\n'
                                                               'Store Player() in p so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 12: p.score = 50\n'
                                                               'Store 50 in p.score so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               "Line 13: print('Valid Score set:', p.score)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Valid Score set: 50',
                                                'output': 'Valid Score set: 50',
                                                'title': 'Example 2: Validating attribute assignment with '
                                                         'setter'},
                                               {'code': 'class Person:\n'
                                                        '    def __init__(self, first, last):\n'
                                                        '        self.first = first\n'
                                                        '        self.last = last\n'
                                                        '    @property\n'
                                                        '    def full_name(self):\n'
                                                        "        return f'{self.first} {self.last}'\n"
                                                        "p = Person('Alan', 'Turing')\n"
                                                        "print('Full Name:', p.full_name)",
                                                'explanation': 'Purpose: Example 3: Dynamic full name getter '
                                                               'and setter shows the current lesson idea in '
                                                               'a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Person:\n'
                                                               'Define the class Person. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, first, last):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, first, last) are local '
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.first = first\n'
                                                               'Store first in self.first so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: self.last = last\n'
                                                               'Store last in self.last so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: @property\n'
                                                               'This decorator makes the next method behave '
                                                               'like a readable attribute.\n'
                                                               '\n'
                                                               'Line 6: def full_name(self):\n'
                                                               'Define a function named full_name. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 7: return f'{self.first} {self.last}'\n"
                                                               "Send f'{self.first} {self.last}' back to the "
                                                               'caller and end this function call.\n'
                                                               '\n'
                                                               "Line 8: p = Person('Alan', 'Turing')\n"
                                                               "Store Person('Alan', 'Turing') in p so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 9: print('Full Name:', p.full_name)\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Full Name: Alan Turing',
                                                'output': 'Full Name: Alan Turing',
                                                'title': 'Example 3: Dynamic full name getter and setter'}],
                        'practice_questions': [{'answer': '@property lets a method be read like an '
                                                          'attribute; a setter controls assignment.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'An attribute can look simple to callers while '
                                                          'being computed or validated.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Invalid values can raise valueerror; a property '
                                                          'does not make data secure.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is validating a player’s '
                                           'score when it is assigned. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Properties keep a convenient attribute interface while '
                                   'checking values. Invalid values can raise valueerror; a property does '
                                   'not make data secure The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'class Rectangle:\n'
                                            '    def __init__(self, w, h):\n'
                                            '        self.w = w\n'
                                            '        self.h = h\n'
                                            '    @property\n'
                                            '    def area(self):\n'
                                            '        return self.w * self.h\n'
                                            'r = Rectangle(4, 5)\n'
                                            "print('Calculated Area property:', r.area)",
                        'terminology': [{'definition': 'A decorator that lets a method be read like an '
                                                       'attribute.',
                                         'term': '@property'},
                                        {'definition': 'The property method that runs when a value is read.',
                                         'term': 'Getter'},
                                        {'definition': 'The property method that runs when a value is '
                                                       'assigned.',
                                         'term': 'Setter'}],
                        'title': 'Property Decorators (@property)'},
             'number': 101,
             'quizzes': [{'explanation': '@property turns a method into a read-only attribute accessed '
                                         'without parentheses: c.radius returns 5.',
                          'options': [{'explanation': 'Correct! @property allows method execution via '
                                                      'attribute access syntax.',
                                       'is_correct': True,
                                       'text': '5'},
                                      {'explanation': 'Incorrect. @property invokes the getter '
                                                      'automatically.',
                                       'is_correct': False,
                                       'text': '<bound method Circle.radius...>'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect. Calling c.radius() would cause that; '
                                                      'c.radius is attribute syntax.',
                                       'is_correct': False,
                                       'text': "TypeError: 'int' object is not callable"}],
                          'question': 'What is the output of the `@property` getter snippet?\n'
                                      '\n'
                                      'class Circle:\n'
                                      '    def __init__(self, r):\n'
                                      '        self._r = r\n'
                                      '    @property\n'
                                      '    def radius(self):\n'
                                      '        return self._r\n'
                                      '\n'
                                      'c = Circle(5)\n'
                                      'print(c.radius)'},
                         {'explanation': '`@score.setter` decorates the setter method in Python properties.',
                          'options': [{'explanation': 'Correct! @property_name.setter defines the attribute '
                                                      'mutator.',
                                       'is_correct': True,
                                       'text': '@score.setter'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '@setter'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '@property(set=True)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '@set_score'}],
                          'question': 'What decorator defines a setter method for a property named '
                                      '`score`?'}],
             'title': 'Property Decorators (@property)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Make Employee inherit from Person.\n2. Call the parent constructor with super() to save the employee name.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class Person:\n'
                                       '    def __init__(self, name):\n'
                                       '        self.name = name\n'
                                       'class Employee(Person):\n'
                                       '    def __init__(self, name, employee_id):\n'
                                       '        super().__init__(name)\n'
                                       '        self.employee_id = employee_id\n'
                                       "employee = Employee('Mia', 12)\n"
                                       "print(f'{employee.name}: {employee.employee_id}')"],
                             'initial_code': '# Method Overriding in Subclasses\n'
                                             '# Step 1: Define Shape and Square(Shape):\n'
                                             '\n'
                                             '# Step 2: Instantiate Square(4) and print s.area():\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Person:\n'
                                              '    def __init__(self, name):\n'
                                              '        self.name = name\n'
                                              'class Employee(Person):\n'
                                              '    def __init__(self, name, employee_id):\n'
                                              '        super().__init__(name)\n'
                                              '        self.employee_id = employee_id\n'
                                              "employee = Employee('Mia', 12)\n"
                                              "print(f'{employee.name}: {employee.employee_id}')",
                             'test_cases': [{'expected_output': 'Mia: 12',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Reuse a Parent Constructor with super',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Create Circle as a child of Shape.\n2. Use super() to save the color and print the circle details.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Shape:\n'
                                       '    def __init__(self, color):\n'
                                       '        self.color = color\n'
                                       'class Circle(Shape):\n'
                                       '    def __init__(self, color, radius):\n'
                                       '        super().__init__(color)\n'
                                       '        self.radius = radius\n'
                                       '    def describe(self):\n'
                                       "        return f'{self.color} circle, radius {self.radius}'\n"
                                       "print(Circle('red', 4).describe())"],
                             'initial_code': '# ⚔️ Boss Challenge: Polymorphic Party Attack\n'
                                             '# Step 1: Define Character, Warrior, and Mage:\n'
                                             '\n'
                                             '# Step 2: Iterate party and print hero.attack():\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Shape:\n'
                                              '    def __init__(self, color):\n'
                                              '        self.color = color\n'
                                              'class Circle(Shape):\n'
                                              '    def __init__(self, color, radius):\n'
                                              '        super().__init__(color)\n'
                                              '        self.radius = radius\n'
                                              '    def describe(self):\n'
                                              "        return f'{self.color} circle, radius {self.radius}'\n"
                                              "print(Circle('red', 4).describe())",
                             'test_cases': [{'expected_output': 'red circle, radius 4',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Inherited Shape Data',
                             'xp_reward': 150}],
             'description': 'Reuse code and build specialized class hierarchies using inheritance and the '
                            'super() function.',
             'lesson': {'common_mistakes': [{'fix': 'Use inheritance for a true “is a” relationship and '
                                                    'extend the base safely.',
                                             'mistake': 'composition may be clearer when objects are related '
                                                        'by “has a” rather than “is a”',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A new class can reuse and extend '
                                                'behavior from a related class. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: Inheritance makes a child class receive '
                                                'behavior from a base class. Python uses this idea to '
                                                'super() follows Python’s method resolution order and is '
                                                'commonly used for cooperative initialization\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Composition may be clearer when objects are '
                                                'related by “has a” rather than “is a”. If you change the '
                                                'example’s input or value, check this rule again because it '
                                                'can change the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Breathing oxygen...\nFlying high!',
                        'id': 102,
                        'introduction': 'Why learn this? A new class can reuse and extend behavior from a '
                                        'related class. In this lesson, we will see inheritance makes a '
                                        'child class receive behavior from a base class, follow how Python '
                                        'handles it, and practice a small example you can change yourself.',
                        'learning_objectives': ['Explain inheritance makes a child class receive behavior '
                                                'from a base class in your own words.',
                                                'Trace a small Inheritance and super() example and predict '
                                                'what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'composition may be clearer when objects are related by “has '
                                                'a” rather than “is a”.'],
                        'level_id': 102,
                        'line_by_line': [{'code': 'class Animal:',
                                          'explanation': 'Define the class Animal. This is the blueprint for '
                                                         'instances; the indented lines below describe its '
                                                         'data or behavior.',
                                          'line': '1'},
                                         {'code': '    def breathe(self):',
                                          'explanation': 'Define a function named breathe. Its parameters '
                                                         '(self) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '2'},
                                         {'code': "        return 'Breathing oxygen...'",
                                          'explanation': "Send 'Breathing oxygen...' back to the caller and "
                                                         'end this function call.',
                                          'line': '3'},
                                         {'code': 'class Bird(Animal):',
                                          'explanation': 'Define the class Bird. This is the blueprint for '
                                                         'instances; the indented lines below describe its '
                                                         'data or behavior. It inherits from Animal.',
                                          'line': '4'},
                                         {'code': '    def fly(self):',
                                          'explanation': 'Define a function named fly. Its parameters (self) '
                                                         'are local names that receive values when the '
                                                         'function is called. The colon starts the indented '
                                                         'body; defining it does not run it yet.',
                                          'line': '5'},
                                         {'code': "        return 'Flying high!'",
                                          'explanation': "Send 'Flying high!' back to the caller and end "
                                                         'this function call.',
                                          'line': '6'},
                                         {'code': 'b = Bird()',
                                          'explanation': 'Store Bird() in b so later instructions can use '
                                                         'it.',
                                          'line': '7'},
                                         {'code': 'print(b.breathe())',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '8'},
                                         {'code': 'print(b.fly())',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '9'}],
                        'practical_examples': [{'code': 'class Animal:\n'
                                                        '    def breathe(self):\n'
                                                        "        return 'Breathing oxygen...'\n"
                                                        'class Bird(Animal):\n'
                                                        '    def fly(self):\n'
                                                        "        return 'Flying high!'\n"
                                                        'b = Bird()\n'
                                                        'print(b.breathe())\n'
                                                        'print(b.fly())',
                                                'explanation': 'Purpose: Example 1: Inheriting methods from '
                                                               'parent shows the current lesson idea in a '
                                                               'small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Animal:\n'
                                                               'Define the class Animal. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def breathe(self):\n'
                                                               'Define a function named breathe. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 3: return 'Breathing oxygen...'\n"
                                                               "Send 'Breathing oxygen...' back to the "
                                                               'caller and end this function call.\n'
                                                               '\n'
                                                               'Line 4: class Bird(Animal):\n'
                                                               'Define the class Bird. This is the blueprint '
                                                               'for instances; the indented lines below '
                                                               'describe its data or behavior. It inherits '
                                                               'from Animal.\n'
                                                               '\n'
                                                               'Line 5: def fly(self):\n'
                                                               'Define a function named fly. Its parameters '
                                                               '(self) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               "Line 6: return 'Flying high!'\n"
                                                               "Send 'Flying high!' back to the caller and "
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 7: b = Bird()\n'
                                                               'Store Bird() in b so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 8: print(b.breathe())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 9: print(b.fly())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Breathing oxygen...\n'
                                                               'Flying high!',
                                                'output': 'Breathing oxygen...\nFlying high!',
                                                'title': 'Example 1: Inheriting methods from parent'},
                                               {'code': 'class Vehicle:\n'
                                                        '    def __init__(self, wheels):\n'
                                                        '        self.wheels = wheels\n'
                                                        'class Motorcycle(Vehicle):\n'
                                                        '    def __init__(self):\n'
                                                        '        super().__init__(2)\n'
                                                        'm = Motorcycle()\n'
                                                        "print('Motorcycle wheels:', m.wheels)",
                                                'explanation': 'Purpose: Example 2: Using super() in '
                                                               'constructor extension shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Vehicle:\n'
                                                               'Define the class Vehicle. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, wheels):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, wheels) are local names '
                                                               'that receive values when the function is '
                                                               'called. The colon starts the indented body; '
                                                               'defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.wheels = wheels\n'
                                                               'Store wheels in self.wheels so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: class Motorcycle(Vehicle):\n'
                                                               'Define the class Motorcycle. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior. It '
                                                               'inherits from Vehicle.\n'
                                                               '\n'
                                                               'Line 5: def __init__(self):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 6: super().__init__(2)\n'
                                                               'Call super now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Line 7: m = Motorcycle()\n'
                                                               'Store Motorcycle() in m so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 8: print('Motorcycle wheels:', "
                                                               'm.wheels)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Motorcycle wheels: 2',
                                                'output': 'Motorcycle wheels: 2',
                                                'title': 'Example 2: Using super() in constructor extension'},
                                               {'code': 'class Employee:\n'
                                                        '    pass\n'
                                                        'class Manager(Employee):\n'
                                                        '    pass\n'
                                                        "print('Is Manager a subclass of Employee?', "
                                                        'issubclass(Manager, Employee))',
                                                'explanation': 'Purpose: Example 3: Checking inheritance '
                                                               'relationships with issubclass shows the '
                                                               'current lesson idea in a small, complete '
                                                               'example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Employee:\n'
                                                               'Define the class Employee. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 3: class Manager(Employee):\n'
                                                               'Define the class Manager. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior. It '
                                                               'inherits from Employee.\n'
                                                               '\n'
                                                               'Line 4: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 5: print('Is Manager a subclass of "
                                                               "Employee?', issubclass(Manager, Employee))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Is Manager a subclass of '
                                                               'Employee? True',
                                                'output': 'Is Manager a subclass of Employee? True',
                                                'title': 'Example 3: Checking inheritance relationships with '
                                                         'issubclass'}],
                        'practice_questions': [{'answer': 'Inheritance makes a child class receive behavior '
                                                          'from a base class.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A new class can reuse and extend behavior from a '
                                                          'related class.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Composition may be clearer when objects are '
                                                          'related by “has a” rather than “is a”.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a SavingsAccount that '
                                           'extends shared Account behavior. The same pattern helps a larger '
                                           'program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Use inheritance for a true “is a” relationship and extend the '
                                   'base safely. Composition may be clearer when objects are related by “has '
                                   'a” rather than “is a” The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'class Animal:\n'
                                            '    def breathe(self):\n'
                                            "        return 'Breathing oxygen...'\n"
                                            'class Bird(Animal):\n'
                                            '    def fly(self):\n'
                                            "        return 'Flying high!'\n"
                                            'b = Bird()\n'
                                            'print(b.breathe())\n'
                                            'print(b.fly())',
                        'terminology': [{'definition': 'The class whose behavior is inherited.',
                                         'term': 'Base class'},
                                        {'definition': 'A class that extends or changes a base class.',
                                         'term': 'Subclass'},
                                        {'definition': 'A proxy for following the method resolution order.',
                                         'term': 'super()'}],
                        'title': 'Inheritance and super()'},
             'number': 102,
             'quizzes': [{'explanation': "super().sound() calls Animal.sound() ('Base'), which is "
                                         "concatenated with ' Woof': 'Base Woof'.",
                          'options': [{'explanation': 'Correct! super().sound() delegates to the parent '
                                                      'implementation.',
                                       'is_correct': True,
                                       'text': 'Base Woof'},
                                      {'explanation': 'Incorrect. super().sound() was called.',
                                       'is_correct': False,
                                       'text': 'Woof'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'Base'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of calling super() in inheritance?\n'
                                      '\n'
                                      'class Animal:\n'
                                      '    def sound(self):\n'
                                      "        return 'Base'\n"
                                      '\n'
                                      'class Dog(Animal):\n'
                                      '    def sound(self):\n'
                                      "        return super().sound() + ' Woof'\n"
                                      '\n'
                                      'print(Dog().sound())'},
                         {'explanation': '`super()` returns a proxy object delegating method calls to a '
                                         'parent or sibling class.',
                          'options': [{'explanation': 'Correct! super() delegates to parent classes '
                                                      'according to the MRO.',
                                       'is_correct': True,
                                       'text': 'super()'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'parent()'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'base()'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'inherit()'}],
                          'question': 'What function in Python provides access to methods of a parent or '
                                      'sibling superclass?'}],
             'title': 'Inheritance and super()'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Make Dog override Animal.speak().\n2. Call speak() on both objects to see the different results.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class Animal:\n'
                                       '    def speak(self):\n'
                                       "        return 'Some sound'\n"
                                       'class Dog(Animal):\n'
                                       '    def speak(self):\n'
                                       "        return 'Woof!'\n"
                                       'print(Animal().speak())\n'
                                       'print(Dog().speak())'],
                             'initial_code': '# Encapsulation: Private Attributes\n'
                                             '# Step 1: Define Vault with __secret and get_secret():\n'
                                             '\n'
                                             '# Step 2: Instantiate and print secret below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Animal:\n'
                                              '    def speak(self):\n'
                                              "        return 'Some sound'\n"
                                              'class Dog(Animal):\n'
                                              '    def speak(self):\n'
                                              "        return 'Woof!'\n"
                                              'print(Animal().speak())\n'
                                              'print(Dog().speak())',
                             'test_cases': [{'expected_output': 'Some sound\nWoof!',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Override a Method',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Give several animal classes the same speak() method.\n2. Call it on each object through one loop.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Dog:\n'
                                       '    def speak(self):\n'
                                       "        return 'Woof'\n"
                                       'class Cat:\n'
                                       '    def speak(self):\n'
                                       "        return 'Meow'\n"
                                       'class Cow:\n'
                                       '    def speak(self):\n'
                                       "        return 'Moo'\n"
                                       'for animal in (Dog(), Cat(), Cow()):\n'
                                       '    print(animal.speak())'],
                             'initial_code': '# ⚔️ Boss Challenge: Validated Property Setter\n'
                                             '# Step 1: Define Temperature with @property and setter:\n'
                                             '\n'
                                             '# Step 2: Test valid and invalid assignments:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Dog:\n'
                                              '    def speak(self):\n'
                                              "        return 'Woof'\n"
                                              'class Cat:\n'
                                              '    def speak(self):\n'
                                              "        return 'Meow'\n"
                                              'class Cow:\n'
                                              '    def speak(self):\n'
                                              "        return 'Moo'\n"
                                              'for animal in (Dog(), Cat(), Cow()):\n'
                                              '    print(animal.speak())',
                             'test_cases': [{'expected_output': 'Woof\nMeow\nMoo',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Polymorphic Sounds',
                             'xp_reward': 150}],
             'description': 'Customize inherited behaviors and treat distinct object types uniformly via '
                            'polymorphism.',
             'lesson': {'common_mistakes': [{'fix': 'Same operation, different object behavior is '
                                                    'polymorphism.',
                                             'mistake': 'overriding is not function overloading; duck typing '
                                                        'depends on behavior, not declared ancestry',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Different object types can answer the '
                                                'same request in their own way. This is the practical '
                                                'problem the feature solves.\n'
                                                '\n'
                                                'What it means: Overriding replaces an inherited method in a '
                                                'subclass; polymorphism uses one interface across types. '
                                                'Python uses this idea to a caller invokes the same method '
                                                'name and the object’s implementation runs\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Overriding is not function overloading; '
                                                'duck typing depends on behavior, not declared ancestry. If '
                                                'you change the example’s input or value, check this rule '
                                                'again because it can change the result or the path Python '
                                                'takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Alert sound: Chime!\nAlert sound: Knock!',
                        'id': 103,
                        'introduction': 'Why learn this? Different object types can answer the same request '
                                        'in their own way. In this lesson, we will see overriding replaces '
                                        'an inherited method in a subclass; polymorphism uses one interface '
                                        'across types, follow how Python handles it, and practice a small '
                                        'example you can change yourself.',
                        'learning_objectives': ['Explain overriding replaces an inherited method in a '
                                                'subclass; polymorphism uses one interface across types in '
                                                'your own words.',
                                                'Trace a small Method Overriding and Polymorphism example '
                                                'and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'overriding is not function overloading; duck typing depends '
                                                'on behavior, not declared ancestry.'],
                        'level_id': 103,
                        'line_by_line': [{'code': 'class Notification:',
                                          'explanation': 'Define the class Notification. This is the '
                                                         'blueprint for instances; the indented lines below '
                                                         'describe its data or behavior.',
                                          'line': '1'},
                                         {'code': '    def play(self):',
                                          'explanation': 'Define a function named play. Its parameters '
                                                         '(self) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '2'},
                                         {'code': '        pass',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '3'},
                                         {'code': 'class EmailAlert(Notification):',
                                          'explanation': 'Define the class EmailAlert. This is the blueprint '
                                                         'for instances; the indented lines below describe '
                                                         'its data or behavior. It inherits from '
                                                         'Notification.',
                                          'line': '4'},
                                         {'code': '    def play(self):',
                                          'explanation': 'Define a function named play. Its parameters '
                                                         '(self) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '5'},
                                         {'code': "        return 'Chime!'",
                                          'explanation': "Send 'Chime!' back to the caller and end this "
                                                         'function call.',
                                          'line': '6'},
                                         {'code': 'class SlackAlert(Notification):',
                                          'explanation': 'Define the class SlackAlert. This is the blueprint '
                                                         'for instances; the indented lines below describe '
                                                         'its data or behavior. It inherits from '
                                                         'Notification.',
                                          'line': '7'},
                                         {'code': '    def play(self):',
                                          'explanation': 'Define a function named play. Its parameters '
                                                         '(self) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '8'},
                                         {'code': "        return 'Knock!'",
                                          'explanation': "Send 'Knock!' back to the caller and end this "
                                                         'function call.',
                                          'line': '9'},
                                         {'code': 'for a in [EmailAlert(), SlackAlert()]:',
                                          'explanation': 'Start a loop. Each turn, take the next value from '
                                                         '[EmailAlert(), SlackAlert()] and store it in a '
                                                         'before running the indented block.',
                                          'line': '10'},
                                         {'code': "    print('Alert sound:', a.play())",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '11'}],
                        'practical_examples': [{'code': 'class Notification:\n'
                                                        '    def play(self):\n'
                                                        '        pass\n'
                                                        'class EmailAlert(Notification):\n'
                                                        '    def play(self):\n'
                                                        "        return 'Chime!'\n"
                                                        'class SlackAlert(Notification):\n'
                                                        '    def play(self):\n'
                                                        "        return 'Knock!'\n"
                                                        'for a in [EmailAlert(), SlackAlert()]:\n'
                                                        "    print('Alert sound:', a.play())",
                                                'explanation': 'Purpose: Example 1: Polymorphic audio '
                                                               'notification sounds shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Notification:\n'
                                                               'Define the class Notification. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def play(self):\n'
                                                               'Define a function named play. Its parameters '
                                                               '(self) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               'Line 3: pass\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 4: class EmailAlert(Notification):\n'
                                                               'Define the class EmailAlert. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior. It '
                                                               'inherits from Notification.\n'
                                                               '\n'
                                                               'Line 5: def play(self):\n'
                                                               'Define a function named play. Its parameters '
                                                               '(self) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               "Line 6: return 'Chime!'\n"
                                                               "Send 'Chime!' back to the caller and end "
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 7: class SlackAlert(Notification):\n'
                                                               'Define the class SlackAlert. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior. It '
                                                               'inherits from Notification.\n'
                                                               '\n'
                                                               'Line 8: def play(self):\n'
                                                               'Define a function named play. Its parameters '
                                                               '(self) are local names that receive values '
                                                               'when the function is called. The colon '
                                                               'starts the indented body; defining it does '
                                                               'not run it yet.\n'
                                                               '\n'
                                                               "Line 9: return 'Knock!'\n"
                                                               "Send 'Knock!' back to the caller and end "
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 10: for a in [EmailAlert(), '
                                                               'SlackAlert()]:\n'
                                                               'Start a loop. Each turn, take the next value '
                                                               'from [EmailAlert(), SlackAlert()] and store '
                                                               'it in a before running the indented block.\n'
                                                               '\n'
                                                               "Line 11: print('Alert sound:', a.play())\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Alert sound: Chime!\n'
                                                               'Alert sound: Knock!',
                                                'output': 'Alert sound: Chime!\nAlert sound: Knock!',
                                                'title': 'Example 1: Polymorphic audio notification sounds'},
                                               {'code': 'class BaseLogger:\n'
                                                        '    def log(self, msg):\n'
                                                        "        return f'[BASE] {msg}'\n"
                                                        'class TimeLogger(BaseLogger):\n'
                                                        '    def log(self, msg):\n'
                                                        '        parent_log = super().log(msg)\n'
                                                        "        return f'2026-11-03 {parent_log}'\n"
                                                        "print(TimeLogger().log('User login'))",
                                                'explanation': 'Purpose: Example 2: Method overriding with '
                                                               'partial super call shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class BaseLogger:\n'
                                                               'Define the class BaseLogger. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def log(self, msg):\n'
                                                               'Define a function named log. Its parameters '
                                                               '(self, msg) are local names that receive '
                                                               'values when the function is called. The '
                                                               'colon starts the indented body; defining it '
                                                               'does not run it yet.\n'
                                                               '\n'
                                                               "Line 3: return f'[BASE] {msg}'\n"
                                                               "Send f'[BASE] {msg}' back to the caller and "
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 4: class TimeLogger(BaseLogger):\n'
                                                               'Define the class TimeLogger. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior. It '
                                                               'inherits from BaseLogger.\n'
                                                               '\n'
                                                               'Line 5: def log(self, msg):\n'
                                                               'Define a function named log. Its parameters '
                                                               '(self, msg) are local names that receive '
                                                               'values when the function is called. The '
                                                               'colon starts the indented body; defining it '
                                                               'does not run it yet.\n'
                                                               '\n'
                                                               'Line 6: parent_log = super().log(msg)\n'
                                                               'Store super().log(msg) in parent_log so '
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               "Line 7: return f'2026-11-03 {parent_log}'\n"
                                                               "Send f'2026-11-03 {parent_log}' back to the "
                                                               'caller and end this function call.\n'
                                                               '\n'
                                                               "Line 8: print(TimeLogger().log('User "
                                                               "login'))\n"
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: 2026-11-03 [BASE] User login',
                                                'output': '2026-11-03 [BASE] User login',
                                                'title': 'Example 2: Method overriding with partial super '
                                                         'call'},
                                               {'code': 'class PDFDoc:\n'
                                                        '    def render(self):\n'
                                                        "        return 'Rendering PDF'\n"
                                                        'class HTMLDoc:\n'
                                                        '    def render(self):\n'
                                                        "        return 'Rendering HTML'\n"
                                                        'def display(doc):\n'
                                                        '    return doc.render()\n'
                                                        'print(display(PDFDoc()))\n'
                                                        'print(display(HTMLDoc()))',
                                                'explanation': 'Purpose: Example 3: Duck typing '
                                                               '(polymorphism without explicit inheritance) '
                                                               'shows the current lesson idea in a small, '
                                                               'complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class PDFDoc:\n'
                                                               'Define the class PDFDoc. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def render(self):\n'
                                                               'Define a function named render. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 3: return 'Rendering PDF'\n"
                                                               "Send 'Rendering PDF' back to the caller and "
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 4: class HTMLDoc:\n'
                                                               'Define the class HTMLDoc. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 5: def render(self):\n'
                                                               'Define a function named render. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 6: return 'Rendering HTML'\n"
                                                               "Send 'Rendering HTML' back to the caller and "
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 7: def display(doc):\n'
                                                               'Define a function named display. Its '
                                                               'parameters (doc) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 8: return doc.render()\n'
                                                               'Send doc.render() back to the caller and end '
                                                               'this function call.\n'
                                                               '\n'
                                                               'Line 9: print(display(PDFDoc()))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Line 10: print(display(HTMLDoc()))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Rendering PDF\n'
                                                               'Rendering HTML',
                                                'output': 'Rendering PDF\nRendering HTML',
                                                'title': 'Example 3: Duck typing (polymorphism without '
                                                         'explicit inheritance)'}],
                        'practice_questions': [{'answer': 'Overriding replaces an inherited method in a '
                                                          'subclass; polymorphism uses one interface across '
                                                          'types.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Different object types can answer the same '
                                                          'request in their own way.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Overriding is not function overloading; duck '
                                                          'typing depends on behavior, not declared '
                                                          'ancestry.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is rendering different '
                                           'notification types through send(). The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Same operation, different object behavior is polymorphism. '
                                   'Overriding is not function overloading; duck typing depends on behavior, '
                                   'not declared ancestry The practical example and its line-by-line '
                                   'walkthrough show the idea in action.',
                        'syntax_breakdown': 'class Notification:\n'
                                            '    def play(self):\n'
                                            '        pass\n'
                                            'class EmailAlert(Notification):\n'
                                            '    def play(self):\n'
                                            "        return 'Chime!'\n"
                                            'class SlackAlert(Notification):\n'
                                            '    def play(self):\n'
                                            "        return 'Knock!'\n"
                                            'for a in [EmailAlert(), SlackAlert()]:\n'
                                            "    print('Alert sound:', a.play())",
                        'terminology': [{'definition': 'Define a subclass method with the same name to '
                                                       'replace inherited behavior.',
                                         'term': 'Override'},
                                        {'definition': 'Use a shared operation whose behavior depends on the '
                                                       'object.',
                                         'term': 'Polymorphism'},
                                        {'definition': 'Use an object based on the behavior it provides.',
                                         'term': 'Duck typing'}],
                        'title': 'Method Overriding and Polymorphism'},
             'number': 103,
             'quizzes': [{'explanation': 'Both Cat and Duck implement speak(). The list comprehension calls '
                                         "speak() polymorphically: ['Meow', 'Quack'].",
                          'options': [{'explanation': 'Correct! Python executes speak() on each object based '
                                                      'on its dynamic type.',
                                       'is_correct': True,
                                       'text': "['Meow', 'Quack']"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "['Meow', 'Meow']"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': "['Quack', 'Quack']"},
                                      {'explanation': 'Incorrect. Both classes have a speak method.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the polymorphic method calls?\n'
                                      '\n'
                                      "class Cat: def speak(self): return 'Meow'\n"
                                      "class Duck: def speak(self): return 'Quack'\n"
                                      '\n'
                                      'animals = [Cat(), Duck()]\n'
                                      'print([a.speak() for a in animals])'},
                         {'explanation': 'isinstance() checks inheritance relationships, returning True if '
                                         'Dog is a subclass of Animal.',
                          'options': [{'explanation': 'Correct! A child instance is an instance of its '
                                                      'parent class.',
                                       'is_correct': True,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect. Dog inherits from Animal.',
                                       'is_correct': False,
                                       'text': 'False'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'Dog'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'}],
                          'question': 'What is the output of: print(isinstance(Dog(), Animal)) when Dog '
                                      'inherits from Animal?'}],
             'title': 'Method Overriding and Polymorphism'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create a Point that saves an x and y position.\n2. Add Python’s __str__ method so printing the point shows its position in parentheses.\n3. Try it with the point (3, 7).\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['class Point:\n'
                                       '    def __init__(self, x, y):\n'
                                       '        self.x, self.y = x, y\n'
                                       '    def __str__(self):\n'
                                       "        return f'({self.x}, {self.y})'\n"
                                       'p = Point(3, 7)\n'
                                       'print(str(p))'],
                             'initial_code': '# Special Methods: __str__\n'
                                             '# Step 1: Define Point with __str__:\n'
                                             '\n'
                                             '# Step 2: Print str(Point(3, 7)) below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Point:\n'
                                              '    def __init__(self, x, y):\n'
                                              '        self.x = x\n'
                                              '        self.y = y\n'
                                              '\n'
                                              '    def __str__(self):\n'
                                              "        return f'({self.x}, {self.y})'\n"
                                              '\n'
                                              'point = Point(3, 7)\n'
                                              'print(str(point))',
                             'test_cases': [{'expected_output': '(3, 7)',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'String Representation with __str__',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Teach Vector what the plus sign should do: add the two x values and the two y values to make a new Vector.\n2. Add (2, 3) and (4, 5), then print the result.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class Vector:\n'
                                       '    def __init__(self, x, y):\n'
                                       '        self.x = x\n'
                                       '        self.y = y\n'
                                       '    def __add__(self, other):\n'
                                       '        return Vector(self.x + other.x, self.y + other.y)\n'
                                       '    def __str__(self):\n'
                                       "        return f'Vector({self.x}, {self.y})'\n"
                                       'v1 = Vector(2, 3)\n'
                                       'v2 = Vector(4, 5)\n'
                                       'print(str(v1 + v2))'],
                             'initial_code': '# ⚔️ Boss Challenge: Operator Overloading with __add__\n'
                                             '# Step 1: Define Vector with __add__ and __str__:\n'
                                             '\n'
                                             '# Step 2: Add v1 + v2 and print result:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class Vector:\n'
                                              '    def __init__(self, x, y):\n'
                                              '        self.x = x\n'
                                              '        self.y = y\n'
                                              '\n'
                                              '    def __str__(self):\n'
                                              "        return f'Vector({self.x}, {self.y})'\n"
                                              '\n'
                                              '    def __add__(self, other):\n'
                                              '        return Vector(self.x + other.x, self.y + other.y)\n'
                                              '\n'
                                              'v1 = Vector(2, 3)\n'
                                              'v2 = Vector(4, 5)\n'
                                              'print(v1 + v2)',
                             'test_cases': [{'expected_output': 'Vector(6, 8)',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Operator Overloading with __add__',
                             'xp_reward': 150}],
             'description': 'Overload operators and define built-in behaviors using double-underscore magic '
                            'methods.',
             'lesson': {'common_mistakes': [{'fix': 'Implement the matching special method for the built-in '
                                                    'operation you want to support.',
                                             'mistake': 'return the type each special method promises; '
                                                        '__len__ should return a non-negative integer',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: Built-in operations need a standard '
                                                'way to display or measure custom objects. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: Dunder methods are special hooks with double '
                                                'underscores. Python uses this idea to __str__ serves '
                                                'str/print, __repr__ serves repr/debugging, and __len__ '
                                                'serves len()\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Return the type each special method '
                                                'promises; __len__ should return a non-negative integer. If '
                                                'you change the example’s input or value, check this rule '
                                                'again because it can change the result or the path Python '
                                                'takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Hero(Name=Aria, Lvl=12)',
                        'id': 104,
                        'introduction': 'Why learn this? Built-in operations need a standard way to display '
                                        'or measure custom objects. In this lesson, we will see dunder '
                                        'methods are special hooks with double underscores, follow how '
                                        'Python handles it, and practice a small example you can change '
                                        'yourself.',
                        'learning_objectives': ['Explain dunder methods are special hooks with double '
                                                'underscores in your own words.',
                                                'Trace a small Magic / Dunder Methods (__str__, __repr__, '
                                                '__len__) example and predict what Python does next.',
                                                'Use the concept safely, including this important rule: '
                                                'return the type each special method promises; __len__ '
                                                'should return a non-negative integer.'],
                        'level_id': 104,
                        'line_by_line': [{'code': 'class Hero:',
                                          'explanation': 'Define the class Hero. This is the blueprint for '
                                                         'instances; the indented lines below describe its '
                                                         'data or behavior.',
                                          'line': '1'},
                                         {'code': '    def __init__(self, name, level):',
                                          'explanation': 'Define a function named __init__. Its parameters '
                                                         '(self, name, level) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '2'},
                                         {'code': '        self.name = name',
                                          'explanation': 'Store name in self.name so later instructions can '
                                                         'use it.',
                                          'line': '3'},
                                         {'code': '        self.level = level',
                                          'explanation': 'Store level in self.level so later instructions '
                                                         'can use it.',
                                          'line': '4'},
                                         {'code': '    def __str__(self):',
                                          'explanation': 'Define a function named __str__. Its parameters '
                                                         '(self) are local names that receive values when '
                                                         'the function is called. The colon starts the '
                                                         'indented body; defining it does not run it yet.',
                                          'line': '5'},
                                         {'code': "        return f'Hero(Name={self.name}, "
                                                  "Lvl={self.level})'",
                                          'explanation': "Send f'Hero(Name={self.name}, Lvl={self.level})' "
                                                         'back to the caller and end this function call.',
                                          'line': '6'},
                                         {'code': "h = Hero('Aria', 12)",
                                          'explanation': "Store Hero('Aria', 12) in h so later instructions "
                                                         'can use it.',
                                          'line': '7'},
                                         {'code': 'print(str(h))',
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '8'}],
                        'practical_examples': [{'code': 'class Hero:\n'
                                                        '    def __init__(self, name, level):\n'
                                                        '        self.name = name\n'
                                                        '        self.level = level\n'
                                                        '    def __str__(self):\n'
                                                        "        return f'Hero(Name={self.name}, "
                                                        "Lvl={self.level})'\n"
                                                        "h = Hero('Aria', 12)\n"
                                                        'print(str(h))',
                                                'explanation': 'Purpose: Example 1: Custom __str__ for '
                                                               'human-friendly printing shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Hero:\n'
                                                               'Define the class Hero. This is the blueprint '
                                                               'for instances; the indented lines below '
                                                               'describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, name, level):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, name, level) are local '
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.name = name\n'
                                                               'Store name in self.name so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: self.level = level\n'
                                                               'Store level in self.level so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: def __str__(self):\n'
                                                               'Define a function named __str__. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 6: return f'Hero(Name={self.name}, "
                                                               "Lvl={self.level})'\n"
                                                               "Send f'Hero(Name={self.name}, "
                                                               "Lvl={self.level})' back to the caller and "
                                                               'end this function call.\n'
                                                               '\n'
                                                               "Line 7: h = Hero('Aria', 12)\n"
                                                               "Store Hero('Aria', 12) in h so later "
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 8: print(str(h))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Hero(Name=Aria, Lvl=12)',
                                                'output': 'Hero(Name=Aria, Lvl=12)',
                                                'title': 'Example 1: Custom __str__ for human-friendly '
                                                         'printing'},
                                               {'code': 'class Point:\n'
                                                        '    def __init__(self, x, y):\n'
                                                        '        self.x = x\n'
                                                        '        self.y = y\n'
                                                        '    def __repr__(self):\n'
                                                        "        return f'Point({self.x}, {self.y})'\n"
                                                        'pt = Point(10, 20)\n'
                                                        "print('Repr representation:', repr(pt))",
                                                'explanation': 'Purpose: Example 2: Custom __repr__ for '
                                                               'developer debugging shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Point:\n'
                                                               'Define the class Point. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, x, y):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, x, y) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 3: self.x = x\n'
                                                               'Store x in self.x so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 4: self.y = y\n'
                                                               'Store y in self.y so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               'Line 5: def __repr__(self):\n'
                                                               'Define a function named __repr__. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 6: return f'Point({self.x}, {self.y})'\n"
                                                               "Send f'Point({self.x}, {self.y})' back to "
                                                               'the caller and end this function call.\n'
                                                               '\n'
                                                               'Line 7: pt = Point(10, 20)\n'
                                                               'Store Point(10, 20) in pt so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               "Line 8: print('Repr representation:', "
                                                               'repr(pt))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Repr representation: Point(10, '
                                                               '20)',
                                                'output': 'Repr representation: Point(10, 20)',
                                                'title': 'Example 2: Custom __repr__ for developer '
                                                         'debugging'},
                                               {'code': 'class Deck:\n'
                                                        '    def __init__(self):\n'
                                                        "        self.cards = ['Ace', 'King', 'Queen']\n"
                                                        '    def __len__(self):\n'
                                                        '        return len(self.cards)\n'
                                                        'd = Deck()\n'
                                                        "print('Remaining cards in deck:', len(d))",
                                                'explanation': 'Purpose: Example 3: Implementing __len__ on '
                                                               'a custom deck class shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Deck:\n'
                                                               'Define the class Deck. This is the blueprint '
                                                               'for instances; the indented lines below '
                                                               'describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 3: self.cards = ['Ace', 'King', "
                                                               "'Queen']\n"
                                                               'Create the list shown and store it in '
                                                               'self.cards. The list keeps items in order '
                                                               'and can be processed one item at a time.\n'
                                                               '\n'
                                                               'Line 4: def __len__(self):\n'
                                                               'Define a function named __len__. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 5: return len(self.cards)\n'
                                                               'Send len(self.cards) back to the caller and '
                                                               'end this function call.\n'
                                                               '\n'
                                                               'Line 6: d = Deck()\n'
                                                               'Store Deck() in d so later instructions can '
                                                               'use it.\n'
                                                               '\n'
                                                               "Line 7: print('Remaining cards in deck:', "
                                                               'len(d))\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Remaining cards in deck: 3',
                                                'output': 'Remaining cards in deck: 3',
                                                'title': 'Example 3: Implementing __len__ on a custom deck '
                                                         'class'}],
                        'practice_questions': [{'answer': 'Dunder methods are special hooks with double '
                                                          'underscores.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'Built-in operations need a standard way to '
                                                          'display or measure custom objects.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Return the type each special method promises; '
                                                          '__len__ should return a non-negative integer.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is printing a clear account '
                                           'label or counting cards in a deck. The same pattern helps a '
                                           'larger program stay clear when it handles the same kind of task '
                                           'repeatedly.',
                        'summary': 'Remember: Implement the matching special method for the built-in '
                                   'operation you want to support. Return the type each special method '
                                   'promises; __len__ should return a non-negative integer The practical '
                                   'example and its line-by-line walkthrough show the idea in action.',
                        'syntax_breakdown': 'class Hero:\n'
                                            '    def __init__(self, name, level):\n'
                                            '        self.name = name\n'
                                            '        self.level = level\n'
                                            '    def __str__(self):\n'
                                            "        return f'Hero(Name={self.name}, Lvl={self.level})'\n"
                                            "h = Hero('Aria', 12)\n"
                                            'print(str(h))',
                        'terminology': [{'definition': 'A special method with double underscores around its '
                                                       'name.',
                                         'term': 'Dunder method'},
                                        {'definition': 'The user-facing text used by str() and print().',
                                         'term': '__str__'},
                                        {'definition': 'The developer-facing representation used by repr().',
                                         'term': '__repr__'},
                                        {'definition': 'The special method used by len(); it returns a '
                                                       'non-negative integer count.',
                                         'term': '__len__'}],
                        'title': 'Magic / Dunder Methods (__str__, __repr__, __len__)'},
             'number': 104,
             'quizzes': [{'explanation': 'The + operator triggers __add__, producing a new Point with x = 10 '
                                         '+ 25 = 35.',
                          'options': [{'explanation': 'Correct! __add__ overloads the + operator.',
                                       'is_correct': True,
                                       'text': '35'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '10'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '25'},
                                      {'explanation': 'Incorrect. __add__ was defined.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the overloaded `__add__` operator?\n'
                                      '\n'
                                      'class Point:\n'
                                      '    def __init__(self, x):\n'
                                      '        self.x = x\n'
                                      '    def __add__(self, other):\n'
                                      '        return Point(self.x + other.x)\n'
                                      '\n'
                                      'p = Point(10) + Point(25)\n'
                                      'print(p.x)'},
                         {'explanation': '`__len__` is called by the built-in len() function.',
                          'options': [{'explanation': 'Correct! len(obj) delegates to obj.__len__().',
                                       'is_correct': True,
                                       'text': '__len__(self)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '__count__(self)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '__size__(self)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '__length__(self)'}],
                          'question': 'Which dunder method must be implemented to support the `len(obj)` '
                                      'built-in function on custom objects?'}],
             'title': 'Magic / Dunder Methods (__str__, __repr__, __len__)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create an account with a balance, deposit money, and print the updated balance.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['class BankAccount:\n'
                                       '    def __init__(self, owner, balance=0):\n'
                                       '        self.owner = owner\n'
                                       '        self.__balance = balance\n'
                                       '    def deposit(self, amount):\n'
                                       '        if amount > 0:\n'
                                       '            self.__balance += amount\n'
                                       '    def get_balance(self):\n'
                                       '        return self.__balance\n'
                                       "account = BankAccount('Mia', 100)\n"
                                       'account.deposit(50)\n'
                                       "print(f'{account.owner}: {account.get_balance()}')"],
                             'initial_code': '# World 10 Capstone: RPG Entity Hierarchy\n'
                                             '# Step 1: Define QuestEntity and Boss(QuestEntity):\n'
                                             '\n'
                                             "# Step 2: Instantiate Boss('Dragon', 500, 2) and print:\n"
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class BankAccount:\n'
                                              '    def __init__(self, owner, balance=0):\n'
                                              '        self.owner = owner\n'
                                              '        self.__balance = balance\n'
                                              '    def deposit(self, amount):\n'
                                              '        if amount > 0:\n'
                                              '            self.__balance += amount\n'
                                              '    def get_balance(self):\n'
                                              '        return self.__balance\n'
                                              "account = BankAccount('Mia', 100)\n"
                                              'account.deposit(50)\n'
                                              "print(f'{account.owner}: {account.get_balance()}')",
                             'test_cases': [{'expected_output': 'Mia: 150',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Bank Account Capstone',
                             'xp_reward': 50},
                            {'description': 'Your task, step by step:\n1. Make a bank account iterable over its transactions.\n2. Add two transactions and print them in order.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['class BankAccount:\n'
                                       '    def __init__(self, owner):\n'
                                       '        self.owner = owner\n'
                                       '        self.transactions = []\n'
                                       '    def deposit(self, amount):\n'
                                       '        self.transactions.append(amount)\n'
                                       '    def __iter__(self):\n'
                                       '        return iter(self.transactions)\n'
                                       "account = BankAccount('Mia')\n"
                                       'account.deposit(100)\n'
                                       'account.deposit(-25)\n'
                                       'for transaction in account:\n'
                                       '    print(transaction)'],
                             'initial_code': '# ⚔️ Boss Challenge: Custom Countdown Iterator\n'
                                             '\n'
                                             'class Countdown:\n'
                                             '    def __init__(self, start):\n'
                                             '        self.current = start\n'
                                             '\n'
                                             '    def __iter__(self):\n'
                                             '        return self\n'
                                             '\n'
                                             '    def __next__(self):\n'
                                             '        # Step 1: Check if self.current > 0, return it and '
                                             'decrement.\n'
                                             '        # Otherwise raise StopIteration:\n'
                                             '        pass\n'
                                             '\n'
                                             '# Step 2: Iterate over Countdown(3) and print each number:\n'
                                             'for num in Countdown(3):\n'
                                             "    print(f'Countdown: {num}')\n"
                                             '\n'
                                             "print('Liftoff!')\n",
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'class BankAccount:\n'
                                              '    def __init__(self, owner):\n'
                                              '        self.owner = owner\n'
                                              '        self.transactions = []\n'
                                              '    def deposit(self, amount):\n'
                                              '        self.transactions.append(amount)\n'
                                              '    def __iter__(self):\n'
                                              '        return iter(self.transactions)\n'
                                              "account = BankAccount('Mia')\n"
                                              'account.deposit(100)\n'
                                              'account.deposit(-25)\n'
                                              'for transaction in account:\n'
                                              '    print(transaction)',
                             'test_cases': [{'expected_output': '100\n-25',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Iterable Transaction History',
                             'xp_reward': 250}],
             'description': 'Synthesize classes, inheritance, encapsulation, polymorphism, and dunder '
                            'methods into a complete Banking System.',
             'lesson': {'common_mistakes': [{'fix': 'Model safe state changes for learning only; never use '
                                                    'this toy program for real funds.',
                                             'mistake': 'real banking needs security, persistence, audit '
                                                        'controls, concurrency, and decimal-safe financial '
                                                        'design beyond this lesson',
                                             'why': 'Python follows the rule exactly; ignoring it can cause '
                                                    'a wrong result, an exception, or confusing behavior.'},
                                            {'fix': 'Read the walkthrough from top to bottom, then change '
                                                    'one value and predict what will happen.',
                                             'mistake': 'Copying an example without checking what each name '
                                                        'and line means.',
                                             'why': 'A changed value or omitted step can change the '
                                                    'program’s behavior.'}],
                        'detailed_explanation': 'Why this idea exists: A banking example can teach state, '
                                                'validation, methods, and inheritance together. This is the '
                                                'practical problem the feature solves.\n'
                                                '\n'
                                                'What it means: This capstone is a learning simulation, not '
                                                'real banking software. Python uses this idea to store money '
                                                'as integer cents, validate each transaction, and let '
                                                'account methods control updates\n'
                                                '\n'
                                                'How to follow it: Read the example below one line at a '
                                                'time. Names hold values, indented lines show which block '
                                                'belongs together, and Python follows the program’s '
                                                'execution order. The walkthrough below explains what each '
                                                'line changes and why it is there.\n'
                                                '\n'
                                                'Important rule: Real banking needs security, persistence, '
                                                'audit controls, concurrency, and decimal-safe financial '
                                                'design beyond this lesson. If you change the example’s '
                                                'input or value, check this rule again because it can change '
                                                'the result or the path Python takes.\n'
                                                '\n'
                                                'Try a variation: change one value or option in the example '
                                                'and predict the result before running it. Then compare your '
                                                'prediction with the exact output.',
                        'expected_output': 'Balance in cents: 12000',
                        'id': 105,
                        'introduction': 'Why learn this? A banking example can teach state, validation, '
                                        'methods, and inheritance together. In this lesson, we will see this '
                                        'capstone is a learning simulation, not real banking software, '
                                        'follow how Python handles it, and practice a small example you can '
                                        'change yourself.',
                        'learning_objectives': ['Explain this capstone is a learning simulation, not real '
                                                'banking software in your own words.',
                                                'Trace a small World 10 Examination & Capstone: Banking '
                                                'Management System example and predict what Python does '
                                                'next.',
                                                'Use the concept safely, including this important rule: real '
                                                'banking needs security, persistence, audit controls, '
                                                'concurrency, and decimal-safe financial design beyond this '
                                                'lesson.'],
                        'level_id': 105,
                        'line_by_line': [{'code': 'class Account:',
                                          'explanation': 'Define the class Account. This is the blueprint '
                                                         'for instances; the indented lines below describe '
                                                         'its data or behavior.',
                                          'line': '1'},
                                         {'code': '    def __init__(self, owner, balance_cents=0):',
                                          'explanation': 'Define a function named __init__. Its parameters '
                                                         '(self, owner, balance_cents=0) are local names '
                                                         'that receive values when the function is called. '
                                                         'The colon starts the indented body; defining it '
                                                         'does not run it yet.',
                                          'line': '2'},
                                         {'code': '        self.owner = owner',
                                          'explanation': 'Store owner in self.owner so later instructions '
                                                         'can use it.',
                                          'line': '3'},
                                         {'code': '        self._balance_cents = balance_cents',
                                          'explanation': 'Store balance_cents in self._balance_cents so '
                                                         'later instructions can use it.',
                                          'line': '4'},
                                         {'code': '    @property',
                                          'explanation': 'This decorator makes the next method behave like a '
                                                         'readable attribute.',
                                          'line': '5'},
                                         {'code': '    def balance_cents(self):',
                                          'explanation': 'Define a function named balance_cents. Its '
                                                         'parameters (self) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '6'},
                                         {'code': '        return self._balance_cents',
                                          'explanation': 'Send self._balance_cents back to the caller and '
                                                         'end this function call.',
                                          'line': '7'},
                                         {'code': '    def deposit(self, amount_cents):',
                                          'explanation': 'Define a function named deposit. Its parameters '
                                                         '(self, amount_cents) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '8'},
                                         {'code': '        if amount_cents <= 0:',
                                          'explanation': 'Check whether amount_cents <= 0 is true. If it is, '
                                                         'run the indented block; otherwise Python skips '
                                                         'that block.',
                                          'line': '9'},
                                         {'code': "            raise ValueError('Deposit must be positive')",
                                          'explanation': "Stop this path by raising ValueError('Deposit must "
                                                         "be positive'). Python passes that error to the "
                                                         'caller unless a matching except block handles it.',
                                          'line': '10'},
                                         {'code': '        self._balance_cents += amount_cents',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '11'},
                                         {'code': '    def withdraw(self, amount_cents):',
                                          'explanation': 'Define a function named withdraw. Its parameters '
                                                         '(self, amount_cents) are local names that receive '
                                                         'values when the function is called. The colon '
                                                         'starts the indented body; defining it does not run '
                                                         'it yet.',
                                          'line': '12'},
                                         {'code': '        if amount_cents <= 0:',
                                          'explanation': 'Check whether amount_cents <= 0 is true. If it is, '
                                                         'run the indented block; otherwise Python skips '
                                                         'that block.',
                                          'line': '13'},
                                         {'code': "            raise ValueError('Withdrawal must be "
                                                  "positive')",
                                          'explanation': "Stop this path by raising ValueError('Withdrawal "
                                                         "must be positive'). Python passes that error to "
                                                         'the caller unless a matching except block handles '
                                                         'it.',
                                          'line': '14'},
                                         {'code': '        if amount_cents > self._balance_cents:',
                                          'explanation': 'Check whether amount_cents > self._balance_cents '
                                                         'is true. If it is, run the indented block; '
                                                         'otherwise Python skips that block.',
                                          'line': '15'},
                                         {'code': '            return False',
                                          'explanation': 'Send False back to the caller and end this '
                                                         'function call.',
                                          'line': '16'},
                                         {'code': '        self._balance_cents -= amount_cents',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '17'},
                                         {'code': '        return True',
                                          'explanation': 'Send True back to the caller and end this function '
                                                         'call.',
                                          'line': '18'},
                                         {'code': '',
                                          'explanation': 'The blank line separates steps so the program is '
                                                         'easier to scan.',
                                          'line': '19'},
                                         {'code': "account = Account('Ari', 10000)",
                                          'explanation': "Store Account('Ari', 10000) in account so later "
                                                         'instructions can use it.',
                                          'line': '20'},
                                         {'code': 'account.deposit(5000)',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '21'},
                                         {'code': 'account.withdraw(3000)',
                                          'explanation': 'Python runs this instruction as the next step. Its '
                                                         'indentation shows which function, class, or '
                                                         'control-flow block it belongs to.',
                                          'line': '22'},
                                         {'code': "print('Balance in cents:', account.balance_cents)",
                                          'explanation': 'Display the value or message inside print(). If it '
                                                         'contains variables or a calculation, Python fills '
                                                         'in or calculates those values first.',
                                          'line': '23'}],
                        'practical_examples': [{'code': 'class Account:\n'
                                                        '    def __init__(self, owner, balance_cents=0):\n'
                                                        '        self.owner = owner\n'
                                                        '        self._balance_cents = balance_cents\n'
                                                        '    @property\n'
                                                        '    def balance_cents(self):\n'
                                                        '        return self._balance_cents\n'
                                                        '    def deposit(self, amount_cents):\n'
                                                        '        if amount_cents <= 0:\n'
                                                        "            raise ValueError('Deposit must be "
                                                        "positive')\n"
                                                        '        self._balance_cents += amount_cents\n'
                                                        '    def withdraw(self, amount_cents):\n'
                                                        '        if amount_cents <= 0:\n'
                                                        "            raise ValueError('Withdrawal must be "
                                                        "positive')\n"
                                                        '        if amount_cents > self._balance_cents:\n'
                                                        '            return False\n'
                                                        '        self._balance_cents -= amount_cents\n'
                                                        '        return True\n'
                                                        '\n'
                                                        "account = Account('Ari', 10000)\n"
                                                        'account.deposit(5000)\n'
                                                        'account.withdraw(3000)\n'
                                                        "print('Balance in cents:', account.balance_cents)",
                                                'explanation': 'Purpose: Build an account with checked '
                                                               'deposits and withdrawals shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Account:\n'
                                                               'Define the class Account. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, owner, '
                                                               'balance_cents=0):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, owner, balance_cents=0) '
                                                               'are local names that receive values when the '
                                                               'function is called. The colon starts the '
                                                               'indented body; defining it does not run it '
                                                               'yet.\n'
                                                               '\n'
                                                               'Line 3: self.owner = owner\n'
                                                               'Store owner in self.owner so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: self._balance_cents = balance_cents\n'
                                                               'Store balance_cents in self._balance_cents '
                                                               'so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: @property\n'
                                                               'This decorator makes the next method behave '
                                                               'like a readable attribute.\n'
                                                               '\n'
                                                               'Line 6: def balance_cents(self):\n'
                                                               'Define a function named balance_cents. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 7: return self._balance_cents\n'
                                                               'Send self._balance_cents back to the caller '
                                                               'and end this function call.\n'
                                                               '\n'
                                                               'Line 8: def deposit(self, amount_cents):\n'
                                                               'Define a function named deposit. Its '
                                                               'parameters (self, amount_cents) are local '
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 9: if amount_cents <= 0:\n'
                                                               'Check whether amount_cents <= 0 is true. If '
                                                               'it is, run the indented block; otherwise '
                                                               'Python skips that block.\n'
                                                               '\n'
                                                               "Line 10: raise ValueError('Deposit must be "
                                                               "positive')\n"
                                                               'Stop this path by raising '
                                                               "ValueError('Deposit must be positive'). "
                                                               'Python passes that error to the caller '
                                                               'unless a matching except block handles it.\n'
                                                               '\n'
                                                               'Line 11: self._balance_cents += '
                                                               'amount_cents\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 12: def withdraw(self, amount_cents):\n'
                                                               'Define a function named withdraw. Its '
                                                               'parameters (self, amount_cents) are local '
                                                               'names that receive values when the function '
                                                               'is called. The colon starts the indented '
                                                               'body; defining it does not run it yet.\n'
                                                               '\n'
                                                               'Line 13: if amount_cents <= 0:\n'
                                                               'Check whether amount_cents <= 0 is true. If '
                                                               'it is, run the indented block; otherwise '
                                                               'Python skips that block.\n'
                                                               '\n'
                                                               "Line 14: raise ValueError('Withdrawal must "
                                                               "be positive')\n"
                                                               'Stop this path by raising '
                                                               "ValueError('Withdrawal must be positive'). "
                                                               'Python passes that error to the caller '
                                                               'unless a matching except block handles it.\n'
                                                               '\n'
                                                               'Line 15: if amount_cents > '
                                                               'self._balance_cents:\n'
                                                               'Check whether amount_cents > '
                                                               'self._balance_cents is true. If it is, run '
                                                               'the indented block; otherwise Python skips '
                                                               'that block.\n'
                                                               '\n'
                                                               'Line 16: return False\n'
                                                               'Send False back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 17: self._balance_cents -= '
                                                               'amount_cents\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 18: return True\n'
                                                               'Send True back to the caller and end this '
                                                               'function call.\n'
                                                               '\n'
                                                               'Line 19: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 20: account = Account('Ari', 10000)\n"
                                                               "Store Account('Ari', 10000) in account so "
                                                               'later instructions can use it.\n'
                                                               '\n'
                                                               'Line 21: account.deposit(5000)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 22: account.withdraw(3000)\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               "Line 23: print('Balance in cents:', "
                                                               'account.balance_cents)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Balance in cents: 12000',
                                                'output': 'Balance in cents: 12000',
                                                'title': 'Build an account with checked deposits and '
                                                         'withdrawals'},
                                               {'code': 'class Account:\n'
                                                        '    def __init__(self, owner, balance_cents):\n'
                                                        '        self.owner = owner\n'
                                                        '        self._balance_cents = balance_cents\n'
                                                        '    @property\n'
                                                        '    def balance_cents(self):\n'
                                                        '        return self._balance_cents\n'
                                                        '\n'
                                                        'class SavingsAccount(Account):\n'
                                                        '    def __init__(self, owner, balance_cents, '
                                                        'rate_basis_points):\n'
                                                        '        super().__init__(owner, balance_cents)\n'
                                                        '        self.rate_basis_points = rate_basis_points\n'
                                                        '    def add_interest(self):\n'
                                                        '        interest = self.balance_cents * '
                                                        'self.rate_basis_points // 10000\n'
                                                        '        self._balance_cents += interest\n'
                                                        '\n'
                                                        "savings = SavingsAccount('Mina', 100000, 500)\n"
                                                        'savings.add_interest()\n'
                                                        "print('Balance in cents:', savings.balance_cents)",
                                                'explanation': 'Purpose: Extend an account and calculate '
                                                               'savings interest in cents shows the current '
                                                               'lesson idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Account:\n'
                                                               'Define the class Account. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def __init__(self, owner, '
                                                               'balance_cents):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, owner, balance_cents) are '
                                                               'local names that receive values when the '
                                                               'function is called. The colon starts the '
                                                               'indented body; defining it does not run it '
                                                               'yet.\n'
                                                               '\n'
                                                               'Line 3: self.owner = owner\n'
                                                               'Store owner in self.owner so later '
                                                               'instructions can use it.\n'
                                                               '\n'
                                                               'Line 4: self._balance_cents = balance_cents\n'
                                                               'Store balance_cents in self._balance_cents '
                                                               'so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 5: @property\n'
                                                               'This decorator makes the next method behave '
                                                               'like a readable attribute.\n'
                                                               '\n'
                                                               'Line 6: def balance_cents(self):\n'
                                                               'Define a function named balance_cents. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 7: return self._balance_cents\n'
                                                               'Send self._balance_cents back to the caller '
                                                               'and end this function call.\n'
                                                               '\n'
                                                               'Line 8: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 9: class SavingsAccount(Account):\n'
                                                               'Define the class SavingsAccount. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior. It '
                                                               'inherits from Account.\n'
                                                               '\n'
                                                               'Line 10: def __init__(self, owner, '
                                                               'balance_cents, rate_basis_points):\n'
                                                               'Define a function named __init__. Its '
                                                               'parameters (self, owner, balance_cents, '
                                                               'rate_basis_points) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 11: super().__init__(owner, '
                                                               'balance_cents)\n'
                                                               'Call super now. Python runs its body, and '
                                                               'any returned result is available to the '
                                                               'caller.\n'
                                                               '\n'
                                                               'Line 12: self.rate_basis_points = '
                                                               'rate_basis_points\n'
                                                               'Store rate_basis_points in '
                                                               'self.rate_basis_points so later instructions '
                                                               'can use it.\n'
                                                               '\n'
                                                               'Line 13: def add_interest(self):\n'
                                                               'Define a function named add_interest. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               'Line 14: interest = self.balance_cents * '
                                                               'self.rate_basis_points // 10000\n'
                                                               'Calculate or compare self.balance_cents * '
                                                               'self.rate_basis_points // 10000, then save '
                                                               'the result in interest.\n'
                                                               '\n'
                                                               'Line 15: self._balance_cents += interest\n'
                                                               'Python runs this instruction as the next '
                                                               'step. Its indentation shows which function, '
                                                               'class, or control-flow block it belongs to.\n'
                                                               '\n'
                                                               'Line 16: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               "Line 17: savings = SavingsAccount('Mina', "
                                                               '100000, 500)\n'
                                                               "Store SavingsAccount('Mina', 100000, 500) in "
                                                               'savings so later instructions can use it.\n'
                                                               '\n'
                                                               'Line 18: savings.add_interest()\n'
                                                               'Call savings.add_interest now. Python runs '
                                                               'its body, and any returned result is '
                                                               'available to the caller.\n'
                                                               '\n'
                                                               "Line 19: print('Balance in cents:', "
                                                               'savings.balance_cents)\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Balance in cents: 105000',
                                                'output': 'Balance in cents: 105000',
                                                'title': 'Extend an account and calculate savings interest '
                                                         'in cents'},
                                               {'code': 'class Account:\n'
                                                        '    def monthly_message(self):\n'
                                                        "        return 'Standard account statement'\n"
                                                        '\n'
                                                        'class SavingsAccount(Account):\n'
                                                        '    def monthly_message(self):\n'
                                                        "        return 'Savings account statement'\n"
                                                        '\n'
                                                        'accounts = [Account(), SavingsAccount()]\n'
                                                        'for account in accounts:\n'
                                                        '    print(account.monthly_message())',
                                                'explanation': 'Purpose: Use one method name with different '
                                                               'account behavior shows the current lesson '
                                                               'idea in a small, complete example.\n'
                                                               '\n'
                                                               'Step by step:\n'
                                                               'Line 1: class Account:\n'
                                                               'Define the class Account. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior.\n'
                                                               '\n'
                                                               'Line 2: def monthly_message(self):\n'
                                                               'Define a function named monthly_message. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 3: return 'Standard account statement'\n"
                                                               "Send 'Standard account statement' back to "
                                                               'the caller and end this function call.\n'
                                                               '\n'
                                                               'Line 4: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 5: class SavingsAccount(Account):\n'
                                                               'Define the class SavingsAccount. This is the '
                                                               'blueprint for instances; the indented lines '
                                                               'below describe its data or behavior. It '
                                                               'inherits from Account.\n'
                                                               '\n'
                                                               'Line 6: def monthly_message(self):\n'
                                                               'Define a function named monthly_message. Its '
                                                               'parameters (self) are local names that '
                                                               'receive values when the function is called. '
                                                               'The colon starts the indented body; defining '
                                                               'it does not run it yet.\n'
                                                               '\n'
                                                               "Line 7: return 'Savings account statement'\n"
                                                               "Send 'Savings account statement' back to the "
                                                               'caller and end this function call.\n'
                                                               '\n'
                                                               'Line 8: \n'
                                                               'The blank line separates steps so the '
                                                               'program is easier to scan.\n'
                                                               '\n'
                                                               'Line 9: accounts = [Account(), '
                                                               'SavingsAccount()]\n'
                                                               'Create the list shown and store it in '
                                                               'accounts. The list keeps items in order and '
                                                               'can be processed one item at a time.\n'
                                                               '\n'
                                                               'Line 10: for account in accounts:\n'
                                                               'Start a loop. Each turn, take the next value '
                                                               'from accounts and store it in account before '
                                                               'running the indented block.\n'
                                                               '\n'
                                                               'Line 11: print(account.monthly_message())\n'
                                                               'Display the value or message inside print(). '
                                                               'If it contains variables or a calculation, '
                                                               'Python fills in or calculates those values '
                                                               'first.\n'
                                                               '\n'
                                                               'Output trace: Standard account statement\n'
                                                               'Savings account statement',
                                                'output': 'Standard account statement\n'
                                                          'Savings account statement',
                                                'title': 'Use one method name with different account '
                                                         'behavior'}],
                        'practice_questions': [{'answer': 'This capstone is a learning simulation, not real '
                                                          'banking software.',
                                                'question': 'What is the key idea in this lesson?'},
                                               {'answer': 'A banking example can teach state, validation, '
                                                          'methods, and inheritance together.',
                                                'question': 'What problem does it help solve?'},
                                               {'answer': 'Real banking needs security, persistence, audit '
                                                          'controls, concurrency, and decimal-safe financial '
                                                          'design beyond this lesson.',
                                                'question': 'What rule should you remember before using it?'},
                                               {'answer': 'Solution: Example 2 above is the complete worked '
                                                          'solution. Change only one value, trace each line '
                                                          'using its explanation, and compare your result '
                                                          'with the output shown.',
                                                'question': 'Practice: change one value or option in Example '
                                                            '2, predict what changes, then run it.'}],
                        'prerequisites': 'Variables, functions, collections, and reading indented blocks. '
                                         'The lesson briefly explains any new word before relying on it.',
                        'real_world_apps': 'A realistic use of this exact idea is a classroom model of '
                                           'deposits, withdrawals, and savings interest. The same pattern '
                                           'helps a larger program stay clear when it handles the same kind '
                                           'of task repeatedly.',
                        'summary': 'Remember: Model safe state changes for learning only; never use this toy '
                                   'program for real funds. Real banking needs security, persistence, audit '
                                   'controls, concurrency, and decimal-safe financial design beyond this '
                                   'lesson The practical example and its line-by-line walkthrough show the '
                                   'idea in action.',
                        'syntax_breakdown': 'class Account:\n'
                                            '    def __init__(self, owner, balance_cents=0):\n'
                                            '        self.owner = owner\n'
                                            '        self._balance_cents = balance_cents\n'
                                            '    @property\n'
                                            '    def balance_cents(self):\n'
                                            '        return self._balance_cents\n'
                                            '    def deposit(self, amount_cents):\n'
                                            '        if amount_cents <= 0:\n'
                                            "            raise ValueError('Deposit must be positive')\n"
                                            '        self._balance_cents += amount_cents\n'
                                            '    def withdraw(self, amount_cents):\n'
                                            '        if amount_cents <= 0:\n'
                                            "            raise ValueError('Withdrawal must be positive')\n"
                                            '        if amount_cents > self._balance_cents:\n'
                                            '            return False\n'
                                            '        self._balance_cents -= amount_cents\n'
                                            '        return True\n'
                                            '\n'
                                            "account = Account('Ari', 10000)\n"
                                            'account.deposit(5000)\n'
                                            'account.withdraw(3000)\n'
                                            "print('Balance in cents:', account.balance_cents)",
                        'terminology': [{'definition': 'A proposed change to an account balance.',
                                         'term': 'Transaction'},
                                        {'definition': 'A whole-number representation of money amounts for '
                                                       'this lesson.',
                                         'term': 'Integer cents'},
                                        {'definition': 'A simplified program that is not safe for real '
                                                       'banking.',
                                         'term': 'Learning simulation'}],
                        'title': 'World 10 Examination & Capstone: Banking Management System'},
             'number': 105,
             'quizzes': [{'explanation': 'str(Account(250)) calls __str__(), which formats the balance: '
                                         "'$250'.",
                          'options': [{'explanation': 'Correct! __str__ formats the human-readable string '
                                                      'representation.',
                                       'is_correct': True,
                                       'text': '$250'},
                                      {'explanation': 'Incorrect. That is default repr without __str__.',
                                       'is_correct': False,
                                       'text': 'Account object'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '250'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'TypeError'}],
                          'question': 'What is the output of the string representation dunder method?\n'
                                      '\n'
                                      'class Account:\n'
                                      '    def __init__(self, bal):\n'
                                      '        self.bal = bal\n'
                                      '    def __str__(self):\n'
                                      "        return f'${self.bal}'\n"
                                      '\n'
                                      'print(str(Account(250)))'},
                         {'explanation': '`__str__` provides a readable string for end users; `__repr__` '
                                         'provides an unambiguous developer representation, ideally '
                                         'executable as code.',
                          'options': [{'explanation': 'Correct! str is for users; repr is for debugging and '
                                                      'developers.',
                                       'is_correct': True,
                                       'text': '__str__ is for end-user readable output; __repr__ is '
                                               'unambiguous developer output'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '__str__ is only for numbers; __repr__ is for strings'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'They are completely identical with no differences'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '__repr__ was removed in Python 3'}],
                          'question': 'What is the difference between `__str__` and `__repr__` in Python?'}],
             'title': 'World 10 Examination & Capstone: Banking Management System'}],
 'number': 10,
 'title': 'Object-Oriented Programming'}
