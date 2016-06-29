"""
Написать скрипт простой игры "Угадай слово".
При запуске игры должно отображаться сообщение с приветсвием "Вы хотите начать игру Y/N?".
При вводе "Y" появляется строка с количеством оставшихся попыток, зашифрованное слово (#### = слон)
и курсор с сообщением для ввода буквы ("Введите букву: ").
При вводе "N" - выйти из скрипта.
Если введенная буква окажется верной - отображать слово с этой буквой (##о#, ##он и т.д.).
Если введенная буква не присутсвует в слове - уменьшать количетво попыток, выводить введенные буквы
и давать возможность для повторного ввода.
Если слово не угадано за указанное количество попыток - выводить сообщение о том, что игра закончилась
и дать игроку возможность для повторного ее прохождения ("Хотите сыграть еще раз Y/N?").
Если слово угадано - вывести соответсвующее сообщение (с указанием слова, которое было загадано)
и предложить игроку сыграть еще раз.
Скрипт должен содержать подмодуль с данными (массив слов, из которых будет выбираться слово для игры).
Эти данные должны быть импортированы в основной скрипт.
"""
import words
import random

attempts = 0
word = ''
strikeout = []
letters_tried = set()


def init_fields():
    global attempts
    global word
    global strikeout
    global letters_tried

    i = random.randint(0, len(words.words) - 1)
    word = words.words[i]
    strikeout = ['#'] * len(word)  # list because we need to replace # to correct letter - but String is immutable
    attempts = 5
    letters_tried = set()


def play():
    global attempts

    if len(letters_tried) > 0:
        print('Letter that you tried:', ', '.join(letters_tried))
    print('The number of remaining attempts:', attempts)
    print('word:', ''.join(strikeout))  # list to string
    letter_from_user = input('Enter your letter:\n')
    letters_tried.add(letter_from_user)

    if len(letter_from_user) > 1:
        print('Enter only one letter')
    elif letter_from_user.isdigit():
        print('Numbers not in the game')

    elif letter_from_user not in word or letter_from_user in strikeout:
        attempts -= 1
    elif letter_from_user.lower() in word:
        list_indexes = [i for i, char in enumerate(word) if char == letter_from_user]  # list comprehension, I like it
        for i in list_indexes:
            strikeout[i] = letter_from_user.lower()
        if '#' not in strikeout:
            print('WIN! The word is:', (''.join(word)).upper(), '\n')
            continue_or_not = input('Play again?[Y/N]\n')
            if continue_or_not.lower() == 'y':
                init_fields()
                play()
            exit()
    if attempts == 0:
        continue_or_not = input('Game over. Play again[Y/N]?\n')
        init_fields()
        if continue_or_not.lower() != 'y':
            exit()
    play()


start_or_not = input('Do you want start the game? [Y/N]\n')
if start_or_not.lower() == 'y':
    init_fields()
    play()



