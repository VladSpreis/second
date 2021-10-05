#первый способ
def my_func_1(x, y):
    if x > 0 and y < 0:
        return x ** y


#второй способ

def my_func_2(a, b):
    if b < 0:
        result = 1
        for i in range(0, -b):
            result *= a

        return 1 / result


t = my_func_2(2, -3)
print(t)


