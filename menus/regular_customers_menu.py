from utils.display_utils import print_table

def print_regular_customers_menu():
    print("\nМеню 'Постоянные клиенты':")
    print("1) Просмотр списка постоянных клиентов")
    print("2) Анализ данных клиентов")
    print("0) Назад")


def view_regular_customers(cafe):
    """Функция для просмотра списка постоянных клиентов."""
    if not cafe.regular_customers:
        print("Нет постоянных клиентов.")
        return

    print("\nСписок постоянных клиентов:")
    headers = ["Имя", "Общая сумма", "Последний визит", "Заказов", "Напитков", "Закусок"]
    rows = []
    for client in cafe.regular_customers:
        rows.append([
            client["name"],
            f"{client['total_spent']} руб.",
            client["last_visit_date"],
            client["total_orders"],
            client["drinks_ordered"],
            client["snacks_ordered"]
        ])
    print_table(headers, rows)


def analyze_regular_customers(cafe):
    """Функция для анализа данных постоянных клиентов."""
    if not cafe.regular_customers:
        print("Нет постоянных клиентов.")
        return

    total_clients = len(cafe.regular_customers)
    total_spent = sum(client["total_spent"] for client in cafe.regular_customers)
    average_spent = total_spent / total_clients if total_clients > 0 else 0

    print("\nАнализ данных постоянных клиентов:")
    print(f"Общее количество клиентов: {total_clients}")
    print(f"Общая сумма потраченных средств: {total_spent} руб.")
    print(f"Средний чек: {average_spent:.2f} руб.")


def handle_regular_customers_menu(cafe):
    """Основная функция для работы с меню постоянных клиентов."""
    while True:
        print_regular_customers_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            view_regular_customers(cafe)
        elif choice == "2":
            analyze_regular_customers(cafe)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
