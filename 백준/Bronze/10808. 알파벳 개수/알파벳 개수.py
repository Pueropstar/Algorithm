from collections import defaultdict
from sys import stdin

input = stdin.readline

arr = [0 for i in range(26)]

S = input().strip()

for i in range(len(S)):
    arr[ord(S[i])-97] +=1

for i in arr:
    print(i,end=" ")

