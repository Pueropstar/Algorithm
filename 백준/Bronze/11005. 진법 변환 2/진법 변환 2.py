from sys import stdin

input = stdin.readline

arr_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = ''

N,B = map(int,input().split())


while N//B !=0:
    ans = arr_num[N%B]+ ans
    
    N = N//B

ans = arr_num[N] + ans


print(ans)
