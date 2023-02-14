import sys
import heapq

T = int(input())
INF = int(1e10)

def Dijkstra(start, graph, V):
    D = [INF]*(V+1)
    D[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while len(heap) > 0:
        dis, now = heapq.heappop(heap)      
        if dis > D[now]:
            continue
        for i in graph[now]: # i = 0: index, i = 1: 거리
            if i[1] + dis < D[i[0]]:
                D[i[0]] = i[1] + dis
                heapq.heappush(heap, (i[1] + dis, i[0]))
    return D                
    
    
for _ in range(T):
    V, E, d = map(int, input().split())
    start, g, h = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    dest = []
    gh = 0
    for i in range(E):
        a, b, w = map(int, sys.stdin.readline().split())
        if (a == g and b == h) or (a == h and b == g):
            gh = w           
        graph[a].append([b, w])
        graph[b].append([a, w])
        
    for i in range(d):
        dest.append(int(input()))
    
    start_Dis = Dijkstra(start, graph, V)
    g_Dis = Dijkstra(g, graph, V)
    h_Dis = Dijkstra(h, graph, V)
    
    ans = []
    for i in dest:
        if start_Dis[g] + gh + h_Dis[i] == start_Dis[i] or start_Dis[h] + gh + g_Dis[i] == start_Dis[i]:
            ans.append(i)
    ans.sort()
    for i in ans:
        print(i, end = " ")
    print()