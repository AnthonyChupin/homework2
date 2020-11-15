from functools import reduce
def my_f(num_1, num_2):
    return num_1 * num_2
list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(my_f, list))

