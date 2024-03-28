from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

input = stdin.readline

# 상 하 좌 우

def dfs(y, x):
    dx = [0, 0, -1, 1] 
    dy = [-1, 1, 0, 0]
        
    field[y][x] = 0

    for i in range(len(dx)):
        nx = dx[i]+x
        ny = dy[i]+y

        if 0<=ny<N and 0<=nx<M and field[ny][nx] == 1:
            dfs(ny,nx)
        
T = int(input())

for _ in range(T):

    ans = 0

    M,N,K = map(int,input().split()) # N 행 M열

    field = [[0]*(M)for _ in range(N)]

    for _ in range(K):
        x,y = map(int,input().split())
        field[y][x] = 1

    for i in range(N):
        for j in range(M):

            if field[i][j] == 1:
                dfs(i,j)
                ans+=1
    print(ans)
            