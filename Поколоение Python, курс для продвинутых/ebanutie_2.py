
n, m = list(map(int, input().split()))
left = 0
right = 0
top = 0
down = 0
counter = 0
string = 'to_right'
first = True
a = [[0] * m for i in range(n)]

for k in range(n * m):
    if n == 1 and m == 1:
        a[0][0] = 1
        break
    elif (left + right + counter >= m - 1) and (string == 'l-r'):
        if left + right + counter > m - 1:
            counter = 1
        else:
            counter = 0
        string = 'to_down'
        top += 1
        first = False
    elif (down + top + counter == n) and (string == 't-b'):
        string = 'to_left'
        counter = 0
        right += 1
    elif (left + right + counter == m) and (string == 'r-l'):
        string = 'to_up'
        counter = 0
        down += 1
    elif (left + right + counter == n) and (string == 'b-t'):
        string = 'to_right'
        counter = 0
        left += 1

    if first:
        a[top][counter + left] = k + 1
    elif string == 'to_right':
        a[top][counter + left] = k + 1
    elif string == 'to_down':
        a[counter + top - 1][m - right - 1] = k + 1
    elif string == 'to_left':
        a[n - down - 1][m - counter - right] = k + 1
    elif string == 'to_up':
        a[n - down - counter][left] = k + 1
    counter += 1

for i in a:
    for j in i:
        print(str(j).ljust(2), end = ' ')
    print()
