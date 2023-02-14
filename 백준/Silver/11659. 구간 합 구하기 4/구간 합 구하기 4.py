N, M = map(int,input().split())
A = list(map(int,input().split()))
sum_A = [0,A[0]]
for i in range(1,N):
    sum_A.append(sum_A[-1]+A[i])

for _ in range(M):
    i,j = map(int,input().split())
    print(sum_A[j]-sum_A[i-1])