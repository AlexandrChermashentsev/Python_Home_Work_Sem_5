# 3. Создайте программу для игры в ""Крестики-нолики"" 3x3. Консольный граф.интерфейс

import os
import random
os.system('clear')

def victory_condition(list_my) -> bool:
    if  (list_my[0] == ' X ' and list_my[1] == ' X ' and list_my[2] == ' X ') or \
        (list_my[3] == ' X ' and list_my[4] == ' X ' and list_my[5] == ' X ') or \
        (list_my[6] == ' X ' and list_my[7] == ' X ' and list_my[8] == ' X ') or \
        (list_my[0] == ' X ' and list_my[3] == ' X ' and list_my[6] == ' X ') or \
        (list_my[1] == ' X ' and list_my[4] == ' X ' and list_my[7] == ' X ') or \
        (list_my[2] == ' X ' and list_my[5] == ' X ' and list_my[8] == ' X ') or \
        (list_my[0] == ' X ' and list_my[4] == ' X ' and list_my[8] == ' X ') or \
        (list_my[6] == ' X ' and list_my[4] == ' X ' and list_my[2] == ' X '):
        print('Победил Игрок 1')
        return False
    elif (list_my[0] == ' 0 ' and list_my[1] == ' 0 ' and list_my[2] == ' 0 ') or \
        (list_my[3] == ' 0 ' and list_my[4] == ' 0 ' and list_my[5] == ' 0 ') or \
        (list_my[6] == ' 0 ' and list_my[7] == ' 0 ' and list_my[8] == ' 0 ') or \
        (list_my[0] == ' 0 ' and list_my[3] == ' 0 ' and list_my[6] == ' 0 ') or \
        (list_my[1] == ' 0 ' and list_my[4] == ' 0 ' and list_my[7] == ' 0 ') or \
        (list_my[2] == ' 0 ' and list_my[5] == ' 0 ' and list_my[8] == ' 0 ') or \
        (list_my[0] == ' 0 ' and list_my[4] == ' 0 ' and list_my[8] == ' 0 ') or \
        (list_my[6] == ' 0 ' and list_my[4] == ' 0 ' and list_my[2] == ' 0 '):
        print('Победил Игрок 2')
        return False
    else: return True

def take_point(string, number, number_player):
    if number_player == 1:
        symbol = 'X'
        str_list = string.split('|')
        str_list[number-1] = f' {symbol} '
        number_player = 2
    else: 
        symbol = '0'
        str_list = string.split('|')
        str_list[number-1] = f' {symbol} '
        number_player = 1
    string = '|'.join(str_list)
    os.system('clear')
    return string, number_player


string_1 = ' 1 | 2 | 3 '
string_2 = ' 4 | 5 | 6 '
string_3 = ' 7 | 8 | 9 '
all_string = string_1.split('|') + string_2.split('|') + string_3.split('|')
print(all_string)
print(f'{string_1}\n{string_2}\n{string_3}')
move = random.randint(1,2)
i = 0

while victory_condition(all_string):
    if i == 9:
        print('Ничья')
        break
    u_numb = int(input(f'Ходит игрок {move}.\nНа какую позицию поставить ваш знак? 1-9: '))
    if 0 < u_numb <= 3 and all_string[u_numb-1] != ' X '\
and all_string[u_numb-1] != ' 0 ':

        string_1, move = take_point(string_1, u_numb, move)
        print(f'{string_1}\n{string_2}\n{string_3}')
        all_string = string_1.split('|') + string_2.split('|') + string_3.split('|')
        i += 1
    
    elif 3 < u_numb <= 6 and all_string[u_numb-1] != ' X '\
and all_string[u_numb-1] != ' 0 ':
        string_2, move = take_point(string_2, u_numb-3, move)
        print(f'{string_1}\n{string_2}\n{string_3}')
        all_string = string_1.split('|') + string_2.split('|') + string_3.split('|')
        i += 1

    elif 6 < u_numb <= 9 and all_string[u_numb-1] != ' X '\
and all_string[u_numb-1] != ' 0 ':
        string_3, move = take_point(string_3, u_numb-6, move)
        print(f'{string_1}\n{string_2}\n{string_3}')
        all_string = string_1.split('|') + string_2.split('|') + string_3.split('|')
        i += 1

    else: print('Введите другое число. Эта ячейка занята')