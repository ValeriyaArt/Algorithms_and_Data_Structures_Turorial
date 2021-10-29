# загрузка библиотек
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()
# чтение данных из файла

input_file = open('input.txt', 'r')
n, numbers = input_file.readlines()
n = int(n)
numbers = list(map(int, numbers.split(',')))
input_file.close()
# основная функция


def insertion_sort(n, numbers):
    """
    Функция сортировки вставкой по возрастанию
    :param n: количество чисел в массиве
    :param numbers: массив чисел
    :return: отсортированный массив
    """
    for j in range(1, n):
        key = numbers[j]
        i = j - 1
        while i >= 0 and numbers[i] >= key:
            numbers[i + 1] = numbers[i]
            i = i - 1
        numbers[i + 1] = key
    return numbers
# вызов функции

sorted_numbers = insertion_sort(n, numbers)

# запись результата в файл
output_file = open('output.txt', 'w')
sorted_numbers_str = list(map(str, sorted_numbers))
output_file.write(' '.join(sorted_numbers_str))
output_file.close()

# вывод времени работы алгоритма и затраченной памяти

print("Время работы алгоритма ", (time.perf_counter() - t_start), "секунд")
print("Текущий объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[0]/2**20, "MB")
print("Пиковый объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[1]/2**20, "MB")
