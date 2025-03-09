from utils.file_operations import load_data, save_data
from menus.main_menu import print_main_menu
from menus.assortment_menu import print_assortment_menu
from menus.drinks_menu import handle_drinks_menu
from menus.snacks_menu import handle_snacks_menu
from menus.inventory_menu import handle_inventory_menu
from menus.staff_menu import handle_staff_menu
from menus.orders_menu import handle_orders_menu
from menus.regular_customers_menu import handle_regular_customers_menu, view_regular_customers, analyze_regular_customers
from utils.StatePositionMenu import StatePositionMenu


def handle_state(cafe, state_manager):
    """Функция для обработки переходов по состояниям."""
    while True:
        current_state = state_manager.get_state()

        if current_state == state_manager.State.MAIN_MENU:
            print_main_menu()
            choice = input("Выберите пункт меню: ")

            if choice == "1":
                state_manager.set_state(state_manager.State.ASSORTMENT_MENU)
            elif choice == "2":
                state_manager.set_state(state_manager.State.STAFF_MENU)
            elif choice == "3":
                state_manager.set_state(state_manager.State.INVENTORY_MENU)
            elif choice == "4":
                state_manager.set_state(state_manager.State.REGULAR_CUSTOMERS_MENU)
            elif choice == "5":
                state_manager.set_state(state_manager.State.ORDERS_MENU)
            elif choice == "0":
                state_manager.set_state(state_manager.State.EXIT)
            else:
                print("Неверный выбор. Попробуйте снова.")

        elif current_state == state_manager.State.ASSORTMENT_MENU:
            print_assortment_menu()
            sub_choice = input("Выберите пункт меню: ")

            if sub_choice == "1":
                state_manager.set_state(state_manager.State.DRINKS_MENU)
            elif sub_choice == "2":
                state_manager.set_state(state_manager.State.SNACKS_MENU)
            elif sub_choice == "0":
                state_manager.set_state(state_manager.State.MAIN_MENU)
            else:
                print("Неверный выбор. Попробуйте снова.")

        elif current_state == state_manager.State.DRINKS_MENU:
            handle_drinks_menu(cafe)
            state_manager.set_state(state_manager.State.ASSORTMENT_MENU)

        elif current_state == state_manager.State.SNACKS_MENU:
            handle_snacks_menu(cafe)
            state_manager.set_state(state_manager.State.ASSORTMENT_MENU)

        elif current_state == state_manager.State.INVENTORY_MENU:
            handle_inventory_menu(cafe)
            state_manager.set_state(state_manager.State.MAIN_MENU)

        elif current_state == state_manager.State.STAFF_MENU:
            handle_staff_menu(cafe)
            state_manager.set_state(state_manager.State.MAIN_MENU)

        elif current_state == state_manager.State.ORDERS_MENU:
            handle_orders_menu(cafe)
            state_manager.set_state(state_manager.State.MAIN_MENU)

        elif current_state == state_manager.State.REGULAR_CUSTOMERS_MENU:
            handle_regular_customers_menu(cafe)
            state_manager.set_state(state_manager.State.MAIN_MENU)

        elif current_state == state_manager.State.VIEW_REGULAR_CUSTOMERS:
            view_regular_customers(cafe)
            state_manager.set_state(state_manager.State.REGULAR_CUSTOMERS_MENU)

        elif current_state == state_manager.State.ANALYZE_CUSTOMERS:
            analyze_regular_customers(cafe)
            state_manager.set_state(state_manager.State.REGULAR_CUSTOMERS_MENU)

        elif current_state == state_manager.State.EXIT:
            print("Выход из программы.")
            break

        else:
            print("Неизвестное состояние. Возврат в главное меню.")
            state_manager.set_state(state_manager.State.MAIN_MENU)


def main():
    filename = "cafe_data.json"
    cafe = load_data(filename)

    state_manager = StatePositionMenu()
    handle_state(cafe, state_manager)

    save_data(cafe, filename)
    print("Данные сохранены. Выход из программы.")

if __name__ == "__main__":
    main()
