from random import *


def correct_answer(answer):
    if answer.lower() == 'y' or answer.lower() == 'да' or answer.lower() == 'n' or answer.lower() == 'нет':
        return True
    return False


def correct_answer_range_pass(answer):
    if answer.isdigit() and int(answer) >= 1:
        return True
    return False

def password_gen():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_.'
    chars = []

    print('Введите количество паролей для генерации:')
    count_password = input()
    while True:
        if correct_answer_range_pass(count_password) == True:
            break
        print('Введите корректный ответ')
        print('Введите количество паролей для генерации:')
        count_password = input()
    count_password = int(count_password)

    print('Введите длину пароля')
    range_pass = input()
    while True:
        if correct_answer_range_pass(range_pass) == True:
            break
        print('Введите корректный ответ')
        print('Введите длину пароля')
        range_pass = input()
    range_pass = int(range_pass)

    print('Включать цифры в Ваш пароль? y/ДА n/НЕТ')
    numbers_in_pass = input()
    while True:
        if correct_answer(numbers_in_pass) == True:
            break
        print('Введите корректный ответ')
        print('Включать цифры в Ваш пароль? y/ДА n/НЕТ')
        numbers_in_pass = input()
    if numbers_in_pass.lower() == 'y' or numbers_in_pass.lower() == 'да':
        chars.extend(digits)

    print('Включать прописные буквы в Ваш пароль? y/ДА n/НЕТ')
    upper_alpha = input()
    while True:
        if correct_answer(upper_alpha) == True:
            break

        print('Введите корректный ответ')
        print('Включать прописные буквы в Ваш пароль? y/ДА n/НЕТ')
        upper_alpha = input()
    if upper_alpha.lower() == 'y' or upper_alpha.lower() == 'да':
        chars.extend(uppercase_letters)

    print('Включать строчные буквы в Ваш пароль?? y/ДА n/НЕТ')
    small_ch = input()
    while True:
        if correct_answer(small_ch) == True:
            break
    if small_ch.lower() == 'y' or small_ch.lower() == 'да':
        chars.extend(lowercase_letters)

    print('Включать спецсимволы в Ваш пароль? y/ДА n/НЕТ')
    symbols = input()
    while True:
        if correct_answer(symbols) == True:
            break
        print('Введите корректный ответ')
        print('Включать спецсимволы в Ваш пароль? y/ДА n/НЕТ')
        symbols = input()
    if symbols.lower() == 'y' or symbols.lower() == 'да':
        chars.extend(punctuation)

    print('Исключать неоднозначные символы (il1Lo0O) в Вашем пароле? y/ДА n/НЕТ')
    del_sym = input()
    while True:
        if correct_answer(del_sym) == True:
            break
        print('Введите корректный ответ')
        print('Исключать неоднозначные символы (il1Lo0O) в Вашем пароле? y/ДА n/НЕТ')
    if del_sym.lower() == 'n' or del_sym.lower() == 'нет':
        chars_2 = chars
        chars = [i for i in chars_2 if i not in 'il1Lo0O']


    def generate_password(range_pass, chars):
        password = ''
        for i in range(range_pass):
            password += chars[randint(0, len(chars) - 1)]
        return password


    for i in range(count_password):
        print(generate_password(range_pass, chars))
    print()
    print('Продолжить выполнение программы? y/ДА n/НЕТ')
    answer_exit = input()
    while True:
        if correct_answer(answer_exit) == True:
            break
        print('Введите корректный ответ')
        print('Продолжить выполнение программы? y/ДА n/НЕТ')
        answer_exit = input()
    if answer_exit.lower() == 'y' or answer_exit.lower() == 'да':
        password_gen()


password_gen()
