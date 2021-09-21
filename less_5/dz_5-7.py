# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
import json

average_profit = 0
count = 0
firm_prof = {}
aver_prof = {}
result = []

with open('dz_5-7.txt', 'r', encoding='UTF-8') as f_o:
    for line in f_o:
        info_firm = line.split()
        profit = int(info_firm[2]) - int(info_firm[3])
        if profit > 0:
            firm_prof[info_firm[0]] = profit
            average_profit += profit
            count += 1
        else:
            firm_prof[info_firm[0]] = abs(profit)
    aver_prof['average_profit'] = f'{average_profit/count:.2f}'
    result = [firm_prof, aver_prof]

with open('dz-5_7.json', 'w') as f_j:
    result = json.dump(result,f_j)
