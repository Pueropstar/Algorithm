from sys import stdin

input = stdin.readline

word = input().strip()


word_len = len(word)

arr = []
for i in range(1,word_len-1):
    
    for j in range(word_len-2-i+1,0,-1):
        
        first= word[0:i]
        second= word[i:i+j]
        third= word[i+j:word_len]

        # print(first, second, third)
        arr.append(first[::-1]+second[::-1]+third[::-1])
    

sorted_arr = sorted(arr)


# print(sorted_arr)
print(sorted_arr[0])


# 1/6/1 1/6/1
# 2/5/1 1/5/2
# 3/4/1 1/4/3
# 4/3/1 1/3/4
# 5/2/1 1/2/5
# 6/1/1 1/1/6


# 1/5/1 1/5/1 1/5/2 1/4/2 1/3/3 1/2/4 1/1/5
# 2/4/1 1/4/2 2/4/2 2/5/1 2/2/4 2/3/3
# 3/3/1 1/3/3 3/3/2 3/4/1 3/2/3 3/1/4 
# 4/2/1 1/2/4 4/3/1 4/2/2 4/1/3 
# 5/1/1 1/1/5 5/2/1 5/1/2
            # 6/1/1 