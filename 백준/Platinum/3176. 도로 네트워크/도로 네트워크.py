import sys
sys.setrecursionlimit(10**5)
N = int(input())

graph = [[] for _ in range(N + 1)]
parent = [[0]*(N + 1) for _ in range(18)]
mini = [[int(1e9)]*(N + 1) for _ in range(18)]
maxi = [[0]*(N + 1) for _ in range(18)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dfs(node, l):
    visited[node] = True
    depth[node] = l

    for n, w in graph[node]:
        if visited[n]:
            continue
        mini[0][n] = w
        maxi[0][n] = w
        parent[0][n] = node
        dfs(n, l + 1)

def lca(a, b):
    ans = int(1e9)
    ans2 = 0
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(17, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            ans = min(ans, mini[i][b])
            ans2 = max(ans2, maxi[i][b])
            b = parent[i][b]

    if a == b:
        return [a, ans, ans2]

    for i in range(17, -1, -1):
        if parent[i][a] != parent[i][b]:
            ans = min(ans, mini[i][a], mini[i][b])
            ans2 = max(ans2, maxi[i][a], maxi[i][b])
            a = parent[i][a]
            b = parent[i][b]

    return [parent[0][a], min(ans, mini[0][a], mini[0][b]), max(ans2, maxi[0][a], maxi[0][b])]

dfs(1, 0)

for i in range(1, 17):
    for j in range(1, N + 1):
        mini[i][j] = min(mini[i - 1][j], mini[i - 1][parent[i - 1][j]])
        maxi[i][j] = max(maxi[i - 1][j], maxi[i - 1][parent[i - 1][j]])
        parent[i][j] = parent[i - 1][parent[i - 1][j]]

K = int(input())

for _ in range(K):
    p, q = map(int, sys.stdin.readline().split())
    _, ans, ans2 = lca(p, q)
    print(ans, ans2)



