from collections import deque
from sys import stdin; input = stdin.readline

def bfs(start):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N,M = map(int,input().split())

visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]

ans = 0

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        ans+=1
print(ans)

