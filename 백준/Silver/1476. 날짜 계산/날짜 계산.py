import time
from sys import stdin


input = stdin.readline


E,S,M = map(int,input().split())

count = 0
inc_E=1
inc_S=1
inc_M=1

while(1):
    count+=1
    if inc_E == E and inc_M == M and inc_S ==S:
        break
    
    inc_E+=1
    inc_S+=1
    inc_M+=1
    
    if inc_E==16:
        inc_E=1
    if inc_S ==29:
        inc_S = 1
    if inc_M ==20:
        inc_M =1

print(count)


    