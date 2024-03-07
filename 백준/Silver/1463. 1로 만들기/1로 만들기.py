from sys import stdin

input = stdin.readline

N = int(input())

dp = [0 for i in range(N+1)]

for i in range(2,N+1,1):
    dp[i] = dp[i-1]+1

    if (i%2==0):
        dp[i] = min(dp[i], dp[i//2]+1)
    if (i%3==0):
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])

# 6 의 배수일때 생각 안함 때문에 elif가 아닌 if를 써야함