my_list = [7, 5, 3, 3, 2]
request = input('Vvedite ')
for index, number in enumerate(my_list):
    if int(request) < int(number):
        continue
    my_list.insert(index, request)
    break
else:
    my_list.append(request)
print(my_list)