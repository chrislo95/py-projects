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
final_result = 0


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
            forward_count = forward_count + int(last_list[x + 1])
        elif down_check == last_list[x]:
            down_count = down_count + int(last_list[x + 1])
        elif up_check == last_list[x]:
            up_count = up_count + int(last_list[x + 1])

    """print(last_list)"""

    final_result = down_count - up_count
    final_result = final_result * forward_count

    print(final_result)


f.close()
