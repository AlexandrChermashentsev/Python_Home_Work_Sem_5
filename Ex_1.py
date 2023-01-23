# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
import os
os.system('clear')

my_str = 'Абв! свыьлц Остволт абвыдц'
if 'абв' in  my_str:
    new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
    print(new_str)

