import json

FILE_NAME = "expenses.json"
expenses = []

def load_data():
    global expenses
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)

def add_expense():
    name = input("Название покупки: ")
    category = input("Категория: ")
    price = float(input("Стоимость: "))
    date = input("Дата (дд-мм-гггг): ")

    expense = {
        "name": name,
        "category": category,
        "price": price,
        "date": date
    }

    expenses.append(expense)
    print("Покупка добавлена")

def show_all():
    if not expenses:
        print("Список пуст")
        return

    for i, e in enumerate(expenses, 1):
        print(f'''{i}. {e['name']} 
              | {e['category']} 
              | {e['price']} 
              | {e['date']}''')


def filter_by_date_category():
    date = input("Введите дату (или Enter для пропуска): ")
    category = input("Введите категорию (или Enter для пропуска): ")

    result = expenses

    if date:
        result = [e for e in result if e["date"] == date]
    if category:
        result = [e for e in result if e["category"] == category]

    for e in result:
        print(e)


def sort_by_price():
    choice = input("1 — по возрастанию, 2 — по убыванию: ")

    reverse = choice == "2"
    sorted_list = sorted(
                            expenses, 
                            key=lambda x: x["price"], 
                            reverse=reverse
                        )

    for e in sorted_list:
        print(e)


def delete_expense():
    show_all()
    index = int(input("Введите номер записи для удаления: ")) - 1

    if 0 <= index < len(expenses):
        del expenses[index]
        print("Запись удалена")
    else:
        print("Ошибка")


def menu():
    while True:
        print("\n--- Меню ---")
        print("1. Добавить покупку")
        print("2. Просмотреть все покупки")
        print("3. Фильтр по дате и категории")
        print("4. Сортировка по стоимости")
        print("5. Удалить запись")
        print("6. Сохранить данные")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_all()
        elif choice == "3":
            filter_by_date_category()
        elif choice == "4":
            sort_by_price()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            save_data()
            print("Данные сохранены")
        elif choice == "0":
            save_data()
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")


load_data()
menu()
