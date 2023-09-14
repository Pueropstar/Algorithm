from sys import stdin

input = stdin.readline

N = int(input())

arr_grade = []

for i in range(N):
    grade = input().split()
    arr_grade.append(grade)

sorted_arr = sorted(arr_grade, key = lambda x :(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in sorted_arr:
    print(i[0])
