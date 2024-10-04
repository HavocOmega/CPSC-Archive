"""def IsPrime(value):
    for i in range(value):
        if i == 0:
            continue
        if i != 1 and i != value and value % i == 0:
            return False
    return True
    print(value + " is prime")
    
largestPrimeFactor = 0
    
for i in range(600851475):
    if i == 0:
        continue
    if 600851475 % i == 0:
        if IsPrime(i) and i > largestPrimeFactor:
           largestPrimeFactor = i
           print("New Largest Prime Factor: " + str(largestPrimeFactor))
print(largestPrimeFactor)"""


"""for i in range(int(600851475143 / 2)):
    if i == 0:
        continue
    if 600851475143 % i == 0:
        print("Facter found: "+str(i))"""
        
def largestPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
    
lpf = largestPrimeFactor(600851475143)
print(str(lpf))