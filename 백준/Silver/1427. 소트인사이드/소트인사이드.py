from sys import stdin

input = stdin.readline

N = input().strip()

num_N = int(N)

ans_arr = []
ans = 0
for i in range(len(N)-1, -1, -1):
    
    ans_arr.append(num_N//10**i)
    num_N = num_N%10**i

ans_arr.sort(reverse=True)

for i in range(len(ans_arr)):
    ans += ans_arr[i]*10**(len(ans_arr)-1-i)

print(ans)
