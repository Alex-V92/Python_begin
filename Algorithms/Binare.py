a = list(range(1, 129))
low = 0
high = len(a) - 1
mid = 0
gues = 0
number = 36
while low <= high:
    mid = int((low + high) / 2)
    gues = a[mid]
    if gues == number:
        print(gues)
        break
    elif gues > number:
        high = mid - 1
    else:
        low = mid + 1


import math

print(math.log2(32))
