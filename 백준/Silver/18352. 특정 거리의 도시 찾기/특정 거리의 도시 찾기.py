from collections import deque
from sys import stdin

input = stdin.readline

def bfs(start,graph,distance):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for new_node in graph[v]:
            if distance[new_node] == -1:
                distance[new_node] = distance[v] + 1
                queue.append(new_node)
                
N, M, K, X = map(int,input().split())

graph = [[]for _ in range(N+1)]

distance = [-1] * (N+1)

distance[X] = 0

for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)


bfs(X, graph, distance)

isExist = False

for i in range(len(distance)):
    
    if distance[i] == K:
        print(i)
        isExist = True

if not isExist:
    print(-1)    
    