from colorama import Fore, Style


def print_error(message: str):
    print(Fore.RED + message + Style.RESET_ALL)


def print_table(headers: list[str], rows: list[list[str]]):
    # Вычисляем ширину столбцов
    col_widths = [len(header) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Создаем строку разделителя
    separator = "+" + "+".join("-" * (width + 2) for width in col_widths) + "+"

    # Выводим заголовки
    header_row = "|" + "|".join(header.center(col_widths[i] + 2) for i, header in enumerate(headers)) + "|"
    print(separator)
    print(header_row)
    print(separator)

    # Выводим строки
    for row in rows:
        row_str = "|" + "|".join(str(cell).ljust(col_widths[i] + 2) for i, cell in enumerate(row)) + "|"
        print(row_str)
        print(separator)
