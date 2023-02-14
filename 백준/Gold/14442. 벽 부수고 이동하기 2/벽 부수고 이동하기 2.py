from collections import deque

H, W, K = map(int, input().split())

arr = [[] for _ in range(H)]
for i in range(H):
    a = input()
    for j in range(W):
        if a[j] == '1':
            arr[i].append(-1)
        else:
            arr[i].append(0)
            
visited = []
       
for _ in range(K + 1):
    visited.append([x[:] for x in arr])
    
Q = deque()
visited[0][0][0] = 1
Q.append([0, 0, 1, 0])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while len(Q) > 0:
    u = Q.popleft()
    
    for i in range(4):
        ny, nx = dy[i] + u[0], dx[i] + u[1]
        nk = u[3]
        
        if 0 <= ny < H and 0 <= nx < W:
            if visited[nk][ny][nx] == 0:
                visited[nk][ny][nx] = u[2] + 1
                Q.append([ny, nx, u[2]+1, nk])
                
            elif visited[nk][ny][nx] == -1 and nk < K:
                visited[nk][ny][nx] = u[2] + 1
                Q.append([ny, nx, u[2]+1, nk+1])
                
            if ny == H-1 and nx == W-1:
                print(visited[nk][ny][nx])
               
                exit()
if visited[0][H-1][W-1] > 0:
    print(visited[0][H-1][W-1])
else:
    print(-1)
                
