digit_sum, digit_sum1, digit_sum2, digit_sum3, digit_sum4 = '88', '22', '16', '17', '32'
def digit_func(x, digit_answer):
    digit_x = 0
    x = str(x)
    x_len = len(x) - 1
    for i in x:
        digit_x += int(i) * (digit_answer ** x_len)
        x_len -= 1
    return digit_x


def digit_func_answer(x1, x2, x3, x4, x_sum, digit_answer):
    flag = False
    while flag == False:
        if digit_func(x1, digit_answer) + digit_func(x2, digit_answer) + digit_func(x3, digit_answer) + digit_func(x4,
                                                                                                                   digit_answer) != digit_func(
                x_sum, digit_answer):
            digit_answer += 1
        else:
            flag = True
    return digit_answer

print(digit_func_answer(digit_sum1, digit_sum2, digit_sum3, digit_sum4, digit_sum, 2))
