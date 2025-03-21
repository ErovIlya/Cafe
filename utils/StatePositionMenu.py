from enum import Enum, auto


class StatePositionMenu:
    class State(Enum):
#         # Главная страница
#         MAIN_MENU = auto()
#         ASSORTIMENT_MENU
#         PERSONAL_MENU
#         INVENTORY_MENU
#         CUSTOMERS_MENU
#         ORDER_MENU
#         # Ассортимент
#         DRINK_MENU
#         SNACK_MENU
#         # Напитки
#         DRINK_ADD
#         DRINK_DELETE
#         DRINK_DISCOUNT_ADD
#         DRINK_DISCOUNT_DELETE
#         # Закуски
#         SNACK_ADD
#         SNACK_DELETE
#         SNACK_DISCOUNT_ADD
#         SNACK_DISCOUNT_DELETE
#         # Персонал
#         POST_MENU
#         PERSONAL_MENU
#         # Должности
#         POST_ADD
#         POST_DEFUALT
#         POST_SALARY
#         POST_ORDER
#         # Персонал
#         PERSONAL_ADD
#         PERSONAL_CHANGE_POST
#         PERSONAL_CHANGE_SALARY
#         PERSONAL_DELETE
#         # Инвентарь
#
#
        ACCEPT_ORDER = auto()
        CLOSE_ORDER = auto()
        VIEW_ACTIVE_ORDERS = auto()
        VIEW_TODAY_ORDERS = auto()
        MAIN_MENU = auto()
        ASSORTMENT_MENU = auto()
        DRINKS_MENU = auto()
        SNACKS_MENU = auto()
        INVENTORY_MENU = auto()
        STAFF_MENU = auto()
        ORDERS_MENU = auto()
        REGULAR_CUSTOMERS_MENU = auto()
        VIEW_REGULAR_CUSTOMERS = auto()
        ANALYZE_CUSTOMERS = auto()
        EXIT = auto()

        # Состояния для подменю
        DRINKS_ADD = auto()
        DRINKS_REMOVE = auto()
        DRINKS_APPLY_DISCOUNT = auto()
        DRINKS_REMOVE_DISCOUNT = auto()
        DRINKS_VIEW = auto()

        SNACKS_ADD = auto()
        SNACKS_REMOVE = auto()
        SNACKS_APPLY_DISCOUNT = auto()
        SNACKS_REMOVE_DISCOUNT = auto()
        SNACKS_VIEW = auto()

        INVENTORY_VIEW = auto()
        INVENTORY_ADD = auto()
        INVENTORY_REMOVE = auto()

        STAFF_POSITIONS = auto()
        STAFF_EMPLOYEES = auto()
        STAFF_ADD_POSITION = auto()
        STAFF_ADD_EMPLOYEE = auto()
        STAFF_UPDATE_EMPLOYEE = auto()
        STAFF_REMOVE_EMPLOYEE = auto()

        REGULAR_CUSTOMERS_VIEW = auto()
        REGULAR_CUSTOMERS_ANALYZE = auto()

    def __init__(self):
        self.current_state = self.State.MAIN_MENU

    def set_state(self, new_state: State):
        self.current_state = new_state

    def get_state(self):
        return self.current_state
