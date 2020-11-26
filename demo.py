i = 0
j = 15 / 5
j2 = 15 / j
my_list = []
i2 = 0
while i < j:

    while i2 < j2:
        my_list.append('*')
        i2 += 1
    print(str(''.join(my_list)))
    i += 1
