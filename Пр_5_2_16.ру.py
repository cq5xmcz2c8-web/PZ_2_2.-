# Описать функцию Power1(A, B) вещественного типа, находящую величину A^B
# по формуле A^B = exp(B * ln(A)). В случае нулевого или отрицательного
# параметра A функция возвращает 0. С помощью этой функции найти степени
# A^P, B^P, C^P, если даны числа P, A, B, C.

import math


def power1(a, b):
    if a > 0:
        return math.exp(b * math.log(a))
    return 0


p = input("Введите число P: ")
while type(p) != float:  # Обработка исключений
    try:
        p = float(p)
    except ValueError:
        print("Число введено неправильно")
        p = input("Введите число P: ")

a = input("Введите число A: ")
while type(a) != float:  # Обработка исключений
    try:
        a = float(a)
    except ValueError:
        print("Число введено неправильно")
        a = input("Введите число A: ")

b = input("Введите число B: ")
while type(b) != float:  # Обработка исключений
    try:
        b = float(b)
    except ValueError:
        print("Число введено неправильно")
        b = input("Введите число B: ")

c = input("Введите число C: ")
while type(c) != float:  # Обработка исключений
    try:
        c = float(c)
    except ValueError:
        print("Число введено неправильно")
        c = input("Введите число C: ")

print("A в степени P:", round(power1(a, p), 4))
print("B в степени P:", round(power1(b, p), 4))
print("C в степени P:", round(power1(c, p), 4))