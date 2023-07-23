"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""
import random


def is_attacking(x1, y1, x2, y2):
    # Проверка, бьют ли ферзи друг друга по вертикали, горизонтали или диагоналям
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def has_attacking_queens(queens_coordinates):
    # Проверка наличия бьющих друг друга ферзей
    for i in range(len(queens_coordinates)):
        x1, y1 = queens_coordinates[i]
        for j in range(i + 1, len(queens_coordinates)):
            x2, y2 = queens_coordinates[j]
            if is_attacking(x1, y1, x2, y2):
                return True
    return False

# Пример ручного использования
queens_coordinates = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
result = has_attacking_queens(queens_coordinates)
print(result)  # Вернет False, так как ферзи не бьют друг друга

