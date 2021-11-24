class Lion:
    def roar(self):
        self.roar = print('Rrrrrrr!!!')
'''simba = Lion()
simba.roar()'''

class Counter:

    def start_from(self, value=0):
        self.start_inc = value

    def increment(self):
        self.start_inc += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.start_inc}')

    def reset(self):
        self.start_inc = 0

class Point:
    def set_coordinates(self,x_coord,y_coord):
        self.x = x_coord
        self.y = y_coord
    def get_distance(self,pifagor):
        if not isinstance(pifagor, Point):
            return print("Передана не точка")
        return ((self.x - pifagor.x) ** 2 + (self.y - pifagor.y) ** 2) **0.5
'''p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)
p1.get_distance(10)'''

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'

'''hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"'''

class SoccerPlayer:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, score_goal=1):
        self.goals += score_goal
    def make_assist(self, assist_make=1):
        self.assists += assist_make
    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals},передачи: {self.assists}')

'''leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"'''

class Zebra:
    def __init__(self):
        self.count_print = 0
    def which_stripe(self):
        self.count_print += 1
        print("Полоска белая" if self.count_print % 2 == 1 else "Полоска черная")

'''z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"'''

class Person:
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f'{self.last_name} {self.first_name}'
    def is_adult(self):
        if self.age >= 18:
            return True
        return False

'''p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f'{self.name} is {self.age} years old'
    def speak(self, sound):
        return f'{self.name} says {sound}'

'''jack = Dog("Jack", 4)

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'''

class Stack:
    def __init__(self):
        self.values = []
    def push(self,item):
        self.values.append(item)
    def pop(self):
        if len(self.values) == 0:
            print('Empty Stack')
        else:
            return self.values.pop(-1)
    def peek(self):
        if len(self.values) == 0:
            print('Empty Stack')
            return None
        else:
            return self.values[-1]
    def is_empty(self):
        if len(self.values) == 0:
            return True
        return False
    def size(self):
        return len(self.values)

'''s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2'''


class UserMail:
    def __init__(self,login, mail):
        self.login = login
        self.__email = mail
    def get_email(self):
        return self.__email
    def set_email(self, new_mail):
        if new_mail.count('@') == 1 and '.' in new_mail[(new_mail.index('@')):]:
            self.__email = new_mail
        else:
            print('Ошибочная почта')
    email = property(fget=get_email, fset=set_email)

'''k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait'''

class Money:
    def __init__(self, dollars, cents):
        self.total_cents = cents + dollars * 100


    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = self.cents + value * 100
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100


    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:
            self.total_cents = self.dollars * 100 + value
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'

'''Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов'''


class Squart:
    def __init__(self,line_a, line_b):
        self.__line_a = line_a
        self.__line_b = line_b
        self.__area = None

    @property
    def sides(self):
        return self.__line_a, self.__line_b


    @sides.setter
    def sides(self, values:tuple):

        self.__line_a, self.__line_b = values[0], values[1]
        self.__area = None


    @property
    def area(self):
        if self.__area is None:
            print('Calculated')
            self.__area = self.__line_a * self.__line_b
            return self.__area
        return self.__area

'''a = Squart(5, 10)
print(a.area)
print(a.area)
a.sides = 10, 15
print(a.area)
print(a.area)'''

class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f'Робот {self.name} был создан')

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} уничтожен')


    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')


'''r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"'''

class Person:

    def __init__(self, name, surname, gender ='male'):
        self.name = name
        self.surname = surname
        if gender != 'male' or 'female':
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'
        else:
            self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'

p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"

class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if len(self.values) != 0:
            return f'Вектор{tuple(i for i in self.values)}'
        return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):

            return Vector(*tuple(i + other for i in self.values))

        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*tuple(other.values[i] + self.values[i] for i in range(len(self.values))))

            else:
                return 'Сложение векторов разной длины недопустимо'
        else:
            print( f'Вектор нельзя сложить с {other}')

    def __radd__(self, other):
        return self.values + other

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*tuple(i * other for i in self.values))
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*tuple(other.values[i] * self.values[i] for i in range(len(self.values))))
            else:
                return 'Умножение векторов разной длины недопустимо'
        else:
            print( f'Вектор нельзя умножать  с {other}')

'''v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
v6 = Vector(1)
v7 = v6 + v1
v8 = v1 * v2
print(v8)
v9 = v6 * v1
v5 * "hi"'''
