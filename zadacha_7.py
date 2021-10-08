import itertools
from math import factorial


def fact():
    for i in itertools.count(1):
        yield factorial(i)


try:
    n = int(input("Введите число факториал которого нужно посчитать: "))
    count = 1
    for el in fact():
        if count > n:
            break
        count += 1
        print(el)
except ValueError:
    print("Программа принимает только числа")
