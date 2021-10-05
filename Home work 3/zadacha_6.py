def my_func(words):
    if type(words) == str:
        return words.title()
    else:
        return "Эта функция работает только со строками"


def my_func_1():
    my_str = " "
    my_words = input("Введите слова маленькими буквами: ").split(" ")
    for i in my_words:
        my_str += " " + my_func(i)
    print(my_str.strip())

my_func_1()



