from sys import stdin

input = stdin.readline

N = int(input())

for i in range(N):
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    C = int(input())

    while (C>=25):
        C-=25
        quarter+=1
    while (C>=10):
        C-=10
        dime +=1
    while(C>=5):
        C-=5
        nickel+=1
    while(C>=1):
        C-=1
        penny+=1

    print(quarter, dime, nickel, penny)



