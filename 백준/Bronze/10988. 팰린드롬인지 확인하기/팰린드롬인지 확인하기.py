from sys import stdin

input = stdin.readline

word = input().strip()

arr_word = []
for i in range(len(word)):
    arr_word.append(word[i])
word_len = len(word)
reverse = arr_word[::-1]

count = 0

for i in range(word_len):

    if arr_word[i] != reverse[i]:
        count +=1
        break
        
if count !=0:
    print(0)
else:
    print(1)

