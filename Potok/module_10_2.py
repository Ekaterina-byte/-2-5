from threading import Thread
import time

class Knight (Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name                     #имя рыцаря
        self.power = power                   #сила рыцаря
        self.enemy = 100
    def run(self):
        print(f'{self.name}, на нас напали!')
        i = 0                                 #rол-во дней битвы
        while self.enemy > 0:
            self.enemy = self.enemy - self.power
            i += 1
            print(f'{self.name} сражается {i} дней, осталось {self.enemy} воинов')
            time.sleep(1)
            if self.enemy==0:
                print(f'{self.name} одержал победу спустя {i} дней (дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()