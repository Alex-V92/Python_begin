'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring

У вас есть неограниченное число попыток.
Время одной попытки: 5 mins
'''
import requests
with open('dataset_3_5.txt') as f, open('answer_3_5_1.txt', 'w') as output_file:
    for row in f:
        api_url = f'http://numbersapi.com/{row.strip()}/math?json=true'
        res = requests.get(api_url)
        if res.json()['found']:
            print('Interesting',file=output_file)
        else:
            print('Boring', file=output_file)