with open('file_number_two.txt', 'r', encoding='utf-8') as new_file:
    number_of_lines = 0
    number_of_letter = 0
    for lines in new_file:
        number_of_lines += 1
        for letters in lines:
            if letters != ',' and letters != ' ' and letters != "\n":
                number_of_letter += 1
    print(f"Количество строчек: {number_of_letter}\nКоличество букв: {number_of_lines}")
