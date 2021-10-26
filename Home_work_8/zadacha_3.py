class Errorexception(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


my_list = []
while True:
    input_numbers = input("Введите число для заполнения списка, или 'q' для выхода: ")
    if input_numbers == "q":
        break
    try:
        if not input_numbers.isdigit():
            raise Errorexception(f"'{input_numbers}' не является числом!")
        my_list.append(int(input_numbers))
    except Errorexception as ex:
        print(ex)
print(my_list)
