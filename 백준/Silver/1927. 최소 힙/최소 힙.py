import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, command)
   
