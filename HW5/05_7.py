import json

firm_dict = {}
average_profit = []
with open('05_7.txt', encoding='utf-8') as f:
    lines = f.readline()
    for line in lines:
        name, form, revenue, costs = line.split() #не могу понять (not enough values to unpack) почему он говорит, что у меня меньше значений в строке, чем переменных
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            average_profit.append(profit)
average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'average_profit': average_profit}]

with open('05_7.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('05_7.json') as f_json:
    print(json.load(f_json))