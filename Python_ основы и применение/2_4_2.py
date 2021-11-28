'''
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
'''
import zipfile
import os
question = zipfile.ZipFile('main.zip')
question.extractall()
list_answer = []
for current_dir, dir, files in os.walk('main'):
    for file in files:
        if file[-2:] == 'py':
            if current_dir not in list_answer:
                list_answer.append(current_dir)

print(sorted(list_answer,key= lambda x:x))
with open('answer_file.txt', 'w', encoding='utf-8') as file_answer:
    for ele in sorted(list_answer):
        file_answer.write(ele)
        file_answer.write('\n')
