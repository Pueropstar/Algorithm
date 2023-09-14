from sys import stdin

input = stdin.readline

N = int(input())

arr_grade = []

for i in range(N):
    name,*score = input().split()
    arr_grade.append((name,*map(int,score)))


sorted_arr = sorted(arr_grade, key = lambda x :(-x[1],x[2],-x[3],x[0]))


for i in sorted_arr:
    print(i[0])
