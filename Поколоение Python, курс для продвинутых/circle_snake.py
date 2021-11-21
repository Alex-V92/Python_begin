n, m = list(map(int, input().split()))
left =right = top = bottom = counter = 0
rotation = 'to_right'
first = True
matrix = [[0] * m for i in range(n)]

for k in range(n * m):
    if n == 1 and m == 1:
        matrix[0][0] = 1
        break
    elif (left + right + counter >= m - 1) and (rotation == 'to_right'):
        if left + right + counter > m - 1:
            counter = 1
        else:
            counter = 0
        rotation = 'to_down'
        top += 1
        first = False
    elif (bottom + top + counter == n) and (rotation == 'to_down'):
        rotation = 'to_left'
        counter = 0
        right += 1
    elif (left + right + counter == m) and (rotation == 'to_left'):
        rotation = 'to_up'
        counter = 0
        bottom += 1
    elif (left + right + counter == n) and (rotation == 'to_up'):
        rotation = 'to_right'
        counter = 0
        left += 1

    if first:
        matrix[top][counter + left] = k + 1
    elif rotation == 'to_right':
        matrix[top][counter + left] = k + 1
    elif rotation == 'to_down':
        matrix[counter + top - 1][m - right - 1] = k + 1
    elif rotation == 'to_left':
        matrix[n - bottom - 1][m - counter - right] = k + 1
    elif rotation == 'to_up':
        matrix[n - bottom - counter][left] = k + 1
    counter += 1

for i in matrix:
    for j in i:
        print(str(j).ljust(2), end = ' ')
    print()
