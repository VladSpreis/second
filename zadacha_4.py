number_of_lines= input("Введите несколько слов:").split(" ")
number = 1
for i in number_of_lines:
    if len(str(i)) > 10:
        print(f"{number}){i}")
        number += 1
    else:
        print(f"{number}){i[:10]}")


