from os import linesep

tail_line_2 = 0
counter_2 = 0
counter_3 = 0
counter = 0
number_list = list(range(2000))
lol_number = 0
number_2 = 0

with open('input.txt') as f:
    lines = f.readlines()
    lines_length = len(lines)
    print(lines_length)
    print(lines[0])
    numer = int(lines[0])
    print(numer)

    for x in lines:
        lol_number = int(lines[counter_2])
        number_list.append(lol_number)
        counter_2 = counter_2 + 1

    for x in lines:
        number_2 = int(number_list[counter_3])
        if number_2 > tail_line_2:
            print(number_2)
            print(tail_line_2)
            counter = counter + 1
            counter_3 = counter_3 + 1
            tail_line_2 = number_2
        else:
            tail_line_2 = number_2
            counter_3 = counter_3 + 1

print(counter)

f.close()