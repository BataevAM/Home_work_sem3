# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.


k = int(input('Введите число: '))

def fibonacci(k):
    numbs = []
    a, b = 1, 1
    for i in range(k):
        numbs.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k+1):
        numbs.insert(0, a)
        a, b = b, a - b
    return numbs

numbs = fibonacci(k)
print(fibonacci(k))