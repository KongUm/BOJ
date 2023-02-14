import heapq
N, K = map(int, input().split()) # N = 수빈이 위치, K = 동생 위치

INF = int(1e7)
distance = [INF]*100001
heap = []

def Dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while len(heap) > 0:
        dist, now = heapq.heappop(heap)
        
        if dist > distance[now]:
            continue
            
        if now+1 <= 100000 and dist + 1 < distance[now+1]:
            distance[now+1] = dist + 1
            heapq.heappush(heap, (dist + 1, now+1))
            
        if now-1 >= 0 and dist + 1 < distance[now-1]:
            distance[now-1] = dist + 1
            heapq.heappush(heap, (dist + 1, now-1))
            
        if now*2 <= 100000 and dist < distance[now*2]:
            distance[now*2] = dist
            heapq.heappush(heap, (dist, now*2))
            
Dijkstra(N)
print(distance[K])
            
            
