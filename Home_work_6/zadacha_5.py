class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки!")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)
        print(title)

    def draw(self):
        print("Запуск зарисовки ручкой!")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)
        print(title)

    def draw(self):
        print("Запуск зарисовки карандашом!")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)
        print(title)

    def draw(self):
        print("Запуск зарисовки маркером!")


pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карандаш")
pencil.draw()
handle = Handle("Маркер")
handle.draw()
