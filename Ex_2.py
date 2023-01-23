# 2. Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#     Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#     Все конфеты оппонента достаются сделавшему последний ход. 
#     Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#         a) Добавьте игру против бота
#         b) Подумайте как наделить бота "интеллектом"
# Ост(м+1)К
# m = 2021 % 29 # = 20

import random
import os
os.system('clear')


def check_number():
    number = int(input('Cколько конфет вы заберете со стола? Нужно ввести от 1 до 28: '))
    while number > 28 or number < 1:
        number = int(input('Введите число от 1 до 28! '))
    return number

def player_move(candy, move):
    if move == 1:
        move = 2
    elif move == 2:
        move = 1
    take_candy = check_number()
    candy -= take_candy
    return (take_candy, candy, move)

def who_move(move):
    if move == 1:
        return 'игрок'
    else:
        return 'компьютер'

def computer_move(difficulty, candy, take_candy):
    if difficulty == 1: # Легко. Бот в 70 % случаев действует наугад
        error = random.randint(1, 100)
        if error >= 30:
            take_candy = random.randint(1, 28)
        else:
            take_candy = candy - ((candy // 29) * 29)

    elif difficulty == 2: # Средний. Бот в 30 % случаях действует наугад
        error = random.randint(1, 100)
        if error <= 30:
            take_candy = random.randint(1, 28)
        else:
            take_candy = candy - ((candy // 29) * 29)
            if take_candy == 0:
                take_candy = random.randint(1, 28)

    elif difficulty == 3: # Трудно. Бот в 5 % случаях действует наугад
        error = random.randint(1, 100)
        if error <= 5:
            take_candy = random.randint(1, 28)
        else:
            take_candy = candy - ((candy // 29) * 29)
            if take_candy == 0:
                take_candy = random.randint(1, 28)
    print(f'Компьютер взял со стола {take_candy} конфет(ы).')
    candy -= take_candy
    return take_candy, candy


choice = int(input('С кем хотите сыграть? Если с компьютером то введите - 1, если с человеком то - 2: '))
candy = 250

if choice == 2:
    print(f'\nНа столе лежит {candy} конфет(а). Играют два игрока делая ход друг после друга.\n\
За один ход можно забрать не более чем 28 конфет. Побеждает тот кто сделает последний ход.')
    move = random.randint(1,2)
    print(f'\nПервым ходит игрок {move}')
    take_candy, candy, move = player_move(candy, move)

    while candy > 28:
        print(f'\nХод игрока - {move}. На столе осталось - {candy}')
        take_candy, candy, move = player_move(candy, move)      
    print(f'\nНа столе осталось {candy}. Победа {move} игрока')

else:
    print(f'\nНа столе лежит {candy} конфет(а). Вы играете против компьютера, делая ход друг за другом.\
\nЗа один ход можно забрать не более чем 28 конфет. Побеждает тот кто сделает последний ход.')
    choice_diff = int(input(f'\nВведите сложность игры, где 1 - легко, 2 - средне, а 3 - сложно: '))
    move = random.randint(1, 2)
    if move == 1:
        print(f'\nПервым ходит игрок')
        take_candy, candy, move = player_move(candy, move)
    else:
        print('\nПервым ходит компьютер') 
        take_candy = candy - ((candy // 29) * 29)
        candy -= take_candy
        move = 1
        print(f'Компьютер взял со стола {take_candy}.')

    while candy > 28:
        if move == 1:
            print(f'\nХод - {who_move(move)}а. На столе осталось - {candy}')
            take_candy, candy, move = player_move(candy, move)
            print(f'игрок взял {take_candy} конфет(ы)')
        else:
            print(f'\nХод - {who_move(move)}а. На столе осталось - {candy}')
            take_candy, candy = computer_move(choice_diff, candy, take_candy)
            move = 1

    print(f'\nНа столе осталось {candy}. Победа {who_move(move)}а')


