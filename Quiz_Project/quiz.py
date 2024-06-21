def intro():
    print("\n\t\t\t<-------- CODE WITH AMINA NOOR -------->\n")
    print("\t\t\t\t<-------- WELCOME TO THE Quiz App -------->\n")

def ask_questions(question, options, correct_option):
    print("\n", question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
        
    while True:
        try:
            choice = int(input("Your Choice is (1 - 4)"))
            if 1 <= choice <= 4:
                return choice == correct_option
            else:
                print("Invalid choice. Please Select a number b/w 1 and 4.")
            
        except ValueError:
            print("Invalid Input. Please select a number b/w 1 and 4.")
            
def run_quiz():
    questions = [
        {
            "question": "What is a correct syntax to output 'Hello World' in Python?",
            "options": ["echo 'Hello World!'", "echo('Hello World!')", "print('Hello World!')", "p('Hello World!)"],
            "correct_option": 3,
        },
        
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": ["//Comment", "#Comment", "/* Comment */", "<!-- Comment -->"],
            "correct_option": 2,
        },
        
        {
            "question": "Which one is NOT a legal variable name?",
            "options": ["_myvar", "my_var", "Myvar", "my-var"],
            "correct_option": 3,
        },
        
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": ["//Comment", "#Comment", "/* Comment */", "<!-- Comment -->"],
            "correct_option": 2,
        },
        
         {
            "question": "What is a correct syntax to output 'Hello World' in Python?",
            "options": ["echo 'Hello World!'", "echo('Hello World!')", "print('Hello World!')", "p('Hello World!)"],
            "correct_option": 3,
        },
        
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": ["//Comment", "#Comment", "/* Comment */", "<!-- Comment -->"],
            "correct_option": 2,
        },
        
        {
            "question": "What is a correct syntax to output 'Hello World' in Python?",
            "options": ["echo 'Hello World!'", "echo('Hello World!')", "print('Hello World!')", "p('Hello World!)"],
            "correct_option": 3,
        },
        
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": ["//Comment", "#Comment", "/* Comment */", "<!-- Comment -->"],
            "correct_option": 2,
        },
        
         {
            "question": "What is a correct syntax to output 'Hello World' in Python?",
            "options": ["echo 'Hello World!'", "echo('Hello World!')", "print('Hello World!')", "p('Hello World!)"],
            "correct_option": 3,
        },
        
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": ["//Comment", "#Comment", "/* Comment */", "<!-- Comment -->"],
            "correct_option": 2,
        },
    ]
                



