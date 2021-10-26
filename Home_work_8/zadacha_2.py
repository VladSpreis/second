class MyZeroDivisionError(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


class Number(int):

    def __init__(self, number):
        self.number = number

    def __truediv__(self, other):
        if other == 0:
            raise MyZeroDivisionError

        return self.number / other


n_1 = Number(10)
n_2 = Number(0)
x = n_1 / n_2
print(x)
