class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

h1 = House("ЖК Горский", 18)
print(House.houses_history)
h2 = House("Домик в деревне", 2)
print(House.houses_history)
h3 = House("ЖК Птицино", 5)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
