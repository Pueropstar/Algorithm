from sys import stdin

input = stdin.readline


list = []

for i in range(1,1001):
    for j in range(i):
        list.append(i)
        

a,b = map(int, input().split())


print(sum(list[a-1:b]))
    