import sys
import heapq

N = int(input())

max_heap = []
min_heap = []

heapq.heappush(max_heap, -int(input()))
print(- max_heap[0])

for i in range(1,N): # i = 힙에 들어있는 개수 (x 추가 전)
    x = int(sys.stdin.readline())
    if i % 2 == 1: # 추가 전에 홀수 개 일때
        if x < - max_heap[0]:
            heapq.heappush(min_heap, - heapq.heappop(max_heap))
            heapq.heappush(max_heap, - x)
        else:
            heapq.heappush(min_heap, x)
    else: # 추가 전에 짝수 개 일때
        if x > min_heap[0]:
            heapq.heappush(max_heap, - heapq.heappop(min_heap))
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap, -x)
    print(- max_heap[0])