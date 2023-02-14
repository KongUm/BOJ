from collections import deque
N = int(input())
arr = []

sy, sx = 0,0
size = 2
for i in range(N):
    S = list(map(int, input().split()))
    for j in range(N):
        if S[j] == 9:
            sy, sx = i, j
    arr.append(S)

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(sy, sx, size):
    visited = [[False]*N for _ in range(N)]
    Q = deque()
    visited[sy][sx] = True
    Q.append([sy, sx, 0])
    mini_len = -1
    eat = []
    
    while len(Q) > 0:
        y, x, cnt = Q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == False and arr[ny][nx] <= size:
              
                if arr[ny][nx] != 0 and size > arr[ny][nx]:
                    if mini_len < 0:
                        mini_len = cnt+1
                    elif cnt+1 > mini_len:
                        return eat, mini_len
                    eat.append([ny, nx])
                Q.append([ny, nx, cnt + 1])
                visited[ny][nx] = True
    
    return eat, mini_len

ans = 0              
eat_cnt = 0  
for p in range(N**2):
    eat, time = bfs(sy, sx, size)
    arr[sy][sx] = 0
    
    if time == -1:
        break
    
    eat.sort()
    sy, sx = eat[0][0], eat[0][1]
    eat_cnt += 1
    if eat_cnt >= size:
        size += 1
        eat_cnt = 0
    arr[sy][sx] = 9
    ans += time
    
print(ans)