import requests
import re
link_one = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
link_two = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

flag = 'Yes'
link_one_req = requests.get(link_one)
print(link_one_req.status_code)
if link_one_req.status_code == 404:
    flag = 'No'
link_in_one = re.findall('https.*html',link_one_req.text)
total_count = 0
for link in link_in_one:
    temp = requests.get(link)
    if link_two in re.findall('https.*html',temp.text):
        total_count +=1
print(['No','Yes'][total_count] if flag =='Yes' else 'No')



























# A_reg = re.sub(r'(<a href=")|(">1</a>)','', A.text)
# print(A_reg)
