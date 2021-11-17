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
'''from random import randint
test_list = [randint(111,777) for i in range(25)]
with open('random1.txt','w') as output:
    print(*test_list,  sep = '\n', file=output)'''



'''with open('input.txt','r') as input_file, open('output.txt','w') as output_file:
    for i in enumerate(input_file.readlines(),1):
        print(str(i[0]) +')', i[1].strip('\n'), file=output_file)'''

'''with open('new_scores.txt','w', encoding='utf-8') as output_file, open('class_scores.txt','r',encoding='utf-8') as input_file :
    for line in input_file.readlines():
        asnwer_list = list(map(lambda x: x if x.isalpha() else int(x) +5 if int(x) < 95 else 100, line.split() ))
        print(*asnwer_list, file=output_file)'''

'''with open('goats.txt','r') as file_goats, open('answer.txt','w') as file_answer:
    answer_dict = {}
    total_goat = 0
    for line in file_goats.readlines()[1:]:
        if line.strip('\n') == 'GOATS' or line.strip('\n') == 'COLOURS':
            continue
        if line.strip('\n') in answer_dict:
            answer_dict[line.strip('\n')] += 1
            total_goat += 1
        else:
            answer_dict[line.strip('\n')] = 0
    for key,value in answer_dict.items():
        if total_goat / 100 * value > 7:
            print(key, file=file_answer)'''

'''n = int(input())
list_files = [input() for i in range(n)]
with open('output.txt','r') as file_output:
    for line in list_files:
        with open(line) as file_input:
            file_output.write(file_input)'''
'''with open('logfile.txt','r',encoding='utf-8') as file_log, open('output.txt','w',encoding='utf-8') as file_answer:
    dict_answer = {}
    for line in file_log.readlines():
        time_user = list(line.strip('\n').split(', '))
        if time_user[0] in dict_answer:
            dict_answer[time_user[0]] += (int(time_user[2][:2]) * 60 +int(time_user[2][3:]) ) - (int(time_user[1][:2]) * 60 +int(time_user[1][3:]) )
        else:
            dict_answer[time_user[0]] = (int(time_user[2][:2]) * 60 + int(time_user[2][3:])) - (
                        int(time_user[1][:2]) * 60 + int(time_user[1][3:]))
    for key, value in dict_answer.items():
        if value >= 60:
            print(key, file=file_answer)'''




'''with open('grades.txt') as file_open:
    total = 0
    for line in file_open.readlines():
        student = line.split()
        if len(list(filter(lambda x:int(x) >= 65, student[1:]))) == 3:
            total += 1
    print(total)'''

'''with open('words.txt') as file_open:
    list_t = list(file_open.read().split())
    print(*list(filter(lambda x:len(x) == len(max(list_t, key=len)) ,list_t)),sep='\n')'''

'''#name_file = input()
with open('input.txt') as file_open:
    print(*file_open.read().split('\n')[-10:],sep='\n')'''
'''d = { 'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya' }
with open('cyrillic.txt',encoding='utf-8') as file_open, open('transliteration.txt','w') as file_save:
    for letter in file_open.read():
        if letter in d:
            print(d[letter],file=file_save,end='')
        else:
            print(letter,file=file_save,end='')'''

'''with open('input.txt',encoding='utf-8') as file_open:
    list_test = list([i for i in file_open.readlines()])

    total_desc = 0
    list_funcs = []
    for i in range(len(list_test)):
        word = ''
        if list_test[i][:3] == 'def':
            if i == 0:
                for j in list_test[i][4:]:
                    if j == '(':
                        list_funcs.append(word)
                        break
                    else:
                        word += j
                continue
            elif list_test[i-1][0] != '#':
                for j in list_test[i][4:]:
                    if j == '(':
                        list_funcs.append(word)
                        break
                    else:
                        word += j
            else:
                total_desc += 1
                continue
    if len(list_funcs) == 0:
        print('Best Programming Team')
    else:
        print(*list_funcs,sep='\n')'''

'''with open('forbidden_words.txt') as file_regect, open('data (1).txt',encoding='utf-8') as file_output:
    stop_words = file_regect.read().lower().split()
    answer = file_output.read()
    answer_low = answer.lower()
    for word in stop_words:
        answer_low = answer_low.replace(word,'*'*len(word))
    for i in range(len(answer)):
        if answer[i].lower() == answer_low[i]:
            print(answer[i],end='')
        else:
            print('*',end='')'''


