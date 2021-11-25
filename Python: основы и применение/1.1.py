'''fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))'''

'''list_t = [int(input()) for i in range(int(input()))]
print(sum(list_t))'''

objects = [1, 2, 1, 2, 3]
ans = 0
for i in range(len(objects)):
    for j in range(i+1, len(objects)):
        if objects[i] is objects[j]:
            ans -= 1
            break
    ans += 1
print(ans)
