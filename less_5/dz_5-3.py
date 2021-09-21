# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников.

work_20 = []
all_work = 0
total = 0
with open('dz_5-3.txt') as f_o:
    for line in f_o:
        all_work += 1
        worker = line.split()
        worker_wage = float(worker[1])
        total += worker_wage
        if worker_wage < 20000:
            work_20.append(worker[0])
print(f'Средняя зп - {total/all_work:.2f}')
print(f'Сотрудники с зп менее 20000 - {work_20}')