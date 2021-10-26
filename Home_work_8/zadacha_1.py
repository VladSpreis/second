class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []
        for i in date.split("-"):
            my_date.append(int(i))
        return my_date[0], my_date[1], my_date[2]

    @staticmethod
    def valid(day, month):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                return f'Проверка проведена! Никаких ошибок не обнаружено!'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.date)}'


today = Data('14-1-1993')
print(today)
print(Data.valid(11, 11))
print(today.valid(11, 13))
print(Data.extract('23-6-2075'))
print(today.extract('11-11-2020'))
print(Data.valid(1, 11))



