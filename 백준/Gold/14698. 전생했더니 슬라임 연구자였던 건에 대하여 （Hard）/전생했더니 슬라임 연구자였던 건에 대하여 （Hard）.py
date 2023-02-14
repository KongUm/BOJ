import heapq
import sys
T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    heap = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(heap)
    ans = 1
    
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        ans = ans * ((a * b) % 1000000007) % 1000000007
        heapq.heappush(heap, a * b)
    print(ans)