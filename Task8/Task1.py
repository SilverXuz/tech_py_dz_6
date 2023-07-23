"""
Задание №7
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию
"""

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
    print(is_valid_date('25.05.2012'))
