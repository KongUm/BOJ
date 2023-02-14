N = int(input())
A = list(map(int, input().split()))
A.sort()

mid = N - 1
cnt = 0
for i in range(N):
    if A[i] <= mid - 1:
        mid -= A[i] + 1
        cnt += A[i]
        A[i] = 0
print(mid + cnt)

