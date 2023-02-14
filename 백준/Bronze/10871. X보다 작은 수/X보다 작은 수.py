N,X = input().split()
N,X = int(N), int(X)
a = list(map(int, input().split()))

for i in range(N):
    if(a[i]<X):
        print(a[i], end=' ')
