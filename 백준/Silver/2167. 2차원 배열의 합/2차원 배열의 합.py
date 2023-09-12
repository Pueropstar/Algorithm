from sys import stdin

input = stdin.readline

height,width = map(int, input().split())

arr = []

for i in range(height):
        number = list(input().split())
        arr.append(number)

arr_prefix = [[0 for j in range(width)] for i in range(height)]


for j in range(width):
        for k in range(height):

                if k==0:
                        arr_prefix[k][j] = int(arr[k][j])
                
                else:
                        arr_prefix[k][j] = int(arr[k][j]) + int(arr_prefix[k-1][j])
        
N = int(input())

for i in range(N):
        answer = 0 

        pos_i,pos_j,pos_x,pos_y = map(int, input().split())
        
        if pos_i == pos_x and pos_j == pos_y:
                answer = arr[pos_i-1][pos_j-1]
                
        elif pos_i == pos_x:
                for j in range(pos_j-1, pos_y,1):
                        answer+=int(arr[pos_i-1][j])
        elif pos_j == pos_y:
                for j in range(pos_i-1, pos_x,1):
                        answer+=int(arr[j][pos_j-1])
        else:
                if pos_i-1 == 0:
                        for j in range(pos_j-1,pos_y,1):
                                answer+=arr_prefix[pos_x-1][j]
                else:
                        for j in range(pos_j-1,pos_y,1):
                                answer+=arr_prefix[pos_x-1][j]-arr_prefix[pos_i-2][j]
        print(answer)
