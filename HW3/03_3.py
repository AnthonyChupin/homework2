def my_func(num_1, num_2, num_3):
    list = [num_1, num_2, num_3]
    list.sort()
    print(list[1] + list[2])

num_1 = int(input("Vvedite chislo 1: "))
num_2 = int(input("Vvedite chislo 2: "))
num_3 = int(input("Vvedite chislo 3: "))
my_func(num_1, num_2, num_3)
