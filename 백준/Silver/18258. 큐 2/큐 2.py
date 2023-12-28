from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

command_arr = []
num_arr = deque()

for i in range(N):
    command_arr = input().strip().split()
    
    if command_arr[0]=='push':
        num_arr.append(command_arr[1])
    elif command_arr[0]== 'pop':
        if len(num_arr):
            print(num_arr.popleft())
        else:
            print(-1)
    elif command_arr[0]== 'size':
        print(len(num_arr))
    elif command_arr[0] == 'empty':
        if len(num_arr):
            print(0)
        else:
            print(1)
    elif command_arr[0] == 'front':
        if len(num_arr):
            print(num_arr[0])
        else:
            print(-1)
    elif command_arr[0] == 'back':
        if len(num_arr):
            print(num_arr[-1])
        else:
            print(-1)

