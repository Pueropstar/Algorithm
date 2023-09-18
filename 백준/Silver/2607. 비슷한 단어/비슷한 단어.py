# import copy
from sys import stdin
from collections import Counter
input = stdin.readline

N = int(input())

answer = 0

first_word = list(input().rstrip())

for i in range(N-1):
    count = 0
    copy_first = first_word[:]
    # copy_first = copy.deepcopy(first_word)
    word = input().rstrip()

    for j in word:

        if j in copy_first:
            copy_first.remove(j)
        else:
            count+=1

    if count<=1 and len(copy_first)<=1 :
        answer+=1

print(answer)