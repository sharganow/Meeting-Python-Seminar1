# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
list = ['центре координат', 'в первой четверти', 'во второй четверти', 'в третьей четверти', 'в четвертой четверти']
x = 0
y = 0
quarter = 0
while x == 0 and y == 0:
    print('Введите координаты X и Y для определения четверти')
    x = float(input('Введите координату X: '))
    y = float(input('Введите координату Y: '))
    if x == 0 and y == 0:
        print('Точка не должна находиться на пересечении координатных осей')

if x == 0:
    print('Точка лежит на оси Y')
elif x > 0:
    if y == 0:
        print('Точка лежит на оси X')
    elif y > 0:
        quarter = 1
    else:
        quarter = 2
else:
    if y == 0:
        print('Точка лежит на оси X')
    elif y < 0:
        quarter = 3
    else:
        quarter = 4
if quarter != 0:
    answer = list[quarter]
    print(f'Точка с координатами X={x}; Y={y} лежит {answer}')

