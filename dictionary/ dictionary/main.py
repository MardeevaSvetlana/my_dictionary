from numpy.core.defchararray import capitalize, upper, lower
from words import words
import random
from phrases import *

br = ('*' * 60)
print(br)
print('Привет! How do you do?')

""" Выбор : перевод слов или устойчивых выражений"""
def change_user():
    try:
        print('Хочешь переводить:\n -слова -(1)\n -устойчивые выражения -(2)')
        ch_user = int(input())
        if (ch_user <= 0) or (ch_user > 2):
            print('Только "1" или "2"')
            change_user()
        else:
            change(ch_user)
    except Exception as error:
        print('Что- то пошло не так:', error)


""" Выбор режима перевода: англ- русс/ русс- анг"""
def change(ch_user):
    try:
        print('Выбери режим перевода:\n -c английского на русский -(1)\n -с русского на английский -(2)')
        ch = int(input())
        if (ch <= 0) or (ch > 2):
            print('Только "1" или "2"')
            change(ch_user)
        else:
            introduction(ch, ch_user)
    except Exception as error:
        print('Что- то пошло не так:', error)


""" Выбор количества слов/ фраз"""
def introduction(ch, ch_user):
    try:
        print(br)
        print('\nСколько слов\ фраз переведем?:')
        answer = int(input())
        if answer < 0:
            print('Так не работает, попробуй еще раз')
            introduction(ch, ch_user)
        elif answer > 50:
            print('Не стоит так напрягаться, введи число поменьше')
            introduction(ch, ch_user)
        else:
            print('Ну что ж,вперед!')
            print(br)
            if ch_user == 1:
                train_word(answer, ch)
            else:
                train_ph(answer, ch)
    except Exception as error:
        print('Что- то пошло не так:', error)


"""Перевод слов"""
def train_word(answer, ch):
    count, mist = 0, 0
    try:
        print('По дефолту- глаголы, мужской род')
        for i in range(answer):
            if ch == 1:
                word, key = random.choice(list(words.items()))
            else:
                key, word = random.choice(list(words.items()))
            print('Введи перевод слова "', word,'"')
            ans_user = lower(input())
            if ans_user == key:
                count += 1
                print('Отлично!!! Слово "', upper(word),'"', 'переводится как "', upper(key),'"')
                print('Правильных ответов:', count)
            else:
                mist += 1
                print('Ошибочка вышла. Слово "', upper(word),'"' ,'переводится как "', upper(key),'"')
                print('Количество ошибок:', mist)
        results(count, mist)
    except Exception as error:
        print('Что- то пошло не так:', error)


"""Перевод устойчивых выражений"""
def train_ph(answer, ch):
    try:
        print('Глаголы вида "ходить, учить" и т д, буква "Ё" не используется')
        count, mist = 0, 0
        for i in range(answer):
            if ch == 1:
                word, key = random.choice(list(phrases.items()))
            else:
                key, word = random.choice(list(phrases.items()))

            print('Переведи фразу -', word)
            ans_user = lower(input())
            if ans_user == key:
                count += 1
                print('Отлично!!! Фраза "', upper(word), '"','переводится как "', '"',upper(key))
                print('Правильных ответов:', count)
            else:
                mist += 1
                print('Ошибочка вышла.Фраза "', upper(word),'"', 'переводится как "', upper(key),'"')
                print('Количество ошибок:', mist)
        results(count, mist)

    except Exception as error:
        print('Что- то пошло не так:', error)

"""Итоги"""
def results(count, mist):
    print(br)
    try:
        if mist == 0:
            print('\nПотрясающе! Ни одной ошибки !!!')
        elif count == 0:
            print('\nТы старался. В следующий раз получится)')
        else:
            print('\nПодведем итоги:\nПравильных ответов:', count, '\nОшибок:', mist)

    except Exception as error:
        print('Что- то пошло не так:', error)
    finally:
        print('\nИспытание закончено.\nGoogbye')

change_user()
input()
