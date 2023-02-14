from collections import deque

N, K = map(int, input().split())
M = max(N, K)

visited = [0]*(2*M+1)
dp = [-1]*(2*M+1)
Q = deque()

visited[N] = True
Q.append([N, 0])
ans = 0

while len(Q) > 0:
    u = Q.popleft()
    if u[0] == K:
        ans = u[1]
        break
    for i in range(-1, 2, 2):
        if 0 <= u[0]+i <= 2*M and visited[u[0]+i] == False:
            Q.append([u[0]+i, u[1]+1])
            visited[u[0]+i] = True
            dp[u[0]+i] = u[0]
            
        if 0 <= u[0]*2 <= 2*M and visited[u[0]*2] == False:
            Q.append([u[0]*2, u[1]+1])
            visited[u[0]*2] = True
            dp[u[0]*2] = u[0]
a = K
path = [K]
for i in range(ans):
    path.append(dp[a])
    a = path[-1]
print(ans)
for i in range(ans+1):
    print(path.pop(), end = " ")
    