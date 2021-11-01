import random

random_list = [random.randrange(-10**9, 10**9) for i in range(10**3)]

best_list = random_list.copy()
best_list.sort()

worst_list = random_list.copy()
worst_list.sort(reverse=True)

output_file_normal = open('input_normal.txt', 'w')
output_file_normal.write(str(10**3))
output_file_normal.write('\n')
output_file_normal.write(' '.join(list(map(str, random_list))))
output_file_normal.close()

output_file_best = open('input_best.txt', 'w')
output_file_best.write(str(10**3))
output_file_best.write('\n')
output_file_best.write(' '.join(list(map(str, best_list))))
output_file_best.close()


output_file_worst = open('input_worst.txt', 'w')
output_file_worst.write(str(10**3))
output_file_worst.write('\n')
output_file_worst.write(' '.join(list(map(str, worst_list))))
output_file_worst.close()

