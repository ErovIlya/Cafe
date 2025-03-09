from enum import Enum, auto


class StatePositionMenu:
    class State(Enum):
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
