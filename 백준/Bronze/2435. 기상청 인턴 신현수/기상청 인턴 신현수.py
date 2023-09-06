from sys import stdin

input = stdin.readline

n,k = map(int,input().split())

arr_temper = input().split()

arr_prefix = []

for i in range(len(arr_temper)):

    if i==0:
        arr_prefix.append(int(arr_temper[0]))
    else:
        arr_prefix.append(int(arr_prefix[i-1])+int(arr_temper[i]))

arr_sum_temper = []

i = 0
while (i+k)<=len(arr_temper):
    if i==0:
        arr_sum_temper.append(arr_prefix[k-1])
    else:
        arr_sum_temper.append(arr_prefix[k+i-1]-arr_prefix[i-1])
    
    i+=1

print(max(arr_sum_temper))