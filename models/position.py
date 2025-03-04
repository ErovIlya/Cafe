class Position:
    def __init__(self, name: str, default_salary: float = 0):
        self.name = name
        self.default_salary = default_salary

    def to_dict(self):
        return {
            "name": self.name,
            "default_salary": self.default_salary
        }