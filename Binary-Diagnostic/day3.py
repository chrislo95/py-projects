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
least_common_counter = 0
most_common_counter = 0
ones_counter = 0
zeros_counter = 0
position_counter = 0
ones_list = []
zeros_list = []
ones_counter_least = 0
zeros_counter_least = 0
ones_list_least = []
zeros_list_least = []



with open('input.txt') as f:
    lines = f.readlines()

    for x in lines:
        last_list.extend(x)

    new_list_2 = [[x] for x in lines]
    new_list_3 = [[x] for x in lines]
    
    '''For loop for most common'''
    for x in range(12):
        for y in range(len(new_list_2)):

            if new_list_2[y][0][x] == '1':
                ones_list.append(new_list_2[y])
                ones_counter += 1
            if new_list_2[y][0][x] == '0':
                zeros_list.append(new_list_2[y])
                zeros_counter += 1

        if ones_counter > zeros_counter or ones_counter == zeros_counter:
            new_list_2 = ones_list
            ones_list = []
        if zeros_counter > ones_counter:
            new_list_2 = zeros_list
            zeros_list = []
        ones_counter = 0
        zeros_counter = 0

    '''For loop for least '''
    for x in range(12):
        for y in range(len(new_list_3)):
            if new_list_3[y][0][x] == '1':
                ones_list_least.append(new_list_3[y])
                ones_counter_least += 1
            if new_list_3[y][0][x] == '0':
                zeros_list_least.append(new_list_3[y])
                zeros_counter_least += 1

        if ones_counter_least < zeros_counter_least or ones_counter_least == zeros_counter_least:
            new_list_3 = zeros_list_least
            zeros_list_least = []
        if zeros_counter_least > ones_counter_least:
            new_list_3 = ones_list_least
            ones_list_least = []
        ones_counter_least = 0
        zeros_counter_least = 0

        if x == 1000:
            break

    print(new_list_2)
    print(new_list_3)
    print(len(new_list_2))

    len_list_number = len(last_list)

    '''First part of the question'''
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
        if gamma_list[11 - x] == 1:
            gamma_number = gamma_number + pow(2, x)

    print(gamma_number)
    print(epsi_number)
    final_number = epsi_number * gamma_number
    print(gamma_list)
    print(final_number)
    print(bit_list)
    


f.close()