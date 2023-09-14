from sys import stdin

input = stdin.readline

N = int(input())

arr_word = []

for i in range(N):
    word = input().strip()
    stack = ""
    for j in word:
        
        if not j.isalpha():
            stack+=j
        elif j.isalpha() and stack != "":
            arr_word.append(int(stack))
            stack=""
    if stack!= "":
        arr_word.append(int(stack))

arr_word.sort()

for i in arr_word:
    print(i)


