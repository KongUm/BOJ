N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
A.sort()

for i in range(N):
        print(A[i][0],A[i][1])