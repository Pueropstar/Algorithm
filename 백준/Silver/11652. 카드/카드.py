from collections import defaultdict
from sys import stdin

input = stdin.readline

N = int(input())

arr = []
arr_ans = []
dict = defaultdict(int)

for i in range(N):
    num = int(input())
    dict[num] += 1

arr_tup = list(dict.items())
arr_tup.sort(key=lambda x:-x[1])
most = arr_tup[0][1]

for i in arr_tup:
    if most == i[1]:
        arr_ans.append(i[0])

arr_ans.sort()

print(arr_ans[0])
