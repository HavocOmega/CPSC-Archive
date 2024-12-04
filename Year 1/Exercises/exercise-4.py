import random
random.seed(1)

class Guard:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attacked(self, damage):
        self.health = (self.health - damage) >= 0 and self.health - damage or 0

    def get_health(self):
        return self.health

guard1 = Guard("Adam", 15)
guard2 = Guard("Bob", 22)
guard3 = Guard("Cath", 24)
for i in range(10):
    guard1.attacked(random.randint(1, 3))
    guard2.attacked(random.randint(1, 3))
    guard3.attacked(random.randint(1, 3))
    print("Guard 1 health: ", guard1.get_health())
    print("Guard 2 health: ", guard2.get_health())
    print("Guard 3 health: ", guard3.get_health())
    print()
