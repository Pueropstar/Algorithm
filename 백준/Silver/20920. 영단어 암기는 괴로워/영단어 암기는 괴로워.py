from sys import stdin
from collections import Counter

input = stdin.readline

N,M = map(int,input().split())

arr = []

for i in range(N):
    word = input().strip()
    len_word = len(word)
    if len_word >= M:
        arr.append(word)

dict_counter = Counter(arr).most_common()

sorted_arr = sorted(dict_counter,key = lambda x : (-x[1],-len(x[0]),x[0]))

for i in sorted_arr:
    print(i[0])

        
