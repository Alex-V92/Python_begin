from string import ascii_letters, digits
from random import randint

del_a = '0oIlO'
alpha_all = ascii_letters + digits
alpha_all = ''.join(i for i in alpha_all if i not in del_a)


def generate_password(length):
    return print(*[alpha_all[randint(0, len(alpha_all) - 1)] for i in range(length)], sep='')


def generate_passwords(count, length):
    return print(*[[alpha_all[randint(0, len(alpha_all) - 1)] for i in range(length)] for j in range(count)])
    generate_passwords(2, 33)
generate_passwords(3,5)