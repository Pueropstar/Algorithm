from sys import stdin

input = stdin.readline

N = int(input())

source_arr = list(map(int,input().split()))
source_set= set(source_arr)
sorted_arr = sorted(list(source_set))

for i in range(len(sorted_arr)):
    print(sorted_arr[i], end=' ')


