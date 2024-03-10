from sys import stdin


upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
number = '1234567890'

while True:
    try:
        str = input()
        lower_count = 0
        upper_count = 0
        number_count = 0
        blank_count = str.count(' ')
        for i in str:
            if i in upper:
                upper_count+=1
            elif i in lower:
                lower_count+=1
            elif i in number:
                number_count+=1
        print(lower_count, upper_count, number_count, blank_count)
    except EOFError:
        break