def my_func(el1, el_2):
    try:
        return el1 / el_2
    except ZeroDivisionError:
        print("На ноль делить нельзя")


print(my_func(4, 2))