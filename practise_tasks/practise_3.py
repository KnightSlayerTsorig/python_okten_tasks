
empty_list = []


class Letter:
    __count = 0

    def __init__(self):
        self.__text = ''
        Letter.__count += 1

    @property
    def text(self):
        print(self.__text)
        return self.__text
    
    @text.setter
    def text(self, text):
        self.__text = text
    @classmethod
    def show_count(cls):
        print(f'{cls.__count}')
        return

    def append_into_list(self):
        empty_list.append(self.__text)


# first = Letter()
# first.set_text('This is text')
# first.get_text
# first.show_count
# first.append_into_list()
#
# second = Letter()
# second.show_count
# second.set_text('This is another text')
# second.


class Time:
    def __init__(self, time):
        self.time = time
        self.name = ''

    def count_time(self, other):
        if other.time < self.time:
            diff = self.time - other.time
            print(f'{other.name} is faster then {self.name}. Difference: {diff} hours')
        elif other.time > self.time:
            diff = other.time - self.time
            print(f'{self.name} is faster then {other.name}. Difference: {diff} hours')
        elif other.time == self.time:
            print(f'{self.name} and {other.name} time equal')


class Ticket(Time):

    def __init__(self, time, price):
        super().__init__(time)
        self.price = price


class Plane(Ticket):
    def __init__(self, time, price, reg_time, fly_class):
        super().__init__(time, price)
        self.reg_time = reg_time
        self.fly_class = fly_class
        self.name = 'Plane'

    def total_flight_time(self):
        total = self.time + self.reg_time
        print(f'Total flight time {total}')


class Train(Ticket):
    def __init__(self, time, price, place):
        super().__init__(time, price)
        self.place = place
        self.name = 'Train'

    @property
    def show_data(self):
        print(f'Time in a trip: {self.time} hours')
        print(f'Ticket price: {self.price}$')
        print(f'Wagon type and sit number {self.place}.')
        return


class Car(Time):
    def __init__(self, time, pas, fuel_price, km):
        super().__init__(time)
        self.pas = pas
        self.fuel_price = fuel_price
        self.km = km
        self.name = 'Car'

    @property
    def trip_price(self):
        price = self.fuel_price * self.km
        print(f'Trip price: {price}$')
        return price


bip_bip = Car(2, 4, 2, 250)



chy_chy = Train(12, 200, 'SW 12-b')
fly_fly = Plane(5, 1200, 1, '1st')
fly_fly.count_time(chy_chy)

chy_chy.show_data
bip_bip.count_time(chy_chy)
bip_bip.trip_price
