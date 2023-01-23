# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import os
os.system('clear')

with open ('Ex_4_Sem5_HW_Start.txt', 'w') as data:
    data.write('aattttGGnnnW')

path = 'Ex_4_Sem5_HW_Start.txt'
data = open(path, 'r')
for i in data:
    string_my = i
data.close

count = 1
string_my += ' '
file_string = ''
lst = []
for i in range(len(string_my)-1):
    if string_my[i] != string_my[i+1]:
        if count == 1:
            lst.append(string_my[i])
            count = 1
        elif count == 2:
            lst.append(string_my[i] + string_my[i])
            count = 1
        else:
            lst.append(str(count)+string_my[i])
            count = 1
    else:
        count += 1

file_string = ''.join(lst)
print(file_string)
with open ('Ex_4_Sem5_HW_Start.txt', 'a') as data:
    data.write(f' -> {file_string}')

file_string += ' '
with open ('Ex_4_Sem5_HW_Finish.txt', 'w') as data:
    data.write(file_string)
result_str = ''
for i in range(len(file_string)-1):
    if file_string[i].isdigit():
        result_str += (int(file_string[i])-1) * file_string[i+1]
    if file_string[i].isalpha():
        result_str += file_string[i]
print(result_str)


with open ('Ex_4_Sem5_HW_Finish.txt', 'a') as data:
    data.write(f' -> {result_str}')