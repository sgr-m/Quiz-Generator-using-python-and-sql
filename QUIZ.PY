import mysql.connector
from mysql.connector import Error

# Function to create a MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='quiz',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"Error: {e}")
    return connection

# Function to create the quiz
def create_quiz():
    questions = [
        {"question": "What is the correct way to declare a dictionary in Python?",
         "options": {"A": "{}", "B": "[]", "C": "()", "D": "<>"},
         "correct_answer": "A"},
        
        {"question": "What does the 'len()' function do?",
         "options": {"A": "Returns the length of a string", "B": "Returns the length of a list",
                     "C": "Returns the length of a dictionary", "D": "All of the above"},
         "correct_answer": "D"},

        {"question": "How do you access the value associated with the key 'name' in a dictionary named 'person'?",
         "options": {"A": "person['name']", "B": "person(name)", "C": "person.get('name')", "D": "name(person)"},
         "correct_answer": "A"},

        {"question": "Which method is used to convert a string to uppercase in Python?",
         "options": {"A": "upper()", "B": "capitalize()", "C": "title()", "D": "uppercase()"},
         "correct_answer": "A"},

        {"question": "What does the 'join()' method do for strings in Python?",
         "options": {"A": "Joins two strings together", "B": "Splits a string into a list",
                     "C": "Reverses the characters in a string", "D": "Converts a string to lowercase"},
         "correct_answer": "A"},

        {"question": "Which of the following is a correct way to declare an empty list in Python?",
         "options": {"A": "list = []", "B": "list = {}", "C": "list = ()", "D": "list = None"},
         "correct_answer": "A"},

        {"question": "What is the result of the expression 3 + 2 * 4?",
         "options": {"A": "20", "B": "15", "C": "11", "D": "25"},
         "correct_answer": "C"},

        {"question": "What is the purpose of the 'split()' method for strings in Python?",
         "options": {"A": "Joins two strings together", "B": "Splits a string into a list",
                     "C": "Reverses the characters in a string", "D": "Converts a string to lowercase"},
         "correct_answer": "B"},

        {"question": "In Python, what is the purpose of the 'else' clause in a 'try...except' block?",
         "options": {"A": "It is used to define the exception", "B": "It is executed if no exception occurs",
                     "C": "It is executed when an exception occurs", "D": "It is optional and can be omitted"},
         "correct_answer": "B"},

        {"question": "What is the result of the expression 'hello' + 'world'?",
         "options": {"A": "'helloworld'", "B": "'hello world'", "C": "'hello' 'world'", "D": "'h' 'e' 'l' 'l' 'o' ' ' 'w' 'o' 'r' 'l' 'd'"},
         "correct_answer": "A"},
    ]
    return questions

# Function to conduct the quiz
def conduct_quiz(questions):
    score = 0
    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for option, text in question['options'].items():
            print(f"{option}. {text}")

        user_answer = input("Your answer: ").upper()
        if user_answer == question['correct_answer']:
            score += 1

    return score

# Function to store results in the database
def store_results(connection, participant_name, score):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO quiz_results (participant_name, score) VALUES (%s, %s)"
        data = (participant_name, score)
        cursor.execute(query, data)
        connection.commit()
        print("Results stored successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to display results of all participants
def display_results(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM quiz_results"
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("No results found.")
        else:
            print("\nResults of all participants:")
            print("Participant Name\tScore")
            print("-----------------\t-----")
            for result in results:
                print(f"{result[1]}\t\t\t{result[2]}")

            highest_score = max(results, key=lambda x: x[2])
            print(f"\nParticipant with the highest score: {highest_score[1]} with a score of {highest_score[2]}")

    except Error as e:
        print(f"Error: {e}")

# Main program
if __name__ == "__main__":
    # Create a quiz
    quiz_questions = create_quiz()

    # Get participant's name
    participant_name = input("Enter your name: ")

    # Conduct the quiz
    participant_score = conduct_quiz(quiz_questions)

    # Create a database connection
    connection = create_connection()

    # Store the results in the database
    if connection:
        store_results(connection, participant_name, participant_score)

    # Display results of all participants
    if connection.is_connected():
        display_results(connection)

    # Close the database connection
    if connection.is_connected():
        connection.close()
        print("Connection closed.")