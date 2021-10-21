from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def sum(self):
        pass

    def __add__(self, other):
        main_sum = self.sum() + other.sum()
        self.main_sum = main_sum
        return self.main_sum

    def __str__(self):
        return f"Общий расход ткани: {self.main_sum}"


class Coat(Clothes, ABC):
    def __init__(self, size: (float, int)):
        self.size = size

    def sum(self):
        return self.size * 2 + 0.3

    def __str__(self):
        return f'Размер пальто: {self.size}.\nРасход ткани: {self.sum()}.'


class Suit(Clothes, ABC):
    def __init__(self, height: (float, int)):
        self.height = height

    def sum(self):
        return self.height / 6.5 + 0.5

    def __str__(self):
        return f"Рост костюма: {self.height}.\nРасход ткани: {self.sum()}."


coat = Coat(4)
coat.sum()
print(coat)
suit = Suit(4)
suit.sum()
print(suit)
summa = coat + suit
print(summa)
