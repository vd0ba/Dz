data_base = []
count = 1

while True:
    name = input('Введите название товара - ')
    price = int(input('Введите стоимость товара - '))
    quantity = int(input('Введите количество товара - '))
    unit = input('Введите единицы измерения - ')
    card_product = (count, {'название': name, 'цена': price, 'количество': quantity, 'eд': unit})
    data_base.append(card_product)
    count += 1

    q = input('Хотите ввести еще товар? (y/n)')
    if q.lower() == 'n':
        break

analitics = {'название': [], 'цена': [], 'количество': [], 'eд': []}
for i,j in data_base:
    analitics['название'].append(j['название'])
    analitics['цена'].append(j['цена'])
    analitics['количество'].append(j['количество'])
    analitics['eд'].append(j['eд'])
print(analitics)
