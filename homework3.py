# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

count = int(input("Введите количество элементов массива: "))
nums = []
for i in range(count):
    nums.append(random.randint(1, 9))
print("Ваш массив:", *nums)
el = int(input("Введите число для поиска: "))
print(f"В вашем массиве количество элементов c значением - '{el}' --->  {nums.count(el)}")




# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

count = int(input("Введите количество элементов массива, минимум 5 элементов: "))
if count < 5:
    print("Количество элементов массива меньше 5!")
else:
    max_range = int(input("Установите максимальную величину числа: "))
    nums = []
    for i in range(count):
        nums.append(random.randint(1, max_range))
    print("Ваш массив:", *nums)
    nums.sort()
    el = int(input("Введите число X: "))
    count = nums.count(el) 
    if nums.index(el) == 0: 
        print(nums[count])
    elif nums.index(el) == (len(nums) - 1) or (nums.index(el) + (count - 1)) == (len(nums) - 1):
        print(nums[(len(nums) - 2) - (count - 1)])
    else: 
        if (el - nums[nums.index(el) - 1]) > (nums[nums.index(el) + count] - el): 
            print(nums[nums.index(el) + count])
        else:
            print(nums[nums.index(el) - 1])



# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, 
# что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12

eng = { 1:'AEIOULNSTR',
    2:'DG',
    3:'BCMP',
    4:'FHVWY',
    5:'K',
    8:'JZ',
    10:'QZ'}
rus = { 1:'АВЕИНОРСТ',
    2:'ДКЛМПУ',
    3:'БГЁЬЯ',
    4:'ЙЫ',
    5:'ЖЗХЦЧ',
    8:'ШЭЮ',
    10:'ФЩЪ'}
N = abs(int(input("Если буквы русские, введите '0', если буквы английские, введите '1': ")))
word = input('Введите слово: ').upper()
if N == 1:
	print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
elif N == 0:
	print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
else:
    print('Неверный ввод!')