a = int(input("Введите любое целое положительное число: "))
b = -1
if a > 10:
    while a > 10:
        c = a % 10
        a //= 10
        if c > b:
            b = c
    print(b)
else:
    print(a)




