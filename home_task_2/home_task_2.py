# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад: st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4  вивело в консолі.

some_string = 'as 23 fdfdg544'


def get_numbers(string):
    new_string = ''
    for el in string:
        if el in [str(i) for i in range(10)]:
            new_string += f'{el}, '
    new_string = new_string[:len(new_string) - 2]
    print(new_string)

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


some_string_2 = '1222ffffas 23 fdfdg544 34, 2323, asasas,12 aaaa'


def get_full_numbers(string):
    new_string = ''
    full_number = ''
    check = [str(i) for i in range(10)]
    for el in string:
        if el in check:
            full_number += el
        if el not in check and full_number != '':
            new_string += f'{full_number}, '
            full_number = ''
    if full_number != '':
        new_string += full_number
    else:
        new_string = new_string[:len(new_string) - 2]
    print(new_string)


# list comprehension
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
new_greeting = [i for i in greeting.upper()]
print(new_greeting)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

numbers = [i**2 for i in range(51) if i % 2 != 0]
print(numbers)

# function
# - створити функцію яка виводить ліст


def func_list(array):
    print(array)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.


def func_min(a, b, c):
    n = [a, b, c]
    b = min(n)
    return b

# - створити функцію яка приймає три числа та виводить та повертає найбільше.


def func_max(a, b, c):
    n = [a, b, c]
    b = max(n)
    return b

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше


def func_numbers(*args):
    minimal = min(*args)
    maximal = max(*args)
    print(maximal)
    return minimal

# - створити функцію яка повертає найбільше число з ліста


def func_max_list(array):
    return max(array)

# - створити функцію яка повертає найменьше число з ліста


def func_min_list(array):
    return min(array)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


def func_sum_list(array):
    return sum(array)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.


def func_avg_list(array):
    avg = sum(array) / len(array)
    return avg

# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення


def decor(func):
    def wrapper():
        result = func().replace('_', ' ')
        return result
    return wrapper


@decor
def pr():
    return 'Hello_boss_!!!'


a = pr()
print(a)
