# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def multi_list(example_list):
    length_list = len(example_list)//2 + 1 if len(example_list) % 2 != 0 else len(example_list)//2
    new_list = [example_list[i]*example_list[len(example_list)-i-1] for i in range(length_list)]
    print(new_list)

example_list = [2, 3, 4, 5, 6]
print(example_list)
multi_list(example_list)
example_list = list(map(int, input("Введите числа через пробел:\n").split()))
multi_list(example_list)