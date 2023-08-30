
from sys import stdin
import decimal
from collections import Counter

input = stdin.readline


n = int(input())

def average(arr):
    result = 0
    for i in arr:
        result+=i
    
    if result < 0:
        return int(result/n-0.5)
    else:
        return int(result/n+0.5)

def median(arr):
    mid = int(n/2)
    sorted_arr = sorted(arr)
    return sorted_arr[mid]

def most_frequent(arr):
    fre_ary = []
    dict = Counter(arr)
    most = dict.most_common()
    max = most[0][1]
    
    
    for i in most:
        
        if i[1] == max:
            fre_ary.append(i[0])
            
    fre_ary_len = len(fre_ary)


    if fre_ary_len == 1:
        return fre_ary[0]
    else:
        return sorted(fre_ary)[1]
    
def arr_range(arr):

    sorted_arr = sorted(arr)
    return (sorted_arr[-1]-sorted_arr[0])

arr = []
for i in range(n):
    num = int(input())
    arr.append(num)


print(average(arr))
print(median(arr))
print(most_frequent(arr))
print(arr_range(arr))

