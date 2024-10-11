totalSum = 0
i = 0
while i < 5:
    user_input = float(input("Please enter 1 number: "))
    if user_input > 0:
        totalSum += user_input
        i += 1
print(totalSum)