# Создаем класс телефона
class Phone:
    def __init__(self, name, model, memory, screen_size, release_year, price):
        self.name = name
        self.model = model
        self.memory = memory
        self.screen_size = screen_size
        self.release_year = release_year
        self.price = price


# Создаем список доступных телефонов
phones = [
    Phone("iPhone", "13 Pro", "128GB", "6.1 дюйма", 2021, 79990),
    Phone("Samsung", "Galaxy S23", "256GB", "6.1 дюйма", 2023, 64990),
    Phone("Xiaomi", "13 Pro", "512GB", "6.7 дюйма", 2023, 49990),
    Phone("Honor", "90", "256GB", "6.7 дюйма", 2023, 34990),
]


# Функция для отображения информации о телефоне
def display_phone_info(phone):
    print(f"Название: {phone.name}")
    print(f"Модель: {phone.model}")
    print(f"Память: {phone.memory}")
    print(f"Размер экрана: {phone.screen_size}")
    print(f"Год выпуска: {phone.release_year}")
    print(f"Стоимость: {phone.price} рублей")

print("Добро пожаловать в наш магазин!")
# Основной цикл программы
while True:
    # Показываем список доступных телефонов
    print("\nДоступные модели телефонов:")
    for i, phone in enumerate(phones):
        print(f"{i + 1}. {phone.name} {phone.model}")

    # Получаем выбор пользователя
    try:
        choice = int(input("\nВыберите номер модели: "))
        if 1 <= choice <= len(phones):
            # Показываем информацию о выбранном телефоне
            selected_phone = phones[choice - 1]
            display_phone_info(selected_phone)

            # Спрашиваем о выборе
            response = input("\nПодходит ли вам этот телефон? (да/нет): ").lower()
            if response == "да":
                print("\nХороший выбор, можете пройти на кассу!")
                break
            elif response == "нет":
                print("\nХорошо, давайте посмотрим другие модели.")
            else:
                print("\nПожалуйста, введите 'да' или 'нет'.")
        else:
            print("\nНеверный выбор. Попробуйте снова.")
    except ValueError:
        print("\nПожалуйста, введите число.")
