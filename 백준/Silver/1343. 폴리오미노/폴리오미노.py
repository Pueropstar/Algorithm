from sys import stdin

input = stdin.readline

pol_1 = 'AAAA'
pol_2 = 'BB'

board = input()

first_board = board.replace('XXXX',pol_1)
sec_board = first_board.replace('XX',pol_2)

if 'X' in sec_board:
    print(-1)
else:
    print(sec_board)