from sys import stdin

input = stdin.readline

T = int(input())

dp = [0 for _ in range(11)]

dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(T):
    
    N = int(input())

    for j in range(3,N+1):
        dp[j] = dp[j-1]+dp[j-2]+dp[j-3]

    print(dp[N])


