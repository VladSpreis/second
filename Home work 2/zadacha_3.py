number_of_month = int(input("Введите число месяца:"))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if number_of_month == my_list[0] and number_of_month == my_list[1]:
    print("Зима")
elif number_of_month > my_list[1] and number_of_month < my_list[5]:
    print("Весна")
elif number_of_month > my_list[4] and number_of_month < my_list[8]:
    print("Лето")
elif number_of_month > my_list[7] and number_of_month < my_list[11]:
    print("Осень")
elif number_of_month == my_list[11]:
    print("Зима")
elif number_of_month > my_list[11]:
    print(None)


my_dict={"Зима":[12, 1, 2], "Весна":[3, 4, 5], "Лето":[6, 7, 8], "Осень": [9, 10, 11]}
for i in my_dict["Зима"]:
    if number_of_month == i:
        print("Зима")
for j in my_dict["Весна"]:
    if number_of_month == j:
        print("Весна")
for t in my_dict ["Лето"]:
    if number_of_month == t:
        print("Лето")
for f in my_dict["Осень"]:
    if number_of_month == f:
        print("Осень")


