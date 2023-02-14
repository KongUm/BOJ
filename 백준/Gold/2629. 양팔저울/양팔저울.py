N = int(input())
w = list(map(int,input().split()))
w.insert(0,-1)
M = int(input())
f,a,b=40000,80000,80001
O = list(map(int, input().split()))
D = [[0]*b for _ in range(N+1)]
for i in range(N+1):
    D[i][f] = 1
for i in range(1,N+1):
    for j in range(b):
        if 0<=j-w[i]<=a:            
            D[i][j]=max(D[i-1][j-w[i]],D[i-1][j],D[i][j])           
        if 0<=j+w[i]<=a:
            D[i][j]=max(D[i-1][j+w[i]],D[i-1][j],D[i][j])
for i in O:
    if D[N][f+i] == 1:
        print("Y",end = " ")
    else:
        print("N",end = " ")