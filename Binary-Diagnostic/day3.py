from os import linesep
from typing import final

last_list = []
bit_list = []
gamma_list = []
zero_counter = 0
one_counter = 0
final_number = 0
gamma_number = 0
epsi_number = 0


with open('input.txt') as f:
    lines = f.readlines()

    for x in lines:
        last_list.extend(x)

    len_list_number = len(last_list)
    print(len_list_number)
    
    for x in range(12):
        for y in range(len_list_number):
            if y == 1000:
                break

            if last_list[(13*y)+x] == '0':
                zero_counter = zero_counter + 1

            if last_list[(13*y)+x] == '1':
                
                one_counter = one_counter + 1
            
        
        if zero_counter > one_counter:
            bit_list.append(0)
        else:
            bit_list.append(1)
        print(zero_counter)
        print(one_counter)    
        zero_counter = 0
        one_counter = 0

    for x in range(12):
        if bit_list[x] == 1:
            gamma_list.append(0)
        else:
            gamma_list.append(1)

    for x in range(12):
        if bit_list[11 - x] == 0:
            continue
        if bit_list[11 - x] == 1:
            epsi_number = epsi_number + pow(2, x)

    for x in range(12):
        if gamma_list[11 - x] == 0:
            continue
        if bit_list[11 - x] == 1:
            gamma_number = gamma_number + pow(2, x)

    print(gamma_number)
    print(epsi_number)
    final_number = epsi_number * gamma_number
    print(gamma_list)
    print(final_number)
    print(bit_list)
    

f.close()