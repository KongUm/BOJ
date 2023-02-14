import sys
N, M, S, T = map(int, input().split())
# 노드, 간선, 시작, 도착

INF = int(1e20)
graph = [[INF]*(N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], w)

for i in range(1, N + 1):
    graph[i][i] = 0
    
for m in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            graph[s][e] = min(graph[s][m] + graph[m][e], graph[s][e])

Q = int(input())

for _ in range(Q):
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())
    comp = graph[S][T]
    A = [[a, b, c], [d, e, f]]
    
    for p, q, w in A:
        comp = min(comp, graph[S][p] + w + graph[q][T])
    comp = min(comp, graph[S][a] + c + graph[b][d] + f + graph[e][T])
    comp = min(comp, graph[S][d] + f + graph[e][a] + c + graph[b][T])
        
    if comp >= INF:
        print(-1)
    else:
        print(comp)