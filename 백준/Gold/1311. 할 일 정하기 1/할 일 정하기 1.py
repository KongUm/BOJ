N=int(input())
w=[list(map(int,input().split()))for _ in range(N)] 
d=[[int(1e9)]*(1<<N) for _ in range(N+1)]
d[0][0] = 0
for i in range(1,N+1):
    for j in range(1<<N):
        for u in range(N):         
            if j&(1<<u)!=0 and d[i-1][j-(1<<u)]+w[i-1][u]<d[i][j]:
                d[i][j]=d[i-1][j-(1<<u)]+w[i-1][u]          
print(min(d[N]))
