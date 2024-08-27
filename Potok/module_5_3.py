class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return self.number_of_floors == other


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    def __str__(self):
        return f'Название:  {self.name}, кол-во этажей: {self.number_of_floors}'

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self,other:int):
        return self.__add__(other)


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
#h1.__add__(10) #radd
h1 += 10
print(h1.__str__())
h2.__add__(10) #iadd
print(h2.__str__())

