from models.cafe import Cafe
from models.menu_item import MenuItem
from utils.display_utils import print_table, print_error

def print_drinks_menu():
    print("\nМеню 'Напитки':")
    print("1) Добавить 'Напиток'")
    print("2) Удалить 'Напиток'")
    print("3) Ввести акцию на Напиток")
    print("4) Снять скидку с Напитка")
    print("5) Список напитков")
    print("0) Назад")

def handle_drinks_menu(cafe: Cafe):
    while True:
        print_drinks_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            name = input("Введите название напитка: ").strip().lower()
            price = float(input("Введите цену напитка: "))
            ingredients = {}
            while True:
                ingredient = input("Введите ингредиент (или нажмите Enter для завершения): ").strip().lower()
                if ingredient == "":
                    break
                # Проверка наличия ингредиента
                inventory_item = next((item for item in cafe.inventory if item.name.lower() == ingredient), None)
                if not inventory_item:
                    print_error(f"Ингредиент '{ingredient}' отсутствует на складе. Ввод прекращён.")
                    return  # Прекращаем ввод и возвращаемся в меню
                quantity = int(input("Введите количество: "))
                ingredients[ingredient] = quantity
            new_item = MenuItem(name, price, "напиток", ingredients)
            cafe.add_menu_item(new_item)
            print("Напиток добавлен!")

        elif choice == "2":
            name = input("Введите название напитка для удаления: ").strip().lower()
            cafe.remove_menu_item(name)
            print("Напиток удалён!")

        elif choice == "3":
            print("\nСписок напитков без скидки:")
            drinks_without_discount = [item for item in cafe.menu if item.category == "напиток" and item.discount == 0]
            if not drinks_without_discount:
                print("Нет напитков без скидки.")
            else:
                for i, item in enumerate(drinks_without_discount, start=1):
                    print(f"{i}) {item.name} - {item.price} руб.")
                try:
                    selected_index = int(input("Введите номер напитка для акции: ")) - 1
                    if 0 <= selected_index < len(drinks_without_discount):
                        discount = float(input("Введите размер скидки (в процентах): "))
                        drinks_without_discount[selected_index].apply_discount(discount)
                        print(f"Скидка {discount}% применена к напитку '{drinks_without_discount[selected_index].name}'.")
                    else:
                        print_error("Неверный номер напитка.")
                except ValueError:
                    print_error("Введите корректный номер.")

        elif choice == "4":
            print("\nСписок напитков со скидкой:")
            drinks_with_discount = [item for item in cafe.menu if item.category == "напиток" and item.discount > 0]
            if not drinks_with_discount:
                print("Нет напитков со скидкой.")
            else:
                for i, item in enumerate(drinks_with_discount, start=1):
                    print(f"{i}) {item.name} - {item.price} руб. (скидка {item.discount}%)")
                try:
                    selected_index = int(input("Введите номер напитка для снятия скидки: ")) - 1
                    if 0 <= selected_index < len(drinks_with_discount):
                        drinks_with_discount[selected_index].apply_discount(0)
                        print(f"Скидка снята с напитка '{drinks_with_discount[selected_index].name}'.")
                    else:
                        print_error("Неверный номер напитка.")
                except ValueError:
                    print_error("Введите корректный номер.")

        elif choice == "5":
            print("\nСписок напитков:")
            headers = ["Название", "Цена", "Скидка", "С учётом скидки", "Доступно"]
            rows = []
            for item in cafe.menu:
                if item.category == "напиток":
                    available = True
                    for ingredient, required_quantity in item.ingredients.items():
                        inventory_item = next((inv for inv in cafe.inventory if inv.name.lower() == ingredient.lower()), None)
                        if not inventory_item or inventory_item.quantity < required_quantity:
                            available = False
                            break
                    price_with_discount = item.price * (1 - item.discount / 100)
                    rows.append([item.name, item.price, f"{item.discount}%", f"{price_with_discount:.2f}", "Да" if available else "Нет"])
            print_table(headers, rows)

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")