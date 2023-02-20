from collections import deque

def E(i, sy, sx):
    y, x, c = sy + dy[i], sx + dx[i], 1
    while 0 <= y < N and 0 <= x < N:
        if A[y][x] == 0:
            a, b = sy * N + sx, y * N + x
            g[a].append((b, c))
            g[b].append((a, c))
            return
        y += dy[i]; x += dx[i]; c += 1

def bfs():
    Q=deque()
    Q.append((0,0))
    v[0][0]=0
    while len(Q) > 0:
        u,t=Q.popleft()
        for i,dist in g[u]:
            tmp=(t+1)%(M*2)
            if (dist>1 and t<M)or v[i][tmp]!=-1:continue
            v[i][tmp]=v[u][t]+1
            Q.append((i,tmp))

N,M=map(int,input().split())
A=[list(map(int,input().split()))for _ in range(N)]
dy,dx=[1,0],[0,1]
g=[[]for _ in range(N**2)]
v=[[-1]*(2*M)for _ in range(N**2)]

for y in range(N):
    for x in range(N):
        for i in range(2):
            if A[y][x]==0:E(i,y,x)
bfs()
m=int(1e9)
d="moon"
for i in v[-1]:
    if i>0:m=min(m,i)

p=m//(M*2)
if m%(M*2)<M:
    d="sun"

if N==1:print("1 sun")
elif m==int(1e9):print(-1)
else:print(p+1,d)