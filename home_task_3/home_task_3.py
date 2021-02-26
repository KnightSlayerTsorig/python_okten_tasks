class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, array):
        for el in array:
            if self.shoe_size == el.shoe_size:
                print(f"{self.name} shoe perfectly fit's {el.name} leg.")


class Cinderella(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size


kit = Cinderella('Cat', 12, 28)
sobaka = Cinderella('Sobaka', 12, 36)
dog = Cinderella('Dog', 24, 12)

cinderellas = [dog, sobaka, kit]

hot_dog = Prince('Shashluk', 24, 28)

hot_dog.find_cinderella(cinderellas)

###########################################################


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.s = x * y

    def __len__(self):
        print(2 * (self.x + self.y))
        return 2 * (self.x + self.y)

    def __repr__(self):
        return self.s
    
    def __str__(self):
        return str(self.s)

    def __add__(self, other):
        result = self.s + int(other.__repr__())
        print(f'SUM: {result}')
        return result

    def __sub__(self, other):
        diff = abs(self.s - int(other.__repr__()))
        print(f'Difference: {diff}')
        return diff

    def __eq__(self, other):
        if self.s == other:
            a = f'{self.s} and {other} are equal'
        else:
            a = f'{self.s} and {other} are not equal'
        return a

    def __ne__(self, other):
        if self.s != other:
            a = f'{self.s} and {other} are not equal'
        else:
            a = f'{self.s} and {other} are equal'
        return a

    def __lt__(self, other):
        if self.s < other:
            a = f'{self.s} is smaller then {other}'
        elif self.s > other:
            a = f'{self.s} is bigger then {other}'
        else:
            a = self.__eq__(other)
        return a

    def __gt__(self, other):
        if self.s > other:
            a = f'{self.s} is bigger then {other}'
        elif self.s < other:
            a = f'{self.s} is smaller then {other}'
        else:
            a = self.__eq__(other)
        return a


#####################################
#               TEST                #
#####################################

first_rect = Rectangle(12, 6)
second_rect = Rectangle(12, 6)
third_rect = Rectangle(24, 8)
fourth_rect = Rectangle(4, 2)


first_rect.__len__()

first_rect + second_rect
first_rect + 244

first_rect - fourth_rect
first_rect - 44


print(first_rect == fourth_rect)
print(first_rect != fourth_rect)
print(first_rect == second_rect)


print(first_rect > 40)
print(first_rect > 100)
print(first_rect > 72)
print(first_rect < 40)
print(first_rect < 100)
print(first_rect < 72)
