import sys
N,K=map(int,input().split())
w=list(map(int,input().split()))
b=[list(map(int, sys.stdin.readline().split())) for _ in range(K)]
def check(x, y):
    for i in range(K):
        p,q=b[i]
        if p==x or q==y or abs(p-x)==abs(q-y):return 1
    return 0
m,c,a="MATE","CHECK",[]
for i in range(w[0]-1,w[0]+2):
    for j in range(w[1]-1,w[1]+2):
        if i<1or i>N or j<1or j>N:a.append(1)
        else:a.append(check(i,j))
s,f=sum(a),a[4]
if s==9:print(c+m)
elif s==8and f==0:print("STALE"+m)
elif f==1:print(c)
else:print("NONE")