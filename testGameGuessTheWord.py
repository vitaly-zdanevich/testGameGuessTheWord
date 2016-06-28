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