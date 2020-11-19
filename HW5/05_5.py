"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран"""
f_obj = open('05_5.txt', 'w+', encoding='utf-8')
my_str = '10 1 20 49 4'
f_obj.write(''.join(my_str))
f_obj.seek(0)
my_list = f_obj.readline().split(' ')
my_sum = 0
for el in my_list:
    my_sum += int(el)
print(my_sum)