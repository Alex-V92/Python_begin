'''
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
'''

with open('dataset_24465_4.txt','r', encoding='utf-8') as input_file, open('asnwer.txt','w', encoding='utf-8') as output_file:
    for line in input_file.readlines()[::-1]:
        output_file.write(line)
