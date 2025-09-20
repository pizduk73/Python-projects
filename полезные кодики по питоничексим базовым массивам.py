a = ["зеленый слоник","утомленны солнцем 2"]
print(*a)
print(*a, sep="\n")
print(*a, sep=', ')

print("Число писателей")
a=int(input())
print("Фамилии  писателей")
arr = []
for i in range(a):
    num = (input(f"Фамилия {i+1}: "))
    arr.append(num)
arr.sort()
print(*arr)

import random
array_size = 10
array = [random.randint(1, 100) for _ in range(array_size)]
print(array)
a=sum(array)
print(a)

import random
array_size = 10
array = [random.randint(1,100) for _ in range(array_size)]
print("Исходный массив:",*array)
print("Самый большой элемент:",max(array))

import random
arr_size = 10
arr = [random.randint(1, 100) for _ in range(arr_size)]
print("исходный массив:",*arr)
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] = 0
print("Отсортированный массив(Все нечет. заменены на 0):",*arr)


import random

arr_size = 10
arr = [random.randint(-100, 100) for _ in range(arr_size)]
print("исходный массив:",*arr)
arr = [5, -2, 8, -1, 3, -4, 7, 0, -3]

possitive = [x for x in arr if x >= 0]
negative = [x for x in arr if x < 0]
result = possitive + negative

print(*result)

import random

a = [random.randint(0, 10) for i in range(10)]
print("Массив a:", *a)

b = [x for x in a if x <= 5]
print("Массив b(без чисел, меньше 5):", *b)