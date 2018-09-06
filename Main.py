# Importing random
from random import randint

# =============================================================

#        PYTHON MAGIC 8BALL CONSOLE APPLICATION
#                    Kenneth Melendez

# =============================================================


# ==============================================

#  Data Validation

# ==============================================


# Check if variable is an int for data validation
def check_if_int(variable):
    try:
        int(variable)
        return True
    except ValueError:
        return False


# ==============================================

#  Messages and Promps

# ==============================================


# Method for returning a response for the user
def response(question):
    print(f"{question}.. ?")
    responses = ["Yes", "No", "Maybe"]
    print(responses[randint(0, len(responses) - 1)])


# Method for prompting the user for a response and checking for an answer (Data Validation)
def prompt_question():
    response = "Ask me a question!"
    user_input = input(response)

    while user_input == "" or check_if_int(user_input):
        if check_if_int(user_input):
            print("Hey that's a number!")
        user_input = input("Please input a correct response")

    return user_input


# Introduction prompt
def display_introduction():
    print("Welcome to the Magic 8 Ball Application")


# GoodBye Message
def goodbye_msg():
    print("GoodBye!")


# ==============================================

#  Main Application Method

# ==============================================


# Main application method everything will load here
def run_application():
    display_introduction()
    response(prompt_question())
    goodbye_msg()


# Loading Application
run_application()
