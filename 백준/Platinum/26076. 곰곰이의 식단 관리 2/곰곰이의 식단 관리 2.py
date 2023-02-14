from collections import deque
H, W = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[int(1e9)]*(W + 1) for _ in range(H + 1)]

graph = [[[] for _ in range(W + 1)] for _ in range(H + 1)]


if H != 1 and W != 1:
    a, b = arr[0][1] == 1, arr[1][0] == 1
    c, d = arr[H-2][W-1] == 1, arr[H-1][W-2] == 1
    a, b, c, d = int(a), int(b), int(c), int(d)
    
    if a + b == 2 or c + d == 2:
        visited[H][W] = 0
    elif a + b + c + d > 0:
        visited[H][W] = 1
    else:
        visited[H][W] = 2
    
dy = [1, 1, 0, -1, -1, -1, 0, 1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy2 = [2, 2, 2, 1, 0, -1, -2, -2, -2, -2, -2, -1, 0, 1, 2, 2]
dx2 = [0, 1, 2, 2, 2, 2, 2, 1, 0, -1, -2, -2, -2, -2, -2, -1]
Dy = dy + dy2; Dx = dx + dx2

for y in range(H):
    for x in range(W):
        if arr[y][x] == 1:
            for i in range(24):
                ny, nx = Dy[i] + y, Dx[i] + x
                if 0 <= ny < H and 0 <= nx < W and arr[ny][nx] == 1:
                    if abs(Dy[i]) == 2 or abs(Dx[i]) == 2:
                        graph[y][x].append((ny, nx, 1))
                    else:
                        graph[y][x].append((ny, nx, 0))
for x in range(1, W):
    graph[H][0].append((0, x, 0))
for x in range(W - 1):
    graph[H - 1][x].append((H, W, 0))
for y in range(H - 1):
    graph[H][0].append((y, W - 1, 0))
for y in range(1, H):
    graph[y][0].append((H, W, 0))
    
def bfs(sy, sx):
    Q = deque()
    visited[sy][sx] = 0
    Q.append((sy, sx, 0))
    while len(Q) > 0:
        y, x, dist = Q.popleft()
        if visited[y][x] < dist:
            continue
   
        for ny, nx, cnt in graph[y][x]:
            if cnt == 0:
                if visited[ny][nx] > dist:
                    visited[ny][nx] = dist
                    Q.appendleft((ny, nx, dist))
            else:
                if visited[ny][nx] > dist + 1:
                    visited[ny][nx] = dist + 1
                    Q.append((ny, nx, dist + 1))

if H == 1 or W == 1:
    for y in range(H):
        for x in range(W):
            if arr[y][x] == 1:
                print(0)
                exit()
    print(1)
else:
    bfs(H, 0)
    print(visited[H][W])
