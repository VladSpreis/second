class Cage:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cage(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cage(self.count - other.count)
        print(f"{self.count} - {other.count}")

    def __mul__(self, other):
        return Cage(self.count * other.count)

    def __truediv__(self, other):
        return Cage(self.count // other.count)

    def make_order(self, per_row):
        rows, tail = self.count // per_row, self.count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self.count} ячеек"


cage_1 = Cage(12)
print(cage_1)
cage_2 = Cage(15)
print(cage_2)
print((cage_1 * cage_2).make_order(10))