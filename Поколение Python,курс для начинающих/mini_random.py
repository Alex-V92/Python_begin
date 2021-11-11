print('Добро пожаловать в числовую угадайку. До какого числа Вы хотите угадывать?:')


def is_valid(x, y):
    if x.isdigit() and y.isdigit() and 1 <= int(x) <= int(y):
        return True
    return False


def is_valid_max(x):
    if x.isdigit() and int(x) >= 2:
        return True
    return False


total_try = 0
from random import *


def random_game():
    x = 0
    while x == 0:
        number_max = input()
        if is_valid_max(number_max) == False:
            print('Введите другое число')
            continue
        else:
            x = 1

    number = randint(1, int(number_max))
    global total_try
    total_try = 0
    print(f'Введите число от 1 до {number_max}:')

    while True:
        total_try += 1
        number_player = input()
        if is_valid(number_player, number_max) == False:
            print(f'А может быть все-таки введем целое число от 1 до {number_max}?')
            continue
        number_player = int(number_player)
        if number_player < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif number_player > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Количество ваших попыток:', total_try)
            print('Сыграть ещё разок? y/ДА n/НЕТ')
            asnwer_player = input()

            while True:
                if asnwer_player.lower() == 'y' or asnwer_player.upper() == 'ДА':
                    print('И снова добро пожаловать в числовую угадайку. До какого числа Вы хотите угадывать?')
                    random_game()
                    break
                elif asnwer_player.lower() == 'n' or asnwer_player.upper() == 'НЕТ':
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    break
                else:
                    print('Ответьте корректно на вопрос. Сыграть ещё разок? y/ДА n/НЕТ')
                    asnwer_player = input()
            break


random_game()
