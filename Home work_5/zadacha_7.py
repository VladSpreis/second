import json
with open('file_number_seven.txt', 'r', encoding='utf-8') as new_file:
    new_dict = {}
    number_of_costs = 0
    average_prof=0
    for i in new_file:
        company, index, income, cost = i.split()
        x = int(income) - int(cost)
        if x >= 0:
            average_prof += x
            number_of_costs += 1
            new_dict[company] = x

    average_prof /= number_of_costs
with open('json_1.json', 'w', encoding='utf-8') as new_json_file:
    json.dump([new_dict, {'average_prof': average_prof}], new_json_file, )






