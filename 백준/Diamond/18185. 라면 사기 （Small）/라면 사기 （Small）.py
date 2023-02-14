N = int(input())
A = list(map(int, input().split()))

one, two = 0, 0
cnt, s = 0, sum(A)

for i in range(N):
    one = two
    two = 0
    if A[i] > 0:
        cnt += A[i]
        two += A[i]
        A[i] = 0
    
    if i + 1 < N and A[i + 1] == 0:
        two = 0
        continue
    if i + 1 < N and A[i + 1] > 0:
        diff = min(A[i + 1], two)
        A[i + 1] -= diff
        two = diff
        if A[i + 1] > 0:
            A[i + 1] = max(0, A[i + 1] - one)
     

print(cnt + s * 2)

