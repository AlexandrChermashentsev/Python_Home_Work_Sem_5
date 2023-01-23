import random
import os
os.system('clear')

vvod = 'aaabccccCCaB' #input()
if len(vvod) > 1:
    count = 1
    prev = ''
    lst = []
    for i in vvod:
        if i != prev:
            if prev:
                entry = ''
                entry = str(count) + prev
                lst.append(entry)
            count = 1
            prev = i
        else:
                count += 1
    else:
        entry = str(count) + i
        lst.append(entry)
    edinici = ''.join(lst)
    x = ''
    for i in edinici:
        if i != '1':
            x = x + i
    print(x)
else:
    print(vvod)
