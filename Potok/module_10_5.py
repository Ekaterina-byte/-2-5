import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


#filenames = [f'./file {number}.txt' for number in range(1, 5)]
filenames = ['file 1.txt', 'file 2.txt','file 3.txt','file 4.txt',]

#линейный вызов
start = datetime.datetime.now()

for filename in filenames:
    read_info(filename)
end = datetime.datetime.now()
print(f'{end-start} - линейный вызов')

    #многопроцессорный вызов
if __name__ == '__main__':
    start_1 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end_1 = datetime.datetime.now()

    print(f'{end_1-start_1} - многопроцессорный вызов')