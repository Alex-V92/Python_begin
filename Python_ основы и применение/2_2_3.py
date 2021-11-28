from simplecrypt import decrypt
with open('encrypted.bin','rb') as input_file, open('passwords.txt') as pass_file:
    crypt_file = input_file.read()
    for pass_try in pass_file:
        try:
            answer = decrypt(pass_try.strip(), crypt_file).decode('utf-8')
            break
        except:
            print('wrong pass')
    print(answer)

