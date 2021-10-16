class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, direction):
        if direction == "left" or direction == "влево":
            print("Машина повернула влево!")
        elif direction == "right" or direction == "вправо":
            print("Машина повернула вправо!")
        else:
            print("Метод не принимает других значений!")

    def show_speed(self):
        print(f"Машина едет со скоростью: {self.speed} км/ч")


class Towncar(Car):
    is_police = False
    intended = "Передвижение по городу"
    max_speed = "120 км/ч"

    def __init__(self, speed, color, name, ):
        super().__init__(speed, color, name)
        print(f"{color} {name}")

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Машина превысила скорость!")


class Sportcar(Car):
    is_police = False
    intended = " Предназначена для спортивных соревнований"
    max_speed = "320 км/ч"

    def __init__(self, speed, color, name, ):
        super().__init__(speed, color, name)
        print(f"{color} {name}")


class Workcar(Car):
    is_police = False
    intended = " Предназначена для строительных работ"
    max_speed = "50 км/ч"

    def __init__(self, speed, color, name, ):
        super().__init__(speed, color, name, )
        print(f"{color} {name}")

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Машина превысила скорость!")


class PoliceCar(Car):
    intended = " Предназначена для охраны правопорядка"
    max_speed = "180 км/ч"
    is_police = True

    def __init__(self, speed, color, name, ):
        super().__init__(speed, color, name, )
        print(f"{color} {name}")


auto_1 = Towncar(70, "red", " Mercedes")
auto_1.go()
auto_1.turn('left')
auto_1.show_speed()
