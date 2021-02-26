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
        self.square = x * y

    def __len__(self):
        print(2 * (self.x + self.y))
        return 2 * (self.x + self.y)

    def sum_of_squares(self, square_inner):
        sum_squares = self.square + square_inner
        print(f'Sum: {sum_squares}.')

    def difference(self, square_inner):
        diff = max(self.square, square_inner) - min(self.square, square_inner)
        if diff == 0:
            print(f'Square of first rectangle {self.square} is equal to the square of second rectangle {square_inner}.')
        else:
            print(f'Difference between rectangles squares: {diff}.')

    def equal(self, square_inner):
        diff = self.square - square_inner
        if diff == 0:
            print(f'Square of first rectangle {self.square} is equal to the square of second rectangle {square_inner}.')

    def not_equal(self, square_inner):
        diff = self.square - square_inner
        if diff != 0:
            print(f'This rectangle not equal {self.square} != {square_inner}.')

    def bigger_smaller(self, square_inner):
        if self.square > square_inner:
            print(f'This rectangle square: {self.square} is bigger then other rectangle square: {square_inner}.')
        elif self.square < square_inner:
            print(f'This rectangle square: {self.square} is smaller then other rectangle square: {square_inner}.')
        else:
            print(f'Square of first rectangle {self.square} is equal to the square of second rectangle {square_inner}.')


first_rect = Rectangle(12, 6)
second_rect = Rectangle(12, 6)
third_rect = Rectangle(24, 8)
fourth_rect = Rectangle(4, 2)


first_rect.__len__()

first_rect.sum_of_squares(second_rect.square)

first_rect.difference(second_rect.square)
first_rect.difference(third_rect.square)
first_rect.difference(fourth_rect.square)

first_rect.equal(second_rect.square)

first_rect.not_equal(third_rect.square)

first_rect.bigger_smaller(third_rect.square)
first_rect.bigger_smaller(fourth_rect.square)
first_rect.bigger_smaller(second_rect.square)

