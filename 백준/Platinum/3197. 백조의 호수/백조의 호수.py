from collections import deque

H, W = map(int, input().split())

A = [input() for _ in range(H)]
arr = [[] for _ in range(H)]
start = []
no_ice = True
for i in range(H):
    for j in range(W):
        if A[i][j] == 'L':
            start.append([i, j])

        if A[i][j] == 'X':
            no_ice = False
            arr[i].append(-1)
        else:
            arr[i].append(0)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = deque()
Q.append([start[0][0], start[0][1], 1])
Q.append([start[1][0], start[1][1], 2])
arr[start[0][0]][start[0][1]] = 1
arr[start[1][0]][start[1][1]] = 2
temp = []


def Search(ny, nx, nt):
    for j in range(4):
        cy, cx = ny + dy[j], nx + dx[j]
        if 0 <= cy < H and 0 <= cx < W:
            if arr[cy][cx] > 0 and arr[cy][cx] != nt:
                return arr[cy][cx]
    return -1


while len(Q) > 0:
    u = Q.popleft()
    for i in range(4):
        ny, nx = dy[i] + u[0], dx[i] + u[1]
        if 0 <= ny < H and 0 <= nx < W:
            if arr[ny][nx] == 0:
                arr[ny][nx] = u[2]
                Q.append([ny, nx, u[2]])


            elif arr[ny][nx] == -1:
                temp.append([ny, nx, u[2]])
                arr[ny][nx] = u[2]

                if Search(ny, nx, u[2]) > 0:
                    print(1)
                    exit()

Q = deque()

def bfs(sy, sx, t):
    Queue = deque()
    arr[sy][sx] = t
    Queue.append([sy, sx])
    Q.append([sy, sx, t, 0])
    while len(Queue) > 0:
        u = Queue.popleft()
        for i in range(4):
            ny, nx = dy[i] + u[0], dx[i] + u[1]
            if 0 <= ny < H and 0 <= nx < W:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = t
                    Queue.append([ny, nx])
                    Q.append([ny, nx, t, 0])

c = 3
for y in range(H):
    for x in range(W):
        if arr[y][x] == 0:
            bfs(y, x, c)
            c += 1

parent = [i for i in range(c + 1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for y, x, t in temp:
    Q.append([y, x, t, 1])

now = 0
while len(Q) > 0:

    y, x, t, cnt = Q.popleft()
    if cnt > now:
        for i in range(1, c+1):
            find(i)
        if find(1) == find(2):
            print(now+1)
            exit()
        now += 1

    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        if 0 <= ny < H and 0 <= nx < W:
            if arr[ny][nx] > 0 and arr[ny][nx] != t:
                union(arr[ny][nx], t)
            elif arr[ny][nx] < 0:
                arr[ny][nx] = t
                Q.append([ny, nx, t, cnt+1])
                for i in range(4):
                    ty, tx = ny + dy[i], nx + dx[i]
                    if 0 <= ty < H and 0 <= tx < W:
                        if arr[ty][tx] > 0 and arr[ty][tx] != t:
                            union(arr[ty][tx], t)


