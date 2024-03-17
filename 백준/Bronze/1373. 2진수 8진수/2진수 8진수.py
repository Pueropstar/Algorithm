import math
from sys import stdin

input = stdin.readline

N = input().strip()

flag = 0
ans = ''

sub_flag = 0
for i in range(len(N)):
    
    if(flag == 3):
        ans  = str(sub_flag)+ ans
        flag = 0
        sub_flag = 0
        
    
    sub_flag += int(int(N[len(N)-1-i])*pow(2,flag))
    
    
    flag+=1
    
ans  = str(sub_flag)+ ans
print(ans)
