from sys import stdin

input = stdin.readline

N = int(input())

input_arr = map(int,input().split())

ans = 0

for i in input_arr:
    flag = 0
    for j in range(1,i+1):

        if i%j == 0:
            flag+=1
    
    if flag==2:
        ans+=1

print(ans)

