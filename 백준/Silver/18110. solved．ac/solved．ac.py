import sys
num = int(input())
input = sys.stdin.readline
list = []

for _ in range(num):
    a = int(input())    
    list.append(a)

list.sort()

cut = int((num*0.15)+0.5)


for i in range(cut):
    list[0+i]=0
    list[-1+(-i)]=0

count = 0 
result = 0 

for i in list:

    if(i!=0):
        count+=1
        result += i

if(count==0):
    print(int(result+0.5))
else:
    print(int((result/count)+0.5))
