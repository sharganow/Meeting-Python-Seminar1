# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

dotsX = ['','']
dotsY = ['','']

dotsX[0] = float(input('Введите координату X первой точки: '))
dotsY[0] = float(input('Введите координату Y первой точки: '))
dotsX[1] = float(input('Введите координату X второй точки: '))
dotsY[1] = float(input('Введите координату Y второй точки: '))
deltaX = dotsX[1] - dotsX[0]
deltaY = dotsY[1] - dotsY[0]

length = deltaX**2 + deltaY**2
length = round(math.sqrt(length), 2)
print(f'Длина отрезка А({dotsX[0]}, {dotsY[0]}); B({dotsX[1]}, {dotsY[1]}) равна {length}')