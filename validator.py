import re


class Validator:

    @staticmethod
    def validate_non_empty(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Ошибка: поле не может быть пустым")

    @staticmethod
    def validate_string(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value and re.fullmatch(r'[а-яА-Яa-zA-Z ]+', value):
                return value
            print("Ошибка: введите только буквы и пробелы")

    @staticmethod
    def validate_integer(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt).strip())
            except ValueError:
                print("Ошибка: введите целое число")

    @staticmethod
    def validate_float(prompt: str) -> float:
        while True:
            try:
                value = float(input(prompt).strip())
                if 1 <= value <= 10:
                    return value
                print("Ошибка: введите число от 1 до 10")
            except ValueError:
                print("Ошибка: введите корректное число")

    @staticmethod
    def validate_choice(prompt: str) -> int:
        while True:
            choice = input(prompt).strip()
            if choice.isdigit() and 21 <= int(choice) <= 70:
                return int(choice)
            print("Ошибка: выберите возраст от 21 до 70")

    @staticmethod
    def validate_date(prompt: str) -> str:
        while True:
            date = input(prompt).strip()
            try:
                day, month, year = map(int, date.split('.'))
                if 1 <= day <= 31 and 1 <= month <= 12 and 1980 <= year <= 2007:
                    return date
                print("Ошибка: некорректная дата")
            except:
                print("Ошибка: используйте формат ДД.ММ.ГГГГ")

    @staticmethod
    def validate_boolean(prompt: str) -> bool:
        while True:
            answer = input(prompt).strip().lower()
            if answer in ['да', 'нет']:
                return answer == 'да'
            print("Ошибка: введите 'да' или 'нет'")

    @staticmethod
    def validate_in_list(prompt: str, items: list, attribute: str = 'name') -> object:
        while True:
            search = input(prompt).strip()
            item = next((i for i in items if getattr(i, attribute) == search), None)
            if item:
                return item
            print("Ошибка: элемент не найден")