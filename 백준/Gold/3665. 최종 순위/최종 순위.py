import sys
from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    team = list(map(int, sys.stdin.readline().split()))
    M = int(input())
    changed = [set() for _ in range(N + 1)]

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        changed[a].add(b)
        changed[b].add(a)

    graph = [[] for _ in range(N + 1)]
    indegree = [0]*(N + 1)

    for i in range(N):
        for j in range(i + 1, N):
            if team[i] in changed[team[j]] or team[j] in changed[team[i]]:
                graph[team[j]].append(team[i])
                indegree[team[i]] += 1
            else:
                graph[team[i]].append(team[j])
                indegree[team[j]] += 1
    path = []
    Q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            Q.append(i)

    while len(Q) > 0:
        u = Q.popleft()
        path.append(u)

        for i in graph[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)
                
    if len(path) < N:
        print("IMPOSSIBLE")
    else:
        for i in path:
            print(i, end=" ")