from sys import stdin
from collections import Counter
input = stdin.readline

room_number = input()

arr = Counter(room_number).most_common()

arr_69 =[]
arr_x = []


for i in range(len(arr)-1):
    if arr[i][0] =='6' or arr[i][0] =='9':
        arr_69.append(arr[i][1])
    else:
        arr_x.append(arr[i][1])

if arr_x:
    max_x = max(arr_x)
else:
    max_x = -1

sum_69 = sum(arr_69)

if sum_69 %2 ==0:
    print(max(sum_69//2, max_x))
else:
    print(max(sum_69//2+1,max_x))


