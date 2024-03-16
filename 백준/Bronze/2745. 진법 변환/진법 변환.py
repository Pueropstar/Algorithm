import math
from sys import stdin

input = stdin.readline

arr_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N,B = input().split()

ans = 0

for i in range(0, len(N),1):
    
    ans += (arr_num.index(N[len(N)-1-i])* math.pow(int(B),i))
    
print(int(ans))
