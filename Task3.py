"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from sys import argv

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 or year % 100 != 0 or year % 400 == 0

def is_valid_date(date: str) -> bool:
    try:
        day, month, year = map(int, date.split('.'))
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:
            if month == 2:
                if is_leap_year(year):
                    return day <= 29
                else:
                    return day <= 28
            elif month in [4, 6, 9, 11]:
                return day <= 30
            else:
                return day <= 31
    except ValueError:
        pass
    return False

if __name__ == '__main__':
    if len(argv) != 2:
        print("Использование: python имя_модуля.py дата в формате DD.MM.YYYY")
        exit(1)

    date = argv[1]
    result = is_valid_date(date)
    if result:
        print(f'Дата {date} существует.')
    else:
        print(f'Дата {date} не существует.')
