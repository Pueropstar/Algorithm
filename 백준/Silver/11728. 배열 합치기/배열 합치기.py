from sys import stdin

input = stdin.readline

N,M = map(int,input().split())

arr_a = list(map(int,input().split()))

arr_b = list(map(int,input().split()))

ans = sorted(arr_a+arr_b)
for i in ans:
    print(i , end=" ")
