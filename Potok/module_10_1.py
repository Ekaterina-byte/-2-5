import time
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name): #word_count - количество записываемых слов,
                                        # file_name - название файла, куда будут записываться слова
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i+1}\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start_1 = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_1 = datetime.now()
time_res_1 = time_end_1-time_start_1
print(f'Работа потоков {time_res_1}')

time_start_2 = datetime.now()

write_words_1 = Thread(target=write_words, args=(10, 'example5.txt'))
write_words_2 = Thread(target=write_words, args=(30, 'example6.txt'))
write_words_3 = Thread(target=write_words, args=(200, 'example7.txt'))
write_words_4 = Thread(target=write_words, args=(100, 'example8.txt'))

write_words_1.start()
write_words_2.start()
write_words_3.start()
write_words_4.start()

write_words_1.join()
write_words_2.join()
write_words_3.join()
write_words_4.join()

time_end_2 = datetime.now()
time_res_2 = time_end_2-time_start_2
print(f'Работа потоков {time_res_2}')

print(f'Вывод разницы начала и конца работы потоков. Потоки работают быстрее функций на {time_res_2-time_res_1} секунд')