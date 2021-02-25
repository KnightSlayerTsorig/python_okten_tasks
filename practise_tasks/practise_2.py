st = 'as 23 fdfdg544'


def elements_count(string):
    c = 0
    count_elements = []
    while c < len(string):
        c_2 = 0
        el_count = 0
        while c_2 < len(string):
            if string[c] == string[c_2]:
                el_count += 1
            c_2 += 1
        el_to_append = f'{string[c]} -> {el_count}'
        if el_to_append not in count_elements:
            count_elements.append(el_to_append)
        c += 1
    for el in count_elements:
        print(el)


elements_count(st)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new_numbers = ['GT' if i > 4 else 'LT' for i in numbers]
print(new_numbers)

list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]

tuple_list = [(i, j) for i in list1 for j in list2 if i + j == 0]
print(tuple_list)


# def is_zero(arr_1, arr_2):
#     counter = 0
#     zero = []
#     min_arr = min(len(arr_1), len(arr_2))
#     while counter < min_arr - 1:
#         if arr_1[counter] + arr_2[counter] == 0:
#             zero.append((arr_1[counter], arr_2[counter]))
#
#         counter += 1
#     print(zero)




