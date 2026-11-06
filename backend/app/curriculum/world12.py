"""Curriculum module: WORLD_12, revised for clear beginner explanations."""

WORLD_12 = {'description': 'Master REST APIs, SQL, SQLite with Python, parameterized security, git, pdb, unittest, and typing.',
 'final_project_desc': 'Architect a production-grade SQLite database application featuring parameterized CRUD, '
                       'transaction rollbacks, schema validation, and unit tests.',
 'final_project_title': 'Complete Database-Connected Python Application',
 'goal': 'Build production-grade, job-ready software with databases, APIs, testing, git, and debugging.',
 'is_unlocked_by_default': False,
 'levels': [{'challenges': [{'description': 'Your task, step by step:\n1. Read one HTTP status code.\n2. Print Success for 200–299, Client Error for 400–499, Server Error for 500–599, and Other for every remaining number.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['code = int(input())\n'
                                       'if 200 <= code <= 299:\n'
                                       "    print('Success')\n"
                                       'elif 400 <= code <= 499:\n'
                                       "    print('Client Error')\n"
                                       'elif 500 <= code <= 599:\n'
                                       "    print('Server Error')\n"
                                       'else:\n'
                                       "    print('Other')"],
                             'initial_code': '# HTTP Status Code Classifier\n'
                                             '# Step 1: Read status code:\n'
                                             'code = int(input())\n'
                                             '\n'
                                             '# Step 2: Classify code range below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'code = int(input())\n'
                                              'if 200 <= code <= 299:\n'
                                              "    print('Success')\n"
                                              'elif 400 <= code <= 499:\n'
                                              "    print('Client Error')\n"
                                              'elif 500 <= code <= 599:\n'
                                              "    print('Server Error')\n"
                                              'else:\n'
                                              "    print('Other')",
                             'test_cases': [{'expected_output': 'Success', 'input_data': '200\n', 'is_hidden': False},
                                            {'expected_output': 'Client Error',
                                             'input_data': '404\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Server Error',
                                             'input_data': '503\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Other', 'input_data': '302\n', 'is_hidden': False}],
                             'title': 'Classify an HTTP Status Code',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Finish dispatch(method, path).\n2. Return the shown response for GET /status, GET /users, and POST /users.\n3. For every other method-and-path pair, return 404 Not Found.\n4. The example calls the function four times and prints each response.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def dispatch(method, path):\n'
                                       '    routes = {\n'
                                       "        ('GET', '/status'): '200 OK: Service Healthy',\n"
                                       "        ('GET', '/users'): '200 OK: 2 Users Online',\n"
                                       "        ('POST', '/users'): '201 Created: New User Registered',\n"
                                       '    }\n'
                                       "    return routes.get((method, path), '404 Not Found')\n"
                                       "for request in [('GET', '/status'), ('GET', '/users'), ('POST', '/users'), "
                                       "('DELETE', '/unknown')]:\n"
                                       '    print(dispatch(*request))'],
                             'initial_code': '# ⚔️ Boss Challenge: RESTful Route Dispatcher\n'
                                             '\n'
                                             'def dispatch(method, path):\n'
                                             '    # Step 1: Return the appropriate HTTP response string:\n'
                                             '    pass\n'
                                             '\n'
                                             '# Step 2: Test your dispatcher with the required routes:\n'
                                             "print(dispatch('GET', '/status'))\n"
                                             "print(dispatch('POST', '/users'))\n"
                                             "print(dispatch('DELETE', '/unknown'))\n",
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def dispatch(method, path):\n'
                                              '    routes = {\n'
                                              "        ('GET', '/status'): '200 OK: Service Healthy',\n"
                                              "        ('GET', '/users'): '200 OK: 2 Users Online',\n"
                                              "        ('POST', '/users'): '201 Created: New User Registered',\n"
                                              '    }\n'
                                              "    return routes.get((method, path), '404 Not Found')\n"
                                              "for request in [('GET', '/status'), ('GET', '/users'), ('POST', "
                                              "'/users'), ('DELETE', '/unknown')]:\n"
                                              '    print(dispatch(*request))',
                             'test_cases': [{'expected_output': '200 OK: Service Healthy\n'
                                                                '200 OK: 2 Users Online\n'
                                                                '201 Created: New User Registered\n'
                                                                '404 Not Found',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Dispatch API Routes',
                             'xp_reward': 150}],
             'description': 'Understand REST client-server architecture, HTTP methods (GET, POST, PUT, DELETE), and '
                            'status codes.',
             'lesson': {'common_mistakes': [{'fix': 'Always use POST or DELETE for state-changing operations.',
                                             'mistake': 'Using GET requests to delete or mutate database data',
                                             'why': 'Web crawlers, browsers, and proxies pre-fetch GET links '
                                                    'automatically! Mutating state via GET can trigger accidental data '
                                                    'deletion.'}],
                        'detailed_explanation': 'A client is the program that asks for something. A server receives '
                                                'the request and sends a reply. A browser is often a client, and the '
                                                'website is often the server.\n'
                                                '\n'
                                                'The HTTP method says what the client wants: GET reads information, '
                                                'POST sends new information, PUT updates information, and DELETE '
                                                'removes information.\n'
                                                '\n'
                                                'The status code tells how the request went. Codes 200–299 mean '
                                                'success. Codes 400–499 mean the request has a problem, such as a '
                                                'missing page. Codes 500–599 mean the server has a problem. This level '
                                                'practices sorting those replies with Python choices; the example does '
                                                'not contact the internet.',
                        'expected_output': 'Success: Resource fetched',
                        'introduction': 'When you open a page, your browser asks another computer for information. The '
                                        'server sends back the information or a short code explaining what happened.',
                        'learning_objectives': ['Explain how a client asks a server for something.',
                                                'Choose GET, POST, PUT, or DELETE for a requested action.',
                                                'Read common HTTP status-code groups.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'status = 200',
                                          'explanation': 'Save the example reply number in status.'},
                                         {'line': '2',
                                          'code': 'if status == 200:',
                                          'explanation': 'Check whether status is exactly 200.'},
                                         {'line': '3',
                                          'code': "    print('Success: Resource fetched')",
                                          'explanation': 'Because the check is true, display the success message.'},
                                         {'line': '4',
                                          'code': 'elif status == 404:',
                                          'explanation': 'Check this next condition only when the first one was '
                                                         'false.'},
                                         {'line': '5',
                                          'code': "    print('Client Error: Endpoint not found')",
                                          'explanation': 'If the number is 404, display the not-found message.'},
                                         {'line': '6',
                                          'code': 'else:',
                                          'explanation': 'Use this block when none of the earlier checks matched.'},
                                         {'line': '7',
                                          'code': "    print('Status:', status)",
                                          'explanation': 'Show the number for every other status.'}],
                        'practical_examples': [{'code': 'status = 200\n'
                                                        'if status == 200:\n'
                                                        "    print('Success: Resource fetched')\n"
                                                        'elif status == 404:\n'
                                                        "    print('Client Error: Endpoint not found')\n"
                                                        'else:\n'
                                                        "    print('Status:', status)",
                                                'explanation': 'Routes execution based on standard HTTP status '
                                                               'protocol codes.',
                                                'output': 'Success: Resource fetched',
                                                'title': 'Example 1: Inspecting HTTP status code branches'},
                                               {'code': "headers = {'Content-Type': 'application/json', "
                                                        "'Authorization': 'Bearer token123'}\n"
                                                        "print('Request format:', headers['Content-Type'])",
                                                'explanation': 'Headers convey metadata like authentication tokens and '
                                                               'content formats.',
                                                'output': 'Request format: application/json',
                                                'title': 'Example 2: Modeling HTTP request headers dictionary'},
                                               {'code': "base_url = 'https://api.quest.io/v1/search'\n"
                                                        "params = {'q': 'python', 'page': 1}\n"
                                                        "query_str = '&'.join(f'{k}={v}' for k, v in params.items())\n"
                                                        "print('Full URL:', f'{base_url}?{query_str}')",
                                                'explanation': 'Encodes search parameter key-value pairs into standard '
                                                               'URL format.',
                                                'output': 'Full URL: https://api.quest.io/v1/search?q=python&page=1',
                                                'title': 'Example 3: Building dynamic URL query strings'}],
                        'practice_questions': [{'question': 'What does GET usually ask for?',
                                                'answer': 'To read or retrieve information.'},
                                               {'question': 'Which group includes 503?',
                                                'answer': '500–599, a server error.'},
                                               {'question': 'What does 404 usually mean?',
                                                'answer': 'The requested page or item was not found.'}],
                        'prerequisites': 'World 11: Advanced Python',
                        'real_world_apps': 'Websites use methods and status codes when they load pages, save forms, '
                                           'update profiles, and report missing pages.',
                        'summary': 'A client asks a server for an action. The HTTP method names the action, and the '
                                   'status code tells whether it worked.',
                        'syntax_breakdown': 'if 200 <= code <= 299:\n'
                                            "    print('Success')\n"
                                            'elif 400 <= code <= 499:\n'
                                            "    print('Client Error')\n"
                                            'else:\n'
                                            "    print('Other')",
                        'terminology': [{'term': 'Client',
                                         'definition': 'The app or program that asks for information.'},
                                        {'term': 'Server',
                                         'definition': 'The program that receives a request and sends a reply.'},
                                        {'term': 'HTTP method',
                                         'definition': 'A word such as GET or POST that names the requested action.'},
                                        {'term': 'Status code',
                                         'definition': 'A number that gives a short result, such as 200 or 404.'}]},
             'number': 116,
             'quizzes': [{'explanation': '404 is the standard HTTP status code for Not Found.',
                          'options': [{'explanation': 'Correct! 404 matches the first if condition.',
                                       'is_correct': True,
                                       'text': 'Not Found'},
                                      {'explanation': 'Incorrect. 200 is OK.', 'is_correct': False, 'text': 'OK'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'Other'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'}],
                          'question': 'Given this HTTP status handling code:\n'
                                      '\n'
                                      'status_code = 404\n'
                                      'if status_code == 404:\n'
                                      "    print('Not Found')\n"
                                      'elif status_code == 200:\n'
                                      "    print('OK')\n"
                                      'else:\n'
                                      "    print('Other')"},
                         {'explanation': 'POST is used to submit data to be processed and create new resources.',
                          'options': [{'explanation': 'Correct! POST sends data to create resources.',
                                       'is_correct': True,
                                       'text': 'To submit payload data to create a new resource on the server'},
                                      {'explanation': 'Incorrect. That is GET.',
                                       'is_correct': False,
                                       'text': 'To safely retrieve cached data without side effects'},
                                      {'explanation': 'Incorrect. That is DELETE.',
                                       'is_correct': False,
                                       'text': 'To delete a database table'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To establish a TCP handshake'}],
                          'question': 'What is the primary architectural purpose of the HTTP POST verb in REST APIs?'}],
             'title': 'Working with APIs and HTTP Requests'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a status number and one line of JSON text.\n2. If the status is 200, turn the JSON into Python data and print its title and status.\n3. Otherwise, print the HTTP error message shown.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['import json\n'
                                       'status = int(input())\n'
                                       'payload = input()\n'
                                       'if status == 200:\n'
                                       '    data = json.loads(payload)\n'
                                       '    print(f"{data[\'title\']}: {data[\'status\']}")\n'
                                       'else:\n'
                                       "    print(f'HTTP {status}: Request Failed')"],
                             'initial_code': '# Consuming Web APIs: Safe JSON Parsing\n'
                                             'import json\n'
                                             'status = int(input())\n'
                                             'payload = input().strip()\n'
                                             '\n'
                                             '# Step 1: Check status == 200, parse and print below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import json\n'
                                              'status = int(input())\n'
                                              'payload = input()\n'
                                              'if status == 200:\n'
                                              '    data = json.loads(payload)\n'
                                              '    print(f"{data[\'title\']}: {data[\'status\']}")\n'
                                              'else:\n'
                                              "    print(f'HTTP {status}: Request Failed')",
                             'test_cases': [{'expected_output': 'Book: available',
                                             'input_data': '200\n{"title":"Book","status":"available"}\n',
                                             'is_hidden': False},
                                            {'expected_output': 'HTTP 500: Request Failed',
                                             'input_data': '500\n{"error":"server"}\n',
                                             'is_hidden': False}],
                             'title': 'Read a JSON API Response',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read the number of JSON pages.\n2. Each page contains a data list.\n3. Join the lists, then print the number of items and the combined list.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import json\n'
                                       'page_count = int(input())\n'
                                       'all_items = []\n'
                                       'for _ in range(page_count):\n'
                                       '    page = json.loads(input())\n'
                                       "    all_items.extend(page['data'])\n"
                                       "print(f'Total items: {len(all_items)}')\n"
                                       "print(f'Items: {all_items}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Paginated API Stream Consumer\n'
                                             'import json\n'
                                             'n = int(input())\n'
                                             'all_items = []\n'
                                             '\n'
                                             '# Step 1: Loop n times, parse page, extend all_items:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import json\n'
                                              'page_count = int(input())\n'
                                              'all_items = []\n'
                                              'for _ in range(page_count):\n'
                                              '    page = json.loads(input())\n'
                                              "    all_items.extend(page['data'])\n"
                                              "print(f'Total items: {len(all_items)}')\n"
                                              "print(f'Items: {all_items}')",
                             'test_cases': [{'expected_output': 'Total items: 3\nItems: [1, 2, 3]',
                                             'input_data': '2\n{"data":[1,2]}\n{"data":[3]}\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Combine Paginated API Data',
                             'xp_reward': 150}],
             'description': 'Send network requests and parse JSON response payloads using standard libraries and '
                            'patterns.',
             'lesson': {'common_mistakes': [{'fix': 'Always pass a timeout: requests.get(url, timeout=10).',
                                             'mistake': 'Making API requests without setting a timeout',
                                             'why': 'If the remote server hangs, your Python script hangs '
                                                    'indefinitely, freezing your application!'}],
                        'detailed_explanation': 'An API lets one program ask another program for information or an '
                                                'action. The reply has a status code and a response body. The body is '
                                                'the returned data.\n'
                                                '\n'
                                                'JSON is a common text format for that data. It can contain names, '
                                                'values, lists, and nested objects. json.loads(text) reads the text '
                                                'and creates normal Python dictionaries, lists, numbers, and strings.\n'
                                                '\n'
                                                'Check the status before reading fields such as title or data. A '
                                                'successful reply might include those fields; an error reply might '
                                                'contain something different. Our examples use saved sample replies, '
                                                'so they practice handling responses without making a real internet '
                                                'request.',
                        'expected_output': 'Current Temperature: 22.5 C',
                        'introduction': 'A web service often sends its answer as JSON text. Python can turn that text '
                                        'into dictionaries and lists so your program can use the values.',
                        'learning_objectives': ['Read JSON text returned by a web service.',
                                                'Use json.loads() to turn JSON text into Python data.',
                                                'Check for a successful status before using response fields.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'import json',
                                          'explanation': "Load Python's built-in JSON tools."},
                                         {'line': '2',
                                          'code': 'payload = \'{"weather": {"temp": 22.5, "condition": "Sunny"}}\'',
                                          'explanation': 'Save a complete sample response as text.'},
                                         {'line': '3',
                                          'code': 'parsed = json.loads(payload)',
                                          'explanation': 'Turn that text into nested Python dictionaries.'},
                                         {'line': '4',
                                          'code': "print('Current Temperature:', parsed['weather']['temp'], 'C')",
                                          'explanation': 'Read weather, then temp, and display the temperature.'}],
                        'practical_examples': [{'code': 'import json\n'
                                                        'payload = \'{"weather": {"temp": 22.5, "condition": '
                                                        '"Sunny"}}\'\n'
                                                        'parsed = json.loads(payload)\n'
                                                        "print('Current Temperature:', parsed['weather']['temp'], 'C')",
                                                'explanation': 'Navigates nested dictionaries returned by typical '
                                                               'weather APIs.',
                                                'output': 'Current Temperature: 22.5 C',
                                                'title': 'Example 1: Parsing nested JSON REST payloads'},
                                               {'code': "pages = [[{'id': 1}, {'id': 2}], [{'id': 3}]]\n"
                                                        'all_items = []\n'
                                                        'for p in pages:\n'
                                                        '    all_items.extend(p)\n'
                                                        "print('Total records fetched across pages:', len(all_items))",
                                                'explanation': 'Collects items across multiple paginated response '
                                                               'lists.',
                                                'output': 'Total records fetched across pages: 3',
                                                'title': 'Example 2: Simulating paginated API data collection'},
                                               {'code': 'def mock_fetch():\n'
                                                        "    raise TimeoutError('API request timed out')\n"
                                                        'try:\n'
                                                        '    mock_fetch()\n'
                                                        'except TimeoutError as err:\n'
                                                        "    print('Fallback:', err)",
                                                'explanation': 'Demonstrates resilience against network latency '
                                                               'failures.',
                                                'output': 'Fallback: API request timed out',
                                                'title': 'Example 3: Handling API timeout exceptions gracefully'}],
                        'practice_questions': [{'question': 'What does json.loads() return?',
                                                'answer': 'Python values such as dictionaries, lists, strings, and '
                                                          'numbers.'},
                                               {'question': 'Why check the status before reading title?',
                                                'answer': 'An error reply may not contain a title.'},
                                               {'question': "Does this lesson's sample contact a website?",
                                                'answer': 'No. It reads saved sample response text.'}],
                        'prerequisites': 'Level 116: Working with APIs and HTTP Requests',
                        'real_world_apps': 'Apps use this pattern to read weather, books, transit times, and other '
                                           'information returned by web services.',
                        'summary': 'Check whether a request worked, then use json.loads() to turn a JSON response from '
                                   'text into Python data.',
                        'syntax_breakdown': 'import json\n'
                                            'data = json.loads(response_text)\n'
                                            'if status == 200:\n'
                                            "    print(data['title'])\n"
                                            'else:\n'
                                            "    print('Request failed')",
                        'terminology': [{'term': 'API',
                                         'definition': 'A way for one program to ask another program for data or an '
                                                       'action.'},
                                        {'term': 'Response body', 'definition': 'The data sent back by a service.'},
                                        {'term': 'JSON', 'definition': 'A text format for names, values, and lists.'},
                                        {'term': 'json.loads()',
                                         'definition': 'The Python tool that changes JSON text into Python values.'}]},
             'number': 117,
             'quizzes': [{'explanation': "The Content-Type value 'application/json' starts with 'application/', "
                                         'returning True.',
                          'options': [{'explanation': "Correct! 'application/json' starts with 'application/'.",
                                       'is_correct': True,
                                       'text': 'True'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'False'},
                                      {'explanation': 'Incorrect. startswith() returns a boolean.',
                                       'is_correct': False,
                                       'text': 'application/json'},
                                      {'explanation': 'Incorrect. The key exists.',
                                       'is_correct': False,
                                       'text': 'KeyError'}],
                          'question': 'What will be printed when parsing a JSON response header?\n'
                                      '\n'
                                      "headers = {'Content-Type': 'application/json'}\n"
                                      "print(headers['Content-Type'].startswith('application/'))"},
                         {'explanation': 'It prevents the application from hanging indefinitely if the remote server '
                                         'fails to respond within 5 seconds.',
                          'options': [{'explanation': 'Correct! It guards against hanging connections.',
                                       'is_correct': True,
                                       'text': 'It raises a Timeout exception if the server does not respond within 5 '
                                               'seconds'},
                                      {'explanation': 'Incorrect. That is time.sleep().',
                                       'is_correct': False,
                                       'text': 'It pauses the Python program for 5 seconds before making the request'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It limits the download speed to 5 megabytes per second'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It cancels the request after 5 retries'}],
                          'question': 'What is the purpose of passing `timeout=5.0` in `requests.get(url, '
                                      'timeout=5.0)`?'}],
             'title': 'Consuming REST APIs in Python'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a table name and a minimum age.\n2. Print a SELECT statement for people whose age is at least that number.\n3. This task prints SQL text. It does not connect to a database.\n\nInput for this example: The Input box shows 2 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['table = input().strip()\n'
                                       'age = int(input())\n'
                                       "print(f'SELECT name, email FROM {table} WHERE age >= {age};')"],
                             'initial_code': '# SQL Fundamentals: SELECT Queries\n'
                                             'tbl = input().strip()\n'
                                             'age = input().strip()\n'
                                             '\n'
                                             '# Step 1: Print formatted SQL query below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'table = input().strip()\n'
                                              'age = int(input())\n'
                                              "print(f'SELECT name, email FROM {table} WHERE age >= {age};')",
                             'test_cases': [{'expected_output': 'SELECT name, email FROM users WHERE age >= 21;',
                                             'input_data': 'users\n21\n',
                                             'is_hidden': False}],
                             'title': 'Build a SQL SELECT Query',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read student names and scores, then a cutoff.\n2. Store the students in temporary SQLite, then print the names whose scores meet the cutoff, in alphabetical order.\n\nInput for this example: The Input box shows 5 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import sqlite3\n'
                                       'count = int(input())\n'
                                       'rows = [input().split() for _ in range(count)]\n'
                                       'threshold = int(input())\n'
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE students (name TEXT, score INTEGER)')\n"
                                       "connection.executemany('INSERT INTO students VALUES (?, ?)', [(name, "
                                       'int(score)) for name, score in rows])\n'
                                       "for (name,) in connection.execute('SELECT name FROM students WHERE score >= ? "
                                       "ORDER BY name', (threshold,)):\n"
                                       '    print(name)\n'
                                       'connection.close()'],
                             'initial_code': '# ⚔️ Boss Challenge: In-Memory SQL Query Engine\n'
                                             'students = []\n'
                                             'n = int(input())\n'
                                             '\n'
                                             '# Step 1: Read students, then read threshold, filter and print sorted '
                                             'names:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              'count = int(input())\n'
                                              'rows = [input().split() for _ in range(count)]\n'
                                              'threshold = int(input())\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE students (name TEXT, score INTEGER)')\n"
                                              "connection.executemany('INSERT INTO students VALUES (?, ?)', [(name, "
                                              'int(score)) for name, score in rows])\n'
                                              "for (name,) in connection.execute('SELECT name FROM students WHERE "
                                              "score >= ? ORDER BY name', (threshold,)):\n"
                                              '    print(name)\n'
                                              'connection.close()',
                             'test_cases': [{'expected_output': 'Ari\nMia',
                                             'input_data': '3\nMia 90\nBo 65\nAri 80\n75\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Filter Students with SQL',
                             'xp_reward': 150}],
             'description': 'Understand relational database tables, columns, rows, primary keys, and core SQL '
                            'commands.',
             'lesson': {'common_mistakes': [{'fix': 'Always verify your WHERE clause before running DELETE or UPDATE.',
                                             'mistake': 'Running DELETE FROM users; without a WHERE clause',
                                             'why': 'Without a WHERE clause, SQL deletes every single record in the '
                                                    'table permanently!'}],
                        'detailed_explanation': 'A relational database stores related information in tables. A row is '
                                                'one complete record. A column is one kind of detail shared by all '
                                                'records. In a students table, name and score can be columns; one '
                                                "student's name and score make one row.\n"
                                                '\n'
                                                'A primary key is a value that identifies one row, like a student '
                                                'number. Two students may share a name, but their IDs are different. '
                                                'Column types such as INTEGER, TEXT, and REAL describe the kind of '
                                                'value stored.\n'
                                                '\n'
                                                'SQL is the language used to work with tables. SELECT reads rows, '
                                                'INSERT adds rows, UPDATE changes rows, and DELETE removes rows. WHERE '
                                                'limits which rows are affected. Without WHERE, an update or delete '
                                                'can affect every row. The first example below prints SQL text; it '
                                                'does not run a database yet.',
                        'expected_output': 'SELECT name FROM students WHERE score >= 80',
                        'introduction': 'A database table is like a classroom roster. Each row is one person, and each '
                                        'column is one detail such as a name or score.',
                        'learning_objectives': ['Tell database tables, rows, and columns apart.',
                                                'Explain why each row needs a primary key.',
                                                'Recognize SELECT, INSERT, UPDATE, and DELETE.'],
                        'line_by_line': [{'line': '1',
                                          'code': "query = 'SELECT name FROM students WHERE score >= 80'",
                                          'explanation': 'Put a SQL SELECT instruction in a text variable.'},
                                         {'line': '2',
                                          'code': 'print(query)',
                                          'explanation': 'Print the instruction so you can read it. It is not run '
                                                         'because this example has no database connection.'}],
                        'practical_examples': [{'code': "query = 'SELECT name FROM students WHERE score >= 80'\n"
                                                        'print(query)',
                                                'explanation': 'This stores a SQL instruction as text and shows it. No '
                                                               'database is contacted in this example.',
                                                'output': 'SELECT name FROM students WHERE score >= 80',
                                                'title': 'Read a SQL instruction'},
                                               {'code': "sql_insert = 'INSERT INTO users (username, role) VALUES "
                                                        '("alex", "admin");\'\n'
                                                        "print('SQL query:', sql_insert)",
                                                'explanation': 'Maps values into corresponding table columns.',
                                                'output': 'SQL query: INSERT INTO users (username, role) VALUES '
                                                          '("alex", "admin");',
                                                'title': 'Example 2: SQL INSERT statement formatting'},
                                               {'code': "print('Foreign keys connect related tables (e.g. "
                                                        "orders.user_id -> users.id).')",
                                                'explanation': 'Explains relational integrity linking child tables to '
                                                               'parent entities.',
                                                'output': 'Foreign keys connect related tables (e.g. orders.user_id -> '
                                                          'users.id).',
                                                'title': 'Example 3: Relational foreign key concept'}],
                        'practice_questions': [{'question': 'What is one row in a books table?',
                                                'answer': "One book's complete record."},
                                               {'question': 'Why use a primary key if names can repeat?',
                                                'answer': 'It gives every record its own ID.'},
                                               {'question': 'Which SQL word reads rows?', 'answer': 'SELECT.'}],
                        'prerequisites': 'Level 117: Consuming REST APIs in Python',
                        'real_world_apps': 'Schools, shops, games, and banks use tables to keep many records organized '
                                           'and searchable.',
                        'summary': 'Tables organize records into rows and columns. A primary key identifies each row. '
                                   'SQL reads and changes table data.',
                        'syntax_breakdown': 'SELECT name FROM students WHERE score >= 80;\n'
                                            "INSERT INTO students (name, score) VALUES ('Ari', 90);\n"
                                            "UPDATE students SET score = 95 WHERE name = 'Ari';\n"
                                            "DELETE FROM students WHERE name = 'Ari';",
                        'terminology': [{'term': 'Table',
                                         'definition': 'A named group of related records, like a roster.'},
                                        {'term': 'Row', 'definition': 'One record in a table.'},
                                        {'term': 'Column', 'definition': 'One kind of detail stored for every row.'},
                                        {'term': 'Primary key',
                                         'definition': 'A value that uniquely identifies a row.'},
                                        {'term': 'SQL',
                                         'definition': 'The language used to read and change database tables.'}]},
             'number': 118,
             'quizzes': [{'explanation': 'Without a WHERE clause, SQL applies the update to every single row in the '
                                         'users table.',
                          'options': [{'explanation': 'Correct! UPDATE without WHERE modifies the entire table.',
                                       'is_correct': True,
                                       'text': 'Every single row in the users table will have status updated to '
                                               "'INACTIVE'"},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Only the first user row is updated'},
                                      {'explanation': 'Incorrect. SQL allows unfiltered updates.',
                                       'is_correct': False,
                                       'text': 'SQL raises a syntax error requiring a WHERE clause'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'No rows are updated'}],
                          'question': "What is the consequence of executing `UPDATE users SET status = 'INACTIVE';` "
                                      'without a WHERE clause?'},
                         {'explanation': 'A Primary Key uniquely identifies each row in a table and cannot contain '
                                         'NULL values.',
                          'options': [{'explanation': 'Correct! Primary keys guarantee unique row identification.',
                                       'is_correct': True,
                                       'text': 'Uniquely identifies each record and enforces non-null uniqueness'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Encrypts table data on disk'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Automatically deletes old records'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Sorts queries in descending order by default'}],
                          'question': 'What is the primary function of a Primary Key constraint in a relational '
                                      'database table?'}],
             'title': 'Relational Databases and SQL Fundamentals'},
            {'challenges': [{'description': "Your task, step by step:\n1. Create a temporary SQLite database and a users table.\n2. Ask SQLite's table catalog whether users exists, then print Table created: users.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.",
                             'difficulty': 'easy',
                             'hints': ['import sqlite3\n'
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, "
                                       "score INTEGER)')\n"
                                       'found = connection.execute("SELECT name FROM sqlite_master WHERE '
                                       'type=\'table\' AND name=?", (\'users\',)).fetchone()\n'
                                       "print('Table created:', found[0])\n"
                                       'connection.close()'],
                             'initial_code': '# SQLite: Connecting and Creating Tables\n'
                                             'import sqlite3\n'
                                             "conn = sqlite3.connect(':memory:')\n"
                                             'cur = conn.cursor()\n'
                                             '\n'
                                             '# Step 1: Execute CREATE TABLE users:\n'
                                             '\n'
                                             '# Step 2: Verify in sqlite_master and print confirmation:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, "
                                              "username TEXT, score INTEGER)')\n"
                                              'found = connection.execute("SELECT name FROM sqlite_master WHERE '
                                              'type=\'table\' AND name=?", (\'users\',)).fetchone()\n'
                                              "print('Table created:', found[0])\n"
                                              'connection.close()',
                             'test_cases': [{'expected_output': 'Table created: users',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Create and Verify a SQLite Table',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read a table name and its column names.\n2. Create the table with an id column, ask PRAGMA table_info for its columns, and print the names without id.\n\nInput for this example: The Input box shows 4 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import sqlite3\n'
                                       'table = input().strip()\n'
                                       'column_count = int(input())\n'
                                       "columns = [input().strip().split()[0] + ' TEXT' for _ in range(column_count)]\n"
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE ' + table + ' (id INTEGER PRIMARY KEY, ' + ', "
                                       "'.join(columns) + ')')\n"
                                       "info = connection.execute('PRAGMA table_info(' + table + ')').fetchall()\n"
                                       'print([row[1] for row in info][1:])\n'
                                       'connection.close()'],
                             'initial_code': '# ⚔️ Boss Challenge: Dynamic Table Schema Generator\n'
                                             'import sqlite3\n'
                                             'table_name = input().strip()\n'
                                             'col_count = int(input())\n'
                                             'cols = [input().strip() for _ in range(col_count)]\n'
                                             '\n'
                                             '# Step 1: Create table and inspect PRAGMA table_info below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              'table = input().strip()\n'
                                              'column_count = int(input())\n'
                                              "columns = [input().strip().split()[0] + ' TEXT' for _ in "
                                              'range(column_count)]\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE ' + table + ' (id INTEGER PRIMARY KEY, "
                                              "' + ', '.join(columns) + ')')\n"
                                              "info = connection.execute('PRAGMA table_info(' + table + "
                                              "')').fetchall()\n"
                                              'print([row[1] for row in info][1:])\n'
                                              'connection.close()',
                             'test_cases': [{'expected_output': "['item_name', 'quantity']",
                                             'input_data': 'inventory\n2\nitem_name TEXT\nquantity INTEGER\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Build a Table from Column Names',
                             'xp_reward': 150}],
             'description': 'Connect to lightweight SQLite databases and execute CREATE TABLE schemas using the '
                            'built-in sqlite3 module.',
             'lesson': {'common_mistakes': [{'fix': 'Always call conn.commit() after executing data-modifying queries.',
                                             'mistake': 'Executing DDL or INSERT without calling conn.commit()',
                                             'why': 'Uncommitted transactions are rolled back when the connection '
                                                    'closes; changes will vanish!'}],
                        'detailed_explanation': "sqlite3 is Python's built-in tool for SQLite databases. Import it, "
                                                "then call sqlite3.connect(':memory:') to open a temporary database in "
                                                'memory.\n'
                                                '\n'
                                                'The connection is the open link to the database. A cursor sends SQL '
                                                'commands and reads their answers. You can also call '
                                                'connection.execute() for a short command. CREATE TABLE makes a table '
                                                'and lists its column names and types.\n'
                                                '\n'
                                                'SQLite keeps a catalog named sqlite_master that describes tables. A '
                                                'SELECT query can ask that catalog whether your table exists. When '
                                                'finished, close the connection. For a database saved to disk, save '
                                                'changes with commit() before closing.',
                        'expected_output': "Tables found in database: [('test',)]",
                        'introduction': 'Now we will use a real database. We keep it in memory so it disappears when '
                                        'the program ends and leaves no practice files behind.',
                        'learning_objectives': ["Import Python's built-in sqlite3 library.",
                                                "Open a temporary database with sqlite3.connect(':memory:').",
                                                'Create a table and inspect its name.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'import sqlite3',
                                          'explanation': 'Import the library so the program can use SQLite.'},
                                         {'line': '2',
                                          'code': "conn = sqlite3.connect(':memory:')",
                                          'explanation': 'Open a temporary database that exists only while the program '
                                                         'runs.'},
                                         {'line': '3',
                                          'code': 'cur = conn.cursor()',
                                          'explanation': 'Make a cursor for sending SQL commands.'},
                                         {'line': '4',
                                          'code': "cur.execute('CREATE TABLE test (id INT, val TEXT)')",
                                          'explanation': 'Create a table named test with two columns.'},
                                         {'line': '5',
                                          'code': 'cur.execute("SELECT name FROM sqlite_master WHERE type=\'table\'")',
                                          'explanation': "Ask SQLite's catalog for the table names."},
                                         {'line': '6',
                                          'code': "print('Tables found in database:', cur.fetchall())",
                                          'explanation': 'Print the returned rows; the table name is inside a one-item '
                                                         'tuple.'},
                                         {'line': '7',
                                          'code': 'conn.close()',
                                          'explanation': 'Close the connection when the work is finished.'}],
                        'practical_examples': [{'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('CREATE TABLE test (id INT, val TEXT)')\n"
                                                        'cur.execute("SELECT name FROM sqlite_master WHERE '
                                                        'type=\'table\'")\n'
                                                        "print('Tables found in database:', cur.fetchall())\n"
                                                        'conn.close()',
                                                'explanation': 'Queries sqlite_master to verify that the table was '
                                                               'created.',
                                                'output': "Tables found in database: [('test',)]",
                                                'title': 'Example 1: Creating in-memory SQLite table and verifying '
                                                         'schema'},
                                               {'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('CREATE TABLE logs (msg TEXT)')\n"
                                                        'cur.execute(\'INSERT INTO logs VALUES ("System started")\')\n'
                                                        'conn.commit()\n'
                                                        "cur.execute('SELECT count(*) FROM logs')\n"
                                                        "print('Total log rows:', cur.fetchone()[0])\n"
                                                        'conn.close()',
                                                'explanation': 'Executes commit() to persist newly inserted rows.',
                                                'output': 'Total log rows: 1',
                                                'title': 'Example 2: Inserting records and committing transaction'},
                                               {'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'with conn:\n'
                                                        "    conn.execute('CREATE TABLE items (name TEXT)')\n"
                                                        '    conn.execute(\'INSERT INTO items VALUES ("Shield")\')\n'
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('SELECT * FROM items')\n"
                                                        "print('Item fetched:', cur.fetchone()[0])\n"
                                                        'conn.close()',
                                                'explanation': 'with conn automatically commits transactions upon '
                                                               'completion.',
                                                'output': 'Item fetched: Shield',
                                                'title': 'Example 3: Using context manager with sqlite3 connection'}],
                        'practice_questions': [{'question': 'What does :memory: mean?',
                                                'answer': 'Make a temporary database in memory.'},
                                               {'question': 'What does CREATE TABLE do?',
                                                'answer': 'Makes a table and its columns.'},
                                               {'question': 'What does a cursor help you do?',
                                                'answer': 'Send SQL commands and read their results.'}],
                        'prerequisites': 'Level 118: Relational Databases and SQL Fundamentals',
                        'real_world_apps': 'Tests often use in-memory databases so they can practice table code '
                                           'without changing real files.',
                        'summary': 'Import sqlite3, open a connection, create a table, inspect results, and close the '
                                   'connection.',
                        'syntax_breakdown': 'import sqlite3\n'
                                            "connection = sqlite3.connect(':memory:')\n"
                                            "connection.execute('CREATE TABLE users (id INTEGER, name TEXT)')\n"
                                            'rows = connection.execute("SELECT name FROM sqlite_master WHERE '
                                            'type=\'table\'").fetchall()\n'
                                            'connection.close()',
                        'terminology': [{'term': 'sqlite3',
                                         'definition': "Python's built-in library for working with SQLite."},
                                        {'term': 'Connection',
                                         'definition': 'The open link between Python and the database.'},
                                        {'term': 'Cursor',
                                         'definition': 'A helper for sending SQL and reading results.'},
                                        {'term': 'Schema',
                                         'definition': 'The plan for a table: its column names and types.'}]},
             'number': 119,
             'quizzes': [{'explanation': 'fetchone() returns the tuple (42,). Index 0 is the integer 42.',
                          'options': [{'explanation': 'Correct! fetchone()[0] extracts 42.',
                                       'is_correct': True,
                                       'text': '42'},
                                      {'explanation': 'Incorrect. Index [0] was accessed.',
                                       'is_correct': False,
                                       'text': '(42,)'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '[42]'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'}],
                          'question': 'What is the output of the in-memory SQLite execution?\n'
                                      '\n'
                                      'import sqlite3\n'
                                      "conn = sqlite3.connect(':memory:')\n"
                                      'cur = conn.cursor()\n'
                                      "cur.execute('CREATE TABLE t (val INT)')\n"
                                      "cur.execute('INSERT INTO t VALUES (42)')\n"
                                      'conn.commit()\n'
                                      "cur.execute('SELECT val FROM t')\n"
                                      'print(cur.fetchone()[0])'},
                         {'explanation': 'sqlite3 starts transactions automatically. Without conn.commit(), changes '
                                         'are not permanently saved to disk.',
                          'options': [{'explanation': 'Correct! Changes remain in transaction buffer until commit().',
                                       'is_correct': True,
                                       'text': 'To commit the current transaction and persist changes permanently to '
                                               'the database'},
                                      {'explanation': 'Incorrect. That is conn.close().',
                                       'is_correct': False,
                                       'text': 'To close the database connection'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To verify table column types'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To create a backup file'}],
                          'question': 'Why is `conn.commit()` required after executing INSERT or UPDATE queries in '
                                      'Python sqlite3?'}],
             'title': 'SQLite in Python: Connecting and Creating Tables'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create a temporary scores table, add Alex and Sam, then read scores from highest to lowest.\n2. Print each name and score on its own line.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['import sqlite3\n'
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE scores (player TEXT, points INTEGER)')\n"
                                       "connection.execute('INSERT INTO scores VALUES (?, ?)', ('Hero', 150))\n"
                                       'connection.commit()\n'
                                       "player, points = connection.execute('SELECT player, points FROM "
                                       "scores').fetchone()\n"
                                       "print(f'{player}: {points} pts')\n"
                                       'connection.close()'],
                             'initial_code': '# SQLite CRUD: Insert and Select\n'
                                             'import sqlite3\n'
                                             "conn = sqlite3.connect(':memory:')\n"
                                             'cur = conn.cursor()\n'
                                             '\n'
                                             '# Step 1: CREATE TABLE, INSERT, and SELECT:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE scores (player TEXT, points "
                                              "INTEGER)')\n"
                                              "connection.execute('INSERT INTO scores VALUES (?, ?)', ('Hero', 150))\n"
                                              'connection.commit()\n'
                                              "player, points = connection.execute('SELECT player, points FROM "
                                              "scores').fetchone()\n"
                                              "print(f'{player}: {points} pts')\n"
                                              'connection.close()',
                             'test_cases': [{'expected_output': 'Hero: 150 pts', 'input_data': '', 'is_hidden': False}],
                             'title': 'Create and Read a Score with SQLite',
                             'xp_reward': 35},
                            {'description': "Your task, step by step:\n1. Create an inventory table.\n2. Add Shield and Potion, change Potion's count to 15, remove Shield, then print the remaining item and the completion message.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.",
                             'difficulty': 'boss',
                             'hints': ['import sqlite3\n'
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE inventory (id INTEGER PRIMARY KEY, item TEXT, "
                                       "count INTEGER)')\n"
                                       "connection.executemany('INSERT INTO inventory VALUES (?, ?, ?)', [(1, "
                                       "'Shield', 5), (2, 'Potion', 10)])\n"
                                       "connection.execute('UPDATE inventory SET count = ? WHERE item = ?', (15, "
                                       "'Potion'))\n"
                                       "connection.execute('DELETE FROM inventory WHERE item = ?', ('Shield',))\n"
                                       'connection.commit()\n'
                                       "item, count = connection.execute('SELECT item, count FROM "
                                       "inventory').fetchone()\n"
                                       "print(f'Inventory: {item} (Count: {count})')\n"
                                       "print('CRUD Engine Cycle Complete!')\n"
                                       'connection.close()'],
                             'initial_code': '# ⚔️ Boss Challenge: Full SQLite CRUD Engine\n'
                                             'import sqlite3\n'
                                             '\n'
                                             '# Step 1: Connect to in-memory database:\n'
                                             "conn = sqlite3.connect(':memory:')\n"
                                             'cur = conn.cursor()\n'
                                             '\n'
                                             '# Step 2: Create inventory table (id INTEGER PRIMARY KEY, item TEXT, '
                                             'count INTEGER):\n'
                                             '\n'
                                             '\n'
                                             "# Step 3: Insert 'Shield' (count 5) and 'Potion' (count 10):\n"
                                             '\n'
                                             '\n'
                                             "# Step 4: Update 'Potion' count to 15:\n"
                                             '\n'
                                             '\n'
                                             "# Step 5: Delete 'Shield':\n"
                                             '\n'
                                             '\n'
                                             '# Step 6: Commit changes:\n'
                                             '\n'
                                             '\n'
                                             "# Step 7: Select remaining items, print each as 'Inventory: <item> "
                                             "(Count: <count>)', then print 'CRUD Engine Cycle Complete!':\n"
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE inventory (id INTEGER PRIMARY KEY, "
                                              "item TEXT, count INTEGER)')\n"
                                              "connection.executemany('INSERT INTO inventory VALUES (?, ?, ?)', [(1, "
                                              "'Shield', 5), (2, 'Potion', 10)])\n"
                                              "connection.execute('UPDATE inventory SET count = ? WHERE item = ?', "
                                              "(15, 'Potion'))\n"
                                              "connection.execute('DELETE FROM inventory WHERE item = ?', "
                                              "('Shield',))\n"
                                              'connection.commit()\n'
                                              "item, count = connection.execute('SELECT item, count FROM "
                                              "inventory').fetchone()\n"
                                              "print(f'Inventory: {item} (Count: {count})')\n"
                                              "print('CRUD Engine Cycle Complete!')\n"
                                              'connection.close()',
                             'test_cases': [{'expected_output': 'Inventory: Potion (Count: 15)\n'
                                                                'CRUD Engine Cycle Complete!',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Complete the SQLite CRUD Cycle',
                             'xp_reward': 150}],
             'description': 'Execute Create, Read, Update, and Delete operations and fetch records with fetchone() and '
                            'fetchall().',
             'lesson': {'common_mistakes': [{'fix': 'Always execute a SELECT query before calling fetch methods.',
                                             'mistake': 'Calling fetchone() or fetchall() before executing a SELECT '
                                                        'query',
                                             'why': 'The cursor has no active result set; raises OperationalError.'}],
                        'detailed_explanation': 'CRUD means Create, Read, Update, and Delete. INSERT adds a row. '
                                                'SELECT reads rows. UPDATE changes existing rows. DELETE removes '
                                                'rows.\n'
                                                '\n'
                                                'A query can return one row or many rows. fetchone() gives one row as '
                                                'a tuple. fetchall() gives a list of all remaining rows. Use a loop to '
                                                'display each row in that list.\n'
                                                '\n'
                                                'Use WHERE to choose which row to change. If you leave WHERE off '
                                                'UPDATE or DELETE, SQLite may change or remove every row. Use '
                                                'question-mark placeholders for user values; the next lesson explains '
                                                'why they are safer.',
                        'expected_output': 'Sam: 150 pts\nAlex: 100 pts',
                        'introduction': 'A game inventory changes as you play: you add an item, look at your items, '
                                        'change a count, or remove something. Those four actions are called CRUD.',
                        'learning_objectives': ['Add rows with INSERT and read them with SELECT.',
                                                'Change or remove selected rows with UPDATE and DELETE.',
                                                'Use fetchone() for one row and fetchall() for a list of rows.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'import sqlite3',
                                          'explanation': "Load Python's SQLite library."},
                                         {'line': '2',
                                          'code': "conn = sqlite3.connect(':memory:')",
                                          'explanation': 'Open a temporary database.'},
                                         {'line': '3',
                                          'code': 'cur = conn.cursor()',
                                          'explanation': 'Create a cursor to send commands.'},
                                         {'line': '4',
                                          'code': "cur.execute('CREATE TABLE scores (player TEXT, score INT)')",
                                          'explanation': 'Create a table with player and score columns.'},
                                         {'line': '5',
                                          'code': "cur.executemany('INSERT INTO scores VALUES (?, ?)', [('Alex', 100), "
                                                  "('Sam', 150)])",
                                          'explanation': 'Add two rows. executemany repeats the command for each '
                                                         'tuple.'},
                                         {'line': '6',
                                          'code': "cur.execute('SELECT player, score FROM scores ORDER BY score DESC')",
                                          'explanation': 'Read both columns and sort from highest score to lowest.'},
                                         {'line': '7',
                                          'code': 'for row in cur.fetchall():',
                                          'explanation': 'Get all returned rows and handle one at a time.'},
                                         {'line': '8',
                                          'code': "    print(f'{row[0]}: {row[1]} pts')",
                                          'explanation': 'Display the player and score from this row.'},
                                         {'line': '9',
                                          'code': 'conn.close()',
                                          'explanation': 'Close the database connection.'}],
                        'practical_examples': [{'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('CREATE TABLE scores (player TEXT, score INT)')\n"
                                                        "cur.executemany('INSERT INTO scores VALUES (?, ?)', [('Alex', "
                                                        "100), ('Sam', 150)])\n"
                                                        "cur.execute('SELECT player, score FROM scores ORDER BY score "
                                                        "DESC')\n"
                                                        'for row in cur.fetchall():\n'
                                                        "    print(f'{row[0]}: {row[1]} pts')\n"
                                                        'conn.close()',
                                                'explanation': 'executemany inserts a batch of tuples; fetchall '
                                                               'retrieves all results.',
                                                'output': 'Sam: 150 pts\nAlex: 100 pts',
                                                'title': 'Example 1: Fetching multiple rows with fetchall()'},
                                               {'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('CREATE TABLE status (active INT)')\n"
                                                        "cur.execute('INSERT INTO status VALUES (0)')\n"
                                                        "cur.execute('UPDATE status SET active = 1 WHERE active = 0')\n"
                                                        "cur.execute('SELECT active FROM status')\n"
                                                        "print('Updated status value:', cur.fetchone()[0])\n"
                                                        'conn.close()',
                                                'explanation': 'Modifies table values in place using SQL UPDATE.',
                                                'output': 'Updated status value: 1',
                                                'title': 'Example 2: Updating existing records conditionally'},
                                               {'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('CREATE TABLE users (id INT)')\n"
                                                        "cur.execute('INSERT INTO users VALUES (99)')\n"
                                                        "cur.execute('DELETE FROM users WHERE id = 99')\n"
                                                        "cur.execute('SELECT count(*) FROM users')\n"
                                                        "print('Remaining users count:', cur.fetchone()[0])\n"
                                                        'conn.close()',
                                                'explanation': 'Deletes target record and verifies table is empty.',
                                                'output': 'Remaining users count: 0',
                                                'title': 'Example 3: Deleting records with WHERE constraint'}],
                        'practice_questions': [{'question': 'Which command adds a row?', 'answer': 'INSERT.'},
                                               {'question': 'What does fetchall() return?',
                                                'answer': 'A list of rows.'},
                                               {'question': 'Why add WHERE to DELETE?',
                                                'answer': 'So only the chosen row is removed.'}],
                        'prerequisites': 'Level 119: SQLite in Python: Connecting and Creating Tables',
                        'real_world_apps': 'Shopping carts, game inventories, scoreboards, and contact lists all use '
                                           'CRUD actions.',
                        'summary': 'CRUD adds, reads, changes, and removes records. Use fetchone() or fetchall() to '
                                   'read results and WHERE to target rows.',
                        'syntax_breakdown': 'INSERT INTO scores VALUES (?, ?);\n'
                                            'SELECT player, score FROM scores;\n'
                                            'UPDATE scores SET score = ? WHERE player = ?;\n'
                                            'DELETE FROM scores WHERE player = ?;\n'
                                            'row = cursor.fetchone()\n'
                                            'rows = cursor.fetchall()',
                        'terminology': [{'term': 'CRUD', 'definition': 'Create, Read, Update, and Delete.'},
                                        {'term': 'INSERT', 'definition': 'Add a new row.'},
                                        {'term': 'UPDATE', 'definition': 'Change values in matching rows.'},
                                        {'term': 'DELETE', 'definition': 'Remove matching rows.'},
                                        {'term': 'fetchone() / fetchall()',
                                         'definition': 'Get one result row / get all remaining result rows.'}]},
             'number': 120,
             'quizzes': [{'explanation': 'cur.fetchall() returns a list of row tuples.',
                          'options': [{'explanation': 'Correct! Each row is represented as a tuple inside a list.',
                                       'is_correct': True,
                                       'text': 'A list of tuples'},
                                      {'explanation': 'Incorrect. Standard cursor returns tuples.',
                                       'is_correct': False,
                                       'text': 'A dictionary mapping columns'},
                                      {'explanation': 'Incorrect. That is fetchone().',
                                       'is_correct': False,
                                       'text': 'A single tuple'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'A string'}],
                          'question': 'What is the return type of `cur.fetchall()` after executing a SELECT query in '
                                      'sqlite3?'},
                         {'explanation': 'cur.rowcount reports the number of database rows affected by the query.',
                          'options': [{'explanation': 'Correct! rowcount gives the count of modified rows.',
                                       'is_correct': True,
                                       'text': 'The number of rows matched and modified by the query'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'The total number of rows in the entire table'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'The execution time in milliseconds'},
                                      {'explanation': 'Incorrect. That is lastrowid.',
                                       'is_correct': False,
                                       'text': 'The primary key of the last inserted row'}],
                          'question': 'What does `cur.rowcount` indicate following an UPDATE or DELETE statement in '
                                      'sqlite3?'}],
             'title': 'SQLite in Python: CRUD Operations'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create a users table with Mia and Bo.\n2. Read a username and look up its role with a ? placeholder.\n3. Print the role, or USER NOT FOUND if there is no match.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['import sqlite3\n'
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE users (username TEXT, role TEXT)')\n"
                                       "connection.executemany('INSERT INTO users VALUES (?, ?)', [('Mia', 'admin'), "
                                       "('Bo', 'player')])\n"
                                       'username = input().strip()\n'
                                       "row = connection.execute('SELECT role FROM users WHERE username = ?', "
                                       '(username,)).fetchone()\n'
                                       "print(row[0] if row else 'USER NOT FOUND')\n"
                                       'connection.close()'],
                             'initial_code': '# Secure Database Queries: Preventing SQL Injection\n'
                                             'import sqlite3\n'
                                             "conn = sqlite3.connect(':memory:')\n"
                                             'cur = conn.cursor()\n'
                                             "cur.execute('CREATE TABLE users (username TEXT, role TEXT)')\n"
                                             'cur.execute("INSERT INTO users VALUES (\'admin\', \'superuser\'), '
                                             '(\'alice\', \'guest\')")\n'
                                             'conn.commit()\n'
                                             'u = input().strip()\n'
                                             '\n'
                                             '# Step 1: Query role securely with ? parameter:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE users (username TEXT, role TEXT)')\n"
                                              "connection.executemany('INSERT INTO users VALUES (?, ?)', [('Mia', "
                                              "'admin'), ('Bo', 'player')])\n"
                                              'username = input().strip()\n'
                                              "row = connection.execute('SELECT role FROM users WHERE username = ?', "
                                              '(username,)).fetchone()\n'
                                              "print(row[0] if row else 'USER NOT FOUND')\n"
                                              'connection.close()',
                             'test_cases': [{'expected_output': 'admin', 'input_data': 'Mia\n', 'is_hidden': False},
                                            {'expected_output': 'USER NOT FOUND',
                                             'input_data': 'Eve\n',
                                             'is_hidden': False}],
                             'title': 'Look Up a Role with a Parameterized Query',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read a username that may contain SQL-looking punctuation.\n2. Search with a parameterized query and print the number of exact matches.\n3. Treat the input as text, not as SQL instructions.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import sqlite3\n'
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE users (username TEXT)')\n"
                                       "connection.execute('INSERT INTO users VALUES (?)', ('admin',))\n"
                                       'payload = input().strip()\n'
                                       "count = connection.execute('SELECT username FROM users WHERE username = ?', "
                                       '(payload,)).fetchall()\n'
                                       "print(f'Matches with param query: {len(count)}')\n"
                                       'connection.close()'],
                             'initial_code': '# ⚔️ Boss Challenge: Injection Attack Neutralizer\n'
                                             'import sqlite3\n'
                                             "conn = sqlite3.connect(':memory:')\n"
                                             'cur = conn.cursor()\n'
                                             "cur.execute('CREATE TABLE secrets (id INTEGER, val TEXT)')\n"
                                             'cur.execute("INSERT INTO secrets VALUES (1, \'flag{safe_sql}\'), (2, '
                                             '\'hidden\')")\n'
                                             'conn.commit()\n'
                                             'injection = "\' OR \'1\'=\'1"\n'
                                             '\n'
                                             '# Step 1: Execute parameterized query with injection:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE users (username TEXT)')\n"
                                              "connection.execute('INSERT INTO users VALUES (?)', ('admin',))\n"
                                              'payload = input().strip()\n'
                                              "count = connection.execute('SELECT username FROM users WHERE username = "
                                              "?', (payload,)).fetchall()\n"
                                              "print(f'Matches with param query: {len(count)}')\n"
                                              'connection.close()',
                             'test_cases': [{'expected_output': 'Matches with param query: 0',
                                             'input_data': "' OR '1'='1\n",
                                             'is_hidden': False},
                                            {'expected_output': 'Matches with param query: 1',
                                             'input_data': 'admin\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Block a SQL Injection Attempt',
                             'xp_reward': 150}],
             'description': 'Defend databases against catastrophic SQL injection vulnerabilities using parameterized '
                            'query placeholders.',
             'lesson': {'common_mistakes': [{'fix': "Always use 'SELECT * FROM tbl WHERE id = ?', (user_input,)",
                                             'mistake': 'f"SELECT * FROM tbl WHERE id = {user_input}"',
                                             'why': 'This is a severe security vulnerability that exposes your '
                                                    'database to injection attacks.'}],
                        'detailed_explanation': 'A parameterized query has a question mark where a value should go. '
                                                "Python sends the SQL text and values separately: execute('SELECT role "
                                                "FROM users WHERE username = ?', (username,)).\n"
                                                '\n'
                                                'The comma in (username,) makes a one-item tuple. If there are two '
                                                'question marks, provide two values in order. SQLite puts each value '
                                                'into its matching place safely.\n'
                                                '\n'
                                                'Do not join user input into SQL text. A person could type punctuation '
                                                'that changes the query. With placeholders, that text stays a value to '
                                                'search for. Table and column names usually cannot use value '
                                                'placeholders, so choose those from trusted options.',
                        'expected_output': "Safe Profile Fetch: ('Elena', 28)",
                        'introduction': 'A search box may contain ordinary words or unexpected punctuation. A '
                                        'placeholder tells SQLite to treat what the person typed as data, not as '
                                        'another SQL instruction.',
                        'learning_objectives': ['Put ? placeholders where SQL values belong.',
                                                'Send values separately from the SQL text.',
                                                'Explain how placeholders protect user input from SQL injection.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'import sqlite3',
                                          'explanation': "Import Python's SQLite tool."},
                                         {'line': '2',
                                          'code': "conn = sqlite3.connect(':memory:')",
                                          'explanation': 'Open a temporary database.'},
                                         {'line': '3',
                                          'code': 'cur = conn.cursor()',
                                          'explanation': 'Make a cursor for SQL commands.'},
                                         {'line': '4',
                                          'code': "cur.execute('CREATE TABLE profiles (name TEXT, age INT)')",
                                          'explanation': 'Create a table with name and age columns.'},
                                         {'line': '5',
                                          'code': "cur.execute('INSERT INTO profiles VALUES (?, ?)', ('Elena', 28))",
                                          'explanation': "Add Elena's details; each ? receives one tuple value."},
                                         {'line': '6',
                                          'code': "cur.execute('SELECT name, age FROM profiles WHERE name = ?', "
                                                  "('Elena',))",
                                          'explanation': 'Search with a placeholder instead of joining text into SQL.'},
                                         {'line': '7',
                                          'code': "print('Safe Profile Fetch:', cur.fetchone())",
                                          'explanation': 'Print the one matching row.'},
                                         {'line': '8', 'code': 'conn.close()', 'explanation': 'Close the database.'}],
                        'practical_examples': [{'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('CREATE TABLE profiles (name TEXT, age INT)')\n"
                                                        "cur.execute('INSERT INTO profiles VALUES (?, ?)', ('Elena', "
                                                        '28))\n'
                                                        "cur.execute('SELECT name, age FROM profiles WHERE name = ?', "
                                                        "('Elena',))\n"
                                                        "print('Safe Profile Fetch:', cur.fetchone())\n"
                                                        'conn.close()',
                                                'explanation': 'Supplies parameters as a separate tuple (param,) to '
                                                               'neutralize SQL injection.',
                                                'output': "Safe Profile Fetch: ('Elena', 28)",
                                                'title': 'Example 1: Safe parameterized INSERT with tuple values'},
                                               {'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('CREATE TABLE accounts (id INT, balance REAL)')\n"
                                                        "cur.execute('INSERT INTO accounts VALUES (:id, :bal)', {'id': "
                                                        "101, 'bal': 450.50})\n"
                                                        "cur.execute('SELECT balance FROM accounts WHERE id = :id', "
                                                        "{'id': 101})\n"
                                                        "print('Balance from named query: $', cur.fetchone()[0])\n"
                                                        'conn.close()',
                                                'explanation': 'Named placeholders match dictionary keys for high '
                                                               'query clarity.',
                                                'output': 'Balance from named query: $ 450.5',
                                                'title': 'Example 2: Named parameter placeholders (:key)'},
                                               {'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('CREATE TABLE ranks (title TEXT)')\n"
                                                        "ranks = [('Novice',), ('Journeyman',), ('Master',)]\n"
                                                        "cur.executemany('INSERT INTO ranks VALUES (?)', ranks)\n"
                                                        "cur.execute('SELECT count(*) FROM ranks')\n"
                                                        "print('Total ranks inserted safely:', cur.fetchone()[0])\n"
                                                        'conn.close()',
                                                'explanation': 'Safely parameterizes bulk batches of database records.',
                                                'output': 'Total ranks inserted safely: 3',
                                                'title': 'Example 3: Batch parameterized insertion with executemany'}],
                        'practice_questions': [{'question': 'What does ? mean in a query?',
                                                'answer': 'A place where SQLite safely puts one value.'},
                                               {'question': 'Why is (name,) written with a comma?',
                                                'answer': 'The comma makes a one-item tuple.'},
                                               {'question': 'Can input become SQL code when passed as a parameter?',
                                                'answer': 'No, SQLite treats it as data.'}],
                        'prerequisites': 'Level 120: SQLite in Python: CRUD Operations',
                        'real_world_apps': 'Login forms, search boxes, and payment records should use parameters '
                                           'whenever a query contains user input.',
                        'summary': 'Keep SQL and user values separate. Put ? where each value belongs and pass the '
                                   'values in a tuple.',
                        'syntax_breakdown': "sql = 'SELECT role FROM users WHERE username = ?'\n"
                                            'row = connection.execute(sql, (username,)).fetchone()',
                        'terminology': [{'term': 'Placeholder', 'definition': 'A ? mark that waits for a value.'},
                                        {'term': 'Parameter',
                                         'definition': 'A value sent separately to fill a placeholder.'},
                                        {'term': 'SQL injection',
                                         'definition': 'When input is mistakenly treated as part of a SQL '
                                                       'instruction.'},
                                        {'term': 'Tuple',
                                         'definition': 'An ordered group of values, written in parentheses.'}]},
             'number': 121,
             'quizzes': [{'explanation': "Parameterized queries use question mark placeholders '?' with parameter "
                                         'tuples.',
                          'options': [{'explanation': "Correct! The '?' placeholder prevents SQL injection.",
                                       'is_correct': True,
                                       'text': "cur.execute('SELECT * FROM users WHERE name = ?', (username,))"},
                                      {'explanation': 'Incorrect! F-string formatting creates a severe SQL injection '
                                                      'vulnerability.',
                                       'is_correct': False,
                                       'text': 'cur.execute(f\'SELECT * FROM users WHERE name = "{username}"\')'},
                                      {'explanation': 'Incorrect! String concatenation is vulnerable to SQL injection.',
                                       'is_correct': False,
                                       'text': "cur.execute('SELECT * FROM users WHERE name = ' + username)"},
                                      {'explanation': 'Incorrect. String interpolation is vulnerable.',
                                       'is_correct': False,
                                       'text': "cur.execute('SELECT * FROM users WHERE name = %s' % username)"}],
                          'question': 'Which parameterized query correctly prevents SQL injection in Python sqlite3?'},
                         {'explanation': "Malicious user input containing quotes (e.g. ' OR 1=1 --) can alter query "
                                         'structure and hijack database operations.',
                          'options': [{'explanation': 'Correct! String interpolation enables SQL injection attacks.',
                                       'is_correct': True,
                                       'text': 'User input can break out of string literals and execute arbitrary SQL '
                                               'commands (SQL Injection)'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'F-strings run 100x slower in database drivers'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'SQLite rejects strings with curly braces'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It triggers a Python MemoryError'}],
                          'question': 'Why is writing `f"SELECT * FROM users WHERE name = \'{name}\'"` considered a '
                                      'critical security vulnerability?'}],
             'title': 'Parameterized Queries and Preventing SQL Injection'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a number of commit records.\n2. Each line has a hash and message.\n3. Print the first seven hash characters in brackets, followed by the message.\n\nInput for this example: The Input box shows 3 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['count = int(input())\n'
                                       'for _ in range(count):\n'
                                       '    parts = input().split(maxsplit=1)\n'
                                       '    short_hash = parts[0][:7]\n'
                                       "    message = parts[1] if len(parts) > 1 else ''\n"
                                       "    print(f'[{short_hash}] {message}')"],
                             'initial_code': '# Git Commit Log Formatting\n'
                                             'n = int(input())\n'
                                             '\n'
                                             '# Step 1: For each line, format short hash and message:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'count = int(input())\n'
                                              'for _ in range(count):\n'
                                              '    parts = input().split(maxsplit=1)\n'
                                              '    short_hash = parts[0][:7]\n'
                                              "    message = parts[1] if len(parts) > 1 else ''\n"
                                              "    print(f'[{short_hash}] {message}')",
                             'test_cases': [{'expected_output': '[a1b2c3d] feat: add schema\n[e4f5g6h] fix: login',
                                             'input_data': '2\na1b2c3d99 feat: add schema\ne4f5g6h00 fix: login\n',
                                             'is_hidden': False}],
                             'title': 'Shorten a Git Commit Hash',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Format the supplied branch, commit number, and message records as shown, then print Git Log Formatted Successfully!\n2. This exercise formats sample data it does not run Git.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 4 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["commits = [(1, 'main', 'Initial commit'), (2, 'main', 'Add user login'), (3, "
                                       "'feature', 'Build UI dashboard')]\n"
                                       'for number, branch, message in commits:\n'
                                       "    print(f'[Branch: {branch}] #{number}: {message}')\n"
                                       "print('Git Log Formatted Successfully!')"],
                             'initial_code': '# ⚔️ Boss Challenge: Git Log Formatter\n'
                                             '\n'
                                             'commits = [\n'
                                             "    (1, 'main', 'Initial commit'),\n"
                                             "    (2, 'main', 'Add user login'),\n"
                                             "    (3, 'feature', 'Build UI dashboard')\n"
                                             ']\n'
                                             '\n'
                                             '# Step 1: Iterate over commits and print in required format:\n'
                                             '\n'
                                             '\n'
                                             '# Step 2: Print completion message:\n'
                                             "print('Git Log Formatted Successfully!')\n",
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "commits = [(1, 'main', 'Initial commit'), (2, 'main', 'Add user "
                                              "login'), (3, 'feature', 'Build UI dashboard')]\n"
                                              'for number, branch, message in commits:\n'
                                              "    print(f'[Branch: {branch}] #{number}: {message}')\n"
                                              "print('Git Log Formatted Successfully!')",
                             'test_cases': [{'expected_output': '[Branch: main] #1: Initial commit\n'
                                                                '[Branch: main] #2: Add user login\n'
                                                                '[Branch: feature] #3: Build UI dashboard\n'
                                                                'Git Log Formatted Successfully!',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Format a Branch Commit Log',
                             'xp_reward': 150}],
             'description': 'Track history, branch workflows, collaborate, and commit code using Git and GitHub.',
             'lesson': {'common_mistakes': [{'fix': "Write clear, imperative commit messages (e.g. 'feat: add user "
                                                    "login endpoint').",
                                             'mistake': "Writing generic commit messages like 'fixed stuff' or "
                                                        "'update'",
                                             'why': 'Makes inspecting project history useless when debugging '
                                                    'regressions.'}],
                        'detailed_explanation': 'Git is a tool that records selected changes to project files. Each '
                                                'saved checkpoint is a commit with a message and a long unique-looking '
                                                'ID called a hash. A short piece of the hash is often enough to '
                                                'recognize a commit in a list.\n'
                                                '\n'
                                                'A branch is a named path of work. A team can keep stable work on main '
                                                'and try a new feature on another branch. When the feature is ready, '
                                                'people can review and combine it.\n'
                                                '\n'
                                                'Git runs as a separate command-line tool. The Python examples here '
                                                'store and print sample Git information; they do not run Git commands '
                                                'or change your repository.',
                        'expected_output': "Ready to commit: ['main.py', 'models.py']\nNeed staging: ['README.md']",
                        'introduction': 'Imagine saving a checkpoint in a game. If a new change causes trouble, the '
                                        'checkpoint helps you see what changed or return to an earlier version. Git '
                                        'does this for project files.',
                        'learning_objectives': ['Describe what Git saves in a commit.',
                                                'Recognize a commit hash as an ID for a saved change.',
                                                'Explain what a branch is used for.'],
                        'line_by_line': [{'line': '1',
                                          'code': "git_status = {'staged': ['main.py', 'models.py'], 'modified': "
                                                  "['README.md']}",
                                          'explanation': 'Store two groups of filenames in a dictionary.'},
                                         {'line': '2',
                                          'code': "print('Ready to commit:', git_status['staged'])",
                                          'explanation': 'Show files already staged for the next commit.'},
                                         {'line': '3',
                                          'code': "print('Need staging:', git_status['modified'])",
                                          'explanation': 'Show changed files that still need staging.'}],
                        'practical_examples': [{'code': "git_status = {'staged': ['main.py', 'models.py'], 'modified': "
                                                        "['README.md']}\n"
                                                        "print('Ready to commit:', git_status['staged'])\n"
                                                        "print('Need staging:', git_status['modified'])",
                                                'explanation': "Demonstrates Git's two-stage commit preparation model.",
                                                'output': "Ready to commit: ['main.py', 'models.py']\n"
                                                          "Need staging: ['README.md']",
                                                'title': 'Example 1: Modeling git status staged/unstaged tracking'},
                                               {'code': "ignore_rules = ['__pycache__/', '*.pyc', '.venv/', "
                                                        "'*.sqlite3']\n"
                                                        "print('.gitignore entries prevent committing junk and "
                                                        "secrets:')\n"
                                                        'for rule in ignore_rules:\n'
                                                        "    print(' -', rule)",
                                                'explanation': '.gitignore excludes temporary files and local secrets '
                                                               'from version control.',
                                                'output': '.gitignore entries prevent committing junk and secrets:\n'
                                                          ' - __pycache__/\n'
                                                          ' - *.pyc\n'
                                                          ' - .venv/\n'
                                                          ' - *.sqlite3',
                                                'title': 'Example 2: .gitignore file configuration'},
                                               {'code': "commit_msg = 'feat(auth): implement secure password hashing "
                                                        "with bcrypt'\n"
                                                        "print('Standard conventional commit message:', commit_msg)",
                                                'explanation': 'Uses standard semantic prefixes (feat, fix, docs, '
                                                               'refactor) to document commits.',
                                                'output': 'Standard conventional commit message: feat(auth): implement '
                                                          'secure password hashing with bcrypt',
                                                'title': 'Example 3: Semantic commit message format'}],
                        'practice_questions': [{'question': 'What is a commit?',
                                                'answer': 'A saved set of project changes with a message.'},
                                               {'question': 'What is a branch?', 'answer': 'A named line of work.'},
                                               {'question': 'Do the Python examples run Git?',
                                                'answer': 'No, they only model or format Git information.'}],
                        'prerequisites': 'Level 121: Parameterized SQL Queries & Security',
                        'real_world_apps': 'Teams use Git to review code, compare changes, try features safely, and '
                                           'work together without losing earlier versions.',
                        'summary': 'Git records changes as commits and groups work into branches. The examples model '
                                   'Git information; Git commands run separately in a terminal.',
                        'syntax_breakdown': "commit = {'hash': 'a1b2c3d99', 'message': 'add schema'}\n"
                                            "short_hash = commit['hash'][:7]\n"
                                            "print(short_hash, commit['message'])",
                        'terminology': [{'term': 'Version control',
                                         'definition': 'A way to record and review changes to files.'},
                                        {'term': 'Commit',
                                         'definition': 'A saved group of project changes with a message.'},
                                        {'term': 'Hash', 'definition': 'An ID for a commit.'},
                                        {'term': 'Branch', 'definition': 'A named path for separate work.'}]},
             'number': 122,
             'quizzes': [{'explanation': 'The staging area allows developers to craft precise commits by selecting '
                                         'which file changes to include before committing.',
                          'options': [{'explanation': 'Correct! git add places changes in staging for commit.',
                                       'is_correct': True,
                                       'text': 'An intermediate space to review and select specific changes before '
                                               'committing them to history'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'A remote server backup on GitHub'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'A temporary cache deleted upon restarting the computer'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'A compiler for Git repositories'}],
                          'question': 'What is the purpose of the Git Staging Area (Index) accessed via `git add`?'},
                         {'explanation': '`git checkout -b feature/auth` (or `git switch -c feature/auth`) creates and '
                                         'switches branches.',
                          'options': [{'explanation': 'Correct! -b creates and checks out the branch.',
                                       'is_correct': True,
                                       'text': 'git checkout -b feature/auth'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'git branch --make feature/auth'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'git create feature/auth'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'git add -b feature/auth'}],
                          'question': 'What Git command creates and switches to a new branch named `feature/auth` in '
                                      'one step?'}],
             'title': 'Version Control with Git and GitHub'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read variable=value lines.\n2. Sort by variable name and print each as DBG: name = value.\n\nInput for this example: The Input box shows 4 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['count = int(input())\n'
                                       'variables = {}\n'
                                       'for _ in range(count):\n'
                                       "    name, value = input().split('=', 1)\n"
                                       '    variables[name] = value\n'
                                       'for name in sorted(variables):\n'
                                       "    print(f'DBG: {name} = {variables[name]}')"],
                             'initial_code': '# Debugging: Inspecting Variable State\n'
                                             'n = int(input())\n'
                                             'vars_dict = {}\n'
                                             '\n'
                                             '# Step 1: Read n variables and store in vars_dict:\n'
                                             '\n'
                                             '# Step 2: Print sorted DBG lines:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'count = int(input())\n'
                                              'variables = {}\n'
                                              'for _ in range(count):\n'
                                              "    name, value = input().split('=', 1)\n"
                                              '    variables[name] = value\n'
                                              'for name in sorted(variables):\n'
                                              "    print(f'DBG: {name} = {variables[name]}')",
                             'test_cases': [{'expected_output': 'DBG: auth_token = xyz\n'
                                                                'DBG: retry_count = 2\n'
                                                                'DBG: user_id = 101',
                                             'input_data': '3\nuser_id=101\nauth_token=xyz\nretry_count=2\n',
                                             'is_hidden': False}],
                             'title': 'Display Debugger Variable Values',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Start at debugger line 5 and read the pdb-like commands. n moves one line, p shows a saved value, and c returns to line 5.\n2. Print each response and the final line.\n3. This exercise simulates commands in the editor.\n\nInput for this example: The Input box shows 5 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 5 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ["scope = {'x': 10, 'y': 20, 'total': 30}\n"
                                       'current_line = 5\n'
                                       'count = int(input())\n'
                                       'for _ in range(count):\n'
                                       '    parts = input().split()\n'
                                       "    if parts[0] == 'n':\n"
                                       '        current_line += 1\n'
                                       "        print(f'[PDB] Next -> Line {current_line}')\n"
                                       "    elif parts[0] == 'p':\n"
                                       '        name = parts[1]\n'
                                       "        value = scope.get(name, 'undefined')\n"
                                       "        print(f'[PDB] {name} = {value}')\n"
                                       "    elif parts[0] == 'c':\n"
                                       '        current_line = 5\n'
                                       "        print('[PDB] Continued -> Line 5')\n"
                                       "print(f'Final Debugger Line: {current_line}')"],
                             'initial_code': '# ⚔️ Boss Challenge: PDB Execution Step Simulator\n'
                                             "scope = {'x': 10, 'y': 20, 'total': 30}\n"
                                             'current_line = 5\n'
                                             'n = int(input())\n'
                                             '\n'
                                             '# Step 1: Process n commands below:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': "scope = {'x': 10, 'y': 20, 'total': 30}\n"
                                              'current_line = 5\n'
                                              'count = int(input())\n'
                                              'for _ in range(count):\n'
                                              '    parts = input().split()\n'
                                              "    if parts[0] == 'n':\n"
                                              '        current_line += 1\n'
                                              "        print(f'[PDB] Next -> Line {current_line}')\n"
                                              "    elif parts[0] == 'p':\n"
                                              '        name = parts[1]\n'
                                              "        value = scope.get(name, 'undefined')\n"
                                              "        print(f'[PDB] {name} = {value}')\n"
                                              "    elif parts[0] == 'c':\n"
                                              '        current_line = 5\n'
                                              "        print('[PDB] Continued -> Line 5')\n"
                                              "print(f'Final Debugger Line: {current_line}')",
                             'test_cases': [{'expected_output': '[PDB] Next -> Line 6\n'
                                                                '[PDB] x = 10\n'
                                                                '[PDB] Next -> Line 7\n'
                                                                '[PDB] Continued -> Line 5\n'
                                                                'Final Debugger Line: 5',
                                             'input_data': '4\nn\np x\nn\nc\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Simulate pdb Commands',
                             'xp_reward': 150}],
             'description': 'Diagnose runtime anomalies using breakpoints, the Python debugger (pdb), and stack '
                            'inspection.',
             'lesson': {'common_mistakes': [{'fix': 'Always remove breakpoints before committing or set '
                                                    'PYTHONBREAKPOINT=0 in production.',
                                             'mistake': 'Leaving breakpoint() statements in code committed to '
                                                        'production',
                                             'why': 'The production server will freeze waiting for terminal input that '
                                                    'will never arrive!'}],
                        'detailed_explanation': 'Python includes pdb, a debugger that can pause a running program. Put '
                                                'breakpoint() on a line to pause there. At the prompt, p name shows a '
                                                'value, n moves to the next line, s steps into a function, c '
                                                'continues, and q quits.\n'
                                                '\n'
                                                'A debugger is helpful when the final answer is wrong and you need to '
                                                'see where a value changed. You can inspect it at the exact line where '
                                                'the program is running.\n'
                                                '\n'
                                                'The boss challenge simulates a few pdb commands because this browser '
                                                'editor is not an interactive terminal. It lets you practice how '
                                                'commands change the current line and display a value without opening '
                                                'a separate prompt.',
                        'expected_output': '5.0',
                        'introduction': 'A debugger is like a pause button for a program. You can stop at a line, look '
                                        'at values, and move through the program one step at a time.',
                        'learning_objectives': ['Explain how a debugger helps find a mistake.',
                                                'Recognize the pdb commands n, s, c, p, and q.',
                                                'Use a breakpoint to pause a program while debugging.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'def divide_safely(a, b):',
                                          'explanation': 'Define a function that receives two values; this line does '
                                                         'not run the function yet.'},
                                         {'line': '2',
                                          'code': '    # Debug print statement:',
                                          'explanation': 'This comment names the debugging step. Python ignores '
                                                         'comments.'},
                                         {'line': '3',
                                          'code': "    # print(f'[DEBUG] a={a}, b={b}')",
                                          'explanation': 'This possible debug print is commented out, so it does not '
                                                         'run.'},
                                         {'line': '4',
                                          'code': '    if b == 0:',
                                          'explanation': 'Check whether the divisor is zero.'},
                                         {'line': '5',
                                          'code': "        return 'Error'",
                                          'explanation': 'If it is zero, return Error and end this function call.'},
                                         {'line': '6',
                                          'code': '    return a / b',
                                          'explanation': 'Otherwise divide a by b and return the answer.'},
                                         {'line': '7',
                                          'code': 'print(divide_safely(10, 2))',
                                          'explanation': 'Call the function with 10 and 2, then display its answer.'}],
                        'practical_examples': [{'code': 'def divide_safely(a, b):\n'
                                                        '    # Debug print statement:\n'
                                                        "    # print(f'[DEBUG] a={a}, b={b}')\n"
                                                        '    if b == 0:\n'
                                                        "        return 'Error'\n"
                                                        '    return a / b\n'
                                                        'print(divide_safely(10, 2))',
                                                'explanation': 'Temporary debug logs help trace parameter flow through '
                                                               'functions.',
                                                'output': '5.0',
                                                'title': 'Example 1: Strategic print debugging vs debugger'},
                                               {'code': 'def add_points(score, points):\n'
                                                        "    print('[DEBUG] score:', score)\n"
                                                        '    return score + points\n'
                                                        "print('Updated score:', add_points(10, 5))",
                                                'explanation': 'A temporary print shows the value entering the '
                                                               'function. A debugger can inspect the same value '
                                                               'without adding a print line.',
                                                'output': '[DEBUG] score: 10\nUpdated score: 15',
                                                'title': 'Print a value while debugging'},
                                               {'code': 'def process_age(age):\n'
                                                        "    assert age >= 0, 'Age cannot be negative!'\n"
                                                        '    return age\n'
                                                        "print('Processed age:', process_age(25))",
                                                'explanation': 'assert statements document and verify internal '
                                                               'invariant assumptions.',
                                                'output': 'Processed age: 25',
                                                'title': 'Example 3: Assert statement invariants'}],
                        'practice_questions': [{'question': 'What does p score do in pdb?',
                                                'answer': 'Displays the value of score.'},
                                               {'question': 'What does c do?',
                                                'answer': 'Continues until another breakpoint or the program ends.'},
                                               {'question': 'Why does the boss simulate commands?',
                                                'answer': 'An interactive debugger needs a terminal, so the editor '
                                                          'models the commands as input.'}],
                        'prerequisites': 'Level 122: Version Control with Git and GitHub',
                        'real_world_apps': 'Developers use debuggers to follow bugs in websites, games, automation '
                                           'scripts, and database programs.',
                        'summary': 'A debugger pauses a program so you can inspect values and follow its path. pdb '
                                   'commands help you move, inspect, continue, or quit.',
                        'syntax_breakdown': 'breakpoint()  # pause a real Python run here\n'
                                            '# In the debugger:\n'
                                            '# n     move to the next line\n'
                                            '# p x   show x\n'
                                            '# c     continue running',
                        'terminology': [{'term': 'Debugger',
                                         'definition': 'A tool that pauses code so you can inspect it.'},
                                        {'term': 'Breakpoint',
                                         'definition': 'A chosen place where the debugger pauses.'},
                                        {'term': 'pdb', 'definition': "Python's built-in interactive debugger."},
                                        {'term': 'Call stack',
                                         'definition': 'The functions that led to the current line.'}]},
             'number': 123,
             'quizzes': [{'explanation': '`n` executes the current line moving to the next line in the current '
                                         'function; `s` steps inside the function being called.',
                          'options': [{'explanation': 'Correct! Next steps over; Step steps into.',
                                       'is_correct': True,
                                       'text': '`n` executes the line without stepping into functions; `s` steps into '
                                               'called functions'},
                                      {'explanation': "Incorrect. 'q' exits.",
                                       'is_correct': False,
                                       'text': '`n` exits the debugger; `s` starts debugging'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': '`n` prints numbers; `s` prints strings'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'They perform the exact same action'}],
                          'question': 'What is the difference between `n` (next) and `s` (step) in the Python debugger '
                                      '(pdb)?'},
                         {'explanation': 'Leaving breakpoint() in production code will pause server worker threads '
                                         'waiting for terminal input.',
                          'options': [{'explanation': 'Correct! Unattended breakpoints freeze server processes.',
                                       'is_correct': True,
                                       'text': 'It pauses server processes waiting for interactive console input, '
                                               'causing requests to hang'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Python compiler refuses to build files with breakpoints'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It deletes database tables'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'It increases file size by 50%'}],
                          'question': 'Why should developers remove `breakpoint()` calls before deploying code to '
                                      'production?'}],
             'title': 'Debugging Python Code (pdb and Breakpoints)'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Read a, b, and the expected answer.\n2. Use assert to check whether a + b matches the expected answer, then print the success or failure message.\n\nInput for this example: The Input box shows 1 sample input line. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['parts = input().split()\n'
                                       'a, b, expected = map(int, parts)\n'
                                       'try:\n'
                                       '    assert a + b == expected\n'
                                       "    print('Assertion passed: Math verified')\n"
                                       'except AssertionError:\n'
                                       "    print('Assertion failed: Sum does not match')"],
                             'initial_code': '# Automated Testing: assert Statements\n'
                                             'parts = input().split()\n'
                                             'a, b = int(parts[0]), int(parts[1])\n'
                                             '\n'
                                             '# Step 1: Assert sum matches parts[2] and print confirmation:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'parts = input().split()\n'
                                              'a, b, expected = map(int, parts)\n'
                                              'try:\n'
                                              '    assert a + b == expected\n'
                                              "    print('Assertion passed: Math verified')\n"
                                              'except AssertionError:\n'
                                              "    print('Assertion failed: Sum does not match')",
                             'test_cases': [{'expected_output': 'Assertion passed: Math verified',
                                             'input_data': '20 22 42\n',
                                             'is_hidden': False},
                                            {'expected_output': 'Assertion failed: Sum does not match',
                                             'input_data': '10 20 40\n',
                                             'is_hidden': False}],
                             'title': 'Check an Addition with assert',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Create a unittest.TestCase with two slugify checks.\n2. Run both tests and print the number run and whether they passed.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import io\n'
                                       'import unittest\n'
                                       'def slugify(text):\n'
                                       "    return '-'.join(text.lower().split())\n"
                                       'class SlugTests(unittest.TestCase):\n'
                                       '    def test_spaces(self):\n'
                                       "        self.assertEqual(slugify('Python Quest'), 'python-quest')\n"
                                       '    def test_lowercase(self):\n'
                                       "        self.assertEqual(slugify('HELLO'), 'hello')\n"
                                       'stream = io.StringIO()\n'
                                       'result = '
                                       'unittest.TextTestRunner(stream=stream).run(unittest.defaultTestLoader.loadTestsFromTestCase(SlugTests))\n'
                                       "print(f'Ran {result.testsRun} tests: Was successful = "
                                       "{result.wasSuccessful()}')"],
                             'initial_code': '# ⚔️ Boss Challenge: Programmatic Test Suite Runner\n'
                                             'import unittest, io\n'
                                             '\n'
                                             'def clean_slug(title):\n'
                                             "    return title.strip().lower().replace(' ', '-')\n"
                                             '\n'
                                             '# Step 1: Define TestSlug(unittest.TestCase) and run suite:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import io\n'
                                              'import unittest\n'
                                              'def slugify(text):\n'
                                              "    return '-'.join(text.lower().split())\n"
                                              'class SlugTests(unittest.TestCase):\n'
                                              '    def test_spaces(self):\n'
                                              "        self.assertEqual(slugify('Python Quest'), 'python-quest')\n"
                                              '    def test_lowercase(self):\n'
                                              "        self.assertEqual(slugify('HELLO'), 'hello')\n"
                                              'stream = io.StringIO()\n'
                                              'result = '
                                              'unittest.TextTestRunner(stream=stream).run(unittest.defaultTestLoader.loadTestsFromTestCase(SlugTests))\n'
                                              "print(f'Ran {result.testsRun} tests: Was successful = "
                                              "{result.wasSuccessful()}')",
                             'test_cases': [{'expected_output': 'Ran 2 tests: Was successful = True',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Run a unittest Suite',
                             'xp_reward': 150}],
             'description': 'Write automated test suites using unittest.TestCase, assertion methods, and test '
                            'fixtures.',
             'lesson': {'common_mistakes': [{'fix': 'Always prefix test method names with test_: def test_login(self):',
                                             'mistake': 'Naming test methods without the test_ prefix (e.g. def '
                                                        'check_login(self):)',
                                             'why': 'The test runner ignores any method that does not begin with '
                                                    "'test_'."}],
                        'detailed_explanation': "A unit test checks one small behavior, such as one function. Python's "
                                                'unittest library gives you a TestCase class for grouping checks. Make '
                                                'a class based on TestCase, then write methods whose names start with '
                                                'test_.\n'
                                                '\n'
                                                'An assertion checks a result. For example, assertEqual(actual, '
                                                'expected) passes when the two values match. If they do not, the test '
                                                'runner reports a failure.\n'
                                                '\n'
                                                'A test runner finds and runs the test methods. Running the same '
                                                'checks after each change is faster and more reliable than trying '
                                                'every feature by hand. The small challenge uses assert directly; the '
                                                'boss uses a unittest suite.',
                        'expected_output': 'String test passed: True',
                        'introduction': 'After fixing one bug, you want to know you did not break something else. A '
                                        'test is a small automatic check you can run again whenever the code changes.',
                        'learning_objectives': ['Explain why programs use repeatable tests.',
                                                'Put checks in a unittest.TestCase class.',
                                                'Use assertions to compare an answer with what you expected.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'import unittest',
                                          'explanation': "Import Python's built-in testing tools."},
                                         {'line': '2',
                                          'code': 'class TestStrings(unittest.TestCase):',
                                          'explanation': 'Create a test class based on unittest.TestCase.'},
                                         {'line': '3',
                                          'code': '    def test_upper(self):',
                                          'explanation': 'The test runner looks for methods whose names start with '
                                                         'test_.'},
                                         {'line': '4',
                                          'code': "        self.assertEqual('foo'.upper(), 'FOO')",
                                          'explanation': 'Check that upper() changes foo to FOO. A mismatch fails the '
                                                         'test.'},
                                         {'line': '5',
                                          'code': 'suite = unittest.TestLoader().loadTestsFromTestCase(TestStrings)',
                                          'explanation': 'Load this test class into a suite.'},
                                         {'line': '6',
                                          'code': 'res = unittest.TextTestRunner(verbosity=0).run(suite)',
                                          'explanation': 'Run the suite and save its result.'},
                                         {'line': '7',
                                          'code': "print('String test passed:', res.wasSuccessful())",
                                          'explanation': 'Display whether every test passed.'}],
                        'practical_examples': [{'code': 'import unittest\n'
                                                        'class TestStrings(unittest.TestCase):\n'
                                                        '    def test_upper(self):\n'
                                                        "        self.assertEqual('foo'.upper(), 'FOO')\n"
                                                        'suite = '
                                                        'unittest.TestLoader().loadTestsFromTestCase(TestStrings)\n'
                                                        'res = unittest.TextTestRunner(verbosity=0).run(suite)\n'
                                                        "print('String test passed:', res.wasSuccessful())",
                                                'explanation': 'Asserts equality between function return values and '
                                                               'expected output.',
                                                'output': 'String test passed: True',
                                                'title': 'Example 1: Writing unit tests for string manipulations'},
                                               {'code': 'import unittest\n'
                                                        'def check_positive(n):\n'
                                                        '    if n < 0:\n'
                                                        "        raise ValueError('Must be positive')\n"
                                                        'class TestErrors(unittest.TestCase):\n'
                                                        '    def test_raises(self):\n'
                                                        '        with self.assertRaises(ValueError):\n'
                                                        '            check_positive(-5)\n'
                                                        'suite = '
                                                        'unittest.TestLoader().loadTestsFromTestCase(TestErrors)\n'
                                                        'res = unittest.TextTestRunner(verbosity=0).run(suite)\n'
                                                        "print('Exception test passed:', res.wasSuccessful())",
                                                'explanation': 'Verifies that invalid input triggers the anticipated '
                                                               'error type.',
                                                'output': 'Exception test passed: True',
                                                'title': 'Example 2: Testing exception raising with assertRaises'},
                                               {'code': 'class TestFixture:\n'
                                                        '    def setUp(self):\n'
                                                        "        self.db = 'connected'\n"
                                                        '    def tearDown(self):\n'
                                                        "        self.db = 'closed'\n"
                                                        'f = TestFixture()\n'
                                                        'f.setUp()\n'
                                                        "print('Fixture active:', f.db)\n"
                                                        'f.tearDown()\n'
                                                        "print('Fixture cleaned:', f.db)",
                                                'explanation': 'Prepares and cleans resources before and after test '
                                                               'executions.',
                                                'output': 'Fixture active: connected\nFixture cleaned: closed',
                                                'title': 'Example 3: Test fixture setup with setUp and tearDown'}],
                        'practice_questions': [{'question': 'What does assertEqual check?',
                                                'answer': 'That the actual and expected values match.'},
                                               {'question': 'How should a test method start?', 'answer': 'With test_.'},
                                               {'question': 'Why run tests after changing code?',
                                                'answer': 'To find behavior the change may have broken.'}],
                        'prerequisites': 'Level 123: Debugging Python Code',
                        'real_world_apps': 'Tests protect calculators, checkout flows, account rules, and other '
                                           'features from breaking during updates.',
                        'summary': 'Write small checks with assertions. unittest groups the checks and runs them for '
                                   'you.',
                        'syntax_breakdown': 'import unittest\n'
                                            'class TestAddition(unittest.TestCase):\n'
                                            '    def test_add(self):\n'
                                            '        self.assertEqual(2 + 3, 5)',
                        'terminology': [{'term': 'Unit test', 'definition': 'A small automatic check of one behavior.'},
                                        {'term': 'TestCase',
                                         'definition': 'A unittest class that holds related test methods.'},
                                        {'term': 'Assertion',
                                         'definition': 'A check that passes when a condition is true.'},
                                        {'term': 'Test runner', 'definition': 'The tool that finds and runs tests.'}]},
             'number': 124,
             'quizzes': [{'explanation': "The test runner's discovery mechanism specifically looks for methods "
                                         'prefixed with `test_` to execute.',
                          'options': [{'explanation': 'Correct! test discovery pattern defaults to test_*.',
                                       'is_correct': True,
                                       'text': 'The test runner automatically discovers and runs methods starting with '
                                               "'test_'"},
                                      {'explanation': 'Incorrect. It is unittest test runner convention.',
                                       'is_correct': False,
                                       'text': 'It is a Python keyword requirement'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Methods without test_ are executed in reverse'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'To make them private methods'}],
                          'question': "Why must test methods in Python's `unittest.TestCase` begin with the prefix "
                                      '`test_`?'},
                         {'explanation': '`setUp()` runs before every individual test method, establishing clean state '
                                         'and test fixtures.',
                          'options': [{'explanation': 'Correct! setUp prepares state before each test.',
                                       'is_correct': True,
                                       'text': 'Runs automatically before each individual test method to prepare test '
                                               'fixtures'},
                                      {'explanation': 'Incorrect. That is tearDownClass.',
                                       'is_correct': False,
                                       'text': 'Runs once after all tests finish'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Installs packages from pip'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Formats test reports into HTML'}],
                          'question': 'What is the purpose of the `setUp()` method in a `unittest.TestCase` class?'}],
             'title': 'Automated Testing with unittest'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Define calc_rectangle_area with float hints for its inputs and result.\n2. Calculate 4.5 times 2.0, then print the area and the function annotations.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 2 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'easy',
                             'hints': ['def calc_rectangle_area(width: float, height: float) -> float:\n'
                                       '    return width * height\n'
                                       'print(calc_rectangle_area(4.5, 2.0))\n'
                                       'print(calc_rectangle_area.__annotations__)'],
                             'initial_code': '# PEP 8 and Type Hints\n'
                                             '# Step 1: Define calc_rectangle_area with annotations:\n'
                                             '\n'
                                             '# Step 2: Print area and __annotations__ below:\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def calc_rectangle_area(width: float, height: float) -> float:\n'
                                              '    return width * height\n'
                                              'print(calc_rectangle_area(4.5, 2.0))\n'
                                              'print(calc_rectangle_area.__annotations__)',
                             'test_cases': [{'expected_output': '9.0\n'
                                                                "{'width': <class 'float'>, 'height': <class 'float'>, "
                                                                "'return': <class 'float'>}",
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Use Type Hints on an Area Function',
                             'xp_reward': 35},
                            {'description': 'Your task, step by step:\n1. Read student names and scores.\n2. Use a typed function to print each score to one decimal place and label 70 or more Pass label lower scores Fail.\n\nInput for this example: The Input box shows 4 sample input lines. When you click Run Example, the app sends those lines to input() automatically, in order. Read the values; do not put the sample values into your code. Submit Code checks other values too.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['def result_line(name: str, score: float) -> str:\n'
                                       "    status = 'Pass' if score >= 70 else 'Fail'\n"
                                       "    return f'{name}: {score:.1f} ({status})'\n"
                                       'count = int(input())\n'
                                       'for _ in range(count):\n'
                                       '    name, score = input().split()\n'
                                       '    print(result_line(name, float(score)))'],
                             'initial_code': '# ⚔️ Boss Challenge: PEP 8 Style and Type Validator\n'
                                             'n = int(input())\n'
                                             '\n'
                                             '# Step 1: For each student, parse, format, and print:\n'
                                             '\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'def result_line(name: str, score: float) -> str:\n'
                                              "    status = 'Pass' if score >= 70 else 'Fail'\n"
                                              "    return f'{name}: {score:.1f} ({status})'\n"
                                              'count = int(input())\n'
                                              'for _ in range(count):\n'
                                              '    name, score = input().split()\n'
                                              '    print(result_line(name, float(score)))',
                             'test_cases': [{'expected_output': 'Mia: 88.0 (Pass)\nBo: 67.0 (Fail)\nAri: 70.0 (Pass)',
                                             'input_data': '3\nMia 88\nBo 67\nAri 70\n',
                                             'is_hidden': False}],
                             'title': 'Boss Challenge: Format Typed Student Results',
                             'xp_reward': 150}],
             'description': 'Write clean, self-documenting code following PEP 8 standards, static type hints, and '
                            'linters.',
             'lesson': {'common_mistakes': [{'fix': 'Use runtime validation if strict runtime checking is required.',
                                             'mistake': 'Expecting Python to raise a TypeError at runtime if a type '
                                                        'hint is violated',
                                             'why': 'Type hints are not enforced by Python runtime; they are for '
                                                    'linters, IDEs, and static analysis tools like mypy.'}],
                        'detailed_explanation': "PEP 8 is Python's common style guide. It recommends four spaces for "
                                                'indentation, lowercase_with_underscores for functions and variables, '
                                                'and CapitalizedWords for classes. Consistent style makes code easier '
                                                'to scan.\n'
                                                '\n'
                                                'A type hint is a note in a function definition. In def area(width: '
                                                'float) -> float, the hint says width is expected to be a decimal '
                                                'number and the result is expected to be a decimal number. The arrow '
                                                'points to the result type.\n'
                                                '\n'
                                                'Python normally does not reject a value just because it disagrees '
                                                'with a hint. Hints help readers, editors, and separate tools find '
                                                'possible mistakes. They are labels, not automatic conversions or '
                                                'safety checks.',
                        'expected_output': "{'avg': 90.0}",
                        'introduction': 'A recipe is easier to follow when its steps are neat and its ingredients are '
                                        'labeled. PEP 8 is a shared style guide, and type hints label the kinds of '
                                        'values a function expects.',
                        'learning_objectives': ['Use PEP 8 names and spacing to make code easier to read.',
                                                'Add type hints to describe expected inputs and results.',
                                                'Explain that Python does not enforce ordinary hints by itself.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'from typing import List, Dict',
                                          'explanation': 'Import the List and Dict type labels.'},
                                         {'line': '2',
                                          'code': 'def summarize_scores(scores: List[int]) -> Dict[str, float]:',
                                          'explanation': 'Define a function whose input is a list of whole numbers and '
                                                         'whose result is a dictionary with text keys and decimal '
                                                         'values.'},
                                         {'line': '3',
                                          'code': "    return {'avg': sum(scores) / len(scores)}",
                                          'explanation': 'Add the scores, divide by their count, and return the '
                                                         'average in a dictionary.'},
                                         {'line': '4',
                                          'code': 'print(summarize_scores([90, 80, 100]))',
                                          'explanation': 'Call the function with three scores and display the '
                                                         'result.'}],
                        'practical_examples': [{'code': 'from typing import List, Dict\n'
                                                        'def summarize_scores(scores: List[int]) -> Dict[str, float]:\n'
                                                        "    return {'avg': sum(scores) / len(scores)}\n"
                                                        'print(summarize_scores([90, 80, 100]))',
                                                'explanation': 'Documents functions that accept lists and return '
                                                               'dictionaries.',
                                                'output': "{'avg': 90.0}",
                                                'title': 'Example 1: Annotating complex data structures with typing'},
                                               {'code': 'from typing import Optional\n'
                                                        'def find_user(user_id: int) -> Optional[str]:\n'
                                                        '    if user_id == 1:\n'
                                                        "        return 'Alex'\n"
                                                        '    return None\n'
                                                        "print('Found:', find_user(1))\n"
                                                        "print('Missing:', find_user(99))",
                                                'explanation': 'Optional[str] indicates the function returns either a '
                                                               'str or None.',
                                                'output': 'Found: Alex\nMissing: None',
                                                'title': 'Example 2: Optional types and Union with typing.Optional'},
                                               {'code': 'MAX_RETRIES = 3  # Constants in UPPER_CASE\n'
                                                        'class DatabaseManager:  # Classes in PascalCase\n'
                                                        '    def execute_query(self):  # Functions in snake_case\n'
                                                        "        return 'Query OK'\n"
                                                        'print(DatabaseManager().execute_query())',
                                                'explanation': 'Illustrates universal Python casing conventions.',
                                                'output': 'Query OK',
                                                'title': 'Example 3: Adhering to PEP 8 naming standards'}],
                        'practice_questions': [{'question': 'What does -> float describe?',
                                                'answer': 'The kind of value the function is expected to return.'},
                                               {'question': 'Does width: float convert text to a number?',
                                                'answer': 'No. A hint does not convert a value.'},
                                               {'question': 'How are class names usually written?',
                                                'answer': 'CapitalizedWords, such as StudentRecord.'}],
                        'prerequisites': 'Level 124: Automated Testing with unittest',
                        'real_world_apps': 'Type hints help teammates understand functions and help editors and '
                                           'type-checkers flag possible mismatches.',
                        'summary': 'Use PEP 8 style so people can read the code. Type hints describe expected values '
                                   'but do not enforce or convert them by themselves.',
                        'syntax_breakdown': 'def area(width: float, height: float) -> float:\n'
                                            '    return width * height',
                        'terminology': [{'term': 'PEP 8',
                                         'definition': 'The commonly used guide for formatting Python code.'},
                                        {'term': 'Type hint',
                                         'definition': 'A note describing the kind of value expected.'},
                                        {'term': 'Parameter', 'definition': 'A named input a function receives.'},
                                        {'term': 'Return type',
                                         'definition': 'The kind of value a function is expected to send back.'}]},
             'number': 125,
             'quizzes': [{'explanation': 'Python does NOT enforce type hints at runtime by default. String '
                                         "concatenation executes, returning 'PythonQuest'.",
                          'options': [{'explanation': 'Correct! Type hints are ignored at runtime in standard Python '
                                                      'without external linters.',
                                       'is_correct': True,
                                       'text': 'PythonQuest'},
                                      {'explanation': 'Incorrect. Python runtime does not enforce type annotations.',
                                       'is_correct': False,
                                       'text': 'TypeError: arguments must be int'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': 'None'},
                                      {'explanation': 'Incorrect. Type hints are valid syntax.',
                                       'is_correct': False,
                                       'text': 'SyntaxError'}],
                          'question': 'What is the output of executing typed Python code at runtime?\n'
                                      '\n'
                                      'def add(x: int, y: int) -> int:\n'
                                      '    return x + y\n'
                                      '\n'
                                      "print(add('Python', 'Quest'))"},
                         {'explanation': 'PEP 8 specifies exactly 4 spaces per indentation level.',
                          'options': [{'explanation': 'Correct! PEP 8 standard indentation is 4 spaces.',
                                       'is_correct': True,
                                       'text': '4 spaces'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '2 spaces'},
                                      {'explanation': 'Incorrect.', 'is_correct': False, 'text': '8 spaces'},
                                      {'explanation': 'Incorrect. PEP 8 strongly prefers spaces over tabs.',
                                       'is_correct': False,
                                       'text': '1 tab character'}],
                          'question': 'According to PEP 8, how many spaces should be used for each indentation level '
                                      'in Python?'}],
             'title': 'Code Quality, PEP 8, and Type Hints'},
            {'challenges': [{'description': 'Your task, step by step:\n1. Create a temporary players table, add Hero and Mage with their XP, calculate the average, and print it with one decimal place.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 1 line. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'medium',
                             'hints': ['import sqlite3\n'
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE players (name TEXT, xp INTEGER)')\n"
                                       "connection.executemany('INSERT INTO players VALUES (?, ?)', [('Hero', 1200), "
                                       "('Mage', 950)])\n"
                                       "average = connection.execute('SELECT AVG(xp) FROM players').fetchone()[0]\n"
                                       "print(f'Average XP: {average:.1f}')\n"
                                       'connection.close()'],
                             'initial_code': '# Master Capstone: Database Aggregator\n'
                                             'import sqlite3\n'
                                             "conn = sqlite3.connect(':memory:')\n"
                                             'cur = conn.cursor()\n'
                                             '\n'
                                             '# Step 1: Create table, insert players, calculate AVG(xp):\n'
                                             '\n',
                             'is_boss': False,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE players (name TEXT, xp INTEGER)')\n"
                                              "connection.executemany('INSERT INTO players VALUES (?, ?)', [('Hero', "
                                              "1200), ('Mage', 950)])\n"
                                              "average = connection.execute('SELECT AVG(xp) FROM "
                                              "players').fetchone()[0]\n"
                                              "print(f'Average XP: {average:.1f}')\n"
                                              'connection.close()',
                             'test_cases': [{'expected_output': 'Average XP: 1075.0',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Calculate Average Player XP with SQLite',
                             'xp_reward': 50},
                            {'description': 'Your task, step by step:\n1. Save Alice, Bob, and Charlie in a temporary students table.\n2. Find GPAs of 3.8 or higher, highest first.\n3. Print each student and the number of honors students.\n\nInput for this example: This example supplies no input. Use the values or messages named in the task; do not add input() unless the task asks you to read a value.\n\nOutput to aim for: The sample output has 3 lines. Print the requested result in that order. Match the example exactly, including capital letters, spelling, punctuation, spaces, and line breaks. Do not print prompts or extra text.',
                             'difficulty': 'boss',
                             'hints': ['import sqlite3\n'
                                       "connection = sqlite3.connect(':memory:')\n"
                                       "connection.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, "
                                       "gpa REAL)')\n"
                                       "connection.executemany('INSERT INTO students VALUES (?, ?, ?)', [(1, 'Alice', "
                                       "3.9), (2, 'Bob', 3.4), (3, 'Charlie', 3.85)])\n"
                                       'connection.commit()\n'
                                       "honors = connection.execute('SELECT name, gpa FROM students WHERE gpa >= ? "
                                       "ORDER BY gpa DESC', (3.8,)).fetchall()\n"
                                       'for name, gpa in honors:\n'
                                       "    print(f'Honors: {name} (GPA: {gpa})')\n"
                                       "print(f'Capstone Complete: {len(honors)} honors students recorded!')\n"
                                       'connection.close()'],
                             'initial_code': '# ⚔️ Final Master Capstone: Complete Database Application\n'
                                             'import sqlite3\n'
                                             '\n'
                                             '# Step 1: Connect to an in-memory database and create a cursor:\n'
                                             "conn = sqlite3.connect(':memory:')\n"
                                             'cur = conn.cursor()\n'
                                             '\n'
                                             "# Step 2: Create the 'students' table with id, name, and gpa columns:\n"
                                             '\n'
                                             '\n'
                                             "# Step 3: Insert the 3 students: (1, 'Alice', 3.9), (2, 'Bob', 3.4), (3, "
                                             "'Charlie', 3.85):\n"
                                             '\n'
                                             '\n'
                                             '# Step 4: Commit the transactions:\n'
                                             '\n'
                                             '\n'
                                             '# Step 5: Query honors students (gpa >= 3.8) ordered by gpa DESC, and '
                                             'print each row:\n'
                                             '\n'
                                             '\n'
                                             "# Step 6: Print 'Capstone Complete: 2 honors students recorded!' and "
                                             'close connection:\n',
                             'is_boss': True,
                             'requirements': 'Match the example output, including its words and line breaks.',
                             'solution_code': 'import sqlite3\n'
                                              "connection = sqlite3.connect(':memory:')\n"
                                              "connection.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name "
                                              "TEXT, gpa REAL)')\n"
                                              "connection.executemany('INSERT INTO students VALUES (?, ?, ?)', [(1, "
                                              "'Alice', 3.9), (2, 'Bob', 3.4), (3, 'Charlie', 3.85)])\n"
                                              'connection.commit()\n'
                                              "honors = connection.execute('SELECT name, gpa FROM students WHERE gpa "
                                              ">= ? ORDER BY gpa DESC', (3.8,)).fetchall()\n"
                                              'for name, gpa in honors:\n'
                                              "    print(f'Honors: {name} (GPA: {gpa})')\n"
                                              "print(f'Capstone Complete: {len(honors)} honors students recorded!')\n"
                                              'connection.close()',
                             'test_cases': [{'expected_output': 'Honors: Alice (GPA: 3.9)\n'
                                                                'Honors: Charlie (GPA: 3.85)\n'
                                                                'Capstone Complete: 2 honors students recorded!',
                                             'input_data': '',
                                             'is_hidden': False}],
                             'title': 'Master Capstone: Student Honors Registry',
                             'xp_reward': 500}],
             'description': 'Synthesize the entire 12-world curriculum in a production-grade, secure, '
                            'database-connected application.',
             'lesson': {'common_mistakes': [{'fix': 'Always use ? placeholders for all database queries.',
                                             'mistake': 'Skipping parameterized placeholders under pressure',
                                             'why': 'Security flaws must never be tolerated, even in final capstone '
                                                    'submissions.'}],
                        'detailed_explanation': 'A database-backed program stores information in tables so it can be '
                                                'found later. The first example creates a table, inserts a row with '
                                                'question-mark placeholders, reads the row back, and closes the '
                                                'connection.\n'
                                                '\n'
                                                'A larger student registry could also use functions, input checks, '
                                                'type hints, and tests. Each part has a job: the database saves '
                                                'records, functions organize actions, validation checks input, and '
                                                'tests catch mistakes.\n'
                                                '\n'
                                                'The boss is a focused capstone. It saves three students, selects '
                                                'those whose GPA reaches the cutoff, sorts them, and prints a report. '
                                                'The cutoff is passed as a parameter so it stays data rather than SQL '
                                                'text. The practice database exists only in memory, so it leaves no '
                                                'files behind.',
                        'expected_output': "Master Rank: ('Master', 10000)",
                        'introduction': 'A small school app might save students, find who qualifies for honors, and '
                                        'show a report. This level puts the database steps together from beginning to '
                                        'end.',
                        'learning_objectives': ['Combine table creation, saved rows, and SELECT queries.',
                                                'Use placeholders when putting values into SQL.',
                                                'Explain how a larger project combines skills from earlier levels.'],
                        'line_by_line': [{'line': '1',
                                          'code': 'import sqlite3',
                                          'explanation': 'Import the SQLite library.'},
                                         {'line': '2',
                                          'code': "conn = sqlite3.connect(':memory:')",
                                          'explanation': 'Open a temporary database.'},
                                         {'line': '3',
                                          'code': 'with conn:',
                                          'explanation': 'Use the connection as a transaction; the indented changes '
                                                         'save together if they succeed.'},
                                         {'line': '4',
                                          'code': "    conn.execute('CREATE TABLE ranks (name TEXT, xp INT)')",
                                          'explanation': 'Create a table with name and experience-point columns.'},
                                         {'line': '5',
                                          'code': "    conn.execute('INSERT INTO ranks VALUES (?, ?)', ('Master', "
                                                  '10000))',
                                          'explanation': 'Insert a row. The question marks safely receive the tuple '
                                                         'values.'},
                                         {'line': '6',
                                          'code': 'cur = conn.cursor()',
                                          'explanation': 'Create a cursor for reading query results.'},
                                         {'line': '7',
                                          'code': "cur.execute('SELECT * FROM ranks')",
                                          'explanation': 'Ask for every row in ranks.'},
                                         {'line': '8',
                                          'code': "print('Master Rank:', cur.fetchone())",
                                          'explanation': 'Read one result row and display it.'},
                                         {'line': '9', 'code': 'conn.close()', 'explanation': 'Close the connection.'}],
                        'practical_examples': [{'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        'with conn:\n'
                                                        "    conn.execute('CREATE TABLE ranks (name TEXT, xp INT)')\n"
                                                        "    conn.execute('INSERT INTO ranks VALUES (?, ?)', "
                                                        "('Master', 10000))\n"
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('SELECT * FROM ranks')\n"
                                                        "print('Master Rank:', cur.fetchone())\n"
                                                        'conn.close()',
                                                'explanation': 'Synthesizes table creation, insertion, queries, and '
                                                               'connection cleanup.',
                                                'output': "Master Rank: ('Master', 10000)",
                                                'title': 'Example 1: Complete end-to-end SQLite integration class'},
                                               {'code': 'import sqlite3\n'
                                                        "conn = sqlite3.connect(':memory:')\n"
                                                        "conn.execute('CREATE TABLE ledger (bal INT)')\n"
                                                        'try:\n'
                                                        '    with conn:\n'
                                                        "        conn.execute('INSERT INTO ledger VALUES (100)')\n"
                                                        '        # Simulated error triggering rollback\n'
                                                        "        raise RuntimeError('Network timeout during commit')\n"
                                                        'except RuntimeError:\n'
                                                        '    pass\n'
                                                        'cur = conn.cursor()\n'
                                                        "cur.execute('SELECT count(*) FROM ledger')\n"
                                                        "print('Committed rows after rollback:', cur.fetchone()[0])\n"
                                                        'conn.close()',
                                                'explanation': 'with conn rolls back pending database changes '
                                                               'automatically if an exception is raised.',
                                                'output': 'Committed rows after rollback: 0',
                                                'title': 'Example 2: Transaction rollback on failure'},
                                               {'code': "print('==============================================')\n"
                                                        "print(' PYTHON QUEST: FULL CURRICULUM MASTERY ACHIEVED')\n"
                                                        "print('   12 WORLDS | 126 LEVELS | 100% COMPLETE     ')\n"
                                                        "print('==============================================')",
                                                'explanation': 'Celebrates complete mastery of all 12 Worlds of Python '
                                                               'Quest.',
                                                'output': '==============================================\n'
                                                          ' PYTHON QUEST: FULL CURRICULUM MASTERY ACHIEVED\n'
                                                          '   12 WORLDS | 126 LEVELS | 100% COMPLETE     \n'
                                                          '==============================================',
                                                'title': 'Example 3: Final Python Quest Curriculum Mastery '
                                                         'Certificate'}],
                        'practice_questions': [{'question': 'What happens after the example inserts a row?',
                                                'answer': 'It selects the row and prints it.'},
                                               {'question': 'Why pass the GPA cutoff separately?',
                                                'answer': 'The placeholder treats it as a value, not SQL code.'},
                                               {'question': 'Name two skills a larger app could combine with SQLite.',
                                                'answer': 'For example, functions, validation, type hints, error '
                                                          'handling, or tests.'}],
                        'prerequisites': 'Levels 1 through 125',
                        'real_world_apps': 'A school, shop, or game service can use these steps to store records and '
                                           'build reports.',
                        'summary': 'A database app connects, creates tables, safely stores values, reads records, and '
                                   'closes the connection. A capstone combines these steps with other skills.',
                        'syntax_breakdown': "connection = sqlite3.connect(':memory:')\n"
                                            "connection.execute('CREATE TABLE students (name TEXT, gpa REAL)')\n"
                                            "connection.execute('INSERT INTO students VALUES (?, ?)', (name, gpa))\n"
                                            "rows = connection.execute('SELECT name FROM students WHERE gpa >= ?', "
                                            '(cutoff,)).fetchall()',
                        'terminology': [{'term': 'Capstone',
                                         'definition': 'A final task that combines several skills.'},
                                        {'term': 'Database',
                                         'definition': 'An organized place to store and find records.'},
                                        {'term': 'Transaction',
                                         'definition': 'A group of database changes saved together.'},
                                        {'term': 'Parameterized query',
                                         'definition': 'SQL with placeholders and separate values.'}]},
             'number': 126,
             'quizzes': [{'explanation': 'Violating a PRIMARY KEY or UNIQUE constraint raises a '
                                         'sqlite3.IntegrityError: UNIQUE constraint failed.',
                          'options': [{'explanation': 'Correct! Duplicate primary keys raise sqlite3.IntegrityError.',
                                       'is_correct': True,
                                       'text': 'sqlite3.IntegrityError: UNIQUE constraint failed'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'sqlite3.OperationalError'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'ValueError: duplicate id'},
                                      {'explanation': 'Incorrect. Without INSERT OR REPLACE, it raises an error.',
                                       'is_correct': False,
                                       'text': 'It silently updates the row'}],
                          'question': 'What exception is raised if an INSERT statement attempts to insert a duplicate '
                                      'value into a PRIMARY KEY column in sqlite3?\n'
                                      '\n'
                                      'import sqlite3\n'
                                      "conn = sqlite3.connect(':memory:')\n"
                                      'cur = conn.cursor()\n'
                                      "cur.execute('CREATE TABLE t (id INT PRIMARY KEY)')\n"
                                      "cur.execute('INSERT INTO t VALUES (1)')\n"
                                      "cur.execute('INSERT INTO t VALUES (1)')"},
                         {'explanation': 'Type hints, automated unit testing with unittest/pytest, structured logging, '
                                         'and parameterized DB queries ensure enterprise quality.',
                          'options': [{'explanation': 'Correct! These practices provide reliability, security, and '
                                                      'maintainability.',
                                       'is_correct': True,
                                       'text': 'Type hints, automated unit testing, parameterized SQL queries, and '
                                               'modular package structure'},
                                      {'explanation': 'Incorrect. These are anti-patterns and security hazards.',
                                       'is_correct': False,
                                       'text': 'Global variables, raw f-string SQL queries, and bare try/except '
                                               'blocks'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Writing the entire application in a single 10,000 line file'},
                                      {'explanation': 'Incorrect.',
                                       'is_correct': False,
                                       'text': 'Committing virtual environments to Git repositories'}],
                          'question': 'Which combination represents the industry-standard architecture for robust '
                                      'Python enterprise data applications?'}],
             'title': 'World 12 Examination & Master Capstone: Complete Database Application'}],
 'number': 12,
 'title': 'Real-World Development'}
