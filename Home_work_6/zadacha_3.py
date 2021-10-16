class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self, ):
        print(f"Имя сотрудника: {self.surname + ' ' + self.name} ")

    def get_total_income(self):
        print(f"Доход составляет:{self._income['wage'] + self._income['bonus']} долларов")


position = Position("John", "Smith", "developer", 4, 6)
position.get_full_name()
position.get_total_income()
