N = int(input())
A = list(map(int, input().split()))

info = [0]*(N+1)
info[0] = -1
for i in range(N):
    info[A[i]] = i+1
maxi = 1
cur = 1

for i in range(1, N+1):
    if info[i-1] < info[i]:
        cur += 1
    else:
        maxi = max(cur, maxi)
        cur = 1
print(N-maxi)
        