from itertools import count
from math import factorial


def yie_gen():
    for el in count(1):
        yield factorial(el)


gen = yie_gen()
x = 0
for i in gen:
    if x < 10:
        print(i)
        x += 1
    else:
        break

"""несовсем понял как это работает, решение нашел подсказали"""