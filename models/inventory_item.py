class InventoryItem:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity
        }

    def add_quantity(self, amount: int):
        self.quantity += amount

    def subtract_quantity(self, amount: int):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            raise ValueError("Недостаточно ингредиента на складе.")