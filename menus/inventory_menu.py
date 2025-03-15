from models.cafe import Cafe
from models.inventory_item import InventoryItem
from utils.display_utils import print_table, print_error


def print_inventory_menu():
    print("\nМеню инвентаря:")
    print("1) Просмотреть инвентарь")
    print("2) Добавить ингредиент")
    print("3) Списать ингредиент")
    print("0) Назад")


def handle_inventory_menu(cafe: Cafe):
    while True:
        print_inventory_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("\nИнвентарь:")
            headers = ["Название", "Количество"]
            rows = [[item.name, item.quantity] for item in cafe.inventory]
            print_table(headers, rows)

        elif choice == "2":
            name = input("Введите название ингредиента: ").strip().lower()
            quantity = int(input("Введите количество: "))
            # Проверка, существует ли уже такой ингредиент
            existing_item = None
            for inv in cafe.inventory:
                if inv.name.lower() == name:
                    existing_item = inv
                    break

            if existing_item:
                existing_item.add_quantity(quantity)
                print(f"Количество ингредиента '{name}' увеличено на {quantity}.")
            else:
                cafe.inventory.append(InventoryItem(name, quantity))
                print(f"Ингредиент '{name}' добавлен!")

        elif choice == "3":
            name = input("Введите название ингредиента для списания: ").strip().lower()
            amount = int(input("Введите количество для списания: "))
            for item in cafe.inventory:
                if item.name.lower() == name:
                    try:
                        item.subtract_quantity(amount)
                        print(f"Списано {amount} ингредиента '{name}'.")
                    except ValueError as e:
                        print_error(str(e))
                    break
            else:
                print_error(f"Ингредиент '{name}' не найден.")

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")
