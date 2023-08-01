n=int(input());A=[int(input())for _ in range(n)];v,u,p,q=sorted(A[:]),[0]*n,0,0
def f(x):
    for i in range(n-1,-1,-1):
        if u[i]==0 and v[x]==A[i]:
            x+=1;u[i]=1
    for i in range(n):
        if u[i]==0 and v[x]==A[i]:
            x+=1;u[i]=1
    return x
while p<n:
    p=f(p);q+=1
print(q)