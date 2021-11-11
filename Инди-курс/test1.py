'''a,b=map(int,input().split())
c=[]
for i in range(a):
    c.append(list(map(int,input().split())))
for i in range(a-1,-1,-1):
    for k in range(b):
        print(c[i][k],end=' ')
    print()'''
'''a=0
b=[]
for i in range(5):
    b.append(list(map(int,input().split())))
for i in range(len(b)):
    for j in range (len(b)):
        if 1 ==b[i][j]:
            a+=abs(2-i)
            a+=abs(2-j)
print(a)'''

'''c=[]
for i in range(a):
    c.append(list(map(int,input().split())))
print(c)'''
'''a,b=map(int,input().split())
x = []
y = []
z = 0
c=[]
for i in range(a):
    c.append(list(map(int,input().split())))
for i in range(len(c)):
    x.append((sum(c[i])))
for i in range(b):
    for j in range(a):
        z+=c[j][i]
    y.append(z)
    z=0
print()
print(*x)
print(*y)'''
'''n,m=map(int,input().split())
c=[]
for i in range(n):
    c.append(list(map(int,input().split())))
a=((c[0][0])+(c[0][1]))
b=0
index_max=0
for i in range(n):
    b=0
    for j in range(m):
        b+=(c[i][j])
        if a<=b:
            a=b
            index_max=i
print(a)
print(index_max)'''