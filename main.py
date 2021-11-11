a=int(input())
b=int(input())
c=int(input())
if a<=b<c or a<b<=c or a<b<c:
    print(c)
    print(a)
    print(b)
elif b<=a<c or b<a<=c or b<a<c:
    print(c)
    print(b)
    print(a)
elif c<=a<b or c<a<=b or c<a<b:
    print(b)
    print(c)
    print(a)
elif c<=b<a or c<b<=a or c<b<a:
    print(a)
    print(c)
    print(b)
elif b<c<a or b<=c<a or b<c<=a:
    print(a)
    print(b)
    print(c)
elif a<c<b or a<=c<b or a<c<=b:
    print(b)
    print(a)
    print(c)
else:
    print(a)
    print(b)
    print(c)