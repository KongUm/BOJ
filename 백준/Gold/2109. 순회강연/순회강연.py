import heapq
N=int(input())
c=[list(map(int,input().split()))for _ in range(N)]
c.sort(key=lambda x:x[1])
h=[]
for g,d in c:
    heapq.heappush(h, g)
    if len(h)>d:heapq.heappop(h)
print(sum(h))