N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
        A[i].reverse()
A.sort()

for i in range(N):
        print(A[i][1],A[i][0])