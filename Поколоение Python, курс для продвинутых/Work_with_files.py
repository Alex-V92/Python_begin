'''file = open('prices.txt', encoding='utf-8')
list_file = list([int(i) for i in file.read().split() if i.isdigit()])
print(sum([list_file[i] * list_file[i+1] for i in range(0, len(list_file)-1,2)]))'''

'''with open('prices.txt', encoding='utf-8') as file:
    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')'''

'''with open('data.txt') as file:
    answer = []
    for line in file:
        answer.append(line.strip())
    print(*answer[::-1],sep='\n')'''
'''with open('lines.txt') as file:
    max_len = len(max(list(map(lambda x: x.strip(), file.readlines())), key=len))
    print(max_len)
    file.seek(0)
    answer = list(filter(lambda x:len(x.strip()) == max_len  , file.readlines()))
    print(*[i.strip() for i in answer], sep='\n')
'''
'''import re
with open('nums.txt') as file:
    my_list = [re.findall(r'\d+', line) for line in file.readlines()]
    answer = 0
    for i in my_list:
        for j in i:
            answer += int(j)
    print(answer)'''
'''with open('file.txt') as file:
    words = len([i for i in file.read().split() ])
    file.seek(0)
    lines = len(file.readlines())
    file.seek(0)
    letters = len([i for i in file.read() if i.isalpha() ])
    print(f'Input file contains:\n{letters} letters\n{words} words\n{lines} lines')'''
'''from random import choice
with open('first_names.txt') as first_file, open('last_names.txt') as last_file:
    first_name = list(map(lambda x:x.strip(), first_file.readlines()))
    last_name = list(map(lambda x:x.strip(), last_file.readlines()))
    print(*[f'{choice(first_name)} {choice(last_name)}'for i in range(3)],sep = '\n')
'''
'''with open('population.txt') as file:
    dict_t = {}
    for line in file:
        list_t = list(map(lambda x:x.strip('\n'), line.split('\t')))
        if list_t[0][0] == 'G' and int(list_t[1]) >500000:
            print(list_t[0])
'''
'''def read_csv():
    with open('data.csv') as file:
        list_dict = file.readline().strip('\n').split(',')
        list_values = list(map(lambda x: x.strip().split(','), file.readlines()))
        print(list_values)
        return [(dict(zip(list_dict,i))) for i in list_values]
print(read_csv())'''


