import sys
import heapq

V = int(input())

tree = [[] for _ in range(V+1)]
for _ in range(V):
    info = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(info)-1, 2):
        tree[info[0]].append([info[i], info[i+1]])

INF = int(1e12)
def Dijkstra(start):
    heap = []
    D = [INF]*(V+1)
    heapq.heappush(heap, (0,start))
    D[start] = 0
    
    
    while len(heap) > 0:
        dist, now = heapq.heappop(heap)
        
        if dist > D[now]:
            continue
        
        for i in tree[now]:
            if dist + i[1] < D[i[0]]:
                D[i[0]] = dist + i[1]
                heapq.heappush(heap, (dist + i[1], i[0]))
    return D            
   
D1 = Dijkstra(1)

maxi = 0
idx = 0
for i in range(V+1):
    if D1[i] > maxi and D1[i] != int(1e12):
        maxi = D1[i]
        idx = i
        
D2 = Dijkstra(idx)
maxi = 0
for i in range(V+1):
    if D2[i] > maxi and D2[i] != int(1e12):
        maxi = D2[i]
        idx = i
print(maxi)
    
