# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dict= {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('dz_5-4.txt') as f_o:
    lines = f_o.readlines()

with open('dz_5-4-1.txt', 'w', encoding='UTF-8') as f_o:
    for line in lines:
        str = line.split()
        str[0] = dict[str[0]]
        f_o.write(' '.join(str)+'\n')