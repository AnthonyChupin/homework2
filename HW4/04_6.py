from itertools import count, cycle
x = int(input('startovoe chislo '))
y = int(input('shag '))
z = int(input('konechnoe chislo '))
for i in count(start=x, step=y):
    print(i)
    if i >= z:
        break

colors = ['green', 'yellow', 'red', 'yellow']
for color in cycle(colors):
    q = input('Dlya zaversheniya vvedite q ')
    if q.upper() == 'q':
        break
    else:
        print(color)

