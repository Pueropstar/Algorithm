from sys import stdin

input = stdin.readline

a,b = input().split()

arr_a = []
arr_b = []

for i in a:
    arr_a.append(i)
for j in b:
    arr_b.append(j)
    
arr_a.reverse()
arr_b.reverse()

rev_x = ''
rev_y = ''
for i in arr_a:
    rev_x+=i
for j in arr_b:
    rev_y += j
    
rev_sum = str(int(rev_x) + int(rev_y))

arr_sum = []
for i in rev_sum:
    arr_sum.append(i)

arr_sum.reverse()

result = ''

for i in arr_sum:
    result+=i

print(int(result))