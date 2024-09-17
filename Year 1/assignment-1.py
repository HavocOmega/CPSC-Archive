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
                if intValue < 1900 or intValue > 2024:
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
            
def initialize():
    askQuestions()
    

# Initialize program
initialize()