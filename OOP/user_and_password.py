from string import digits
class Account:

    def __init__(self, name, password):
        self.user = name
        self.my_password = password

    @property
    def my_password(self):
        print('Getter')
        return self.__password

    @my_password.setter
    def my_password(self, value):
        popylar_password = open('password_list.txt','r')
        print('Setter')
        if any(list(filter(lambda x:x in digits, value))) == False or len(value) < 4 or len(value) > 12:
            raise ValueError('Неверный формат пароля')
        else:
            if value in popylar_password.read():
                raise ValueError('Пароль слишком простой. Попробуйте ввести другой')
            else:
                self.__password = value

        popylar_password.close()


first = Account('Vasya','asdsa2')
print(first.user)
print(first.my_password)
first.my_password = 'dsdsdssd5'
print(first.my_password)
print(first.__dict__)



