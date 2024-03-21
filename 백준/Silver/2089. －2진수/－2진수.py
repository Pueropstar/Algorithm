from sys import stdin

input = stdin.readline

ans = ''

N = int(input())

if N==0:
    print(0)
    exit

while(N!=0):
    ans = str(N%2)+ans
    if N%-2 !=0:
        
        N = (N//(-2))+1
    else:
        N = (N//(-2))
        
print(ans)
    