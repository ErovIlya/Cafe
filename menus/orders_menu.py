from datetime import datetime

from models.order import Order
from utils.display_utils import print_table, print_error

def print_orders_menu():
    print("\nМеню 'Заказы':")
    print("1) Список заказов за сегодня")
    print("2) Список действующих заказов")
    print("3) Завершить заказ")
    print("4) Принять заказ")
    print("0) Назад")

def handle_orders_menu(cafe):
    while True:
        print_orders_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("\nСписок заказов за сегодня:")
            today_orders = [order for order in cafe.orders if order.created_at.date() == datetime.now().date()]
            headers = ["ID", "Сотрудник", "Заказы", "Статус", "Время создания"]
            rows = [[order.order_id, order.employee_name, order.items, order.status, order.created_at.strftime("%H:%M:%S")] for order in today_orders]
            print_table(headers, rows)

        elif choice == "2":
            print("\nСписок действующих заказов:")
            active_orders = [order for order in cafe.orders if order.status == "open"]
            headers = ["ID", "Сотрудник", "Заказы", "Время создания"]
            rows = [[order.order_id, order.employee_name, order.items, order.created_at.strftime("%H:%M:%S")] for order in active_orders]
            print_table(headers, rows)

        elif choice == "3":
            # Вывод списка действующих заказов
            print("\nСписок действующих заказов:")
            active_orders = [order for order in cafe.orders if order.status == "open"]
            if not active_orders:
                print("Нет действующих заказов.")
                continue

            headers = ["ID", "Сотрудник", "Заказы", "Время создания"]
            rows = [[order.order_id, order.employee_name, order.items, order.created_at.strftime("%H:%M:%S")] for order in active_orders]
            print_table(headers, rows)

            # Ввод ID заказа для завершения
            try:
                order_id = int(input("Введите ID заказа для завершения: "))
                order_to_close = next((order for order in active_orders if order.order_id == order_id), None)
                if order_to_close:
                    # Вывод подробной информации о заказе
                    print("\nПодробная информация о заказе:")
                    print(f"ID заказа: {order_to_close.order_id}")
                    print(f"Сотрудник: {order_to_close.employee_name}")
                    print("Заказы:")
                    for item, quantity in order_to_close.items.items():
                        print(f"- {item}: {quantity} шт.")
                    print(f"Время создания: {order_to_close.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

                    # Запрос подтверждения на завершение заказа
                    confirm = input("Вы уверены, что хотите завершить этот заказ? (да/нет): ").lower()
                    if confirm == "да":
                        order_to_close.status = "closed"
                        print(f"Заказ #{order_id} завершён.")
                    else:
                        print("Завершение заказа отменено.")
                else:
                    print_error("Заказ с таким ID не найден.")
            except ValueError:
                print_error("Введите корректный ID заказа.")

        elif choice == "4":
            accept_order(cafe)

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

def accept_order(cafe):
    # Проверка наличия сотрудников с должностью для принятия заказов
    if not cafe.order_acceptance_position:
        print_error("Должность для принятия заказов не задана.")
        return

    employees_for_orders = [emp for emp in cafe.employees if emp.position == cafe.order_acceptance_position.name]
    if not employees_for_orders:
        print_error("Нет сотрудников с должностью для принятия заказов.")
        return

    # Выбор сотрудника
    print("\nСотрудники для принятия заказов:")
    for i, emp in enumerate(employees_for_orders, start=1):
        print(f"{i}) {emp.name} - {emp.position}")

    try:
        selected_index = int(input("Введите номер сотрудника, который принимает заказ: ")) - 1
        if 0 <= selected_index < len(employees_for_orders):
            employee_name = employees_for_orders[selected_index].name
        else:
            print_error("Неверный номер сотрудника.")
            return
    except ValueError:
        print_error("Введите корректный номер.")
        return

    # Выбор напитков и закусок
    items = {}
    while True:
        print("\nМеню:")
        headers = ["№", "Название", "Цена", "Категория", "Доступно"]
        rows = []
        for i, item in enumerate(cafe.menu, start=1):
            available = True
            for ingredient, required_quantity in item.ingredients.items():
                inventory_item = next((inv for inv in cafe.inventory if inv.name.lower() == ingredient.lower()), None)
                if not inventory_item or inventory_item.quantity < required_quantity:
                    available = False
                    break
            rows.append([i, item.name, item.price, item.category, "Да" if available else "Нет"])
        print_table(headers, rows)

        try:
            item_number = int(input("Введите номер напитка или закуски (или 0 для завершения): "))
            if item_number == 0:
                break
            elif 1 <= item_number <= len(cafe.menu):
                menu_item = cafe.menu[item_number - 1]
                # Проверка наличия ингредиентов
                missing_ingredients = []
                for ingredient, required_quantity in menu_item.ingredients.items():
                    inventory_item = next((inv for inv in cafe.inventory if inv.name.lower() == ingredient.lower()), None)
                    if not inventory_item or inventory_item.quantity < required_quantity:
                        missing_ingredients.append(ingredient)

                if missing_ingredients:
                    print_error(f"Недостаточно ингредиентов: {', '.join(missing_ingredients)}")
                    continue

                quantity = int(input("Введите количество: "))
                if quantity <= 0:
                    print_error("Количество должно быть больше 0.")
                    continue

                # Проверка наличия ингредиентов с учетом количества
                for ingredient, required_quantity in menu_item.ingredients.items():
                    inventory_item = next(inv for inv in cafe.inventory if inv.name.lower() == ingredient.lower())
                    if inventory_item.quantity < required_quantity * quantity:
                        print_error(f"Недостаточно ингредиента '{ingredient}' на складе.")
                        break
                else:
                    items[menu_item.name] = quantity
            else:
                print_error("Неверный номер позиции.")
        except ValueError:
            print_error("Введите корректный номер.")

    if not items:
        print_error("Заказ не может быть пустым.")
        return

    # Подтверждение заказа
    print("\nИтоговый заказ:")
    headers = ["Название", "Количество"]
    rows = [[item, quantity] for item, quantity in items.items()]
    print_table(headers, rows)

    total = sum(menu_item.price * quantity for menu_item in cafe.menu for item, quantity in items.items() if menu_item.name == item)
    print(f"Итоговая сумма: {total} руб.")

    confirm = input("Подтвердить заказ? (да/нет): ").lower()
    if confirm != "да":
        print("Заказ отменён.")
        return

    # Создание заказа и списание ингредиентов
    order_id = len(cafe.orders) + 1
    new_order = Order(order_id, employee_name, items)
    cafe.orders.append(new_order)

    for item_name, quantity in items.items():
        menu_item = next(item for item in cafe.menu if item.name == item_name)
        for ingredient, required_quantity in menu_item.ingredients.items():
            inventory_item = next(inv for inv in cafe.inventory if inv.name.lower() == ingredient.lower())
            inventory_item.quantity -= required_quantity * quantity

    print(f"Заказ #{order_id} принят.")