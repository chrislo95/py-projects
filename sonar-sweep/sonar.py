from os import linesep


tail_line = "nothing"
counter = 0

with open('input.txt') as f:
    lines = f.readlines()
    print(lines)
    lines_length = len(lines)
    for lines_length in lines :
        if lines is lines[counter] > counter :
            counter = counter + 1
            tail_line = lines
        else :
            tail_line = lines

print(counter)





f.close()