my_list = list(input("Введите элементы списка: "))
list_1 = my_list

number_of_index=0

for i in range(len(list_1)//2):
    list_1[number_of_index],list_1[number_of_index+ 1]=list_1[number_of_index+ 1],list_1[number_of_index]
    number_of_index += 2
print(list_1)
