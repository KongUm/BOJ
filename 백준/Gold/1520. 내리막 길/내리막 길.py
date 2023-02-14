import sys
sys.setrecursionlimit(10000)
M, N = map(int, input().split()) # M = 세로의 길이, N = 가로의 길이

arr = [[-1]*(N+2)]

for i in range(1,M+1):
    arr.append([-1])
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        arr[i].append(temp[j])
    arr[i].append(-1)
arr.append([-1]*(N+2))
dp = [[-1]*(N+2) for _ in range(M+2)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
def dfs(x,y): # 노드를 방문
    global ans
    if x == N and y == M:
        return 1
        
    if dp[y][x] >= 0:
        return dp[y][x]
    dp[y][x] = 0
        
    for i in range(4):
        cx, cy = x + dx[i], y + dy[i]
        if 0 < arr[cy][cx] < arr[y][x]: 
            dp[y][x] += dfs(cx, cy)
    return dp[y][x]
  
dfs(1,1)

print(dp[1][1])