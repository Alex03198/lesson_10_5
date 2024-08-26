from multiprocessing import Pool
from time import sleep
from time import perf_counter


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
    start = perf_counter()
    for file in filenames:
        read_info(file)
    finish = perf_counter()
    print(f'Линейный вызов: {finish - start}')
# Многопроцессный
    start = perf_counter()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    finish = perf_counter()
    print(f'Многопроцессный вызов: {finish - start}')