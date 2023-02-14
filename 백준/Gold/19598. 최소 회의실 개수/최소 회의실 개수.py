import sys
import heapq

N = int(input())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
L.sort()
heap = []

for s, e in L:
    if len(heap) > 0 and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e) 

print(len(heap))