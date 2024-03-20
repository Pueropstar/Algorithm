from sys import stdin

input = stdin.readline


A,B = map(int, input().split())

m = int(input())

arr_input = input().split()

arr_num ='0123456789ABCDEFGHIJKLMNOPQRST'

decimal_num = 0

ans = []
for i in range(m):
    decimal_num +=int(arr_input[i])*pow(A,m-1-i)

while decimal_num // B > 0:
    ans.append(decimal_num%B)
    decimal_num = decimal_num//B

ans.append(decimal_num)

for i in range(len(ans)-1,-1,-1):
    print(ans[i],end=' ')
    
