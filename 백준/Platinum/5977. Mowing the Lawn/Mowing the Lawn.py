import sys
from collections import deque
N, K = map(int, input().split())
A = [0] + [int(sys.stdin.readline()) for _ in range(N)]
Q = deque()
Q.append((0, 0))

for i in range(1, N + 1):
    if i - Q[0][1] - 1 > K:
        Q.popleft()
    
    dp = Q[0][0] + A[i]
    
    while len(Q) > 0 and dp <= Q[-1][0]:
        Q.pop()
    Q.append((dp, i))

ans = 0
s = sum(A)
while len(Q) > 0:
    u = Q.popleft()
    if u[1] >= N - K:
        ans = max(ans, s - u[0])
print(ans)