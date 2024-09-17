# Create a hashtable of valid string responses
valid_responses = {}
valid_responses["is_citizen"] = ["Yes", "yes", "no", "No"]
valid_responses["is_resident"] = ["Yes", "yes", "no", "No"]
valid_responses["birth_month"] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
valid_responses["birth_day"] = []
valid_responses["birth_year"] = []

# Dictionary of all wanted problems
questions = {
    'is_citizen': "Are you a Canadian citizen?",
    'is_resident': "Are you a resident of Alberta?",
    'birth_month': "What is the month of your birth date?",
    'birth_day': "What is the day of your birth date?",
    'birth_year': "What is the year of your birth date?"
}

# Hash table of responses to questions to store for later (tbh idk why i store them it's just convenient for later)
stored_responses = {}

def isResponseValid(value, hashList):
    if value.isdigit():
        print("isDigit")
    elif not value in hashList:
        print("Invalid response.")
        quit()

def askQuestions():
    # Loop through questions dictionary
    for i, v in questions.items():
        # Store responses by the index from the questions dictionary
        stored_responses[i] = input(v + " ")
        isResponseValid(stored_responses[i], valid_responses.get(i))

# Initialize program
askQuestions()