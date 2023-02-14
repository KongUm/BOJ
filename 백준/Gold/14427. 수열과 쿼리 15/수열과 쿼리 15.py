import sys,heapq as p
N=int(input());A=[0]+list(map(int,input().split()));M=int(input());h=[]
for i in range(1,N+1):
    p.heappush(h,(A[i],i))
for _ in range(M):
    q=list(map(int, sys.stdin.readline().split()))
    if q[0]==1:
        j,v=q[1],q[2];A[j]=v;p.heappush(h,(v,j))
    else:
        while A[h[0][1]]!=h[0][0]:p.heappop(h)
        print(h[0][1])