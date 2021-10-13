with open('file_number_six.txt', 'r', encoding='utf-8') as new_file:
    my_dict = {}
    counter = 0
    for i in new_file:
        counter = 0
        el_1, el_2 = i.split(":")
        el_2 = el_2.split()
        for j in el_2:
            if "-" in j:
                continue
            el_3, el_4 = j.split('(')
            counter += int(el_3)
        my_dict[el_1] = counter

    print(my_dict)



