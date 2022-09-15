# Напишите программу, которая будет преобразовывать
#  десятичное число в двоичное.


a = int(input('Введите число: '))
result = []

while a:
    result.append(a % 2)
    a //= 2
result.reverse()
print(result)