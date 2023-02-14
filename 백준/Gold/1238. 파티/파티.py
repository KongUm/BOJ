import sys
import heapq

V, E, P = map(int, input().split())

graph_PT = [[] for _ in range(V+1)] 
graph_HM = [[] for _ in range(V+1)]
INF = int(1e9)

for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    graph_PT[a].append([b,w])
    graph_HM[b].append([a,w])

def Dijkstra(graph, start):
    distance = [INF]*(V+1)
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while len(heap) > 0:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
           
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(heap, (dist + i[1], i[0]))    
    return distance
A = Dijkstra(graph_PT, P)
B = Dijkstra(graph_HM, P)
maxi = 0
for i in range(1,V+1):
    maxi = max(maxi, A[i]+B[i])
print(maxi)
    
