# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def odd_indexes(my_list):
    count = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            count += my_list[i]
    print(f"Сумма чисел на нечетных позициях равна: {count}")

my_list = [2, 3, 5, 9, 3]
print(my_list)
odd_indexes(my_list)
my_list = list(map(int, input("Введите числа через пробел:\n").split()))
odd_indexes(my_list)
