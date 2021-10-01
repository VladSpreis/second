my_list= [(9, 32, 43,),{"apple":"red","lemon":"orange"},["hello","world"],{1, 2, 3, 4, 5, 6},32.6 ]
#сохраняем данные о типе элемента в переменную
a=type(my_list)
b=type(my_list[0])
c=type(my_list[1])
d= type(my_list[2])
print(a,b,c,d)

# через цикл for:

x = -1#-создаем переменную, куда складываются индексы (от -1 потому что индекс ведется от нуля)
for i in my_list:
    x += 1
    z = type(my_list [x])
    print(z)

