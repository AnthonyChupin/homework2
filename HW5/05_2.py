"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

f_obj = open('05_2.txt', encoding='utf-8')

i = 0
for line in f_obj:
    print(line.split(' '))
    print(len(line.split(' ')))
    i += 1

f_obj.close()
print('Kolichestvo strok ', i)


