def my_func (el_1, el_2, el_3):
    if el_1 > el_3 and el_2 > el_3:
        return el_1 + el_2
    elif el_2 > el_1 and el_3 > el_1:
        return el_2 + el_3
    elif el_1 > el_2 and el_3 > el_2:
        return el_1 + el_3


a = my_func(-100, -5, -1)
print(a)