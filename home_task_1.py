# найти min число в листе
def minimal(arr):
    minimal_num = arr[0]
    for el in arr:
        if el < minimal_num:
            minimal_num = el
    print(minimal_num)


# удалить все одинаковые значения
def delete_similar(arr):
    new_arr = arr
    new_numbers = []
    for el in new_arr:
        if el not in new_numbers:
            new_numbers.append(el)
    for el in new_numbers:
        if el in new_arr:
            new_arr.remove(el)
    for el in new_arr:
        if el in new_numbers:
            new_numbers.remove(el)
    print(new_numbers)
    print('Значения ' + str(arr) + ' были временно удалены')


# заменить каждое четвертое значение на "Х"
def change_4_for_x(arr):
    counter = 1
    while counter < len(arr) + 1:
        if counter % 4 == 0:
            arr[counter - 1] = 'X'
        counter += 1
    print(arr)


# вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
def find_avg(arr):
    sum_of_elements = 0
    divider = 0
    for el in arr:
        if type(el) == int:
            sum_of_elements += el
            divider += 1
    avg = sum_of_elements / divider
    avg_in_list = arr[0]
    for el in arr:
        if type(el) == int:
            if avg == el:
                avg_in_list = el
            elif avg - el < avg_in_list:
                avg_in_list = el
    print(avg_in_list)


def stars(height, width):
    if width < 3:
        width = 3
    if height < 3:
        height = 3
    print('*' * width)
    c = 2
    while c < height:
        print('*' + ' ' * (width - 2) + '*')
        c += 1
    print('*' * width)


# вывести табличку умножения с помощью цикла while
def table():
    multiplier_1 = 1
    multiplier_2 = 1
    while multiplier_1 != 10:
        while multiplier_2 != 10:
            print(str(multiplier_1 * multiplier_2) + ' ', end="")
            multiplier_2 += 1
        print('\n')
        multiplier_1 += 1
        multiplier_2 = 1


# переделать первое задание под меню с помощью цикла
while True:
    numbers = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print('Что будем делать?')
    print('Введите 1 что бы найти min число в листе ')
    print('Введите 2 что бы удалить все одинаковые значения')
    print('Введите 3 что бы заменить каждое четвертое значение на "Х"')
    print(
        '''Введите 4 что бы вывести элемент листа, значение которого ближе
всего к среднему арифметическому всех элементов этого же листа'''
    )
    print('Введите 5 что бы увидить магический квадрат')
    print('Введите 6 что бы увидить табличку умножения ')
    print('Введите 7 что бы выйти з программы')
    action = input('Введите число: ')
    action_verification = [str(el) for el in range(1, 8)]
    if action not in action_verification:
        print('Вы ввели неправильное число или вообще не число, не надо так!')
    else:
        action = int(action)
        if action == 1:
            minimal(numbers)
        if action == 2:
            delete_similar(numbers)
        if action == 3:
            change_4_for_x(numbers)
        if action == 4:
            find_avg(numbers)
        if action == 5:
            h = int(input('Введите желаемую высоту магического квадрата: '))
            w = int(input('Введите желаемую  ширину магического квадрата: '))
            if type(h) != int or type(w) != int:
                print('Ну вот опять... вот вам базовый квадрат')
                stars(6, 6)
            else:
                stars(h, w)
            if h != w:
                print('Только это не квадрат а прямоугольник')
        if action == 6:
            table()
        if action == 7:
            break

