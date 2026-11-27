# Дан список A размера N. Вывести его элементы в следующем порядке:
# A1, A2, AN, AN-1, A3, A4, AN-2, AN-3, ...
import random

n = input("Введите размер списка N: ")
while type(n) != int or n <= 0:  # Обработка исключений
    try:
        n = int(n)
        if n <= 0:
            print("Размер должен быть больше 0")
            n = input("Введите размер списка N: ")
    except ValueError:
        print("Число введено неправильно")
        n = input("Введите размер списка N: ")

a = []
for i in range(n):
    a.append(random.randint(1, 100))
print("Исходный список:", a)

result = []
left = 0  # Индекс элемента с начала списка
right = n - 1  # Индекс элемента с конца списка
while left <= right:
    for i in range(2):  # Два элемента с начала
        if left <= right:
            result.append(a[left])
            left += 1
    for i in range(2):  # Два элемента с конца
        if left <= right:
            result.append(a[right])
            right -= 1

print("Результирующий список:", result)