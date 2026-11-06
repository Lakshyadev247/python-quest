import json
from app.database import SessionLocal
from app.models.curriculum import World, Level, Lesson, CodingChallenge, TestCase, QuizQuestion, QuizOption
from app.services.gamification_service import seed_achievements
from app.curriculum.world1 import WORLD_1
from app.curriculum.world2 import WORLD_2
from app.curriculum.world3 import WORLD_3
from app.curriculum.world4 import WORLD_4
from app.curriculum.world5 import WORLD_5
from app.curriculum.world6 import WORLD_6

WORLDS_DATA = [
    {
        "number": 1,
        "title": "Python Beginner",
        "goal": "Introduce programming to someone who has never written code.",
        "description": "Start your journey with fundamental programming concepts, syntax, text, and numbers.",
        "final_project_title": "Personal Introduction Program",
        "final_project_desc": "Build an interactive script that prints a formatted biography card with text, calculations, and comments.",
        "is_unlocked_by_default": True,
        "levels": [
            {"number": 1, "title": "What Is Programming?", "description": "Understand what instructions are and how computers execute logic."},
            {"number": 2, "title": "What Is Python?", "description": "Learn why Python is readable, powerful, and beloved worldwide."},
            {"number": 3, "title": "How Python Runs Code", "description": "Learn how Python reads a saved program from top to bottom, and what comments are for."},
            {"number": 4, "title": "Your First Python Program", "description": "Write and execute your inaugural 'Hello, World!' program."},
            {"number": 5, "title": "Understanding print()", "description": "Master printing multiple values, separators, and end parameters."},
            {"number": 6, "title": "Understanding Text and Strings", "description": "Learn string literals, quotes, escapes, and string concatenation."},
            {"number": 7, "title": "Understanding Numbers", "description": "Explore integers, decimals, and basic numeric output."},
            {"number": 8, "title": "Python Comments", "description": "Document code clearly using single-line and multi-line comments."},
            {"number": 9, "title": "Understanding Basic Syntax", "description": "Master case sensitivity, indentation principles, and statements."},
            {"number": 10, "title": "World 1 Examination", "description": "Synthesize all beginner concepts and build your first full program."}
        ]
    },
    {
        "number": 2,
        "title": "Variables and Data Types",
        "goal": "Store, manipulate, and convert different kinds of data in computer memory.",
        "description": "Master variables, memory references, integers, floats, booleans, and type conversion.",
        "final_project_title": "Personal Information Management Program",
        "final_project_desc": "Create a data store for a contact profile with type validation and conversions.",
        "levels": [
            {"number": 11, "title": "What Are Variables?", "description": "Understand memory containers and labels."},
            {"number": 12, "title": "Creating Variables", "description": "Declare and assign values with the assignment operator."},
            {"number": 13, "title": "Variable Naming Rules", "description": "Learn snake_case conventions and illegal identifiers."},
            {"number": 14, "title": "Updating Variables", "description": "Reassign values and use augmented assignment shortcuts."},
            {"number": 15, "title": "Understanding Integers", "description": "Work with whole numbers and integer operations."},
            {"number": 16, "title": "Understanding Floats", "description": "Master floating-point precision and decimal calculations."},
            {"number": 17, "title": "Formatting Strings with f-strings", "description": "Place variable values inside readable text with f-strings."},
            {"number": 18, "title": "Understanding Booleans", "description": "Represent truth values with True and False."},
            {"number": 19, "title": "Checking Data Types with type()", "description": "Inspect variable types dynamically."},
            {"number": 20, "title": "Type Conversion", "description": "Convert between int, float, str, and bool."},
            {"number": 21, "title": "World 2 Examination", "description": "Test your mastery of data types and variable manipulation."}
        ]
    },
    {
        "number": 3,
        "title": "User Input and Operators",
        "goal": "Build interactive programs that take user input and perform mathematical calculations.",
        "description": "Learn input(), arithmetic operators, comparison operators, and logical operators.",
        "final_project_title": "Interactive Calculator",
        "final_project_desc": "Build a command-line calculator that takes numbers and performs selected arithmetic.",
        "levels": [
            {"number": 22, "title": "Understanding input()", "description": "Pause execution to receive keyboard input from the user."},
            {"number": 23, "title": "Reading Multiple Inputs", "description": "Ask for several answers in order and store each in its own variable."},
            {"number": 24, "title": "Understanding int() and float()", "description": "Convert string input into calculable numbers."},
            {"number": 25, "title": "Arithmetic Operators", "description": "Perform +, -, *, /, //, %, and ** operations."},
            {"number": 26, "title": "Assignment Operators", "description": "Use +=, -=, *=, and other compound operators."},
            {"number": 27, "title": "Comparison Operators", "description": "Evaluate ==, !=, <, >, <=, and >= to booleans."},
            {"number": 28, "title": "Logical Operators", "description": "Combine expressions using and, or, and not."},
            {"number": 29, "title": "Operator Precedence", "description": "Understand PEMDAS order of operations in Python."},
            {"number": 30, "title": "World 3 Examination", "description": "Build interactive computational workflows."}
        ]
    },
    {
        "number": 4,
        "title": "Conditional Statements",
        "goal": "Enable your programs to make decisions and branch execution paths.",
        "description": "Master if, elif, else, nested conditions, and boolean logic branching.",
        "final_project_title": "Age Eligibility and Grade Checker",
        "final_project_desc": "Build an intelligent evaluation engine for student grades and event admission.",
        "levels": [
            {"number": 31, "title": "Decision Making in Programming", "description": "Understand branching logic and conditional flow."},
            {"number": 32, "title": "Understanding if", "description": "Execute code blocks only when a condition evaluates to True."},
            {"number": 33, "title": "Understanding else", "description": "Provide a default fallback path when the condition is False."},
            {"number": 34, "title": "Understanding elif", "description": "Evaluate multiple mutually exclusive conditions in sequence."},
            {"number": 35, "title": "Multiple Conditions", "description": "Combine conditions using logical operators in if statements."},
            {"number": 36, "title": "Nested if Statements", "description": "Structure sub-decisions inside parent conditional blocks."},
            {"number": 37, "title": "Combining Conditions", "description": "Write concise, robust boolean compound conditions."},
            {"number": 38, "title": "Common Conditional Mistakes", "description": "Avoid = vs == errors and improper indentation traps."},
            {"number": 39, "title": "World 4 Examination", "description": "Demonstrate complete mastery of conditional logic."}
        ]
    },
    {
        "number": 5,
        "title": "Loops",
        "goal": "Automate repetitive tasks through iteration and loop controls.",
        "description": "Master while loops, for loops, range(), break, and continue.",
        "final_project_title": "Number Guessing Game",
        "final_project_desc": "Develop a classic interactive guessing game with hint feedback and attempt limits.",
        "levels": [
            {"number": 40, "title": "What Are Loops?", "description": "Understand iteration and repeating execution blocks."},
            {"number": 41, "title": "Understanding while Loops", "description": "Loop as long as a boolean condition remains True."},
            {"number": 42, "title": "Understanding for Loops", "description": "Iterate cleanly over sequences and ranges."},
            {"number": 43, "title": "Understanding range()", "description": "Generate numeric arithmetic sequences with start, stop, step."},
            {"number": 44, "title": "break Statement", "description": "Exit a loop immediately when a condition is met."},
            {"number": 45, "title": "continue Statement", "description": "Skip the current iteration and advance to the next."},
            {"number": 46, "title": "Nested Loops", "description": "Run loops inside loops for matrices and grids."},
            {"number": 47, "title": "Infinite Loops and Prevention", "description": "Recognize loop termination conditions and avoid system hangs."},
            {"number": 48, "title": "World 5 Examination", "description": "Prove your algorithmic repetition and loop control skills."}
        ]
    },
    {
        "number": 6,
        "title": "Strings and Collections",
        "goal": "Store, organize, and transform complex groups of data using Python data structures.",
        "description": "Master string slicing, lists, tuples, sets, dictionaries, and nested collections.",
        "final_project_title": "Student Records Management System",
        "final_project_desc": "Implement a full in-memory student database with grades, lookup, and statistics.",
        "levels": [
            {"number": 49, "title": "Strings in Depth", "description": "Explore character encodings, immutability, and length."},
            {"number": 50, "title": "String Indexing", "description": "Access individual characters using zero-based and negative indices."},
            {"number": 51, "title": "String Slicing", "description": "Extract substrings with [start:stop:step] syntax."},
            {"number": 52, "title": "String Methods", "description": "Transform text using upper(), lower(), strip(), split(), replace()."},
            {"number": 53, "title": "What Are Lists?", "description": "Understand ordered, mutable collections of items."},
            {"number": 54, "title": "Creating and Accessing Lists", "description": "Instantiate lists and retrieve elements by position."},
            {"number": 55, "title": "Adding and Removing List Items", "description": "Use append(), insert(), remove(), and pop()."},
            {"number": 56, "title": "Updating Lists", "description": "Modify list elements in-place and sort them."},
            {"number": 57, "title": "List Methods", "description": "Master index(), count(), reverse(), and sort()."},
            {"number": 58, "title": "Understanding Tuples", "description": "Work with immutable ordered sequences for data safety."},
            {"number": 59, "title": "Understanding Sets", "description": "Store unique elements and perform set union/intersection."},
            {"number": 60, "title": "Understanding Dictionaries", "description": "Store key-value pairs for fast associative lookup."},
            {"number": 61, "title": "Dictionary Methods", "description": "Master keys(), values(), items(), and get()."},
            {"number": 62, "title": "Nested Collections", "description": "Build lists of dictionaries and multidimensional arrays."},
            {"number": 63, "title": "World 6 Examination", "description": "Manipulate complex data architectures and collections."}
        ]
    },
    {
        "number": 7,
        "title": "Functions",
        "goal": "Write reusable, modular, and maintainable code blocks with functions.",
        "description": "Master def, parameters, return values, scope, default arguments, and lambdas.",
        "final_project_title": "Modular Calculator",
        "final_project_desc": "Architect a clean multi-operation mathematical engine organized into discrete functions.",
        "levels": [
            {"number": 64, "title": "What Are Functions?", "description": "Understand code reusability and the DRY principle."},
            {"number": 65, "title": "Creating Functions with def", "description": "Declare function signatures and indented execution bodies."},
            {"number": 66, "title": "Calling Functions", "description": "Invoke functions with parentheses and receive execution control."},
            {"number": 67, "title": "Parameters and Arguments", "description": "Pass values into functions dynamically."},
            {"number": 68, "title": "Return Statements", "description": "Send calculated results back to the caller."},
            {"number": 69, "title": "Local and Global Variables", "description": "Understand variable scope and the global keyword."},
            {"number": 70, "title": "Default Arguments", "description": "Provide optional fallback parameter values."},
            {"number": 71, "title": "Keyword Arguments", "description": "Pass arguments explicitly by name regardless of order."},
            {"number": 72, "title": "Variable-Length Arguments", "description": "Accept arbitrary positional (*args) and keyword (**kwargs) parameters."},
            {"number": 73, "title": "Lambda Functions", "description": "Write concise anonymous single-expression functions."},
            {"number": 74, "title": "World 7 Examination", "description": "Demonstrate modular code design and functional programming."}
        ]
    },
    {
        "number": 8,
        "title": "Error Handling and File Management",
        "goal": "Build crash-resistant applications that persist data permanently to disk.",
        "description": "Master exception handling with try/except/finally, file I/O, and JSON serialization.",
        "final_project_title": "File-Based Notes Application",
        "final_project_desc": "Build a command-line note keeper that saves, reads, and searches notes on disk.",
        "levels": [
            {"number": 75, "title": "Understanding Programming Errors", "description": "Distinguish between compile-time and runtime failures."},
            {"number": 76, "title": "Syntax Errors", "description": "Diagnose and fix syntax, quotation, and colon errors."},
            {"number": 77, "title": "Runtime Errors", "description": "Handle ZeroDivisionError, TypeError, and NameError gracefully."},
            {"number": 78, "title": "Logical Errors", "description": "Debug programs that run but produce incorrect results."},
            {"number": 79, "title": "try and except", "description": "Catch exceptions to prevent application crashes."},
            {"number": 80, "title": "Multiple Exception Handling", "description": "Handle distinct exceptions with specialized handlers."},
            {"number": 81, "title": "finally", "description": "Guarantee cleanup actions regardless of whether errors occurred."},
            {"number": 82, "title": "Reading Files", "description": "Open and read text files safely using the with statement."},
            {"number": 83, "title": "Writing Files", "description": "Write and append structured data to filesystem files."},
            {"number": 84, "title": "Working with JSON", "description": "Serialize and deserialize Python dictionaries to JSON."},
            {"number": 85, "title": "World 8 Examination", "description": "Build robust, error-tolerant, persistent applications."}
        ]
    },
    {
        "number": 9,
        "title": "Modules and Python Tools",
        "goal": "Leverage Python's rich ecosystem of standard and third-party libraries.",
        "description": "Master imports, standard libraries (math, random, os), pip, and virtual environments.",
        "final_project_title": "Utility Toolkit",
        "final_project_desc": "Create a multi-tool utility package providing random password generation and math utilities.",
        "levels": [
            {"number": 86, "title": "What Are Modules?", "description": "Organize code into separate reusable Python files."},
            {"number": 87, "title": "Importing Modules", "description": "Master import, from ... import, and import as aliases."},
            {"number": 88, "title": "Built-in Modules", "description": "Explore the standard library: math, random, datetime, and sys."},
            {"number": 89, "title": "Creating Custom Modules", "description": "Write your own module and import functions across files."},
            {"number": 90, "title": "Understanding pip", "description": "Discover Python package installer and PyPI repository."},
            {"number": 91, "title": "Installing External Libraries", "description": "Install and verify third-party packages."},
            {"number": 92, "title": "Virtual Environments", "description": "Isolate project dependencies with venv."},
            {"number": 93, "title": "Understanding Python Packages", "description": "Structure multi-module libraries with __init__.py."},
            {"number": 94, "title": "World 9 Examination", "description": "Showcase modular system development with libraries."}
        ]
    },
    {
        "number": 10,
        "title": "Object-Oriented Programming",
        "goal": "Model real-world entities and complex systems using classes, objects, and inheritance.",
        "description": "Master classes, attributes, methods, __init__, self, inheritance, and encapsulation.",
        "final_project_title": "Banking Management System",
        "final_project_desc": "Architect a complete banking system with SavingsAccount and CheckingAccount classes.",
        "levels": [
            {"number": 95, "title": "What Is Object-Oriented Programming?", "description": "Understand OOP paradigms and state encapsulation."},
            {"number": 96, "title": "Classes and Objects", "description": "Define class blueprints and instantiate distinct objects."},
            {"number": 97, "title": "Attributes", "description": "Attach and access data properties on instances."},
            {"number": 98, "title": "Methods", "description": "Define functions inside classes that operate on instance data."},
            {"number": 99, "title": "Constructors and __init__()", "description": "Initialize object state upon creation."},
            {"number": 100, "title": "Understanding self", "description": "Master the explicit instance reference in Python methods."},
            {"number": 101, "title": "Inheritance", "description": "Create parent and child classes with shared behaviors."},
            {"number": 102, "title": "Encapsulation", "description": "Protect internal state using private variables and getters/setters."},
            {"number": 103, "title": "Polymorphism", "description": "Override methods to implement specialized subclass behaviors."},
            {"number": 104, "title": "Class Variables and Instance Variables", "description": "Distinguish between shared class state and per-instance data."},
            {"number": 105, "title": "World 10 Examination", "description": "Model robust object-oriented software architectures."}
        ]
    },
    {
        "number": 11,
        "title": "Advanced Python",
        "goal": "Write idiomatic, highly performant Python like an experienced senior developer.",
        "description": "Master comprehensions, generators, decorators, recursion, and context managers.",
        "final_project_title": "Advanced Data Processing Application",
        "final_project_desc": "Build an analytical pipeline transforming datasets with generators and custom decorators.",
        "levels": [
            {"number": 106, "title": "List Comprehensions", "description": "Write concise, performant inline list transformations."},
            {"number": 107, "title": "Dictionary Comprehensions", "description": "Create associative dictionaries cleanly in a single expression."},
            {"number": 108, "title": "Iterators", "description": "Understand __iter__() and __next__() protocols."},
            {"number": 109, "title": "Generators", "description": "Stream large datasets on-demand with yield without memory bloat."},
            {"number": 110, "title": "Decorators", "description": "Wrap and enhance functions using @decorator syntax."},
            {"number": 111, "title": "Recursion", "description": "Solve complex problems by having functions call themselves."},
            {"number": 112, "title": "Working with Dates and Time", "description": "Parse, format, and calculate time intervals with datetime."},
            {"number": 113, "title": "Regular Expressions", "description": "Search and validate string patterns using the re module."},
            {"number": 114, "title": "Context Managers", "description": "Build custom resource handlers with with and __enter__/__exit__."},
            {"number": 115, "title": "Advanced Examination", "description": "Synthesize advanced Python techniques into clean solutions."}
        ]
    },
    {
        "number": 12,
        "title": "Real-World Development",
        "goal": "Transition from syntax mastery to shipping production-ready Python applications.",
        "description": "Master REST APIs, SQL databases, Git version control, testing, and debugging.",
        "final_project_title": "Complete Database-Connected Python Application",
        "final_project_desc": "Construct an end-to-end Python system connected to a SQLite database with automated tests.",
        "levels": [
            {"number": 116, "title": "Introduction to APIs", "description": "Understand how applications communicate over networks."},
            {"number": 117, "title": "HTTP Requests", "description": "Master GET, POST, PUT, DELETE verbs and status codes."},
            {"number": 118, "title": "Working with JSON APIs", "description": "Fetch, parse, and handle responses from modern web services."},
            {"number": 119, "title": "Introduction to SQL", "description": "Understand relational database tables, columns, and queries."},
            {"number": 120, "title": "SQLite with Python", "description": "Connect to SQLite using the built-in sqlite3 module."},
            {"number": 121, "title": "Database CRUD Operations", "description": "Create, Read, Update, and Delete relational records."},
            {"number": 122, "title": "Introduction to Git", "description": "Track changes, manage commits, and version software."},
            {"number": 123, "title": "GitHub Basics", "description": "Push repositories and collaborate using remote version control."},
            {"number": 124, "title": "Debugging Applications", "description": "Use breakpoint debugging and traceback inspection to fix issues."},
            {"number": 125, "title": "Testing with unittest", "description": "Write automated unit test suites to guarantee code stability."},
            {"number": 126, "title": "Final Python Examination", "description": "The ultimate capstone proving complete Python developer capability."}
        ]
    }
]

# Detailed curriculum content for World 1 (Levels 1 to 10)
DETAILED_LESSONS = {
    1: {
        "title": "What Is Programming?",
        "learning_objectives": [
            "Understand what computer programming actually is without confusing jargon",
            "Learn how computers interpret and execute sequential instructions",
            "Discover why programming empowers you to solve real-world problems",
            "Identify the difference between human languages and programming languages"
        ],
        "prerequisites": "None! This level is crafted for someone who has never written a single line of code.",
        "introduction": "Welcome to Python Quest! Imagine you are teaching someone how to make a cup of tea. You can't just say 'make tea' and expect magic. You must give clear, step-by-step instructions: 1. Boil water. 2. Place tea bag in mug. 3. Pour hot water. 4. Wait 3 minutes. Computer programming is exactly the same: it is the art of writing precise, step-by-step instructions that tell a computer what to do.",
        "detailed_explanation": "Computers are incredibly fast, but they have zero intuition. A computer cannot guess what you want; it will only follow the exact instructions you provide. A programming language is simply a structured language that humans can write and computers can translate into machine actions.\n\nWhy does programming matter? Because with programming, you can automate repetitive tasks, analyze massive amounts of information in seconds, build websites, create games, and solve complex mathematical challenges that would take humans weeks to calculate by hand.",
        "terminology": [
            {"term": "Program", "definition": "A sequence of instructions written in a programming language that tells a computer to perform a specific task."},
            {"term": "Code", "definition": "The actual written instructions in a programming language."},
            {"term": "Execution", "definition": "The act of a computer running your instructions and carrying them out step by step."},
            {"term": "Algorithm", "definition": "A step-by-step procedure or set of rules for solving a specific problem."}
        ],
        "syntax_breakdown": "In Python, each instruction is usually written on its own line. Python executes your instructions from top to bottom, one by one.\nExample:\ninstruction_one\ninstruction_two\ninstruction_three",
        "practical_examples": [
            {
                "title": "Example 1: Displaying a simple message",
                "code": "print('Welcome to programming!')",
                "explanation": "The print function tells Python to display the enclosed words on the screen.",
                "output": "Welcome to programming!"
            },
            {
                "title": "Example 2: Executing multiple sequential steps",
                "code": "print('Step 1: Power On')\nprint('Step 2: Initialize System')\nprint('Step 3: Ready for Quest')",
                "explanation": "Notice how Python displays each step in exact order from top to bottom.",
                "output": "Step 1: Power On\nStep 2: Initialize System\nStep 3: Ready for Quest"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print('Welcome to programming!')", "explanation": "Calls the built-in print command with the message 'Welcome to programming!' inside quotes."}
        ],
        "expected_output": "Welcome to programming!\nStep 1: Power On\nStep 2: Initialize System\nStep 3: Ready for Quest",
        "common_mistakes": [
            {
                "mistake": "Print('Hello')",
                "why": "Python is case-sensitive! 'Print' with a capital P is not recognized; it must be lowercase 'print'.",
                "fix": "print('Hello')"
            },
            {
                "mistake": "print(Hello)",
                "why": "Words without quotation marks confuse Python into thinking they are variables rather than text.",
                "fix": "print('Hello')"
            }
        ],
        "real_world_apps": "Every digital service you use—from Instagram sending you notifications to Spotify organizing your playlists—relies on millions of sequential instructions just like this.",
        "summary": "Programming is writing clear, sequential instructions for a computer. Python runs instructions line by line from top to bottom. Capitalization and quotes matter!",
        "practice_questions": [
            "What does a computer do when it runs a program?",
            "In what order does Python execute multiple lines of code?",
            "Why is print('Hi') valid, but Print('Hi') causes an error?"
        ]
    },
    2: {
        "title": "What Is Python?",
        "learning_objectives": [
            "Discover why Python was created and what makes it unique",
            "Understand Python's philosophy: readability and simplicity",
            "Learn what an interpreted language means",
            "See the vast domains where Python is used (AI, Data, Web, Automation)"
        ],
        "prerequisites": "Level 1: What Is Programming?",
        "introduction": "In the late 1980s, a Dutch programmer named Guido van Rossum wanted a programming language that was as easy and enjoyable to read as plain English. He named it 'Python' not after the snake, but after the British comedy show 'Monty Python's Flying Circus'! Today, Python is the most popular language in the world.",
        "detailed_explanation": "Many older programming languages require cumbersome syntax: semicolons at every line end, curly braces everywhere, and heavy boilerplate. Python replaced all of that with clean indentation and simple English keywords.\n\nPython is an 'interpreted' language. This means you do not have to manually compile your code into machine binary before testing it. An interpreter translates and runs your code immediately, making learning and debugging fast and friendly.",
        "terminology": [
            {"term": "Interpreter", "definition": "A program that reads your Python code line by line and executes it directly."},
            {"term": "Syntax", "definition": "The grammar rules that dictate how code must be formatted and written in a language."},
            {"term": "Readable Code", "definition": "Code that is clear and easy for human beings to read and comprehend."}
        ],
        "syntax_breakdown": "Python uses whitespace and clear English words. Unlike other languages, you do not need semicolons (;) at the end of lines.\nCorrect: print('Python is clean')\nAvoid: print('Python is clean');  # Semicolons are unnecessary in Python",
        "practical_examples": [
            {
                "title": "Example: Python's simplicity vs traditional languages",
                "code": "print('Python makes coding accessible to everyone!')",
                "explanation": "In languages like Java or C++, doing this requires 5 to 7 lines of boilerplate class and main function declarations. In Python, it is a single elegant line.",
                "output": "Python makes coding accessible to everyone!"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print('Python makes coding accessible to everyone!')", "explanation": "Outputs the sentence directly to the console."}
        ],
        "expected_output": "Python makes coding accessible to everyone!",
        "common_mistakes": [
            {
                "mistake": "print 'Hello'",
                "why": "In modern Python 3, print is a function and requires parentheses () around what you want to print.",
                "fix": "print('Hello')"
            }
        ],
        "real_world_apps": "NASA uses Python for scientific computing. Netflix uses Python for recommendation algorithms. Google uses Python for search and backend systems.",
        "summary": "Python is designed for human readability and productivity. It is an interpreted language widely used in AI, Web, Data Science, and Automation.",
        "practice_questions": [
            "Why is Python considered easier to read than many other languages?",
            "What does an interpreter do with your code?"
        ]
    },
    3: {
        "title": "Installing and Running Python",
        "learning_objectives": [
            "Understand how Python runs on your machine",
            "Learn what the Python interactive shell (REPL) is",
            "Understand Python script files with the .py extension",
            "Learn how our integrated learning environment executes your code securely"
        ],
        "prerequisites": "Level 2: What Is Python?",
        "introduction": "To run Python on any computer, you need the Python runtime installed. In this app, we provide a built-in Python runner right in your browser, so you can start practicing immediately while understanding how local Python installations work.",
        "detailed_explanation": "When Python is installed on your computer, it provides two primary modes:\n1. Interactive REPL (Read-Eval-Print Loop): You type one line, press Enter, and get immediate results.\n2. Script Execution: You write your instructions in a text file saved with the '.py' extension (e.g. 'main.py') and tell Python to run the whole file: 'python main.py'.",
        "terminology": [
            {"term": ".py Extension", "definition": "The standard file extension used to save Python source code files."},
            {"term": "Terminal / Console", "definition": "A text-based window where commands are entered and code outputs are displayed."},
            {"term": "Script", "definition": "A file containing Python code meant to be executed from start to finish."}
        ],
        "syntax_breakdown": "Running a script in terminal:\npython filename.py\nInside the file, you write standard Python statements on each line.",
        "practical_examples": [
            {
                "title": "Example: Simulating script execution",
                "code": "print('Executing script: mission_start.py')\nprint('Status: All systems nominal')",
                "explanation": "When Python runs this script, it prints both lines in sequence.",
                "output": "Executing script: mission_start.py\nStatus: All systems nominal"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print('Executing script: mission_start.py')", "explanation": "Prints execution header."},
            {"line": "2", "code": "print('Status: All systems nominal')", "explanation": "Prints status message."}
        ],
        "expected_output": "Executing script: mission_start.py\nStatus: All systems nominal",
        "common_mistakes": [
            {
                "mistake": "Naming files python.py",
                "why": "Never name your own script 'python.py' or 'math.py', as it can confuse the Python interpreter with built-in modules.",
                "fix": "Use descriptive names like 'my_first_program.py' or 'calculator.py'."
            }
        ],
        "real_world_apps": "Professional software engineers save their code in git repositories as structured .py files and run automated test suites.",
        "summary": "Python code is saved in files ending in .py and executed by the Python runtime.",
        "practice_questions": [
            "What is the standard file extension for Python code?",
            "What is the difference between interactive mode and running a script file?"
        ]
    },
    4: {
        "title": "Your First Python Program",
        "learning_objectives": [
            "Write the traditional programmer's 'Hello, World!' program",
            "Understand the structure of a function call with arguments",
            "Experience the thrill of having the computer execute your code"
        ],
        "prerequisites": "Level 3: Installing and Running Python",
        "introduction": "In 1978, computer scientist Brian Kernighan wrote a tutorial that began with printing 'hello, world'. Since then, almost every programmer on Earth begins their journey with this exact tradition. Today, you join that worldwide community!",
        "detailed_explanation": "Let's examine the command:\nprint('Hello, World!')\nHere, 'print' is a built-in tool that Python gives you. The parentheses '()' act like open hands waiting to receive what you want to print. The quotes indicate literal words.",
        "terminology": [
            {"term": "Function Call", "definition": "Invoking a pre-written tool by writing its name followed by parentheses () containing any input data."},
            {"term": "Argument", "definition": "The value you pass inside the parentheses of a function for it to work with."}
        ],
        "syntax_breakdown": "print('Your Message Here')\n- Function: print\n- Opening parenthesis: (\n- Quote: '\n- Content: Your Message Here\n- Closing quote: '\n- Closing parenthesis: )",
        "practical_examples": [
            {
                "title": "Example 1: The classic program",
                "code": "print('Hello, World!')",
                "explanation": "Outputs the famous phrase to your screen.",
                "output": "Hello, World!"
            },
            {
                "title": "Example 2: Personalizing your greeting",
                "code": "print('Hello, Python Quest Learner!')",
                "explanation": "You can print any message you wish inside the quotes.",
                "output": "Hello, Python Quest Learner!"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print('Hello, World!')", "explanation": "Displays 'Hello, World!' on the console."}
        ],
        "expected_output": "Hello, World!",
        "common_mistakes": [
            {
                "mistake": "print('Hello, World!)",
                "why": "Missing the closing quote mark will trigger a SyntaxError: EOL while scanning string literal.",
                "fix": "print('Hello, World!')"
            },
            {
                "mistake": "print('Hello, World!'",
                "why": "Missing the closing parenthesis causes a SyntaxError.",
                "fix": "print('Hello, World!')"
            }
        ],
        "real_world_apps": "Printing is the simplest and most vital debugging tool programmers use to inspect what their program is doing at any moment.",
        "summary": "Every programmer starts with print('Hello, World!'). Always remember matching parentheses and quotation marks.",
        "practice_questions": [
            "Write the code to print 'I am a Python Programmer!'",
            "What error happens if you forget the closing parenthesis?"
        ]
    },
    5: {
        "title": "Understanding print()",
        "learning_objectives": [
            "Print multiple items in a single print statement",
            "Master the sep parameter to change how items are separated",
            "Master the end parameter to control newline behavior"
        ],
        "prerequisites": "Level 4: Your First Python Program",
        "introduction": "So far you have printed one message at a time. But print() is surprisingly versatile! You can print multiple values separated by commas, format output neatly, and control whether Python jumps to a new line.",
        "detailed_explanation": "By default, when you pass multiple items separated by commas inside print(), Python prints them with a space between them:\nprint('Python', 'is', 'awesome') -> 'Python is awesome'\n\nFurthermore, print() has two powerful optional parameters:\n1. sep: Specifies what character separates each item (default is a space ' ').\n2. end: Specifies what is printed at the very end (default is a newline '\\n').",
        "terminology": [
            {"term": "Parameter", "definition": "A named option you can pass to a function to configure its behavior."},
            {"term": "Delimiter / Separator", "definition": "A character used to separate distinct pieces of data, such as a hyphen or comma."},
            {"term": "Newline (\\n)", "definition": "An invisible character that moves the cursor down to the beginning of the next line."}
        ],
        "syntax_breakdown": "print(item1, item2, ..., sep=' ', end='\\n')\n- sep='-' puts a hyphen between items\n- end=' ' keeps the cursor on the same line for the next print statement",
        "practical_examples": [
            {
                "title": "Example 1: Printing multiple items",
                "code": "print('Player:', 'Alex', 'XP:', 150)",
                "explanation": "Python prints all four values on one line with spaces in between.",
                "output": "Player: Alex XP: 150"
            },
            {
                "title": "Example 2: Custom separator with sep",
                "code": "print('2026', '11', '02', sep='-')",
                "explanation": "Using sep='-' separates the date parts with dashes.",
                "output": "2026-11-02"
            },
            {
                "title": "Example 3: Controlling line endings with end",
                "code": "print('Loading', end='... ')\nprint('Done!')",
                "explanation": "Because end='... ' was used, the second print continues on the exact same line.",
                "output": "Loading... Done!"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print('2026', '11', '02', sep='-')", "explanation": "Prints 2026-11-02 separated by dashes."}
        ],
        "expected_output": "Player: Alex XP: 150\n2026-11-02\nLoading... Done!",
        "common_mistakes": [
            {
                "mistake": "print('Apples' 'Bananas')",
                "why": "Forgetting the comma between items merges them together without spaces.",
                "fix": "print('Apples', 'Bananas')"
            }
        ],
        "real_world_apps": "Command-line tools format progress bars, formatted tables, and timestamps using custom separators and line endings.",
        "summary": "print() takes multiple arguments separated by commas. Use sep to customize the spacing character and end to prevent newlines.",
        "practice_questions": [
            "How do you print three words separated by slashes (/)?",
            "How do you print two messages on the exact same line using two print() calls?"
        ]
    },
    6: {
        "title": "Understanding Text and Strings",
        "learning_objectives": [
            "Understand what strings are in programming",
            "Use single quotes vs double quotes vs triple quotes",
            "Master escape characters like \\n (newline) and \\t (tab)",
            "Combine strings using concatenation (+)"
        ],
        "prerequisites": "Level 5: Understanding print()",
        "introduction": "In computer programming, any piece of textual data is called a 'string' (short for a string of characters). Letters, numbers, spaces, and punctuation symbols can all be part of a string.",
        "detailed_explanation": "In Python, you create strings by wrapping characters inside matching quotes. You can use single quotes ('hello') or double quotes (\"hello\").\n\nWhat if your text contains an apostrophe, like \"I'm ready\"? If you use single quotes around it ('I'm ready'), Python gets confused where the string ends. To solve this, you can either wrap it in double quotes (\"I'm ready\") or use an escape character ('I\\'m ready').\n\nFor multi-line text, you can use triple quotes (\"\"\"Text here\"\"\").",
        "terminology": [
            {"term": "String", "definition": "A sequence of characters enclosed in quotation marks representing text."},
            {"term": "Escape Character (\\)", "definition": "A backslash followed by a character that gives it a special meaning, such as \\n for a new line."},
            {"term": "Concatenation", "definition": "Joining two or more strings together end-to-end using the + operator."}
        ],
        "syntax_breakdown": "'Single quoted string'\n\"Double quoted string\"\n\"\"\"Triple quoted multi-line string\"\"\"\n'Hello ' + 'World'  # Concatenation",
        "practical_examples": [
            {
                "title": "Example 1: Quotes and apostrophes",
                "code": "print(\"It's a great day to code!\")",
                "explanation": "Double quotes allow single quotes inside without confusion.",
                "output": "It's a great day to code!"
            },
            {
                "title": "Example 2: Escape characters (\\n and \\t)",
                "code": "print('Item:\\tPython Quest\\nCost:\\tFree')",
                "explanation": "\\n creates a new line; \\t inserts a tab space.",
                "output": "Item:\tPython Quest\nCost:\tFree"
            },
            {
                "title": "Example 3: String concatenation",
                "code": "print('Code' + 'Quest')",
                "explanation": "The + symbol glues strings together.",
                "output": "CodeQuest"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print('Code' + ' ' + 'Quest')", "explanation": "Joins 'Code', a space, and 'Quest' into 'Code Quest'."}
        ],
        "expected_output": "It's a great day to code!\nItem:\tPython Quest\nCost:\tFree\nCodeQuest",
        "common_mistakes": [
            {
                "mistake": "print('I'm coding')",
                "why": "Unescaped single quote closes the string prematurely.",
                "fix": "print(\"I'm coding\")"
            },
            {
                "mistake": "print('Total: ' + 50)",
                "why": "You cannot concatenate a string and a raw number directly with + in Python.",
                "fix": "print('Total: ' + '50') or print('Total:', 50)"
            }
        ],
        "real_world_apps": "Every form field, username, chat message, and article in software is represented and processed as strings.",
        "summary": "Strings represent text wrapped in quotes. Use \\n for newlines and \\t for tabs. Combine strings with +.",
        "practice_questions": [
            "How do you print a string that contains both single and double quotes?",
            "What will 'Python' + ' ' + 'Quest' produce?"
        ]
    },
    7: {
        "title": "Understanding Numbers",
        "learning_objectives": [
            "Distinguish between whole numbers (integers) and decimals (floats)",
            "Perform basic arithmetic directly in Python",
            "Understand why numbers do not need quotation marks"
        ],
        "prerequisites": "Level 6: Understanding Text and Strings",
        "introduction": "Computers were originally invented to calculate numbers. In Python, doing math is as straightforward as using a pocket calculator, but with extraordinary power and precision.",
        "detailed_explanation": "Python has two fundamental numeric types for beginners:\n1. Integers (int): Whole numbers like 5, 0, -42, 1000000. No decimal points.\n2. Floats (float): Numbers with decimal points like 3.14, 0.5, -9.99.\n\nNotice: Numbers must NEVER be surrounded by quotation marks if you want to do math with them. '10' is text (a string), while 10 is an actual calculable number.",
        "terminology": [
            {"term": "Integer (int)", "definition": "A whole number, positive, negative, or zero, without a decimal component."},
            {"term": "Float", "definition": "A floating-point number containing a decimal point."},
            {"term": "Expression", "definition": "A piece of code that evaluates to a single value, such as 10 + 5."}
        ],
        "syntax_breakdown": "print(10 + 5)   # Addition -> 15\nprint(10 - 3)   # Subtraction -> 7\nprint(4 * 2)    # Multiplication -> 8\nprint(10 / 2)   # Division -> 5.0 (always produces a float)",
        "practical_examples": [
            {
                "title": "Example 1: Basic arithmetic in print()",
                "code": "print(100 + 50)\nprint(20 * 4)\nprint(15 / 3)",
                "explanation": "Python calculates the expression inside print() before displaying the result.",
                "output": "150\n80\n5.0"
            },
            {
                "title": "Example 2: Combining strings and math",
                "code": "print('Total Score:', 50 + 25)",
                "explanation": "Passing a string label and a math calculation separated by a comma.",
                "output": "Total Score: 75"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print(10 + 5)", "explanation": "Calculates 10 + 5 and prints 15."}
        ],
        "expected_output": "150\n80\n5.0\nTotal Score: 75",
        "common_mistakes": [
            {
                "mistake": "print('5' + '5')",
                "why": "With quotes, these are strings, so Python concatenates them into '55' instead of adding them into 10!",
                "fix": "print(5 + 5)"
            }
        ],
        "real_world_apps": "Game engines calculate player physics and health points; banking apps calculate interest rates and balances using numeric operations.",
        "summary": "Integers are whole numbers; floats have decimal points. Leave off quotes to calculate mathematical expressions.",
        "practice_questions": [
            "What is the difference in output between print(2 + 2) and print('2 + 2')?",
            "What does division (/) always produce in Python?"
        ]
    },
    8: {
        "title": "Python Comments",
        "learning_objectives": [
            "Understand why code comments are essential for humans",
            "Write single-line comments using the hash symbol (#)",
            "Write multi-line comments and docstrings",
            "Learn how to use comments to temporarily disable code for testing"
        ],
        "prerequisites": "Level 7: Understanding Numbers",
        "introduction": "When you write code, you are not just writing for the computer—you are writing for future you and for other humans who will read your work. Comments are notes you leave in your code that Python completely ignores during execution.",
        "detailed_explanation": "Whenever Python encounters a hash symbol (#), it ignores everything from that symbol to the end of that specific line.\n\nGood comments explain 'WHY' something is done, not just 'WHAT' is done. For instance:\n# Bad comment: print hello\nprint('Hello')\n\n# Good comment: Greet the user after successful login\nprint('Welcome back, Alex!')",
        "terminology": [
            {"term": "Comment", "definition": "A note written in source code intended solely for humans; ignored by the Python interpreter."},
            {"term": "Comment Out", "definition": "Temporarily turning executable code into a comment to test alternative logic without deleting it."}
        ],
        "syntax_breakdown": "# This is a single-line comment\nprint('This runs')  # This is an inline comment\n\n\"\"\"\nThis is a multi-line\ncomment block\n\"\"\"",
        "practical_examples": [
            {
                "title": "Example: Documenting a calculation",
                "code": "# Calculate final quest reward with 20% bonus\nbase_xp = 100\nprint('Reward:', base_xp + 20)",
                "explanation": "The comment line is completely ignored during execution.",
                "output": "Reward: 120"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "# Calculate final quest reward", "explanation": "Comment explaining the purpose of the following code."}
        ],
        "expected_output": "Reward: 120",
        "common_mistakes": [
            {
                "mistake": "print('Test') // comment",
                "why": "Python uses # for comments, NOT // like C, Java, or JavaScript.",
                "fix": "print('Test')  # comment"
            }
        ],
        "real_world_apps": "Professional software teams rely on comments and documentation to maintain millions of lines of code across teams.",
        "summary": "Use # for single-line comments. Comments are ignored by Python and make your code clear and maintainable.",
        "practice_questions": [
            "Which character starts a comment in Python?",
            "Will a line starting with # print anything to the screen?"
        ]
    },
    9: {
        "title": "Understanding Basic Syntax",
        "learning_objectives": [
            "Master Python's case-sensitivity rules",
            "Understand how indentation defines code blocks in Python",
            "Learn how statements and lines are structured",
            "Recognize common syntax error indicators"
        ],
        "prerequisites": "Level 8: Python Comments",
        "introduction": "Every human language has grammar rules: punctuation, capitalization, and sentence structure. In programming, these rules are called 'syntax'. If you break a syntax rule, Python stops and tells you exactly what went wrong.",
        "detailed_explanation": "Two rules are foundational in Python:\n1. Case Sensitivity: 'name', 'Name', and 'NAME' are three completely different things to Python. Python keywords like 'print', 'if', 'for' must always be lowercase.\n2. Indentation: In most languages, spaces at the start of a line are just for aesthetics. In Python, indentation has semantic meaning! Leading spaces indicate that a line belongs inside a specific block.",
        "terminology": [
            {"term": "Syntax", "definition": "The formal rules governing the structure and grammar of code in a language."},
            {"term": "Case Sensitive", "definition": "Distinguishing strictly between uppercase and lowercase letters."},
            {"term": "Indentation", "definition": "The spaces at the beginning of a code line used to define code hierarchy and blocks."}
        ],
        "syntax_breakdown": "# Valid Python statement:\nprint('Properly aligned')\n\n# Indentation error:\n  print('Indented for no reason!')  # Causes IndentationError",
        "practical_examples": [
            {
                "title": "Example: Clean statement alignment",
                "code": "print('Line 1: Clean alignment')\nprint('Line 2: Matches indentation perfectly')",
                "explanation": "Both lines start at column 0 without unexpected leading spaces.",
                "output": "Line 1: Clean alignment\nLine 2: Matches indentation perfectly"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print('Line 1')", "explanation": "Valid unindented top-level statement."}
        ],
        "expected_output": "Line 1: Clean alignment\nLine 2: Matches indentation perfectly",
        "common_mistakes": [
            {
                "mistake": " print('Oops')",
                "why": "Adding random spaces at the start of a line triggers an unexpected IndentationError.",
                "fix": "print('Oops')  # Start at the left margin"
            }
        ],
        "real_world_apps": "Clean syntax and standardized indentation (PEP 8) ensure that large open-source projects can be read effortlessly by anyone.",
        "summary": "Python is case-sensitive. Top-level statements must start at the left margin without random spaces.",
        "practice_questions": [
            "Are print and Print the same in Python?",
            "What error happens if you randomly press space before writing print()?"
        ]
    },
    10: {
        "title": "World 1 Examination",
        "learning_objectives": [
            "Synthesize all concepts from World 1 into a complete program",
            "Combine text, numbers, separators, line breaks, and comments",
            "Complete the World 1 Final Project: Personal Introduction Program"
        ],
        "prerequisites": "Levels 1 through 9",
        "introduction": "Congratulations on reaching the World 1 Examination! You have learned the foundational mechanics of Python: instructions, print formatting, strings, numbers, comments, and syntax. Now it is time to prove your skills and build your first complete project.",
        "detailed_explanation": "In this examination, you will review core concepts through the MCQ test and complete the final Boss Challenge: The Personal Introduction Program. Your program will output a formatted card introducing yourself as a programmer, computing numbers, using custom separators, and featuring clean comments.",
        "terminology": [
            {"term": "Project", "definition": "A complete, self-contained program that achieves a meaningful real-world or simulation objective."}
        ],
        "syntax_breakdown": "# Combine multiple skills:\n# 1. Comments\n# 2. String manipulation\n# 3. Numeric calculations\n# 4. sep and end formatting parameters",
        "practical_examples": [
            {
                "title": "Example: Formatted summary",
                "code": "# Python Quest Bio Card\nprint('=== HERO PROFILE ===')\nprint('Hero:', 'Cipher')\nprint('Starting Level:', 1)\nprint('XP:', 0 + 50)",
                "explanation": "Demonstrates clear comments, string headers, multiple arguments, and math.",
                "output": "=== HERO PROFILE ===\nHero: Cipher\nStarting Level: 1\nXP: 50"
            }
        ],
        "line_by_line": [
            {"line": "1", "code": "print('=== HERO PROFILE ===')", "explanation": "Prints profile card header."}
        ],
        "expected_output": "=== HERO PROFILE ===\nHero: Cipher\nStarting Level: 1\nXP: 50",
        "common_mistakes": [
            {
                "mistake": "Skipping comments or test cases",
                "why": "Always review problem requirements thoroughly before submitting your final challenge.",
                "fix": "Follow each requirement step by step."
            }
        ],
        "real_world_apps": "Real software development is about combining foundational building blocks into useful, coherent applications.",
        "summary": "You are now ready to tackle the World 1 Examination and Boss Challenge. Good luck, developer!",
        "practice_questions": [
            "What makes up a complete beginner Python script?",
            "How do comments help when writing longer programs?"
        ]
    }
}

# Coding challenges for World 1
CHALLENGES_DATA = [
    # Level 1
    {
        "level_number": 1,
        "title": "Instruction Sequence",
        "difficulty": "easy",
        "is_boss": False,
        "description": "Write a Python program that prints two separate lines of instructions:\nLine 1: System Boot\nLine 2: Ready for Quest",
        "requirements": "Use two print() statements. Ensure the exact capitalization matches the prompt.",
        "initial_code": "# Write two print statements below:\n",
        "solution_code": "print('System Boot')\nprint('Ready for Quest')",
        "hints": ["Use print('System Boot') first", "Add print('Ready for Quest') on the second line"],
        "xp_reward": 30,
        "test_cases": [
            {"input_data": "", "expected_output": "System Boot\nReady for Quest", "is_hidden": False, "explanation": "Two sequential lines output correctly."}
        ]
    },
    {
        "level_number": 1,
        "title": "Boss Challenge: Mission Launch Sequence",
        "difficulty": "boss",
        "is_boss": True,
        "description": "Complete the mission launch countdown sequence. Print three lines:\nCountdown: 3\nCountdown: 2\nCountdown: 1\nLaunch Python Quest!",
        "requirements": "Print the exact 4 lines in order.",
        "initial_code": "# Mission Launch Challenge\n",
        "solution_code": "print('Countdown: 3')\nprint('Countdown: 2')\nprint('Countdown: 1')\nprint('Launch Python Quest!')",
        "hints": ["Use 4 separate print() statements", "Check your spelling and punctuation"],
        "xp_reward": 150,
        "test_cases": [
            {"input_data": "", "expected_output": "Countdown: 3\nCountdown: 2\nCountdown: 1\nLaunch Python Quest!", "is_hidden": False}
        ]
    },
    # Level 4
    {
        "level_number": 4,
        "title": "Hello World Tradition",
        "difficulty": "easy",
        "is_boss": False,
        "description": "Print the classic programmer's phrase: Hello, World!",
        "requirements": "Exact string: Hello, World!",
        "initial_code": "# Print Hello, World!\n",
        "solution_code": "print('Hello, World!')",
        "hints": ["Make sure to include the comma and exclamation mark"],
        "xp_reward": 30,
        "test_cases": [
            {"input_data": "", "expected_output": "Hello, World!", "is_hidden": False}
        ]
    },
    {
        "level_number": 4,
        "title": "Boss Challenge: The Developer Oath",
        "difficulty": "boss",
        "is_boss": True,
        "description": "Print the two-line Developer Oath:\nI am a Python developer.\nI will write clean, readable code.",
        "requirements": "Print exactly both lines.",
        "initial_code": "# Write the Developer Oath\n",
        "solution_code": "print('I am a Python developer.')\nprint('I will write clean, readable code.')",
        "hints": ["Check periods at the end of both lines"],
        "xp_reward": 150,
        "test_cases": [
            {"input_data": "", "expected_output": "I am a Python developer.\nI will write clean, readable code.", "is_hidden": False}
        ]
    },
    # Level 5
    {
        "level_number": 5,
        "title": "Custom Delimiters",
        "difficulty": "easy",
        "is_boss": False,
        "description": "Print three fruits: 'Apple', 'Banana', 'Cherry' separated by a hyphen '-' using the sep parameter.",
        "requirements": "Use print('Apple', 'Banana', 'Cherry', sep='-')",
        "initial_code": "# Use sep to separate fruits with a dash:\n",
        "solution_code": "print('Apple', 'Banana', 'Cherry', sep='-')",
        "hints": ["The sep parameter goes at the end: sep='-'"],
        "xp_reward": 30,
        "test_cases": [
            {"input_data": "", "expected_output": "Apple-Banana-Cherry", "is_hidden": False}
        ]
    },
    {
        "level_number": 5,
        "title": "Boss Challenge: Continuous Status Bar",
        "difficulty": "boss",
        "is_boss": True,
        "description": "Print 'Loading' followed by '... ' on the same line, then finish with '100%'.\nOutput should be: Loading... 100%",
        "requirements": "Use two print statements. The first print must use end='... '.",
        "initial_code": "# Use the end parameter on the first print\n",
        "solution_code": "print('Loading', end='... ')\nprint('100%')",
        "hints": ["print('Loading', end='... ')", "Then print('100%')"],
        "xp_reward": 150,
        "test_cases": [
            {"input_data": "", "expected_output": "Loading... 100%", "is_hidden": False}
        ]
    },
    # Level 7
    {
        "level_number": 7,
        "title": "Python Math Calculator",
        "difficulty": "easy",
        "is_boss": False,
        "description": "Calculate and print the result of multiplying 25 by 4.",
        "requirements": "Do not print the string '100', compute it with 25 * 4.",
        "initial_code": "# Calculate 25 times 4\n",
        "solution_code": "print(25 * 4)",
        "hints": ["Use the asterisk * for multiplication"],
        "xp_reward": 30,
        "test_cases": [
            {"input_data": "", "expected_output": "100", "is_hidden": False}
        ]
    },
    {
        "level_number": 7,
        "title": "Boss Challenge: Arithmetic Card",
        "difficulty": "boss",
        "is_boss": True,
        "description": "Print the following two lines showing calculations:\nSum: 150\nProduct: 500\n(Where 150 is calculated as 100 + 50, and 500 is calculated as 50 * 10)",
        "requirements": "Use math expressions for the numbers.",
        "initial_code": "# Arithmetic Card\n",
        "solution_code": "print('Sum:', 100 + 50)\nprint('Product:', 50 * 10)",
        "hints": ["print('Sum:', 100 + 50)", "print('Product:', 50 * 10)"],
        "xp_reward": 150,
        "test_cases": [
            {"input_data": "", "expected_output": "Sum: 150\nProduct: 500", "is_hidden": False}
        ]
    },
    # Level 10
    {
        "level_number": 10,
        "title": "World 1 Capstone: Personal Introduction Program",
        "difficulty": "boss",
        "is_boss": True,
        "description": "Create your official Personal Introduction Program!\nOutput must match this exact format:\n=== PYTHON QUEST PROFILE ===\nName: Quest Explorer\nRole: Python Apprentice\nXP Target: 500\nStatus: Ready for World 2",
        "requirements": "Use comments to document your code. Print the 5 lines shown above.",
        "initial_code": "# World 1 Capstone Project: Personal Introduction Program\n",
        "solution_code": "# World 1 Capstone Project\nprint('=== PYTHON QUEST PROFILE ===')\nprint('Name: Quest Explorer')\nprint('Role: Python Apprentice')\nprint('XP Target:', 250 + 250)\nprint('Status: Ready for World 2')",
        "hints": ["Make sure the header has exactly three equals signs on both sides: ==="],
        "xp_reward": 150,
        "test_cases": [
            {"input_data": "", "expected_output": "=== PYTHON QUEST PROFILE ===\nName: Quest Explorer\nRole: Python Apprentice\nXP Target: 500\nStatus: Ready for World 2", "is_hidden": False}
        ]
    }
]

# MCQ Quiz questions for World 1
# Use the same authored World 1 records for both fresh databases and the
# bundled full curriculum. The legacy list above only covered five levels.
CHALLENGES_DATA = [
    item for item in CHALLENGES_DATA
    if not 1 <= item["level_number"] <= 39
] + [
    {**challenge, "level_number": level["number"]}
    for level in WORLD_1["levels"]
    for challenge in level["challenges"]
] + [
    {**challenge, "level_number": level["number"]}
    for level in WORLD_2["levels"]
    for challenge in level["challenges"]
] + [
    {**challenge, "level_number": level["number"]}
    for level in WORLD_3["levels"]
    for challenge in level["challenges"]
] + [
    {**challenge, "level_number": level["number"]}
    for level in WORLD_4["levels"]
    for challenge in level["challenges"]
]

QUIZ_DATA = [
    # Level 1
    {
        "level_number": 1,
        "question": "What is the primary role of a computer program?",
        "explanation": "A computer program is a sequence of precise instructions telling a computer what tasks to perform.",
        "options": [
            {"text": "A set of sequential instructions telling a computer what to do", "is_correct": True, "explanation": "Correct! Programs direct computer hardware through sequential instructions."},
            {"text": "A physical device inside the computer monitor", "is_correct": False, "explanation": "Incorrect. That is hardware, whereas a program is software."},
            {"text": "A human language spoken by computers", "is_correct": False, "explanation": "Incorrect. Computers execute machine code, not human language."},
            {"text": "A tool used exclusively for browsing social media", "is_correct": False, "explanation": "Incorrect. Programs control all computer software."}
        ]
    },
    {
        "level_number": 1,
        "question": "In what order does Python execute instructions in a script?",
        "explanation": "Python executes code sequentially from top to bottom, one line at a time.",
        "options": [
            {"text": "From top to bottom, line by line", "is_correct": True, "explanation": "Correct! Execution starts at line 1 and proceeds downward."},
            {"text": "From bottom to top in reverse order", "is_correct": False, "explanation": "Incorrect. Code does not run backwards."},
            {"text": "Randomly depending on file size", "is_correct": False, "explanation": "Incorrect. Execution order is deterministic."},
            {"text": "All lines simultaneously at the exact same instant", "is_correct": False, "explanation": "Incorrect. Standard script execution is sequential."}
        ]
    },
    # Level 4
    {
        "level_number": 4,
        "question": "What will be the output of print('Python', 'Quest')?",
        "explanation": "When given multiple arguments, print() separates them with a single space by default.",
        "code_snippet": "print('Python', 'Quest')",
        "options": [
            {"text": "Python Quest", "is_correct": True, "explanation": "Correct! Comma-separated arguments receive a space between them."},
            {"text": "PythonQuest", "is_correct": False, "explanation": "Incorrect. A space is automatically inserted by default."},
            {"text": "('Python', 'Quest')", "is_correct": False, "explanation": "Incorrect. The print function prints values, not tuple syntax."},
            {"text": "Error: Too many arguments", "is_correct": False, "explanation": "Incorrect. print() accepts any number of arguments."}
        ]
    },
    {
        "level_number": 4,
        "question": "Which of the following will result in a SyntaxError?",
        "explanation": "Quotes must match and be properly closed in Python strings.",
        "options": [
            {"text": "print('Hello World)", "is_correct": True, "explanation": "Correct! The string is missing its closing single quotation mark."},
            {"text": "print('Hello World')", "is_correct": False, "explanation": "This is completely valid syntax."},
            {"text": "print(\"Hello World\")", "is_correct": False, "explanation": "Double quotes are completely valid in Python."},
            {"text": "print(100)", "is_correct": False, "explanation": "Printing a number is completely valid."}
        ]
    },
    # Level 5
    {
        "level_number": 5,
        "question": "What does the 'sep' parameter in print() do?",
        "explanation": "The sep parameter defines the separator string between multiple arguments.",
        "options": [
            {"text": "Specifies the character placed between printed items", "is_correct": True, "explanation": "Correct! For example sep='-' puts hyphens between arguments."},
            {"text": "Stops the program from printing errors", "is_correct": False, "explanation": "Incorrect. sep only controls argument separation."},
            {"text": "Sorts the items in alphabetical order", "is_correct": False, "explanation": "Incorrect. print() does not sort values."},
            {"text": "Splits a string into a list", "is_correct": False, "explanation": "Incorrect. That is the split() string method, not the sep parameter."}
        ]
    },
    # Level 7
    {
        "level_number": 7,
        "question": "What is the output of print(10 + 5 * 2)?",
        "explanation": "Python respects operator precedence (PEMDAS): multiplication happens before addition (5 * 2 = 10, then 10 + 10 = 20).",
        "code_snippet": "print(10 + 5 * 2)",
        "options": [
            {"text": "20", "is_correct": True, "explanation": "Correct! 5 * 2 = 10, then 10 + 10 = 20."},
            {"text": "30", "is_correct": False, "explanation": "Incorrect. Multiplication takes precedence over addition."},
            {"text": "100", "is_correct": False, "explanation": "Incorrect calculation."},
            {"text": "'10 + 5 * 2'", "is_correct": False, "explanation": "Incorrect. Without quotes, Python evaluates the math expression."}
        ]
    },
    # Level 10
    {
        "level_number": 10,
        "question": "Which character begins a single-line comment in Python?",
        "explanation": "The hash/pound symbol (#) begins a single-line comment.",
        "options": [
            {"text": "#", "is_correct": True, "explanation": "Correct! # signals that the rest of the line is a comment."},
            {"text": "//", "is_correct": False, "explanation": "Incorrect. // is integer division in Python, or comments in other languages like C/JS."},
            {"text": "/*", "is_correct": False, "explanation": "Incorrect. That is CSS or C multi-line comment syntax."},
            {"text": "--", "is_correct": False, "explanation": "Incorrect. That is SQL comment syntax."}
        ]
    }
]

def _sync_world_content(db, world_data):
    """Update authored lesson and challenge content while keeping challenge IDs/progress."""
    world = db.query(World).filter(World.number == world_data["number"]).first()
    if world:
        world.title = world_data["title"]
        world.goal = world_data.get("goal", world.goal)
        world.description = world_data.get("description", world.description)
        world.final_project_title = world_data.get("final_project_title", world.final_project_title)
        world.final_project_desc = world_data.get("final_project_desc", world.final_project_desc)
    for level_data in world_data["levels"]:
        level = db.query(Level).filter(Level.number == level_data["number"]).first()
        if not level:
            continue
        level.title = level_data["title"]
        level.description = level_data["description"]

        lesson_data = level_data["lesson"]
        lesson = db.query(Lesson).filter(Lesson.level_id == level.id).first()
        if lesson:
            lesson.title = level_data["title"]
            for field in ("learning_objectives", "terminology", "practical_examples", "line_by_line", "common_mistakes", "practice_questions"):
                if field in lesson_data:
                    setattr(lesson, field, json.dumps(lesson_data[field], ensure_ascii=False))
            for field in ("prerequisites", "introduction", "detailed_explanation", "syntax_breakdown", "expected_output", "real_world_apps", "summary"):
                if field in lesson_data:
                    setattr(lesson, field, lesson_data[field])

        for order_index, challenge_data in enumerate(level_data["challenges"], start=1):
            challenge = db.query(CodingChallenge).filter(
                CodingChallenge.level_id == level.id,
                CodingChallenge.is_boss == challenge_data.get("is_boss", False),
            ).order_by(CodingChallenge.id).first()
            if not challenge:
                challenge = CodingChallenge(
                    level_id=level.id,
                    title=challenge_data["title"],
                    description=challenge_data["description"],
                )
                db.add(challenge)
                db.flush()
            challenge.title = challenge_data["title"]
            challenge.difficulty = challenge_data.get("difficulty", "easy")
            challenge.is_boss = challenge_data.get("is_boss", False)
            challenge.description = challenge_data["description"]
            challenge.requirements = challenge_data.get("requirements", "")
            challenge.initial_code = challenge_data.get("initial_code", "# Write your answer below.\\n")
            challenge.solution_code = challenge_data.get("solution_code", "")
            challenge.hints = json.dumps(challenge_data.get("hints", []), ensure_ascii=False)
            challenge.xp_reward = challenge_data.get("xp_reward", 35)
            challenge.order_index = order_index
            db.flush()
            db.query(TestCase).filter(TestCase.challenge_id == challenge.id).delete(synchronize_session=False)
            for test_data in challenge_data.get("test_cases", []):
                db.add(TestCase(
                    challenge_id=challenge.id,
                    input_data=test_data.get("input_data", ""),
                    expected_output=test_data["expected_output"],
                    is_hidden=test_data.get("is_hidden", False),
                    explanation=test_data.get("explanation", ""),
                ))
    db.commit()


def _sync_authored_worlds(db):
    _sync_world_content(db, WORLD_1)
    _sync_world_content(db, WORLD_2)
    _sync_world_content(db, WORLD_3)
    _sync_world_content(db, WORLD_4)
    _sync_world_content(db, WORLD_5)
    _sync_world_content(db, WORLD_6)
    _sync_world_quizzes(db, WORLD_3)
    _sync_world_quizzes(db, WORLD_4)
    _sync_world_quizzes(db, WORLD_5)
    _sync_world_quizzes(db, WORLD_6)


def _sync_world_quizzes(db, world_data):
    """Keep authored quiz questions and choices aligned without changing IDs."""
    for level_data in world_data["levels"]:
        level = db.query(Level).filter(Level.number == level_data["number"]).first()
        if not level:
            continue
        questions = db.query(QuizQuestion).filter(
            QuizQuestion.level_id == level.id
        ).order_by(QuizQuestion.id).all()
        for order_index, question_data in enumerate(level_data.get("quizzes", []), start=1):
            if order_index <= len(questions):
                question = questions[order_index - 1]
            else:
                question = QuizQuestion(
                    level_id=level.id,
                    question=question_data["question"],
                )
                db.add(question)
                db.flush()
                questions.append(question)
            question.question = question_data["question"]
            question.question_type = question_data.get("question_type", "single")
            question.code_snippet = question_data.get("code_snippet")
            question.explanation = question_data.get("explanation", "")
            question.order_index = order_index
            options = db.query(QuizOption).filter(
                QuizOption.question_id == question.id
            ).order_by(QuizOption.id).all()
            for option_index, option_data in enumerate(question_data.get("options", [])):
                if option_index < len(options):
                    option = options[option_index]
                else:
                    option = QuizOption(question_id=question.id)
                    db.add(option)
                option.option_text = option_data["text"]
                option.is_correct = option_data.get("is_correct", False)
                option.explanation = option_data.get("explanation", "")
    db.commit()


def seed_curriculum(db):
    """
    Populates all 12 Worlds, 126 Levels, detailed lessons, coding challenges, test cases, and quizzes.
    """
    # 1. Seed Achievements
    seed_achievements(db)

    # 2. Check if curriculum already populated
    existing_worlds = db.query(World).count()
    if existing_worlds >= 12:
        _sync_authored_worlds(db)
        return

    print("Seeding Python Quest curriculum...")

    for w_data in WORLDS_DATA:
        world = db.query(World).filter(World.number == w_data["number"]).first()
        if not world:
            world = World(
                number=w_data["number"],
                title=w_data["title"],
                goal=w_data["goal"],
                description=w_data["description"],
                final_project_title=w_data["final_project_title"],
                final_project_desc=w_data["final_project_desc"],
                is_unlocked_by_default=w_data.get("is_unlocked_by_default", False)
            )
            db.add(world)
            db.commit()
            db.refresh(world)

        # Create levels in this world
        for order_idx, lvl_data in enumerate(w_data.get("levels", [])):
            level = db.query(Level).filter(Level.number == lvl_data["number"]).first()
            if not level:
                level = Level(
                    world_id=world.id,
                    number=lvl_data["number"],
                    title=lvl_data["title"],
                    description=lvl_data["description"],
                    order_index=order_idx + 1,
                    is_unlocked_by_default=(world.number == 1 and order_idx == 0)
                )
                db.add(level)
                db.commit()
                db.refresh(level)

            # Check if detailed lesson exists for this level
            if lvl_data["number"] in DETAILED_LESSONS:
                d_lesson = DETAILED_LESSONS[lvl_data["number"]]
                existing_lesson = db.query(Lesson).filter(Lesson.level_id == level.id).first()
                if not existing_lesson:
                    new_lesson = Lesson(
                        level_id=level.id,
                        title=d_lesson["title"],
                        learning_objectives=json.dumps(d_lesson["learning_objectives"]),
                        prerequisites=d_lesson["prerequisites"],
                        introduction=d_lesson["introduction"],
                        detailed_explanation=d_lesson["detailed_explanation"],
                        terminology=json.dumps(d_lesson["terminology"]),
                        syntax_breakdown=d_lesson["syntax_breakdown"],
                        practical_examples=json.dumps(d_lesson["practical_examples"]),
                        line_by_line=json.dumps(d_lesson["line_by_line"]),
                        expected_output=d_lesson["expected_output"],
                        common_mistakes=json.dumps(d_lesson["common_mistakes"]),
                        real_world_apps=d_lesson["real_world_apps"],
                        summary=d_lesson["summary"],
                        practice_questions=json.dumps(d_lesson["practice_questions"])
                    )
                    db.add(new_lesson)
            else:
                # Provide structured template lesson for levels 11-126
                existing_lesson = db.query(Lesson).filter(Lesson.level_id == level.id).first()
                if not existing_lesson:
                    new_lesson = Lesson(
                        level_id=level.id,
                        title=lvl_data["title"],
                        learning_objectives=json.dumps([
                            f"Understand core principles of {lvl_data['title']}",
                            "Learn how Python implements this concept efficiently",
                            "Practice writing real code using this technique"
                        ]),
                        prerequisites=f"World {world.number} foundational lessons",
                        introduction=f"In this level, you will master {lvl_data['title']}. {lvl_data['description']}",
                        detailed_explanation=f"Python provides clean and elegant syntax for {lvl_data['title']}. Programmers use this concept to build reliable, high-performance applications.",
                        terminology=json.dumps([
                            {"term": lvl_data["title"], "definition": f"Core Python programming concept for {world.title}."}
                        ]),
                        syntax_breakdown=f"# Syntax for {lvl_data['title']}\n# Follow Python standard formatting principles.",
                        practical_examples=json.dumps([
                            {
                                "title": f"Example: {lvl_data['title']}",
                                "code": f"# Demonstrating {lvl_data['title']}\nprint('Mastering {lvl_data['title']} in Python Quest!')",
                                "explanation": "Executes clean Python logic demonstrating this topic.",
                                "output": f"Mastering {lvl_data['title']} in Python Quest!"
                            }
                        ]),
                        line_by_line=json.dumps([
                            {"line": "1", "code": "print('Python Quest')", "explanation": "Demonstrates the concept."}
                        ]),
                        expected_output=f"Mastering {lvl_data['title']} in Python Quest!",
                        common_mistakes=json.dumps([
                            {
                                "mistake": "Skipping variable initialization or incorrect syntax",
                                "why": "Python requires proper declarations and matching syntax rules.",
                                "fix": "Ensure accurate spelling, indentation, and variable assignments."
                            }
                        ]),
                        real_world_apps=f"Used extensively across backend services, data analysis pipelines, and production systems.",
                        summary=f"Mastery of {lvl_data['title']} equips you with essential problem-solving power in Python.",
                        practice_questions=json.dumps([
                            f"How is {lvl_data['title']} utilized in software development?",
                            "What are the best practices when writing this code?"
                        ])
                    )
                    db.add(new_lesson)

    # Sync authored World 1 and World 2 content for new databases too.
    _sync_authored_worlds(db)

    # 3. Seed Challenges
    for ch_data in CHALLENGES_DATA:
        level = db.query(Level).filter(Level.number == ch_data["level_number"]).first()
        if not level:
            continue

        existing_ch = db.query(CodingChallenge).filter(
            CodingChallenge.level_id == level.id,
            CodingChallenge.title == ch_data["title"]
        ).first()

        if not existing_ch:
            challenge = CodingChallenge(
                level_id=level.id,
                title=ch_data["title"],
                difficulty=ch_data["difficulty"],
                is_boss=ch_data["is_boss"],
                description=ch_data["description"],
                requirements=ch_data.get("requirements", ""),
                initial_code=ch_data.get("initial_code", "# Write your code here\n"),
                solution_code=ch_data.get("solution_code", ""),
                hints=json.dumps(ch_data.get("hints", [])),
                xp_reward=ch_data.get("xp_reward", 30),
                order_index=1 if not ch_data["is_boss"] else 99
            )
            db.add(challenge)
            db.commit()
            db.refresh(challenge)

            for tc in ch_data.get("test_cases", []):
                test_case = TestCase(
                    challenge_id=challenge.id,
                    input_data=tc.get("input_data", ""),
                    expected_output=tc["expected_output"],
                    is_hidden=tc.get("is_hidden", False),
                    explanation=tc.get("explanation", "")
                )
                db.add(test_case)

    # Ensure every level has at least one challenge and one boss challenge
    for level in db.query(Level).all():
        ch_count = db.query(CodingChallenge).filter(CodingChallenge.level_id == level.id).count()
        if ch_count == 0:
            # Add standard challenge
            std_ch = CodingChallenge(
                level_id=level.id,
                title=f"Practice: {level.title}",
                difficulty="medium",
                is_boss=False,
                description=f"Demonstrate your understanding of {level.title}. Print the topic completion confirmation:\n{level.title}: Completed",
                requirements=f"Output: {level.title}: Completed",
                initial_code=f"# Print confirmation for {level.title}\n",
                solution_code=f"print('{level.title}: Completed')",
                hints=json.dumps([f"Use print('{level.title}: Completed')"]),
                xp_reward=50,
                order_index=1
            )
            db.add(std_ch)
            db.commit()
            db.refresh(std_ch)
            db.add(TestCase(challenge_id=std_ch.id, input_data="", expected_output=f"{level.title}: Completed", is_hidden=False))

            # Add boss challenge
            boss_ch = CodingChallenge(
                level_id=level.id,
                title=f"Boss Challenge: {level.title} Mastery",
                difficulty="boss",
                is_boss=True,
                description=f"Mastery challenge for Level {level.number}. Print:\nLevel {level.number} Mastered: {level.title}",
                requirements="Exact line match.",
                initial_code=f"# Boss challenge for Level {level.number}\n",
                solution_code=f"print('Level {level.number} Mastered: {level.title}')",
                hints=json.dumps(["Check exact spelling and spacing"]),
                xp_reward=150,
                order_index=99
            )
            db.add(boss_ch)
            db.commit()
            db.refresh(boss_ch)
            db.add(TestCase(challenge_id=boss_ch.id, input_data="", expected_output=f"Level {level.number} Mastered: {level.title}", is_hidden=False))

    # 4. Seed Quizzes
    for q_data in QUIZ_DATA:
        level = db.query(Level).filter(Level.number == q_data["level_number"]).first()
        if not level:
            continue

        existing_q = db.query(QuizQuestion).filter(
            QuizQuestion.level_id == level.id,
            QuizQuestion.question == q_data["question"]
        ).first()

        if not existing_q:
            quiz_q = QuizQuestion(
                level_id=level.id,
                question=q_data["question"],
                code_snippet=q_data.get("code_snippet"),
                explanation=q_data.get("explanation"),
                order_index=1
            )
            db.add(quiz_q)
            db.commit()
            db.refresh(quiz_q)

            for opt in q_data.get("options", []):
                db.add(QuizOption(
                    question_id=quiz_q.id,
                    option_text=opt["text"],
                    is_correct=opt["is_correct"],
                    explanation=opt.get("explanation", "")
                ))

    # Ensure every level has at least 2 quiz questions
    for level in db.query(Level).all():
        q_count = db.query(QuizQuestion).filter(QuizQuestion.level_id == level.id).count()
        if q_count == 0:
            q1 = QuizQuestion(
                level_id=level.id,
                question=f"What is the core focus of '{level.title}'?",
                explanation=f"{level.title} teaches essential programming fundamentals in Python.",
                order_index=1
            )
            db.add(q1)
            db.commit()
            db.refresh(q1)
            db.add(QuizOption(question_id=q1.id, option_text=f"Mastering practical techniques in {level.title}", is_correct=True, explanation="Correct!"))
            db.add(QuizOption(question_id=q1.id, option_text="Writing unreadable, disorganized code", is_correct=False, explanation="Incorrect."))
            db.add(QuizOption(question_id=q1.id, option_text="Replacing Python with a spreadsheet", is_correct=False, explanation="Incorrect."))
            db.add(QuizOption(question_id=q1.id, option_text="Ignoring syntax rules", is_correct=False, explanation="Incorrect."))

            q2 = QuizQuestion(
                level_id=level.id,
                question=f"Why is {level.title} important when developing software in Python?",
                explanation="Python constructs ensure code correctness, modularity, and maintainability.",
                order_index=2
            )
            db.add(q2)
            db.commit()
            db.refresh(q2)
            db.add(QuizOption(question_id=q2.id, option_text="It provides foundational skills for building real-world programs", is_correct=True, explanation="Correct!"))
            db.add(QuizOption(question_id=q2.id, option_text="It causes random errors in programs", is_correct=False, explanation="Incorrect."))
            db.add(QuizOption(question_id=q2.id, option_text="It is never used in real programming", is_correct=False, explanation="Incorrect."))
            db.add(QuizOption(question_id=q2.id, option_text="It is only needed on older operating systems", is_correct=False, explanation="Incorrect."))

    db.commit()
    print("Python Quest curriculum successfully seeded!")
