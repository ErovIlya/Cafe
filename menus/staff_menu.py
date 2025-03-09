from models.employee import Employee
from models.position import Position
from utils.display_utils import print_table, print_error


def print_staff_menu():
    print("\nМеню персонала:")
    print("1) Должности")
    print("2) Персонал")
    print("0) Назад")


def handle_staff_menu(cafe):
    while True:
        print_staff_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            handle_positions_menu(cafe)

        elif choice == "2":
            handle_employees_menu(cafe)

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


def print_positions_menu():
    print("\nМеню 'Должности':")
    print("1) Список должностей")
    print("2) Добавить должность")
    print("3) Должность по умолчанию")
    print("4) Зарплата")
    print("5) Должность для принятия заказов")
    print("0) Назад")


def handle_positions_menu(cafe):
    while True:
        print_positions_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("\nСписок должностей:")
            headers = ["Название", "Зарплата по умолчанию"]
            rows = [[pos.name, pos.default_salary] for pos in cafe.positions]
            print_table(headers, rows)

        elif choice == "2":
            name = input("Введите название новой должности: ")
            salary = float(input("Введите зарплату по умолчанию: "))
            new_position = Position(name, salary)
            cafe.positions.append(new_position)
            print(f"Должность '{name}' добавлена с зарплатой {salary} руб.")

        elif choice == "3":
            if not cafe.positions:
                print("Нет доступных должностей.")
            else:
                while True:
                    print("\nСписок доступных должностей:")
                    for i, pos in enumerate(cafe.positions, start=1):
                        print(f"{i}) {pos.name}")
                    print("0) Отмена")

                    try:
                        selected_index = int(input("Введите номер должности по умолчанию (или 0 для отмены): ")) - 1
                        if selected_index == -1:
                            print("Действие отменено.")
                            break
                        elif 0 <= selected_index < len(cafe.positions):
                            cafe.default_position = cafe.positions[selected_index]
                            print(f"Должность по умолчанию изменена на '{cafe.default_position.name}'.")
                            break
                        else:
                            print_error("Неверный номер должности. Попробуйте снова.")
                    except ValueError:
                        print_error("Введите корректный номер.")

        elif choice == "4":
            if not cafe.positions:
                print("Нет доступных должностей.")
            else:
                while True:
                    print("\nСписок доступных должностей:")
                    for i, pos in enumerate(cafe.positions, start=1):
                        print(f"{i}) {pos.name}")
                    print("0) Отмена")

                    try:
                        selected_index = int(input("Введите номер должности для изменения зарплаты (или 0 для отмены): ")) - 1
                        if selected_index == -1:
                            print("Действие отменено.")
                            break
                        elif 0 <= selected_index < len(cafe.positions):
                            new_salary = float(input("Введите новую зарплату: "))
                            cafe.positions[selected_index].default_salary = new_salary
                            print(f"Зарплата для должности '{cafe.positions[selected_index].name}' изменена на {new_salary}.")
                            break
                        else:
                            print_error("Неверный номер должности. Попробуйте снова.")
                    except ValueError:
                        print_error("Введите корректный номер.")

        elif choice == "5":
            if not cafe.positions:
                print("Нет доступных должностей.")
            else:
                while True:
                    print("\nСписок доступных должностей:")
                    for i, pos in enumerate(cafe.positions, start=1):
                        print(f"{i}) {pos.name}")
                    print("0) Отмена")

                    try:
                        selected_index = int(input("Введите номер должности для принятия заказов (или 0 для отмены): ")) - 1
                        if selected_index == -1:
                            print("Действие отменено.")
                            break
                        elif 0 <= selected_index < len(cafe.positions):
                            cafe.order_acceptance_position = cafe.positions[selected_index]
                            print(f"Должность для принятия заказов изменена на '{cafe.order_acceptance_position.name}'.")
                            break
                        else:
                            print_error("Неверный номер должности. Попробуйте снова.")
                    except ValueError:
                        print_error("Введите корректный номер.")

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


def print_employees_menu():
    print("\nМеню 'Персонал':")
    print("1) Список персонала")
    print("2) Добавить сотрудника")
    print("3) Изменить должность сотрудника")
    print("4) Изменить надбавку сотруднику")
    print("5) Уволить сотрудника")
    print("6) Выплата ЗП")
    print("0) Назад")


def handle_employees_menu(cafe):
    while True:
        print_employees_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("\nСписок персонала:")
            headers = ["№", "Имя", "Должность", "Зарплата", "Надбавка"]
            rows = [[i + 1, emp.name, emp.position, emp.salary, emp.bonus] for i, emp in enumerate(cafe.employees)]
            print_table(headers, rows)

        elif choice == "2":
            name = input("Введите имя сотрудника: ")
            position = cafe.default_position.name if cafe.default_position else None
            salary = cafe.default_position.default_salary if cafe.default_position else 0
            cafe.employees.append(Employee(name, position, salary))
            print(f"Сотрудник '{name}' добавлен с должностью '{position if position else 'не задана'}'.")

        elif choice == "3":
            if not cafe.employees:
                print("Нет сотрудников.")
            else:
                print("\nСписок сотрудников:")
                for i, emp in enumerate(cafe.employees, start=1):
                    print(f"{i}) {emp.name} - {emp.position}")
                try:
                    selected_index = int(input("Введите номер сотрудника для изменения должности: ")) - 1
                    if 0 <= selected_index < len(cafe.employees):
                        print("\nСписок доступных должностей:")
                        for i, pos in enumerate(cafe.positions, start=1):
                            print(f"{i}) {pos.name}")
                        try:
                            position_index = int(input("Введите номер новой должности: ")) - 1
                            if 0 <= position_index < len(cafe.positions):
                                new_position = cafe.positions[position_index].name
                                cafe.employees[selected_index].update_position(new_position)
                                print(f"Должность сотрудника '{cafe.employees[selected_index].name}' изменена на '{new_position}'.")
                            else:
                                print_error("Неверный номер должности.")
                        except ValueError:
                            print_error("Введите корректный номер.")
                    else:
                        print_error("Неверный номер сотрудника.")
                except ValueError:
                    print_error("Введите корректный номер.")

        elif choice == "4":
            if not cafe.employees:
                print("Нет сотрудников.")
            else:
                print("\nСписок сотрудников:")
                for i, emp in enumerate(cafe.employees, start=1):
                    print(f"{i}) {emp.name} - Надбавка: {emp.bonus}%")
                try:
                    selected_index = int(input("Введите номер сотрудника для изменения надбавки: ")) - 1
                    if 0 <= selected_index < len(cafe.employees):
                        new_bonus = float(input("Введите новую надбавку (в процентах): "))
                        cafe.employees[selected_index].update_bonus(new_bonus)
                        print(f"Надбавка сотрудника '{cafe.employees[selected_index].name}' изменена на {new_bonus}%.")
                    else:
                        print_error("Неверный номер сотрудника.")
                except ValueError:
                    print_error("Введите корректный номер.")

        elif choice == "5":
            if not cafe.employees:
                print("Нет сотрудников.")
            else:
                print("\nСписок сотрудников:")
                for i, emp in enumerate(cafe.employees, start=1):
                    print(f"{i}) {emp.name} - {emp.position}")
                try:
                    selected_index = int(input("Введите номер сотрудника для увольнения: ")) - 1
                    if 0 <= selected_index < len(cafe.employees):
                        employee_name = cafe.employees[selected_index].name
                        cafe.employees.pop(selected_index)
                        print(f"Сотрудник '{employee_name}' уволен.")
                    else:
                        print_error("Неверный номер сотрудника.")
                except ValueError:
                    print_error("Введите корректный номер.")

        elif choice == "6":
            print("\nВыплата ЗП:")
            headers = ["Имя", "Должность", "Зарплата", "Надбавка", "Итоговая выплата"]
            rows = []
            for emp in cafe.employees:
                total_payment = emp.salary + (emp.salary * emp.bonus / 100)
                rows.append([emp.name, emp.position, emp.salary, f"{emp.bonus}%", total_payment])
            print_table(headers, rows)

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")
