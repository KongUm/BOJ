from collections import deque
N,L=map(int,input().split())
A=list(map(int,input().split()))
Q=deque()
for i in range(N):
    if len(Q)==0:
        Q.append((A[i],i))
    else:
        while len(Q)>0 and Q[-1][0]>A[i]:
            Q.pop()
        Q.append((A[i],i))
    if Q[0][1]<i-L+1:
        Q.popleft()
    print(Q[0][0],end = " ")    