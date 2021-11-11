'''import turtle

square = turtle.Turtle()
square.shape("turtle")
square.color('red', 'green')
square.begin_fill()
for j in range(3):
    square.left(20)
    for i in range(4):
        square.forward(100)
        square.left(90)

square.end_fill()
turtle.exitonclick()'''

'''def reverse_list(a,b):
    if len(b)==1:
        return b
    else:
        reverse_list(a,b[-1])
reverse_list(3,1 2 3)'''
'''def fib_index(x):
    if x==0:
        return 0
    if x==1:
        return 1
    return fib_index(x-1)+fib_index(x-2)
print(fib_index(int(input())))'''
'''x=list(map(int,input().split()))
sum_x=[]
def list_sum_recursive (x):
    if len(x)<=1:
        sum_x.append(*x)
        return sum(sum_x)
    sum_x.append(x[0])
    return list_sum_recursive(x[1:])
print(list_sum_recursive(x))'''
'''x=([[[[9]]], [1,2], [[8]]])
z=[]
def flatten(x):'''
'''import datetime

now = datetime.datetime.now()

get_year = lambda x:str(x)[0:4]
get_month = lambda x:str(x)[5:7]
get_day = lambda x:str(x)[8:10]

print(get_day(now),get_month(now),get_year(now))'''


'''#list_buy={'Sony PlayStation 5': ' 46000', 'Телевизор QLED Samsung QE65Q60TAU': ' 87090', 'Смартфон Samsung Galaxy A11': ' 10000', 'Планшет Samsung Galaxy Tab S6': ' 26600'}

list_buy={}
x=list(input().split(':'))
while x!=['конец']:
    list_buy[x[0]]=x[1]
    x=list(input().split(':'))
for i in sorted(list_buy.items(), key=lambda para:int(para[1]),reverse=True):
    print(i[0])
list_buy={'Sony PlayStation 5': ' 46000', 'Телевизор QLED Samsung QE65Q60TAU': ' 87090', 'Смартфон Samsung Galaxy A11': ' 10000', 'Планшет Samsung Galaxy Tab S6': ' 26600'}
'''

'''list_buy={}
count_mark={}
x=list(input().split(', '))
while x!=['конец']:
    print((x[0]))
    if x[0] in list_buy : 
        count_mark[x[0]]+=1
        list_buy[x[0]]+=int(x[1])
    else:
        count_mark[x[0]]=1
        list_buy[x[0]]=int(x[1])   
    x=list(input().split(', '))

''''''list_buy = {'Джек': 5, 'Билл': 16}
count_mark = {'Джек': 2, 'Билл': 4}''''''
for key, value in list_buy.items():
    list_buy[key] = list_buy[key] / count_mark[key]

for i in sorted(list_buy.items(), key=lambda para: (-para[1],para[0])):
    print(i)'''

'''
Леонардо Ди Каприо
Джонни Депп
Леонардо Ди Каприо
Леонардо Ди Каприо
Джонни Депп
Мэтт Деймон
'''


'''count_oscar=6
count_oscar_actor={}
for i in range(count_oscar):
    x=str(input())
    if x not in count_oscar_actor:
        count_oscar_actor[x]=1
    else:
        count_oscar_actor[x]+=1
#count_oscar_actor = {'Леонардо Ди Каприо': 3, 'Джонни Депп': 2, 'Мэтт Деймон': 1}
count_oscar_actor_update=[]
count_oscar_actor_min=''
for i in sorted(count_oscar_actor.items(), key=lambda para: (-para[1])):
    print(i[0],i[1])
    count_oscar_actor_update.append((i[0]+',',i[1]))
print(*count_oscar_actor_update[0])
print(*count_oscar_actor_update[-1])'''
'''
3
444444 Женя
79129874521 Женя
79604845827 Оля
3
Оля
Олег
Женя


count_phone=int(input())
count_x=0
tele_dict={}
list_name=[]
z_list_name=[]
while count_phone!=count_x:
    z_list_name=list(input().split(' '))
    if z_list_name[1] not in tele_dict:
        tele_dict[z_list_name[1]]=[z_list_name[0]]
    else:
        tele_dict[z_list_name[1]] += [z_list_name[0]]
    count_x+=1
count_phone_find=int(input())
list_name_find=[]
count_x_find=0
while count_x_find!=count_phone_find:
    list_name_find.append(str(input()))
    count_x_find+=1
for i in list_name_find:
    if i in tele_dict:
        print(*tele_dict[i])
    else:
        print('Неизвестный номер')
'''
'''
4
Саша 20 янв
Артем 15 июн
Карл 10 янв
Коля 20 июл
3
июн
дек
янв
'''
'''dict_name={}
list_name=[]
for i in range(int(input())):
    list_name=list(input().split(' '))
    if list_name[2] not in dict_name:
        dict_name[list_name[2]]=[list_name[0]]
    else:
        dict_name[list_name[2]] += [list_name[0]]
for key,value in dict_name.items():
    dict_name[key]=(sorted(value))
for i in range(int(input())):
    date_find=str(input())
    if date_find in dict_name:
        print(*dict_name.get(date_find))
    else:
        print('Нет данных')'''

'''def multiply(arg):
    arg
    def multiply_second(arg_second):
        nonlocal arg
        return arg*arg_second
    return multiply_second
f=multiply(5)
print(f(10))'''


'''
print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)
'''

'''def print_given(*args,**kwargs):
    for i in args:
        print (i,type(i))
    for i,j in kwargs.items():
        print(i,j,type(j))
print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)'''

'''number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}
number_names_sorted={}
for i in sorted(number_names.items(), key=lambda para:(para[1])):
    number_names_sorted[i[0]]=i[1]
print(number_names_sorted)
number_names_sorted={8: 'eight', 18: 'eighteen', 11: 'eleven', 15: 'fifteen', 5: 'five', 4: 'four', 14: 'fourteen', 9: 'nine', 19: 'nineteen', 1: 'one', 7: 'seven', 17: 'seventeen', 6: 'six', 16: 'sixteen', 10: 'ten', 13: 'thirteen', 3: 'three', 12: 'twelve', 2: 'two', 0: 'zero'}
#a=list(map(int,input().split()))
a=[0, 1, 1, 2, 3, 5, 8, 13]
a_alpha=[]
for i in a:
    a_alpha.append(number_names[i])
for i in number_names_sorted:
    if i in a_alpha:
        print(i)'''


'''#a,b,c=input(),input(),input()
a,b,c='Париж','Марсель','Лион'
if min(len(a),len(b),len(c))==len(a):
    print(a)
elif min(len(a),len(b),len(c))==len(b):
    print(b)
elif min(len(a),len(b),len(c))==len(c):
    print(c)
if max(len(a),len(b),len(c))==len(a):
    print(a)
elif max(len(a),len(b),len(c))==len(b):
    print(b)
elif max(len(a),len(b),len(c))==len(c):
    print(c)'''

'''import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()
clock = pygame.time.Clock()
while True:
   clock.tick(60)
pygame.quit()'''

import random

random.seed(17)  # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
   print(random.randint(1, 100))

