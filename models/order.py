from datetime import datetime
from models.menu_item import MenuItem


class Order:
    def __init__(self, order_id: int, employee_name: str, items: dict[str, int], client_name: str, status: str = "open"):
        self.order_id = order_id
        self.employee_name = employee_name
        self.items = items
        self.status = status
        self.client_name = client_name
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "employee_name": self.employee_name,
            "items": self.items,
            "client_name": self.client_name,
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def calculate_total(self, menu: list[MenuItem]) -> float:
        total = 0
        for item_name, quantity in self.items.items():
            for menu_item in menu:
                if menu_item.name == item_name:
                    total += menu_item.price * quantity
                    break
        return total
