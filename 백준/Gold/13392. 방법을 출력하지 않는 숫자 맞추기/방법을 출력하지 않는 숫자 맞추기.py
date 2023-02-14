N=int(input())
A=input();B=input();c=10
d=[[int(1e9)]*(c)for _ in range(N+1)];d[0][0]=0
for i in range(1,N+1):
    a,r=int(A[i-1]),int(B[i-1])
    for j in range(c):
        for u in range(c):
            n=(a+j+u)%c;t=d[i-1][j]+u
            if r<=n:t+=n-r
            else:t+=n-r+c
            d[i][(j+u)%c]=min(t,d[i][(j+u)%c]) 
print(min(d[-1]))