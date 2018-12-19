#!/usr/bin/python3
"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random
import sys


class Case:
    # Достаем бочонки по 1 и высчитываем остаток

    def boch(self):
        b_list = list(range(1, 91))
        random.shuffle(b_list)
        for i, y in enumerate(b_list):
            print('{:-^32}'.format('-'))
            print('Новый бочонок: {} (Осталось: {})'.format(y, len(b_list) - (i + 1)))
            yield y

    def __init__(self):
        self.generate = self.boch()


class Loto:
    def __init__(self, name):
        str_list = list(range(1, 91))
        self.name = name
        self.score = 0
        self.cards = [
            __class__.gen_string(str_list),
            __class__.gen_string(str_list),
            __class__.gen_string(str_list)
        ]

# Создаем строку и заполняем ее 5-ю числами в рандомном числами

    @staticmethod
    def gen_string(str_list):
        string = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            digits = random.randint(0, x)
            while string[digits] != '':
                digits += 1
            string[digits] = str_list.pop(random.randint(0, len(str_list) - 1))
        return string

    def __str__(self):
        s_list = '{:-^26}\n'.format(self.name)
        for x in range(3):
            s_list += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*self.cards[x]) + '\n'
        return s_list + '--------------------------'

    def search(self, cards_player, num_case):
        for i, n in enumerate(cards_player):
            if num_case in n:
                cards_player[i][n.index(num_case)] = '><'
                self.score += 1
                if self.score == 15:
                    print('{} Победил!'.format(self.name))
                    sys.exit(1)
                return True
        return False


c = Case()

player = Loto(' Игрок ')
computer = Loto(' Компьютер ')

while True:
    num_cask = next(c.generate)
    print(player)
    print(computer)
    num_reply = input('Зачеркнуть цифру? (y/n/q)')
    num_reply = num_reply.lower()
    if num_reply == 'q':
        print('Выход')
        break
    if num_reply == 'y':
        if player.search(player.cards, num_cask):
            continue
        else:
            print('Вы проиграли :(')
            sys.exit(1)
    if num_reply == 'n':
        if player.search(player.cards, num_cask):
            print('Вы проиграли :(')
            sys.exit(1)
        elif computer.search(computer.cards, num_cask):
            continue
    if num_reply != 'y' or 'n' or 'q':
        print('\n{:*^56}\n'.format('\nНеизвестный символ\n'))
