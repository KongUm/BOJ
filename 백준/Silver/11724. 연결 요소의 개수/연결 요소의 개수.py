import sys
from collections import deque
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

def bfs(n):
    Q = deque()
    visited[n] = True
    Q.append(n)
    while len(Q) > 0:
        u = Q.popleft()
        for i in graph[u]:
            if visited[i] == False:
                Q.append(i)
                visited[i] = True

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N + 1):
    if visited[i] == False:
        bfs(i)
        cnt += 1
print(cnt)