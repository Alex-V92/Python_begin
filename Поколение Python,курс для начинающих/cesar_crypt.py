ru_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
ru_h_alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
eng_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
eng_h_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

print('Шифрование или дешифрование? ш/д')
rotation = input()
while True:
    if rotation.lower() == 'ш' or rotation.lower() == 'д':
        break
    print('Введите корректный ответ')
    print('Шифрование или дешифрование? ш/д')
    rotation = input()

print('Английский или русский? eng/ru')
language_word = input()
while True:
    if language_word.lower() == 'eng' or language_word.lower() == 'ru':
        break
    print('Введите корректный ответ')
    print('Английский или русский? eng/ru')
    language_word = input()

print('Числов сдвига')
count_step = input()
while True:
    if count_step.isdigit():
        break
    print('Введите корректный ответ')
    print('Числов сдвига')
    count_step = input()
count_step = int(count_step)

print('Введите фразу')
word = input()


def cezar_crpt(rotation, language):
    word_crypt = ''
    if rotation.lower() == 'ш':
        if language == 'eng':

            for i in range(len(word)):
                if word[i] in eng_h_alphabet:
                    index_alpha = eng_h_alphabet.index(word[i])
                    word_crypt += eng_h_alphabet[(index_alpha + count_step) % len(eng_h_alphabet)]
                elif word[i] in eng_alphabet:
                    index_alpha = eng_alphabet.index(word[i])
                    word_crypt += eng_alphabet[(index_alpha + count_step) % len(eng_alphabet)]
                else:
                    word_crypt += word[i]
            return word_crypt
        else:
            for i in range(len(word)):
                if word[i] in ru_h_alphabet:
                    index_alpha = ru_h_alphabet.index(word[i])
                    word_crypt += ru_h_alphabet[(index_alpha + count_step) % len(ru_h_alphabet)]
                elif word[i] in ru_alphabet:
                    index_alpha = ru_alphabet.index(word[i])
                    word_crypt += ru_alphabet[(index_alpha + count_step) % len(ru_alphabet)]
                else:
                    word_crypt += word[i]
            return word_crypt
    elif rotation.lower() == 'д':
        if language == 'eng':
            for i in range(len(word)):
                if word[i] in eng_h_alphabet:
                    index_alpha = eng_h_alphabet.index(word[i])
                    word_crypt += eng_h_alphabet[(index_alpha - count_step) % len(eng_h_alphabet)]
                elif word[i] in eng_alphabet:
                    index_alpha = eng_alphabet.index(word[i])
                    word_crypt += eng_alphabet[(index_alpha - count_step) % len(eng_alphabet)]
                else:
                    word_crypt += word[i]
            return word_crypt
        else:

            for i in range(len(word)):
                if word[i] in ru_h_alphabet:
                    index_alpha = ru_h_alphabet.index(word[i])
                    word_crypt += ru_h_alphabet[(index_alpha - count_step) % len(ru_h_alphabet)]
                elif word[i] in ru_alphabet:
                    index_alpha = ru_alphabet.index(word[i])
                    word_crypt += ru_alphabet[(index_alpha - count_step) % len(ru_alphabet)]
                else:
                    word_crypt += word[i]
            return word_crypt


print(cezar_crpt(rotation, language_word))

