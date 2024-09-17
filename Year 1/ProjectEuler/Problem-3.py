def IsPrime(value):
    for i in range(value):
        if i == 0:
            continue
        if i != 1 and i != value and value % i == 0:
            return False
    return True
    
largestPrimeFactor = 0
    
for i in range(600851475):
    if i == 0:
        continue
    if 600851475 % i == 0:
        if IsPrime(i) and i > largestPrimeFactor:
                largestPrimeFactor = i
print(largestPrimeFactor)
