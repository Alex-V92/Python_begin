class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.total_money = 0

    def can_add(self, v):
        if self.total_money + v <= self.capacity:
            return True
        return False

    def add(self, v):
        if self.can_add(v) == True:
            self.total_money += v

'''x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)
'''


class Buffer:
    def __init__(self):
        self.total_num = []
        self.step = 1

    def add(self, *args):
        self.total_num.extend(args)
        while len(self.total_num) >= 5:
            print(sum(self.total_num[:5]))
            del self.total_num[:5]


    def get_current_part(self):
        return self.total_num
