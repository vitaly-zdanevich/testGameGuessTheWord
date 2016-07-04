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
import os
import words
import random


class Game:

    def __init__(self):
        self.word = ''
        self.strikeout = []
        self.attempts = 0
        self.letter_from_user = ''
        self.letters_tried = set()

        Game.init(self)

    def init(self):
        self.word = random.choice(words.words)
        self.strikeout = ['#'] * len(self.word)  # list because we need to replace # to correct letter - but String is immutable
        self.attempts = 5
        self.letters_tried = set()

    def play(self):
        os.system('clear')

        self.print_header()
        self.validate()

    def print_header(self):
        if len(self.letters_tried) > 0:
            print('Letters that you tried:', ', '.join(self.letters_tried))
        print('The number of remaining attempts:', self.attempts)
        print('word:', ''.join(self.strikeout))  # list to string
        self.letter_from_user = input('Enter your letter:\n')
        self.letters_tried.add(self.letter_from_user)

    def validate(self):
        if len(self.letter_from_user) > 1:
            print('Enter only one letter')
        elif self.letter_from_user.isdigit():
            print('Numbers not in the game')

        elif self.letter_from_user not in self.word or self.letter_from_user in self.strikeout:
            self.attempts -= 1
        elif self.letter_from_user.lower() in self.word:
            list_indexes_of_founded_position_of_letter = [i for i, char in enumerate(self.word) if char == self.letter_from_user]  # list comprehension, I like it
            for i in list_indexes_of_founded_position_of_letter:
                self.strikeout[i] = self.letter_from_user.lower()
            if '#' not in self.strikeout:
                print('WIN! The word is:', (''.join(self.word)).upper(), '\n')
                continue_or_not = input('Play again?[Y/N]\n')
                if continue_or_not.lower() == 'y':
                    game.init()
                    self.play()
                exit()
        if self.attempts == 0:
            continue_or_not = input('Game over. Play again[Y/N]?\n')
            if continue_or_not.lower() != 'y':
                exit()
            game.init()
        self.play()


start_or_not = input('Do you want start the game? [Y/N]\n')
if start_or_not.lower() == 'y':
    game = Game()
    game.play()



