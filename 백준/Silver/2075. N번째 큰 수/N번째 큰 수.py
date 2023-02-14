import heapq
import sys

N = int(input())

heap = []

for _ in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        if len(heap) == N:
            if A[i] > heap[0]:
                 heapq.heappop(heap)
                 heapq.heappush(heap, A[i])            
        else:
            heapq.heappush(heap, A[i])
print(heapq.heappop(heap))