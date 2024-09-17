#Shitty ass implementation tbh
"""
finalSum = 0
lastTerm = 0
currentTerm = 1

while True:
    result = currentTerm + lastTerm
    lastTerm = currentTerm
    currentTerm = result
    print(currentTerm)
    if result % 2 == 0:
        finalSum += result
    if currentTerm > (4000000):
        break
        
print(finalSum)
"""

#Improved and more efficient and compact
finalSum = 0
lastTerm = 0
currentTerm = 1
while currentTerm < (4000000):
    result = currentTerm + lastTerm
    if result % 2 == 0:
        finalSum += result
    lastTerm = currentTerm
    currentTerm = result
print(finalSum)