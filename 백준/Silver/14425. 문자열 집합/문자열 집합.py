from sys import stdin

input = stdin.readline

N,M = map(int,input().split())

source_set = set()

ans = 0 

for i in range(N):
    source_str = input()
    source_set.add(source_str)


for j in range(M):
    target_str = input()
    if target_str in source_set:
        ans+=1

print(ans)