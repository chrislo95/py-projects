from os import linesep
lol_number = 0
number_list = []
counter_2 = 0
new_list = []



with open('input.txt') as f:
    lines = f.readlines()

    """
    new_list = lines[1].split()
    print(new_list[0])
    print(new_list[1])
    print(lines[2].split()

    """
    list_ln = len(lines)

    """cast numbers to int"""
    for x in range(list_ln):
        new_list.append(lines[x].split())


        
f.close()