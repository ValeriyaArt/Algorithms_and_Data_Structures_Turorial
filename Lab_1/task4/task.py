# загрузка библиотек
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()
# чтение данных из файла

input_file = open('input.txt', 'r')
numbers, number_to_find = input_file.readlines()
number_to_find = int(number_to_find)
numbers = list(map(int, numbers.split(' ')))
input_file.close()
# основная функция


def linear_search(array, number):
    """
    Функция линейного поиска числа в массиве
    :param array: массив
    :param number: элемент, который необходимо найти
    :return: количество найденных элементов, индексы найденных элементов
    """
    num_indexes = []
    for i in range(len(array)):
        if array[i] == number:
            num_indexes.append(i)
    if len(num_indexes) == 0:
        return -1, -1
    return len(num_indexes), num_indexes


# вызов функции
count_number, num_indexes = linear_search(numbers, number_to_find)
# запись результата в файл
output_file = open('output.txt', 'w')
if type(num_indexes) == 'list':
    num_indexes_str = list(map(str, num_indexes))
    output_file.write(' '.join(num_indexes_str))
    output_file.write('\n')
    output_file.write(str(count_number))
else:
    output_file.write(str(count_number))
output_file.close()

# вывод времени работы алгоритма и затраченной памяти

print("Время работы алгоритма ", (time.perf_counter() - t_start), "секунд")
print("Текущий объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[0]/2**20, "MB")
print("Пиковый объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[1]/2**20, "MB")
