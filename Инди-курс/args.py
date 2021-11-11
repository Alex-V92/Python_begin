'''def print_goods(*args):
    count_list=1
    for i in args:
        if i == str(i) and len(i)>0:
            print(str(count_list)+'.',i)
            count_list+=1
    if count_list==1:
        return print('Нет товаров')
print_goods('asdasd')'''
'''def info_kwargs(*args,**kwargs):
    for k,v in sorted(kwargs.items()):
        print(k,'=',v)

info_kwargs(first_name="John", last_name="Doe", age=33)'''