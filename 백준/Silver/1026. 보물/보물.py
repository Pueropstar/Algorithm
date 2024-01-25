from sys import stdin

input = stdin.readline

N = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))


ans = 0

for i in range(N):
    ans += (min(a)*max(b))
    a.remove(min(a))
    b.remove(max(b))
    
print(ans)