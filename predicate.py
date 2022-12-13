# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

x = bool
y = bool
z = bool
first = bool
second = bool

for i in range(2):
   z = not z
   for j in range(2):
      y = not y
      for k in range(2):
         x = not x
         first = not (x or y or z)
         second = (not x) and (not y) and (not z)
         if first == second:
            print(f'для значений x = {x} , y = {y}, z = {z} выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно, - first = {first}, а second = {second}')
         else:
            print(f'для значений x = {x} , y = {y}, z = {z} вырожение не справедливо - first = {first}, а second = {second}')
