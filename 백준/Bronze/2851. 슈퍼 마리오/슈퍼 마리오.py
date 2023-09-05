from sys import stdin

input = stdin.readline

arr = []
for i in range(10):
    a = int(input())
    arr.append(a)


arr_prefix = []
for j in range(10):
    if j == 0:
        arr_prefix.append(arr[j])
    else:
        arr_prefix.append(arr_prefix[j-1]+arr[j])

min = 1000000
index = 0

for i in range(len(arr_prefix)):
    if abs(arr_prefix[i]-100)<=min:
        min = abs(arr_prefix[i] - 100)
        index = i
    
print(arr_prefix[index])