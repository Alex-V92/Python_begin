class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return 'Невозможно выполнить сравнение'


'''magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)  # False
print(ian == 2789)  # True
print(magnus == ian)  # False
print(magnus > ian)  # True
print(magnus < ian)  # False
print(magnus < [1, 2])  # печатает "Невозможно выполнить сравнениe"'''


class City:
    answer = 'aeiou'

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return f'{self.name}'

    def __bool__(self):
        return self.name[-1] not in City.answer


'''p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"'''


class Quadrilateral:
    def __init__(self, width, height=None):
        self.width = width
        if height == None:
            self.height = self.width
        else:
            self.height = height

    def __str__(self):
        if self.height == self.width:
            return f'Куб размером {self.width}х{self.height}'
        return f'Прямоугольник  размером {self.width}х{self.height}'

    def __bool__(self):
        return self.height == self.width


'''q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"'''


class Vector:
    def __init__(self, **kwargs):
        self.dict_new = kwargs

    def __str__(self):
        return f'{self.dict_new}'

    def __getitem__(self, item):
        if item in self.dict_new:
            return self.dict_new[item]
        else:
            raise KeyError('Нет такого ключа')


'''v1 = Vector(asd=1, a=9, adsdsadsadsa='asdasdads')
print(v1['asd'])
print(v1['asds'])
'''


class NewInt(int):
    def repeat(self, n: int = 2):
        number = ''.join([str(self) for i in range(n)])
        return int(number)

    def to_bin(self):
        return bin(self)[2:]

'''a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35
c = NewInt()
print(c.repeat())'''

class Transport:
    def __init__(self,brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'

class Car(Transport):
    def __init__(self,brand, max_speed, mileage,gasoline_residue):
        super().__init__(brand, max_speed,kind=Car)
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter
    def gasoline(self, value:int):
        if isinstance(value,int):
            self.__gasoline_residue += value
            return f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л'
        else:
            print('Ошибка заправки автомобиля')

class Boat(Transport):
    def __init__(self,brand, max_speed, owners_name):
        super().__init__(brand, max_speed,kind=Boat)
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'

class Plane(Transport):
    def __init__(self,brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind=Plane)
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'

'''transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
print(first_car.gasoline)  # Осталось бензина на 320 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr'''

class Initialization:
    def __init__(self, capacity:int, food:list):
        if not isinstance(capacity,int):
            print('Количество людей должно быть целым числом')
        else:
            self.capacity = capacity
            self.food = food

class Vegetarian(Initialization):
    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'

class MeatEater(Initialization):
    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'

class SweetTooth(Initialization):
    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        if isinstance(other,Initialization):
            return self.capacity == other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        if isinstance(other,Initialization):
            return self.capacity < other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        if isinstance(other,Initialization):
            return self.capacity > other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

'''v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # True
print(30000 == s_first)  # True
print(s_first == 25000)  # False
print(100000 < s_first)  # False
print(100 < s_first)  # True'''

class Wallet:
    def __init__(self, currency:str, balance:int):
        self.balance = balance
        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        if not len(currency) == 3:
            raise NameError('Неверная длина названия валюты')
        if not currency == currency.upper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        if self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        new_balance_ad = self.balance+other.balance
        return Wallet(self.currency, new_balance_ad)


    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        new_balance_sub = self.balance-other.balance
        return Wallet(self.currency, new_balance_sub)


'''wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
wallet2 + 45  # ValueError('Данная операция запрещена')'''