digit_16 = {10:'A', 11:'B', 12:'C', 13: 'D', 14:'E', 15:'F'}
def convert_on_10(digit, digit_convert):
    new_digit_list = []
    while digit >= digit_convert :
        new_digit_list.insert(0, digit % digit_convert)
        digit = digit //  digit_convert
    new_digit_list.insert(0, digit)
    new_digit_list = [i if int(i) not in digit_16 else digit_16[i] for i in new_digit_list]
    return new_digit_list
print (*convert_on_10(513, 2), sep = '')