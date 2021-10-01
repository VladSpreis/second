goods=[(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
list_1= []#сюда складываются значения из словаря в первом кортеже
list_2 =[]#сюда складываются значения из словаря  второго кортежа
list_3 =[]#сюда складываются значения из словаря в третьего кортежа
title = []#0
price=[]#1
number= []#2
unit=[]
main_dict=''
for i in range(0,1):
    for j in list(goods[0]):
        if type(j) == dict:
            dict_1 = j
            main_dict=j
            for k in dict_1.values():
                first_value = k
                list_1.append(first_value)
                unit.append(list_1[-1])
title.append(list_1[0])
price.append(list_1[1])
number.append(list_1[2])

for p in range(0,1):
    for f in list(goods[1]):
        if type(f) == dict:
            dict_2 = f
            for y in dict_2.values():
                second_value = y
                list_2.append(second_value)
title.append(list_2[0])
price.append(list_2[1])
number.append(list_2[2])


for t in range(0,1):
    for x in list(goods[2]):
        if type(x) == dict:
            dict_3 = x
            for y in dict_3.values():
                third_value = y
                list_3.append(third_value)
title.append(list_3[0])
price.append(list_3[1])
number.append(list_3[2])
main_dict["название"] = title
main_dict["цена"] = price
main_dict["количество"] =number
print(main_dict)







