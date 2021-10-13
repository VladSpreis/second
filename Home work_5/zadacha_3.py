with open("file_number_three.txt", "r", encoding='utf-8') as new_file:
    sal = []
    poor = []
    my_list = new_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
    print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')
