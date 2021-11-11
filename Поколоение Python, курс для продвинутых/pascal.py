def pascal(n):
    s = [[1] * (i + 1) for i in range(n+1)]
    for i in range(len(s)):
        if i <= 1:
            continue
        else:
            for j in range(len(s[i])):
                if j == 0 or j == len(s[i]) - 1:
                    continue
                else:
                    s[i][j] = s[i - 1][j - 1] + s[i - 1][j]
    print(*s[-1])


def pascal_2(n):
    s = [[1] * (i + 1) for i in range(n)]
    for i in range(len(s)):
        if i <= 1:
            print(*s[i])
            continue
        else:
            for j in range(len(s[i])):
                if j == 0 or j == len(s[i]) - 1:
                    print(s[i][j], end=' ')
                else:
                    s[i][j] = s[i - 1][j - 1] + s[i - 1][j]
                    print(s[i][j], end=' ')
        print()
pascal_2(5)