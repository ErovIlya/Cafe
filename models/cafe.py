from typing import List, Dict
from models.menu_item import MenuItem
from models.employee import Employee
from models.position import Position
from models.order import Order
from models.inventory_item import InventoryItem


class Cafe:
    def __init__(self):
        self.menu: List[MenuItem] = []
        self.employees: List[Employee] = []
        self.positions: List[Position] = []
        self.default_position: Position = None
        self.order_acceptance_position: Position = None
        self.inventory: List[InventoryItem] = []
        self.regular_customers: List[Dict] = []
        self.orders: List[Order] = []

    def add_menu_item(self, item: MenuItem):
        """Добавляет новую позицию в меню."""
        self.menu.append(item)

    def remove_menu_item(self, name: str):
        """Удаляет позицию из меню по названию."""
        self.menu = [item for item in self.menu if item.name != name]

    def apply_discount_to_item(self, name: str, discount: float):
        """Применяет скидку к позиции в меню по названию."""
        for item in self.menu:
            if item.name == name:
                item.apply_discount(discount)
                break

    def to_dict(self):
        return {
            "menu": [item.to_dict() for item in self.menu],
            "employees": [emp.to_dict() for emp in self.employees],
            "positions": [pos.to_dict() for pos in self.positions],
            "default_position": self.default_position.to_dict() if self.default_position else None,
            "order_acceptance_position": self.order_acceptance_position.to_dict() if self.order_acceptance_position else None,
            "inventory": [inv.to_dict() for inv in self.inventory],
            "regular_customers": self.regular_customers,
            "orders": [order.to_dict() for order in self.orders]
        }

    @classmethod
    def from_dict(cls, data: Dict):
        cafe = cls()
        cafe.menu = [MenuItem(**item) for item in data.get("menu", [])]
        cafe.employees = [Employee(**emp) for emp in data.get("employees", [])]
        cafe.positions = [Position(**pos) for pos in data.get("positions", [])]
        default_pos_data = data.get("default_position")
        if default_pos_data:
            cafe.default_position = Position(**default_pos_data)
        order_acceptance_pos_data = data.get("order_acceptance_position")
        if order_acceptance_pos_data:
            cafe.order_acceptance_position = Position(**order_acceptance_pos_data)
        cafe.inventory = [InventoryItem(**inv) for inv in data.get("inventory", [])]
        cafe.regular_customers = data.get("regular_customers", [])

        # Исправление для заказов: не передаем created_at в конструктор
        cafe.orders = []
        for order_data in data.get("orders", []):
            order = Order(
                order_id=order_data["order_id"],
                employee_name=order_data["employee_name"],
                items=order_data["items"],
                status=order_data["status"]
            )
            cafe.orders.append(order)

        return cafe