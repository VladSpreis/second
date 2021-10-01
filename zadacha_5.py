rating = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2,]
new_element= int(input("Введите новый элемент рейтинга: "))
if rating[0] < new_element:
    rating.insert(0, new_element)
elif rating[9] > new_element:
    rating.append(new_element)
elif new_element < rating[0] and new_element > rating[9]:
    for i in range(len(rating) + 1):
        if rating[i] == new_element:
            rating.insert(i, new_element)
            break
        elif rating[i] == rating[i - 1]:
            rating.insert(i, new_element)
            break
print(rating)

