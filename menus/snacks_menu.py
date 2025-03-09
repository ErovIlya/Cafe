from models.cafe import Cafe
from models.menu_item import MenuItem
from utils.display_utils import print_table, print_error


def print_snacks_menu():
    print("\nМеню 'Закуски':")
    print("1) Добавить 'Закуску'")
    print("2) Удалить 'Закуску'")
    print("3) Ввести акцию на Закуску")
    print("4) Снять скидку с Закуски")
    print("5) Список закусок")
    print("0) Назад")


def handle_snacks_menu(cafe: Cafe):
    while True:
        print_snacks_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            name = input("Введите название закуски: ").strip().lower()
            price = float(input("Введите цену закуски: "))
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
            new_item = MenuItem(name, price, "закуска", ingredients)
            cafe.add_menu_item(new_item)
            print("Закуска добавлена!")

        elif choice == "2":
            print("\nСписок закусок:")
            headers = ["№", "Название", "Цена", "Скидка", "С учётом скидки", "Доступно"]
            rows = []
            for i, item in enumerate(cafe.menu, start=1):
                if item.category == "закуска":
                    available = True
                    for ingredient, required_quantity in item.ingredients.items():
                        inventory_item = next((inv for inv in cafe.inventory if inv.name.lower() == ingredient.lower()),
                                              None)
                        if not inventory_item or inventory_item.quantity < required_quantity:
                            available = False
                            break
                    price_with_discount = item.price * (1 - item.discount / 100)
                    rows.append([i, item.name, item.price, f"{item.discount}%", f"{price_with_discount:.2f}",
                                 "Да" if available else "Нет"])
            print_table(headers, rows)

            try:
                item_number = int(input("Введите номер закуски для удаления: "))
                if 1 <= item_number <= len(cafe.menu):
                    item_to_remove = cafe.menu[item_number - 1]
                    if item_to_remove.category == "закуска":
                        cafe.remove_menu_item(item_to_remove.name)
                        print(f"Закуска '{item_to_remove.name}' удалена.")
                    else:
                        print_error("Выбранный объект не является закуской.")
                else:
                    print_error("Неверный номер закуски.")
            except ValueError:
                print_error("Введите корректный номер.")

        elif choice == "3":
            print("\nСписок закусок без скидки:")
            snacks_without_discount = [item for item in cafe.menu if item.category == "закуска" and item.discount == 0]
            if not snacks_without_discount:
                print("Нет закусок без скидки.")
            else:
                for i, item in enumerate(snacks_without_discount, start=1):
                    print(f"{i}) {item.name} - {item.price} руб.")
                try:
                    selected_index = int(input("Введите номер закуски для акции: ")) - 1
                    if 0 <= selected_index < len(snacks_without_discount):
                        discount = float(input("Введите размер скидки (в процентах): "))
                        snacks_without_discount[selected_index].apply_discount(discount)
                        print(f"Скидка {discount}% применена к закуске '{snacks_without_discount[selected_index].name}'.")
                    else:
                        print_error("Неверный номер закуски.")
                except ValueError:
                    print_error("Введите корректный номер.")

        elif choice == "4":
            print("\nСписок закусок со скидкой:")
            snacks_with_discount = [item for item in cafe.menu if item.category == "закуска" and item.discount > 0]
            if not snacks_with_discount:
                print("Нет закусок со скидкой.")
            else:
                for i, item in enumerate(snacks_with_discount, start=1):
                    print(f"{i}) {item.name} - {item.price} руб. (скидка {item.discount}%)")
                try:
                    selected_index = int(input("Введите номер закуски для снятия скидки: ")) - 1
                    if 0 <= selected_index < len(snacks_with_discount):
                        snacks_with_discount[selected_index].apply_discount(0)
                        print(f"Скидка снята с закуски '{snacks_with_discount[selected_index].name}'.")
                    else:
                        print_error("Неверный номер закуски.")
                except ValueError:
                    print_error("Введите корректный номер.")

        elif choice == "5":
            print("\nСписок закусок:")
            headers = ["Название", "Цена", "Скидка", "С учётом скидки", "Доступно"]
            rows = []
            for item in cafe.menu:
                if item.category == "закуска":
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
