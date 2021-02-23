shopping_list = {}

print('select action')
action = input(': ')

while True:
    if action == '1':
        purchase_name = input('Enter purchase name: ')
        purchase_price = int(input('Enter purchase price: '))
        shopping_list[purchase_name] = purchase_price
        action = input(': ')

    if action == '2':
        print(shopping_list)
        action = input(': ')

    if action == '3':
        total_sum = 0
        for v in shopping_list.values():
            total_sum += v
        print(total_sum)
        action = input(': ')

    if action == '4':
        max_name = ''
        max_sum = 0
        for k, v in shopping_list.items():
            if v > max_sum:
                max_sum = v
                max_name = k
        print('The most expensive purchase is ' + max_name + ': ' + str(max_sum))
        action = input(': ')

    if action == '5':
        purchase_name = input('Enter purchase name: ')
        if purchase_name in shopping_list:
            print(purchase_name + ': ' + str(shopping_list[purchase_name]))
        action = input(': ')

    if action == '6':
        over_1000 = {}
        for k, v in shopping_list.items():
            if v > 1000:
                over_1000[k] = v
        print(over_1000)
        action = input(': ')

    if action == '7':
        first_letter = input('Please enter first letter of purchases you are looking for: ')
        c_first = {}
        for k, v in shopping_list.items():
            if k[0] == first_letter:
                c_first[k] = v
        print(c_first)
        action = input(': ')

    if action == '8':
        break


