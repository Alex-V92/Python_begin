class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super().append(x)


'''a = PositiveList([1,2,3,4,5])
a.append(6)
a.append(-1)'''

