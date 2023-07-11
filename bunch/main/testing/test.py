class person:
    age = 10
    def __init__(self, name):
        self.name = name
    
bob = person("bob")
sally = person("sally")

print(bob.age, sally.age)

bob.age = 13

print(bob.age, sally.age)