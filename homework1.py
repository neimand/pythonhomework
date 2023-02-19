# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input('Введите трехзначное число: ')
sum_n = 0
for i in number:
    sum_n += int(i)
print(sum_n)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

count = int(input('Введите количество журавликов: '))
print(f"Петя сделал {int((count / 3) / 2)}, Катя сделала {int((count / 3) * 2)}, Сережа сделал {int((count / 3) / 2)}")

# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

happy_ticket = input('Введите номер билетика: ')
first_part = happy_ticket[:3]
second_part = happy_ticket[3:]
first_sum = 0
second_sum = 0

for i in first_part:
    first_sum += int(i)
for i in second_part:
    second_sum += int(i)

if first_sum == second_sum:
    print('Билетик счастливый, поздравляю!')
else:
    print('Билетик, к сожалению, не счастливый :(')



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите длину шоколадки: '))
m = int(input('Введите ширину шоколадки: '))
k = int(input('Введите количество долек, которые нужно отломить: '))

if ((k % m == 0 or k % n == 0) and k < n * m) and k > 0:
    print('Да, столько отломить можно.')
elif k <= 0:
    print('Количество отламываемых долек должно быть больше нуля.')
elif k == n * m:
    print('Количество отламываемых долек не должно быть равно размеру шоколадки.')
elif k > n * m:
    print('Количество отламываемых долек не должно быть больше размера шоколадки.')
else:
    print('Отломить такое количество долек нельзя.')
