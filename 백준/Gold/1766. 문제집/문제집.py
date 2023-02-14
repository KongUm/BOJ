import sys
import heapq

V, M = map(int, input().split())

graph = [[] for _ in range(V+1)]
indegree = [0]*(V+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
    
def Topological_sort():
    ans = []
    heap = []
    for i in range(1, V+1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
    while len(heap) > 0:
        u = heapq.heappop(heap)
        ans.append(u)
        
        for i in graph[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(heap, i)
    return ans
ans = Topological_sort()
for i in ans:
    print(i, end = " ")