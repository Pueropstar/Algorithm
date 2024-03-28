from sys import stdin

input = stdin.readline

def dfs(graph, v, visited, count):

    visited[v] = True
    count+=1
    for i in graph[v]:
        if not visited[i]:
            count = dfs(graph, i, visited, count)
    return count

C = int(input())

N = int(input())

graph = [[] for _ in range(C+1)]

visited = [False] * (C+1)

count = 0

for _ in range(N):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

ans = dfs(graph, 1, visited, count)

print(ans-1)