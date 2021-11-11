'''from string import ascii_uppercase
a=ascii_uppercase
print([a[i]*(i+1) for i in range(int(input()))])'''
'''a, b = map(int, input().split())
if a <= b:
    print([(i ) ** 2 for i in range(a, b + 1)])
else:
    print([(i ) ** 3 for i in range(a , b-1, -1 )])'''
a=int(input())
print([i for i in range(1,a+1) if a%i==0 ])