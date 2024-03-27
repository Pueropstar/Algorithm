from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

def dfs(y,x):
    
    if x<=-1 \
        or x>=w \
            or y<=-1 \
                or y>=h:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0

        dfs(y-1,x)
        dfs(y+1,x)
        dfs(y,x+1)
        dfs(y,x-1)
        dfs(y-1,x-1)
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)

        return True
    return False



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
            if dfs(i,j) == True:
                ans+=1
    print(ans)