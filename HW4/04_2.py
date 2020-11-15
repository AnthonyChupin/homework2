my_list =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el-1] < my_list[el]]
print(new_list)