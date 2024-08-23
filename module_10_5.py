from multiprocessing import Pool
from time import sleep
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f_n:
        while True:
            line = f_n.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
# # Линейный вызов
#    with Pool(4) as pool:
#     start = datetime.now()
#     for file in filenames:
#         read_info(file)
#     end = datetime.now()
#     print(f'Линейный вызов: {end - start}')
# Многопроцессный
    with Pool(4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'Многопроцессный вызов: {end - start}')