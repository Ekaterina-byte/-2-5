class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors < other.number_of_floors and self.number_of_floors == other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors > other.number_of_floors and self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors < other.number_of_floors and self.number_of_floors > other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __str__(self):
        return f'Название:  {self.name}, кол-во этажей: {self.number_of_floors}'

    def __radd__(self, value):
        self.number_of_floors += value
        return self.__add__()

    def __iadd__(self,value):
        self.number_of_floors += value
        return self.__add__()


h1 = House("ЖК Горский", 18)
h2 = House("Домик в деревне", 2)

print(h1.__str__())  # первоначальное значение
print(h2.__str__()) # первоначальное значение

print(h1==h2) #eq
print(h1<h2) #lt
print(h1>h2) #le
print(h1>h2) #gt
print(h1<h2) #ge
print(h1>h2) #ne
h1.__add__(10) #add
print(h1.__str__())
h1.__add__(10) #radd
print(h1.__str__())
h2.__add__(10) #iadd
print(h2.__str__())

