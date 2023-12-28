from sys import stdin

input = stdin.readline

count_a = 0
count_b = 0
count_c = 0

N = int(input())

while(N>=300):
    N-=300
    count_a+=1

while (N>=60):
    N-=60
    count_b+=1

while (N>=10):
    N-=10
    count_c+=1

if (N!=0):
    print(-1)
else:
    print(count_a, count_b, count_c)
