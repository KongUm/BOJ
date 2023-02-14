import sys
import heapq

V, E = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(V + 1)] # 인접 리스트로 그래프 구현
distance = [INF] * (V+1) # 모든 정점의 거리 값을 INF로 초기화
pq = []  # 최소 힙

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))  # index = 1 목적지, # index = 2 거리

def Dijkstra(start):

    heapq.heappush(pq, (0, start)) # 최소 힙에 (거리 = 0, 시작 지점)을 넣는다
    distance[start] = 0 # 시작 지점 이므로 거리는 0

    while len(pq) > 0:
        dist, now = heapq.heappop(pq) # 최소 힙에서 가장 거리가 짧은 노드를 선택 한다

        
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(pq, (dist + i[1], i[0]))
Dijkstra(start)

for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])




