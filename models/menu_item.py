class MenuItem:
    def __init__(self, name: str, price: float, category: str, ingredients: dict[str, int], discount: float = 0):
        self.name = name
        self.price = price
        self.category = category
        self.ingredients = ingredients
        self.discount = discount

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "ingredients": self.ingredients,
            "discount": self.discount
        }

    def apply_discount(self, discount: float):
        self.discount = discount
