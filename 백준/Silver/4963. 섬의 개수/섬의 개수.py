from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

# 상 하 좌 우 왼위 오위 왼아래 오아래
def dfs(y,x):

    dx =[0, 0, -1, 1, -1, 1, -1, 1]
    dy =[-1, 1, 0, 0, -1, -1, 1, 1]


    graph[y][x] = 0

    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<w \
            and 0<=ny<h \
                and graph[ny][nx] == 1:
            dfs(ny,nx)

while True:

    ans = 0 
    graph = []

    w,h = map(int,input().split())
    if w == 0\
        or h == 0 :
        break

    for _ in range(h):
        graph.append(list(map(int,input().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                ans+=1
    print(ans)