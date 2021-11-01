# загрузка библиотек
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()
# чтение данных из файла

input_file_normal = open('input_normal.txt', 'r')
n_normal, normal_list = input_file_normal.readlines()
n_normal = int(n_normal)
normal_list = list(map(int, normal_list.split(' ')))
input_file_normal.close()

input_file_best = open('input_best.txt', 'r')
n_best, best_list = input_file_best.readlines()
n_best = int(n_best)
best_list = list(map(int, best_list.split(' ')))
input_file_best.close()

input_file_worst = open('input_worst.txt', 'r')
n_worst, worst_list = input_file_worst.readlines()
n_worst = int(n_worst)
worst_list = list(map(int, worst_list.split(' ')))
input_file_worst.close()


# основная функция

def selection_sort(n, array):
    sorted_list = []
    for i in range(n):
        min_element = min(array)
        sorted_list.append(min_element)
        array.remove(min_element)
    return sorted_list


# вызов функции

sorted_normal = selection_sort(n_normal, normal_list)
# запись результата в файл
output_file_normal = open('output_normal.txt', 'w')
output_file_normal.write(' '.join(list(map(str, sorted_normal))))
output_file_normal.close()

print("Время работы алгоритма ", (time.perf_counter() - t_start), "секунд")
print("Текущий объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[0]/2**20, "MB")
print("Пиковый объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[1]/2**20, "MB")

sorted_best = selection_sort(n_best, best_list)

output_file_best = open('output_best.txt', 'w')
output_file_best.write(' '.join(list(map(str, sorted_best))))
output_file_best.close()

print("Время работы алгоритма ", (time.perf_counter() - t_start), "секунд")
print("Текущий объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[0]/2**20, "MB")
print("Пиковый объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[1]/2**20, "MB")

sorted_worst = selection_sort(n_worst, worst_list)

output_file_worst = open('output_worst.txt', 'w')
output_file_worst.write(' '.join(list(map(str, sorted_worst))))
output_file_worst.close()

# вывод времени работы алгоритма и затраченной памяти

print("Время работы алгоритма ", (time.perf_counter() - t_start), "секунд")
print("Текущий объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[0]/2**20, "MB")
print("Пиковый объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[1]/2**20, "MB")
