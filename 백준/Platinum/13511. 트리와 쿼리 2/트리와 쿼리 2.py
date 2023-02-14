import sys
sys.setrecursionlimit(10 ** 5)
N = int(input())

graph = [[] for _ in range(N + 1)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)
parent = [[0]*(N + 1) for _ in range(18)]
length = [[0]*(N + 1) for _ in range(18)]

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
        length[0][n] = w
        parent[0][n] = node
        dfs(n, l + 1)

def setTable():
    dfs(1, 0)
    for i in range(1, 18):
        for j in range(1, N + 1):
            length[i][j] = length[i - 1][j] + length[i - 1][parent[i - 1][j]]
            parent[i][j] = parent[i - 1][parent[i - 1][j]]

def lca(a, b):
    ans = 0
    
    if depth[a] > depth[b]:
        a, b = b, a
    
    for i in range(17, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            ans += length[i][b]
            b = parent[i][b]
    
    if a == b:
        return (a, ans)
    
    for i in range(17, -1, -1):
        if parent[i][a] != parent[i][b]:
            ans += length[i][a] + length[i][b]
            a = parent[i][a]
            b = parent[i][b]
             
    return (parent[0][a], ans + length[0][a] + length[0][b])
    
def getParent(a, l):
    for i in range(17, -1, -1):
        if l >= (1 << i):
            l -= (1 << i)
            a = parent[i][a]
    return a
    

setTable()
M = int(input())

for _ in range(M):
    q = list(map(int, sys.stdin.readline().split()))
    if q[0] == 1:
        u, v = q[1], q[2]
        _, ans = lca(u, v)
        print(ans)
        
    else:
        u, v, k = q[1], q[2], q[3]
        root, _ = lca(u, v)
     
        if k > depth[u] - depth[root]:
            k = (depth[v] - depth[root]) - (k - (depth[u] - depth[root])) + 1
            ans = getParent(v, k)
            
        else:
            k -= 1
            ans = getParent(u, k)
        print(ans)