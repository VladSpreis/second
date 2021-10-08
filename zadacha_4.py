my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_gen = (el for el in my_list if my_list.count(el) == 1)

my_dict = {}
counter = 0
index = 0
for i in my_list:  # программа будет показывать какое количество (цифрами) элементов находится в данном списке
    my_dict[my_list[index]] = i
    for j in my_list:
        if i == j:
            counter += 1
    my_dict[i] = counter
    index += 1
    counter = 0
print(my_dict)  # {2: 4, 7: 2, 23: 1, 1: 1, 44: 2, 3: 1, 10: 1, 4: 1, 11: 1}
new_list = []
for t in my_dict.keys():
    if my_dict[t] == 1:
        new_list.append(t)
print(*new_list)  # 23 1 3 10 4 11


