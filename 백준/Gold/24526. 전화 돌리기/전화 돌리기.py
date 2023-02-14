import sys
from collections import deque
N, M = map(int, input().split())

out_graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
info = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    out_graph[b].append(a)
    indegree[a] += 1

Q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        Q.append(i)

while len(Q) > 0:
    u = Q.popleft()
    info[u] = True
    
    for i in out_graph[u]:
        indegree[i] -= 1
        if indegree[i] == 0:
            Q.append(i)
cnt = 0
for i in range(1, N + 1):
    if info[i]:
        cnt += 1
print(cnt)