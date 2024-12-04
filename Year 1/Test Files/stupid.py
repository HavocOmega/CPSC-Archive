def customSplit(desired_string, splitChar=" "):
    words = []
    word = ""
    for i in range(len(desired_string)):
        if desired_string[i] != splitChar:
            word = word + desired_string[i]
            if i+1 == len(desired_string):
                words.append(word)
                word = ""
        else:
            words.append(word)
            word = ""
    return words

print(customSplit(input("Sentence: ")))