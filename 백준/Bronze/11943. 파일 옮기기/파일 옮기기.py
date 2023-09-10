
arr_first = []
arr_second = []

answer = 0
for i in range(2):
    
    apple,orange = map(int, input().split())
    if i == 0:
        arr_first.append(apple)
        arr_first.append(orange)
    else:
        arr_second.append(apple)  
        arr_second.append(orange)  

if arr_first[0]+arr_second[1]>= arr_first[1]+arr_second[0]:
    answer += (arr_first[1]+arr_second[0])
else:
    answer += (arr_first[0]+arr_second[1])
    
print(answer)