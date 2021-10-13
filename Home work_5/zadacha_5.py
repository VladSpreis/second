with open('file_number_five.txt', 'w') as new_file:
    try:
        my_list = input
        counter = 0
        while my_list:
            my_list = [int(el) for el in input("Введите числа: ").split()]
            for i in my_list:
                counter += i
                if not my_list:
                    break
            print(counter)
    except ValueError:
        print("Только цифры")
    new_file.write(f"{counter}\n")

