ru_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
ru_h_alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
eng_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
eng_h_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def cezar_crpt(rotation, language, word, count_step):
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


word_ces = input().split()
# input - Day, mice. "Year" is a mistake!
# input - my name is Python!


for i in word_ces:
    word_len = 0
    for j in i:
        if j.isalpha():
            word_len += 1
    b = ''.join(i)
    print(cezar_crpt('ш', 'eng', b, word_len), end=' ')
