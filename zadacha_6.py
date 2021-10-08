from itertools import count
from itertools import count, cycle


def my_func():
    el_1 = int(input('Введите стартовое число: '))
    el_2 = int(input('Введите шаг: '))
    limit = int(input('Введите предел: '))
    for el in count(el_1, el_2):
        if el >= limit:
            break
        print(el)


def my_func_1():
    my_list = [input("Введите несколько элементов: ").split()]
    limit = int(input('Введите предел (число): '))
    counter = 0
    for t in cycle(my_list):
        if counter >= limit:
            break
        counter += 1
        print(t)


my_func_1()


if __name__ == "__main__":
    print("hello")