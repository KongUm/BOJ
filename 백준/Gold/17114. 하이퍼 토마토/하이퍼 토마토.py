import sys
from collections import deque
m,n,o,p,q,r,s,t,u,v,w = map(int, input().split())
Queue = deque()

graph = [[[[[[[[[[[]for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)]for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]
# graph[w][v][u][t][s][r][q][p][o][n][m]

count = m*n*o*p*q*r*s*t*u*v*w

for W in range(w):
    for V in range(v):
        for U in range(u):
            for T in range(t):
                for S in range(s):
                    for R in range(r):
                        for Q in range(q):
                            for P in range(p):
                                for O in range(o):
                                    for N in range(n):
                                        a = list(map(int, sys.stdin.readline().split()))
                                        for M in range(m):
                                            if a[M] == 1:
                                                Queue.append([0,W,V,U,T,S,R,Q,P,O,N,M])
                                                count -= 1
                                            elif a[M] == -1:
                                                count -= 1
                                                
                                            graph[W][V][U][T][S][R][Q][P][O][N].append(a[M])
                              

emtpy_count = 0
                                   
                                        
dw = [1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0]
dv = [0,1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0]
du = [0,0,1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0]
dt = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0]
ds = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0]
dr = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0]
dq = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0]
dp = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,0,0,0]
do = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,0,0]
dn = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1,0]
dm = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,-1] # [0] ~ [21]

#print(graph[0][0][0][0][0][0][0][0][0][0][0])
maxi = 0

while len(Queue) != 0:
    info = Queue.popleft()
    for i in range(22):
        nw = info[1] + dw[i]
        nv = info[2] + dv[i]
        nu = info[3] + du[i]
        nt = info[4] + dt[i]
        ns = info[5] + ds[i]
        nr = info[6] + dr[i]
        nq = info[7] + dq[i]
        np = info[8] + dp[i]
        no = info[9] + do[i]
        nn = info[10] + dn[i]
        nm = info[11] + dm[i]
        #print(w)
        if nw < 0 or nw >= w or nv < 0 or nv >= v or nu < 0 or nu >= u or nt < 0 or nt >= t or ns < 0 or ns >= s or nr < 0 or nr >= r or nq < 0 or nq >= q or np < 0 or np >= p or no < 0 or no >= o or nn < 0 or nn >= n or nm < 0 or nm >= m:
            continue
        target = graph[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm]
        if target == 0:
            graph[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = 1
            count -= 1
            Queue.append([info[0]+1,nw,nv,nu,nt,ns,nr,nq,np,no,nn,nm])
            if info[0] + 1 > maxi:
                maxi = info[0] + 1
                
if count == 0:
    print(maxi)
elif count > 0:
    print(-1)
else:
    print(0)
 







                                            
