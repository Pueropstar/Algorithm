from sys import stdin
input= stdin.readline
 

N = int(input())

for i in range(N):
    answer = 1
    dict_wear = {}
    wear_count = int(input())
    
    for j in range(wear_count):
        a,b = input().split()
        if dict_wear.get(b):
            dict_wear[b].append(a)
        else:
            dict_wear[b]=[a]
    dict_keys = list(dict_wear.keys())
    
    key_len = len(dict_keys)
    if len(dict_keys) == 0:
        print(0)
    else:
        for k in range(key_len):
            answer*=(len(dict_wear.get(dict_keys[k]))+1)
        print(answer-1)
