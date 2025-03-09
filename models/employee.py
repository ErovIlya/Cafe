class Employee:
    def __init__(self, name: str, position: str = None, salary: float = 0, bonus: float = 0):
        self.name = name
        self.position = position
        self.salary = salary
        self.bonus = bonus

    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "salary": self.salary,
            "bonus": self.bonus
        }

    def update_position(self, new_position: str):
        self.position = new_position

    def update_bonus(self, new_bonus: float):
        self.bonus = new_bonus
