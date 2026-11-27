# Найти сумму чисел ряда 1, 2, 3, 4, ... от числа n до числа m.
# Суммирование оформить функцией с параметрами.

def sum_numbers(n, m):
    s = 0  # Сумма чисел
    i = n
    while i <= m:
        s += i
        i += 1
    return s


n = input("Введите число n: ")
while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Число введено неправильно")
        n = input("Введите число n: ")

m = input("Введите число m: ")
while type(m) != int:  # Обработка исключений
    try:
        m = int(m)
    except ValueError:
        print("Число введено неправильно")
        m = input("Введите число m: ")

print("Сумма чисел от", n, "до", m, ":", sum_numbers(n, m))