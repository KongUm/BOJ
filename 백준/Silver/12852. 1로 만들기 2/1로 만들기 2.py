from collections import deque
N = int(input())

Q = deque()
visited = [False]*(N+1)
visited[N] = True
Q.append([N, 0])
dp = [-1]*(N+1)

ans = 0
while len(Q) > 0:
    u = Q.popleft()
  
    if u[0] == 1:
        ans = u[1]
    
    if u[0] % 3 == 0 and visited[u[0]//3] == False:
        Q.append([u[0]//3, u[1]+1])
        visited[u[0]//3] = True
        dp[u[0]//3] = u[0]
        
    if u[0] % 2 == 0 and visited[u[0]//2] == False:
        Q.append([u[0]//2, u[1]+1])
        visited[u[0]//2] = True
        dp[u[0]//2] = u[0]
        
    if visited[u[0]-1] == False:
        Q.append([u[0]-1, u[1]+1])
        visited[u[0]-1] = True
        dp[u[0]-1] = u[0]    
        
print(ans)
path = [1]
a = 1
for _ in range(ans):
    path.append(dp[a])
    a = dp[a]

for _ in range(ans+1):
    print(path.pop(), end = " ")