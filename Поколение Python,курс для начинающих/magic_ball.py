from random import *

answer = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
          "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
          "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
          "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
          "Перспективы не очень хорошие", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name_player = input('Как тебя зовут? ')
print(f'Привет {name_player}!')
flag = True
while flag == True:
    player_question = input('Какой вопрос ты хочешь задать? ')
    print(choice(answer))
    print('Хочешь задать ещё один вопрос? y/ДА n/НЕТ')
    player_question_another = input()
    while True:
        if player_question_another.lower() == 'y' or player_question_another.lower() == 'да':
            break
        elif player_question_another.lower() == 'n' or player_question_another.lower() == 'нет':
            flag = False
            break
        else:
            print('Попробуй ответить ещё раз. Хочешь задать ещё один вопрос? y/ДА n/НЕТ')
            player_question_another = input()
