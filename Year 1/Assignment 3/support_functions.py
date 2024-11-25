# Assignment 3
# Written by: Ryll Santillan
# UCID: 30257967


# Greeting function
def get_greetings(name):
    return f"Greetings {name}! I am your virtual assistant Chat231." # Return a string with the name variable embeded into it

# Full word function
def full_word(sentence, word):
    # Get length of the sentence and the word
    sentence_length = len(sentence)
    word_length = len(word)

    # Run through every character in the sentence
    for i in range(sentence_length):
        if sentence[i:i+word_length].lower() == word.lower(): # Check if the characters from the index of "i" plus the word length is equal to the word that's being checked for
            # Check if character before isn't a letter or a digit or if the character is the first character in the sentence
            if (i == 0 or (not sentence[i-1].isalnum())):
                #Check if the characters position plus the word length is equal to the sentence length or if character after isn't a letter or a digit
                if (i+word_length == sentence_length or (not sentence[i+word_length].isalnum())):
                    return True #Return True if all checks are valid
    return False # Default return value if one of the checks is not passed

def get_answer(database, sentence):
    # Get the database list of keywords and their responses
    for word, response in database.items():
        # Check to see if the word is ever mentioned in the sentence
        if full_word(sentence, word):
            return response #Return the corresponding response
    return "Sorry, I do not understand your question." # Default return value if the none of the words match with one in the sentence