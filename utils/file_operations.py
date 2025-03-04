import json
from models.cafe import Cafe

def load_data(filename: str) -> Cafe:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return Cafe.from_dict(data)
    except FileNotFoundError:
        return Cafe()

def save_data(cafe: Cafe, filename: str):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(cafe.to_dict(), file, indent=4, ensure_ascii=False)