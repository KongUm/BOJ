from collections import deque

H, W = map(int, input().split())
arr = [input() for _ in range(H)]
visited = [[0]*W for _ in range(H)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

C = [[0]*W for _ in range(H)]
def bfs(sy, sx, a):
    count = 0
    Q = deque()
    visited[sy][sx] = 1
    count += 1
    Q.append([sy, sx])
    memo = [[sy, sx]]
    
    while len(Q) > 0:
        y, x = Q.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and arr[ny][nx] == '0' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                memo.append([ny, nx])
                Q.append([ny, nx])
                count += 1
    for my, mx in memo:
        visited[my][mx] = count
        C[my][mx] = a
a = 1
for i in range(H):
    for j in range(W):
        if arr[i][j] == '0' and visited[i][j] == 0:
            bfs(i, j, a)
            a += 1
            
ans = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if arr[i][j] == '1':
            ans[i][j] = 1
            used = set()
            
            for u in range(4):
                y, x = dy[u] + i, dx[u] + j
                if 0 <= y < H and 0 <= x < W and C[y][x] not in used: 
                    ans[i][j] += visited[y][x]
                    used.add(C[y][x])
                    
      
for i in range(H):
    for j in range(W):
        print(ans[i][j]%10, end = "")
    print()
            
                    

        
    
