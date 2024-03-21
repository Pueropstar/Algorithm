from sys import stdin

input = stdin.readline

N = int(input())

target = N

ans = []

for i in range(2,N+1):

    

    while(target % i == 0 and target // i  != 1):
        ans.append(i)
        target = target//i

    if (target % i == 0 and target // i  == 1):
        ans.append(i)

    
for i in ans:
    print(i)