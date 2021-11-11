a = '1230'
new_list = []
new_list.append([])

for i in range(len(a)):
    count = i + 1
    while count != len(a) + 1:
        temp_list = []
        temp_list.append(a[i:count])
        new_list.append(temp_list)
        count += 1
print(new_list)
print(sorted(new_list, key = len))