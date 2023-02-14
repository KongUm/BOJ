V, E = map(int, input().split())

INF = int(1e10+11)
graph = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a][b] = min(w, graph[a][b])

for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])
ans = INF
for i in range(1, V+1):
    ans = min(graph[i][i], ans)
    
if ans == INF:
    print(-1)
else:
    print(ans)