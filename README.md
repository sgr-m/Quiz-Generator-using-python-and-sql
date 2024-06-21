# Quiz-Generator-using-python-and-sql
Quiz Generator using MySQL and Python 3.12
___________QUIZ GENERATOR____________
# replace the questions from dictionary as per your need
# Read PDF attached for detailed information

'''
 Function to create a MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost', # add your host
            database='quiz',  # choose your database
            user='root',      # Customize
            password=''	      # customize
        )
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"Error: {e}")
    return connection

'''
