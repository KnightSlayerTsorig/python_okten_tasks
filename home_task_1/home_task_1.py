# найти min число в листе
def minimal(arr):
    minimal_num = arr[0]
    for el in arr:
        if el < minimal_num:
            minimal_num = el
    print(minimal_num)


# удалить все одинаковые значения
def delete_similar(arr):
    new_numbers = []
    for el in arr:
        if el not in new_numbers:
            new_numbers.append(el)
    print(new_numbers)
    print('Дубликаты были временно удалены')


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
    avg_in_list_dif = sum_of_elements
    avg_in_list = 0
    for el in arr:
        if el > 0:
            if el > avg:
                diff = el - avg
                if diff < avg_in_list_dif:
                    avg_in_list_dif = diff
                    avg_in_list = el
            elif avg > el:
                diff = avg - el
                if diff < avg_in_list_dif:
                    avg_in_list_dif = diff
                    avg_in_list = el
            else:
                avg_in_list = el
        elif el < 0:
            if el < avg:
                diff = (avg-avg*2) - (el-el*2)
                if diff < avg_in_list_dif:
                    avg_in_list_dif = diff - diff * 2
                    avg_in_list = el
            elif avg < el:
                diff = (el-el*2) - (avg-avg*2)
                if diff < avg_in_list_dif:
                    avg_in_list_dif = diff - diff * 2
                    avg_in_list = el
            else:
                avg_in_list = el

    print(avg_in_list)

    
# вывести на экран пустой квадрат из "*" сторона которого указана в переменой
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
            a = multiplier_1 * multiplier_2
            if a < 10:
                print(' ' + str(a) + ' ', end="")
            else:
                print(str(a) + ' ', end="")
            multiplier_2 += 1
        print(' ')
        multiplier_1 += 1
        multiplier_2 = 1

        
# переделать первое задание под меню с помощью цикла
numbers1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
numbers2 = [-1, -2, 3, 4, 555]
numbers3 = [5, 5, 5, 5]
numbers4 = [-10, -10, 5, 10]
numbers5 = [-500, -1000, -750, -250, 0, 100, 50000, 10000000]

find_avg(numbers5)


def menu(arr):
    while True:
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
        action_verification = ['1', '2', '3', '4', '5', '6', '7']
        if action not in action_verification:
            print('Вы ввели неправильное число или вообще не число, не надо так!')
        else:
            action = int(action)
            if action == 1:
                minimal(arr)
            if action == 2:
                delete_similar(arr)
            if action == 3:
                change_4_for_x(arr)
            if action == 4:
                find_avg(arr)
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





