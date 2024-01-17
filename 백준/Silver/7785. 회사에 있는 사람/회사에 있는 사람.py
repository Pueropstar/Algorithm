from collections import defaultdict
from sys import stdin

input = stdin.readline

N = int(input())

dict = defaultdict(int)

answer = []

for i in range(N):
    a,b = input().split()
    dict[a] = b

for a,b in dict.items():
    if b == 'enter':
        answer.append(a)

answer.sort(reverse=True)

for p in answer:
    print(p)
        