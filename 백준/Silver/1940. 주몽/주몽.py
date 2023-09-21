from sys import stdin

input = stdin.readline

N = int(input())

M = int(input())

arr = list(map(int,input().split()))
arr.sort()
prefix_sum = 0
result = []
for i in range(N):
    start = i 
    end = len(arr)-1

    while start<end:
        prefix_sum = arr[start]+arr[end]
    
        if prefix_sum > M:
            end-=1
            
        elif prefix_sum < M:
            start+=1
        else:
            result.append((start,end))
            break

result_set = set(result)
print(len(result_set))