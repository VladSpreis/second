my_list = [int(el) for el in input("Введите числа: ").split()]

my_gen = (my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1])
print(list(my_gen))
