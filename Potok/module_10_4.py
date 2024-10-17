import threading
from threading import Thread, Lock
from random import randint
import time
import queue

class Table:

    def __init__(self, number):
        self.number = number       #Номер стола
        self.guest = None          #Гость за столом number


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name          #Имя гостя

    def run(self):
        time.sleep(randint(3,10))  #Задержка времени от 3до 10 сек

class Cafe:

    def __init__(self, *tables):
        self.queue = queue.Queue()            #Очередь - поток
        self.tables = list(tables)            #Список столов

    def guest_arrival(self, *guests):
        for guest in guests:                  # Каждый гость из списка гостей
            for table in self.tables:         # Каждый стол из списка столов
                if table.guest is None:       # Поиск свободного стола
                    table.guest = guest       # Если есть свободный стол - посетителю присваивается номер стола
                    guest.start()             # Запуск потока посетителя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break                     # Если гость за столом - то выходим из цикла
            else:                             # Если нет свободного стола то
                self.queue.put(guest)         # Гость ставится в очередь в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while self.queue or any(table.guest is not None for table in self.tables):
                                              # Пока очередь self.queue не пуста или один из столов из списка занят
            for table in self.tables:         # Проверяем каждый стол из списка столов
                if table.guest is not None and not table.guest.is_alive():  # Если стол занят и поток table.guest завершен
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    table.guest = None        # Стол свободен
                    print(f"Стол номер {table.number} свободен")
                if table.guest is None and self.queue:  # Если стол свободен и очередь есть,то
                    if self.queue.empty() and any(table.guest is None for table in self.tables):
                                                        # Если очередь пуста и все столы свободны
                        return                          # выходим из функции
                    guest = self.queue.get()            # забираем из списка первого гостя
                    table.guest = guest                 # Гостю присваивается номер стола
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    guest.start()


# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()




