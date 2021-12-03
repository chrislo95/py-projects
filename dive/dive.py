from os import linesep
lol_number = 0
number_list = []
counter_2 = 0
new_list = []
last_list = []
forward_check = "forward"
up_check = "up"
down_check = "down"
forward_count = 0
down_count = 0
up_count = 0
last_list_len = 0


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

    for x in new_list:
        last_list.extend(x)

    last_list_len = len(last_list)
    for x in range(last_list_len):
        if forward_check == last_list[x]:
            forward_count = forward_count + int(last_list[x+1])
            print(forward_count)

    print(last_list)


f.close()
