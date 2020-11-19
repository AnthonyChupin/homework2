"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
 При этом английские числительные должны 
 заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""
f_obj = open('05_4.txt', encoding='utf-8')
n_obj = open('05_41.txt', 'w', encoding='utf-8')
my_dict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}
txt = ''
for line in f_obj:
    txt = my_dict.get(line.split(' ')[0]) + line.split(' ')[1] + line.split(' ')[2]
    n_obj.write(''.join(txt))
f_obj.close()
n_obj.close()