num = int(input())
result = 1
answer = 0

def facto(n):
    global result 
    if n==0:
        result = result*1
        return result
    result = result*n
    return facto(n-1)

word = str(facto(num))
wordlen = len(word)

for i in range(wordlen-1,-1,-1):
    if (word[i]=='0'):
        answer+=1
    else:
        break

print(answer)        


