import heapq
V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])
    
p, q = map(int, input().split())
# 경우의 수: 1 > A > B > N, 1 > B > A > N
# 다익스트라는 P점 까지의 최소거리 = P점과 이어져 있는 Q점까지 가는 최소거리 + P와 Q사이의 거리를 이용한 알고리즘이다.

def Dijkstra(start):
     
    INF = int(1e9)
    distance = [INF] * (V+1)
    heap = []

    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while len(heap) > 0:
        dist, now = heapq.heappop(heap)
        
        if dist > distance[now]:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(heap, (dist +i[1], i[0]))
    return [distance[1], distance[p], distance[q], distance[V]]
ans = [0,0]
s1 = Dijkstra(1)
sp = Dijkstra(p)
sq = Dijkstra(q)
ans[0] += s1[1] + sp[2] + sq[3]
ans[1] += s1[2] + sq[1] + sp[3]
if min(ans) >= int(1e9):
    print(-1)
else:
    print(min(ans))

