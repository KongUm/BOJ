import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [[0]*(N + 1) for _ in range(18)]
level = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, l):
    visited[node] = True
    level[node] = l

    for n in graph[node]:
        if visited[n]:
            continue
        parent[0][n] = node
        dfs(n, l + 1)

def lca(a, b):
    if level[a] > level[b]:
        a, b = b, a
    for i in range(17, -1, -1):
        if level[b] - level[a] >= (1 << i):
            b = parent[i][b]

    if a == b:
        return a
    for i in range(17, -1, -1):
        if parent[i][a] != parent[i][b]:
            a = parent[i][a]
            b = parent[i][b]
    return parent[0][a]


dfs(1, 0)

for i in range(1, 18):
    for j in range(1, N + 1):
        parent[i][j] = parent[i - 1][parent[i - 1][j]]

M = int(input())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))



