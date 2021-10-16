class Road:
    lenght = None
    width = None

    def __init__(self, lenght: int, width: int):
        self._lenght = lenght
        self._width = width

    def mass_calculation(self, tickness: int, mass: int, ):
        print(f"Масса асфальта: {self._lenght * self._width * tickness *mass} кг")


element = Road(10, 5)
element.mass_calculation(4, 5)
