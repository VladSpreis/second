from functools import reduce

my_gen = (el for el in range(100, 1001))


def my_func(elem_1, elem_2):
    return elem_1 * elem_2


print(reduce(my_func, my_gen))
