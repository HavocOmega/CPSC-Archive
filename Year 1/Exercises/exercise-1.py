def quadFormula(a: float, b: float, c:float):
    d = b**2 - 4*a*c
    if d < 0:
        print("There are no real solutions for this equation.")
        exit()
    else:
        return (-b + (d**0.5)) / (2*a), (-b - (d**0.5)) / (2*a)

a = float(input("Input the value for a: "))
b = float(input("Input the value for b: "))
c = float(input("Input the value for c: "))

x1, x2 = quadFormula(a,b,c)
print(f"The roots of this equation are x1: {x1} and x2: {x2}")