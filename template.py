# загрузка библиотек
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()
# чтение данных из файла

input = open('input.txt', 'r')

input.close()
# основная функция

# вызов функции

# запись результата в файл
output = open('output.txt', 'w')

output.close()

# вывод времени работы алгоритма и затраченной памяти

print("Время работы алгоритма ", (time.perf_counter() - t_start), "секунд")
print("Текущий объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[0]/2**20, "MB")
print("Пиковый объем затрачиваемой памяти на работу алгоритма ", tracemalloc.get_traced_memory()[1]/2**20, "MB")
