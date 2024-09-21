# Note: Ignore the exit code stuff, I just used it to debug and just know where my code is at in the process

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

# Valid range for the year user was born
minimum_year = 1900
maximum_year = 2024

# Dictionary of all questions
questions = {
    'is_citizen': "Are you a Canadian citizen?",
    'is_resident': "Are you a resident of Alberta?",
    'birth_month': "What is the month of your birth date?",
    'birth_day': "What is the day of your birth date?",
    'birth_year': "What is the year of your birth date?"
}

# Dictionary to assign numerical values to each corresponding month
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

# Hashtable of responses to questions to store for later
stored_responses = {}

# Function to see if a response is valid under certain conditions
def isResponseValid(question, value):
    if value.isdigit(): # Check if the response is a digit
        intValue = int(value) # Convert the response to an integer
        match question:
            case 'birth_day':
                #Check if the user's day of birth is either 0 or negative
                if intValue < 1:
                    print("Invalid birth date.")
                    return 2;
                
                # Retrieve birth month value
                birth_month = stored_responses["birth_month"]
                
                #Check if the user's day of birth is a valid day within that month
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
                # Check if the inputted year is a valid year within the given range
                if intValue < minimum_year or intValue > maximum_year:
                    print("Invalid birth date.")
                    return 2;
            case _: # If the question is not a question that queries for an integer value then it's an invalid response
                print("Invalid response.")
                return 1;
    elif not value in valid_responses.get(question): # Checks if the user's response is one of the valid responses stored earlier
        print("Invalid response.")
        return 1;
    return 0

# Function to ask the user questions when the code is ran
def askQuestions():
    # Loop through questions dictionary
    for i, v in questions.items(): #Note: i is short for index and v is short for value
        # Store responses by the index from the questions dictionary
        stored_responses[i] = input(v + " ") # Query the user
        isValid = isResponseValid(i, stored_responses[i]) # Check if response is valid using the function
        if isValid > 0:
            #print("EXIT CODE: " + str(isValid))
            exit(isValid)
            
# Function to validate the user's birthday
def validateBirth():
    if int(stored_responses["birth_year"]) == maximum_year:
        if valued_months[stored_responses["birth_month"]] > 9: # If the month inputted is a month that is past September then it's invalid
            print("Invalid birth date.")
            #print("EXIT CODE: 2")
            exit(2)
        elif valued_months[stored_responses["birth_month"]] == 9: # If the month and day inputted is past September 27 then it's invalid
            if int(stored_responses["birth_day"]) > 27:
                print("Invalid birth date.")
                #print("EXIT CODE: 2")
                exit(2)
                
# Function to check the user's eligibility to vote
def voterEligibilityCheck():
    # Check if the USER SATIFIES 
    if stored_responses["is_citizen"] == "Yes" or stored_responses["is_citizen"] == "yes":
        if stored_responses["is_resident"] == "Yes" or stored_responses["is_resident"] == "yes":
            if (maximum_year - int(stored_responses["birth_year"])) == 18:
                if (int(valued_months[stored_responses["birth_month"]]) - 9) <= 0:
                    if int(stored_responses["birth_day"]) <= 27:
                        print("You are eligible to vote.")
                        exit()
            elif (maximum_year - int(stored_responses["birth_year"])) > 18:
                print("You are eligible to vote.")
                exit()
        
    print("You are not eligible to vote.")
    exit()
    
# Initialize function
def initialize():
    askQuestions()
    validateBirth()
    voterEligibilityCheck()

# Initialize program
initialize()