def fullword(sentence, word):
    words = sentence.split()
    if word in words:
        return True
    return False

print(fullword(input("Sentence: "), input("Word: ")))