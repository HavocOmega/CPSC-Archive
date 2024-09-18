# Assignment 1
# Written by: Ryll

# Create a hashtable of valid string responses
valid_responses = {}
valid_responses["is_citizen"] = ["Yes", "yes", "no", "No"]
valid_responses["is_resident"] = ["Yes", "yes", "no", "No"]
valid_responses["birth_month"] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
valid_responses["birth_day"] = []
valid_responses["birth_year"] = []

# Months with 30 days
thirty_day_months = ["April", "June", "September", "November"]
# Months with 31 days
thirty_one_day_months = ["January", "March", "May", "July", "August", "October", "December"]

minimum_year = 1999
maximum_year = 2024

# Dictionary of all questions
questions = {
    'is_citizen': "Are you a Canadian citizen?",
    'is_resident': "Are you a resident of Alberta?",
    'birth_month': "What is the month of your birth date?",
    'birth_day': "What is the day of your birth date?",
    'birth_year': "What is the year of your birth date?"
}

valued_months = {
    "January": 1, 
    "February": 2, 
    "March": 3, 
    "April": 4, 
    "May": 5, 
    "June": 6, 
    "July": 7, 
    "August": 8, 
    "September": 9, 
    "October": 10, 
    "November": 11, 
    "December": 12}

# Hash table of responses to questions to store for later (tbh idk why i store them it's just convenient for later)
stored_responses = {}

def isResponseValid(question, value):
    if value.isdigit():
        intValue = int(value)
        match question:
            case 'birth_day':
                birth_month = stored_responses["birth_month"]
                
                match birth_month:
                    case birth_month if birth_month in thirty_day_months:
                        if intValue > 30:
                            print("Invalid birth date.")
                            return 2;
                    case birth_month if birth_month in thirty_one_day_months:
                        if intValue > 31:
                            print("Invalid birth date.")
                            return 2;
                    case _:
                        if intValue > 29:
                            print("Invalid birth date.")
                            return 2;
            case 'birth_year':
                if intValue < minimum_year or intValue > maximum_year:
                    print("Invalid birth date.")
                    return 2;
            case _:
                print("Invalid response.")
                return 1;
    elif not value in valid_responses.get(question):
        print("Invalid response.")
        return 1;
    return 0

def askQuestions():
    # Loop through questions dictionary
    for i, v in questions.items():
        # Store responses by the index from the questions dictionary
        stored_responses[i] = input(v + " ")
        isValid = isResponseValid(i, stored_responses[i])
        if isValid > 0:
            print("EXIT CODE: " + str(isValid))
            quit(isValid)
            
def validateBirth():
    if int(stored_responses["birth_year"]) == maximum_year:
        if valued_months[stored_responses["birth_month"]] > 9:
            print("Invalid birth date.")
            print("EXIT CODE: 2")
            quit(2)
        elif valued_months[stored_responses["birth_month"]] == 9:
            if int(stored_responses["birth_day"]) > 27:
                print("Invalid birth date.")
                print("EXIT CODE: 2")
                quit(2)
        
def initialize():
    askQuestions()
    validateBirth()

# Initialize program
initialize()