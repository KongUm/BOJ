from collections import deque

H, W = map(int, input().split())

arr = [input() for _ in range(H)]
land = []

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'L':
            land.append([i,j])
            
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sy, sx):
    Q = deque()
    Q.append([sy, sx, 0])
    visited = [[0]*W for _ in range(H)]
    visited[sy][sx] = 1
    maxi = 0
    while len(Q) > 0:
        u = Q.popleft()
     
        for i in range(4):
            cy, cx = dy[i] + u[0], dx[i] + u[1]
            if 0 <= cx < W and 0 <= cy < H and visited[cy][cx] == 0 and arr[cy][cx] == 'L':
              
                visited[cy][cx] = u[2] + 1
                Q.append([cy, cx, u[2]+1])
                maxi = max(maxi, u[2]+1)
    return maxi
    
  
ans = 0      
for t in land:
    ans = max(bfs(t[0], t[1]), ans)
print(ans)
    
