from utils.file_operations import load_data, save_data
from models.cafe import Cafe
from menus.main_menu import print_main_menu
from menus.assortment_menu import print_assortment_menu
from menus.drinks_menu import handle_drinks_menu
from menus.snacks_menu import handle_snacks_menu
from menus.inventory_menu import handle_inventory_menu
from menus.staff_menu import handle_staff_menu
from menus.orders_menu import handle_orders_menu

def main():
    filename = "cafe_data.json"
    cafe = load_data(filename)

    while True:
        print_main_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            while True:
                print_assortment_menu()
                sub_choice = input("Выберите пункт меню: ")

                if sub_choice == "1":
                    handle_drinks_menu(cafe)

                elif sub_choice == "2":
                    handle_snacks_menu(cafe)

                elif sub_choice == "0":
                    break

                else:
                    print("Неверный выбор. Попробуйте снова.")

        elif choice == "2":
            handle_staff_menu(cafe)

        elif choice == "3":
            handle_inventory_menu(cafe)

        elif choice == "4":
            print("\nПостоянные клиенты:")
            # Здесь можно добавить логику для работы с постоянными клиентами
            print("Функционал в разработке...")

        elif choice == "5":
            handle_orders_menu(cafe)

        elif choice == "0":
            save_data(cafe, filename)
            print("Данные сохранены. Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()