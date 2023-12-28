from sys import stdin

input = stdin.readline

S = input().strip()

str_len = len(S)

sliced_arr = []
for i in range(str_len):
    sliced = S[i:str_len]
    sliced_arr.append(sliced)

for j in sorted(sliced_arr):
    print(j)