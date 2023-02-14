V = int(input())
E = int(input())

INF = int(1e10+11)
graph = [[INF]*(V+1) for _ in range(V+1)]
waypoint = [[[] for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a][b] = min(w, graph[a][b])
for i in range(V+1):
    graph[i][i] = 0

for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                waypoint[a][b] = waypoint[a][k] + [k] + waypoint[k][b]
                graph[a][b] = graph[a][k] + graph[k][b]
                

for i in range(1, V+1):
    for j in range(1, V+1):
        if graph[i][j] >= INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()
    
for i in range(1, V+1):
    for j in range(1, V+1):
        if graph[i][j] == 0 or graph[i][j] == INF:
            print(0)
        else:
            print(2+len(waypoint[i][j]), end =  " ")
            print(i, end = " ")
            for p in waypoint[i][j]:
                print(p, end = " ")
            print(j)
            