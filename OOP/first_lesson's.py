'''class Lion:
    def roar(self):
        self.roar = print('Rrrrrrr!!!')
simba = Lion()
simba.roar()'''


'''class Counter:

    def start_from(self, value=0):
        self.start_inc = value

    def increment(self):
        self.start_inc += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.start_inc}')

    def reset(self):
        self.start_inc = 0'''

class Point:
    def set_coordinates(self,x_coord,y_coord):
        self.x = x_coord
        self.y = y_coord
    def get_distance(self,pifagor):
        if not isinstance(pifagor, Point):
            return print("Передана не точка")
        return ((self.x - pifagor.x) ** 2 + (self.y - pifagor.y) ** 2) **0.5
p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)
p1.get_distance(10)