
prices = {
    "кола": 200,
    "липтон": 180,
    "фанта": 150,
    "вода": 100,
    "твикс": 80,
    "баунти": 85,
    "кит-кат": 70,
    "круассан": 50
}


# Получаем выбор от клиента
while True:
    prod = input("Выберите напиток или снек: (кола/липтон/фанта/вода/твикс/кит-кат/баунти/круассан): ").lower()

    # Проверяем, есть ли такой продукт в наличии
    if prod not in prices:
        print("Ой, кажется такого у нас нет :(")
    else:
        break

# Получаем внесенную сумму
while True:
    amount = int(input("Стоимость: " + str(prices[prod]) + " рублей. Внесите необходимую сумму: "))

    if amount == prices[prod]:
        print("Все верно! Приятного аппетита!")
        break

    elif amount > prices[prod]:
        change = amount - prices[prod]
        print("Вы внесли больше, чем нужно. Ваша сдача:" + str(change) + " рублей")
        print("Приятного аппетита!")
        break

    elif amount < prices[prod]:
        needed = prices[prod] - amount
        print("Недостаточно средств. Необходимо добавить: " + (needed) + "рублей")
