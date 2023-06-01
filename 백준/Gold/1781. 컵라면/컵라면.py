import sys, heapq
n = int(input())
v = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
v.sort(key = lambda x :(-x[0], -x[1]))
res = 0
idx = 0
heap = []

for i in range(n, 0, -1):
    while (idx < n and v[idx][0] >= i):
        heapq.heappush(heap, -v[idx][1])
        idx += 1
    if (len(heap) > 0):
        res += -heapq.heappop(heap)
print(res)