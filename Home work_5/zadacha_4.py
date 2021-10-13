from translate import Translator

trans = Translator(from_lang='en', to_lang='ru')
with open('file_number_four.txt', 'r', encoding='utf-8') as new_file:
    list_1 = []
    list_2 = []

    for i in new_file:
        i = i.split('-')
        x = str(i[0])
        y = x[:-1]
        text = trans.translate(y)
        list_1.append(text)

    new_file.seek(0)
    counter = 0
    new_list = []
    for j in new_file:
        j = j.split(' ', 1)
        new_list.append(str(list_1[counter]) + ' ' + j[1])
        counter += 1
    print(new_list)


with open('file_number_four_1.txt', 'w') as new_file_1:
    new_file_1.writelines(new_list)
