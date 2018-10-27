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


class Card:
    def __init__(self):
        self.card = list()
        self.numbers_left = 15

    def card_create(self):
        card_numbers = random.sample(range(1, 91), 15)
        for i in range(0, 15, 5):
            line = card_numbers[i:i+5]
            self.card.append(sorted(line))
            for j in range(4):
                self.card[int(i / 5)].insert(random.randint(0, 5 + j), '  ')

    def display_card(self):
        for string in self.card:
            for cell in string:
                print('%+2s' % cell, end=' ')
            print()

    def display_human_card(self):
        print('------ Ваша карточка ------')
        self.display_card()
        print('-' * 27)

    def display_comp_card(self):
        print('--- Карточка компьютера ---')
        self.display_card()
        print('-' * 27)

    def check_barrel_is_exist_in_card(self, barrel_to_check):
        for string in self.card:
            if barrel_to_check in string:
                return True
        return False

    def cross_out_number(self, number_to_cross):
        for i, string in enumerate(self.card):
            self.card[i] = list(map(lambda y: '><' if y == number_to_cross else y, string))
        self.numbers_left -= 1


class BarrelBag:
    def __init__(self):
        self.bag = list()

    def barrel_bag_create(self):
        self.bag = [True] * 90

    def get_random_barrel(self):
        while True:
            random_barrel = random.randint(1, 90)
            if self.bag[random_barrel - 1]:
                self.bag[random_barrel - 1] = False
                return random_barrel

    def get_barrels_left(self):
        return sum(self.bag)


class PlayerComputer:
    def __init__(self):

        pass

# Можно наверно эту функцию сюда перенести
#    def display_comp_card(self, card):

    def turn(self, barrel_in_comp_card, card):
        if barrel_in_comp_card:
            card.cross_out_number(barrel)
            if not card.numbers_left:
                print(' ' + '-' * 28, '\n Компьютер заполнил карточку!\n          ВЫ ПРОИГРАЛИ!\n', '-' * 28)
                exit(0)


class PlayerHuman:
    def __init__(self):

        pass

    def cross_or_not(self):
        while True:
            choice = input('Зачеркнуть число? (y/n)')
            if len(choice) == 1 and choice in 'yn':
                if choice == 'y':
                    return True
                else:
                    return False

    def turn(self, human_choice, barrel_in_human_card, card):

        if human_choice and barrel_in_human_card:
            card.cross_out_number(barrel)
            if not card.numbers_left:
                print(' ' + '-' * 32, '\n ПОБЕДА! Вы выиграли! Поздравляю!\n', '-' * 32)
                exit(0)
        elif human_choice and not barrel_in_human_card:
            print(' ' + '-' * 34, '\n Такого числа нет в вашей карточке!\n          ВЫ ПРОИГРАЛИ!\n', '-' * 34)
            exit(0)
        elif not human_choice and barrel_in_human_card:
            print(' ' + '-' * 28, '\n Число есть в вашей карточке!\n          ВЫ ПРОИГРАЛИ!\n', '-' * 28)
            exit(0)


print('== Лото ==\n')

human = PlayerHuman()
comp = PlayerComputer()
bag_of_barrels = BarrelBag()
bag_of_barrels.barrel_bag_create()
card_computer = Card()
card_computer.card_create()

# -----------Тестовая карточка для компьютера-----------------
# card_computer.card = [[6, 7, 54, '  ', 56, '  ', 63, '  ', '  '],
#                      ['  ', 8, '  ', 16, '  ', 45, 59, 89, '  '],
#                      ['  ', '  ', '  ', 5, '  ', 17, 50, 68, 78]
#                     ]

card_human = Card()
card_human.card_create()

# -----------Тестовая карточка для человека-----------------
# card_human.card = [[25, 32, '  ', '  ', '  ', '  ', 37, 58, 87],
#                   [4, '  ', 33, '  ', 42, '  ', 75, '  ', 88],
#                   [19, '  ', '  ', '  ', 35, 38, '  ', 62, 85]
#                   ]

while True:
    card_computer.display_comp_card()
    card_human.display_human_card()
    barrel = bag_of_barrels.get_random_barrel()
    print(f'Новый бочонок: --{barrel}-- (осталось в мешке - {bag_of_barrels.get_barrels_left()} бочонков) ')

#    ---Подсказки оставил на всякий случай---
#    print("номер есть в карточке человека?",
#          card_human.check_barrel_is_exist_in_card(barrel)
#          )
#    print("номер есть в карточке компьютера?",
#          card_computer.check_barrel_is_exist_in_card(barrel)
#          )

    human.turn(human.cross_or_not(), card_human.check_barrel_is_exist_in_card(barrel), card_human)
    comp.turn(card_computer.check_barrel_is_exist_in_card(barrel), card_computer)
