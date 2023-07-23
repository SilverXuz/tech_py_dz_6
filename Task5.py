"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
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

def random_queens_placement():
    # Случайная расстановка ферзей
    queens_coordinates = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
    return queens_coordinates

successful_placements = []
all_placements = []

# Установим лимит попыток для избежания бесконечного цикла
max_attempts = 10000
attempts = 0

while len(successful_placements) < 4 and attempts < max_attempts:
    queens_coordinates = random_queens_placement()
    all_placements.append(queens_coordinates)
    if not has_attacking_queens(queens_coordinates):
        successful_placements.append(queens_coordinates)
    attempts += 1

if len(successful_placements) == 4:
    for idx, placement in enumerate(all_placements):
        print(f"Расстановка {idx + 1}: {placement}")

    for idx, placement in enumerate(successful_placements):
        print(f"Успешная расстановка {idx + 1}: {placement}")
        print(f"Успешная расстановка {idx + 1}: {'Да' if placement in successful_placements else 'Нет'}")
else:
    print("Не удалось найти 4 успешные расстановки за пределенное количество попыток.")

# Завершение программы
exit()
