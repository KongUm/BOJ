import sys
from collections import deque

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
indegree = [0]*(V+1)

for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
   
path = []
Q = deque()
for i in range(1,V+1):
    if indegree[i] == 0:
        Q.append(i)
while len(Q) > 0:
    u = Q.popleft()
    path.append(u)
    
    for i in graph[u]:
        indegree[i] -= 1
        if indegree[i] == 0:
            Q.append(i)
for i in path:
    print(i, end = " ")