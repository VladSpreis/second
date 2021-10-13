with open('file_number_one.txt', 'w') as new_file:
    input_values = input
    while input_values:
        input_values = input("Введите текст: ")
        for i in range(len(input_values)):
            if not input_values:
                break
        new_file.write(f"{input_values}\n")
