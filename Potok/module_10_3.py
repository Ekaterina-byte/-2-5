import threading
from threading import Thread, Lock
from random import randint
import time

class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0              #баланс банка изначальный
        self.lock = threading.Lock()  #блокировка потоков


    def deposit (self):
         for i in range(100):
            in_money = randint(50, 500) #случайные числа для пополнения
            self.balance = self.balance + in_money
            print(f'Пополнение: {in_money}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            out_money = randint(50, 500)  #случайные числа для снятие
            print(f'Запрос на {out_money}')
            if out_money <= self.balance:
                self.balance = self.balance - out_money
                print(f'Снятие: {out_money}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()




bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

