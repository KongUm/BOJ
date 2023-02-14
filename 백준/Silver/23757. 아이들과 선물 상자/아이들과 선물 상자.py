import heapq
N, M = map(int, input().split())
g = list(map(int, input().split()))
w = list(map(int, input().split()))

heap = []
for i in g:
    heapq.heappush(heap, -i)
for i in w:
    a = -heapq.heappop(heap)
    if i <= a:
        a -= i
        heapq.heappush(heap, - a)
    else:
        print(0)
        exit()
print(1)
    
