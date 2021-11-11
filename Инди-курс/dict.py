'''from string import ascii_lowercase
a=ascii_lowercase
b={}
for i in range(len(a)):
    b[a[i]]=i+1
    print(b[a[i+1]])
''''''
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
rez={}
rez.update(d1)
rez.update(d2)
print(rez)'''
'''a=int(input())
b={}
z=1
for i in range(a):
    c=input()
    if c not in b:
        b.setdefault(c,'OK')
        print(b[c])
    else:
        while c + str(z) in b.keys():
            z += 1
        b.setdefault(c+str(z),(c,(z)))
        print(c+str(z))
        z=1
'''
'''a=input().lower()
b={}
for i in a:
    if i.isalpha():
        if a not in b:
            b[i]=a.count(i)
print(b)'''
'''data={'my_friends': {'count': 10, 'items': [{'first_name': 'Kurt', 'id': 621547005, 'last_name': 'Cobain', 'bdate': '31.8.2005'}, {'first_name': 'Виолетта', 'id': 484200150, 'last_name': 'Кастилио'}, {'first_name': 'Иринка', 'id': 21886133, 'last_name': 'Бушуева', 'bdate': '28.8.1942'}, {'first_name': 'Данил', 'id': 282456573, 'last_name': 'Греков', 'bdate': '4.7.2002'}, {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'}, {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин', 'bdate': '6.12.1982'}, {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова', 'bdate': '4.11.1995'}, {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'}, {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'}, {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова', 'bdate': '20.12'}]}}
name_sorted=[]
for key,value in data.items():
    for key_2,value_2 in value.items():
        if value_2 != 10:
            for key_3 in value_2:
                name_sorted.append(key_3.get('first_name'))
for i in (sorted(name_sorted)):
    print(i)
'''
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
a='Houston we have a problem'
for i in a:
    if i == ' ':
        print()
    else:
        print(morze.get(i),sep='')