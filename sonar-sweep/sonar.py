from os import linesep

tail_line_2 = 0
counter_4 = 0
counter_2 = 0
counter_3 = 0
counter = 0
number_list = []
lol_number = 0
number_2 = 0
sum_list = []
sum_number = 0
counter_sum = 0
sum_counter = 0
tail_sum_number = 0

with open('input.txt') as f:
    lines = f.readlines()
    lines_length = len(lines)
    """print(lines_length)
    print(lines[0])
    numer = int(lines[0])
    print(numer)"""

    for x in lines:
        lol_number = int(lines[counter_2])
        number_list.append(lol_number)
        counter_2 = counter_2 + 1

    for x in number_list:
        if counter_4 == len(number_list) - 2:
            break

        sum_number = number_list[counter_4 + 2] + number_list[counter_4 + 1] + number_list[counter_4]

        if sum_number > tail_sum_number:
            print(tail_sum_number)
            sum_counter = sum_counter + 1
            counter_4 = counter_4 + 1
            tail_sum_number = sum_number
        else:
            counter_4 = counter_4 + 1
            tail_sum_number = sum_number
        """sum_list.append(sum_number)
        counter_4 = counter_4 + 1"""
        
    for x in lines:
        number_2 = int(number_list[counter_3])
        if number_2 > tail_line_2:
            counter = counter + 1
            counter_3 = counter_3 + 1
            tail_line_2 = number_2
        else:
            tail_line_2 = number_2
            counter_3 = counter_3 + 1
    


print(counter - 1)
print(sum_counter - 1)

f.close()