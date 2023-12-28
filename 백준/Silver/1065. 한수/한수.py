from sys import stdin

input = stdin.readline

N = int(input())

count = 0
for i in range(1,N+1,1):
    
    if i<10:
        count+=1
    elif i>=10 and i<100:
        count+=1
    elif i>=100:
        str_num = str(i)
        common_diff = int(str_num[1])-int(str_num[0])
        for i in range(1,len(str_num)-1):
            if (int(str_num[i+1])-int(str_num[i])) == common_diff:
                count+=1
print(count)




