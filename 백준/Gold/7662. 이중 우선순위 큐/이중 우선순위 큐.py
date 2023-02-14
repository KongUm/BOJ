import sys
import heapq
T = int(input())

def min_value():
    while len(min_heap) > 0:
        mini = heapq.heappop(min_heap)
        if D[mini] > 0:
            D[mini] -= 1
            return (mini, True)
    return (0, False)
   
def max_value():
    while len(max_heap) > 0:
        maxi = - heapq.heappop(max_heap)
        if D[maxi] > 0:
            D[maxi] -= 1
            return (maxi, True)
    return (0, False)
    
    
for _ in range(T):
    K = int(input())
    D = {}
    max_heap, min_heap = [], []
    for i in range(K):
        q, n = map(str, sys.stdin.readline().split())
        n = int(n)
        if q == 'I':
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
            if n not in D:
                D[n] = 1
            else:
                D[n] += 1
        else:
            if n == -1: min_value()
            else: max_value()
    a, b = min_value()
    if b == False:
        print("EMPTY")
    else:
        D[a] += 1
        c, d = max_value()
        print(c, a)