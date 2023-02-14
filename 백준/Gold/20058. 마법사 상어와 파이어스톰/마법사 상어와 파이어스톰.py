from collections import deque
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
process = list(map(int, input().split()))

def Rotate(L, sy, sx, ey, ex):
    A = [x[sx : ex + 1] for x in arr[sy: ey + 1]]
    B = [[0]*(2**L) for _ in range(2**L)]
    for y in range(2**L):
        for x in range(2**L):
            B[x][2**L - y -1] = A[y][x]
    for y in range(2**L):
        for x in range(2**L):
            temp[y + sy][x + sx] = B[y][x]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def Melt():
    for y in range(2**N):
        for x in range(2**N):
            if temp[y][x] > 0:
                cnt = 0
                for i in range(4):
                    ny, nx = dy[i] + y, dx[i] + x
                    if 0 <= ny < 2 ** N and 0 <= nx < 2 ** N and temp[ny][nx] > 0:
                        cnt += 1
                if cnt <= 2:
                    arr[y][x] -= 1

def bfs(sy, sx):
    Q = deque()
    Q.append([sy, sx])
    visited[sy][sx] = True
    cnt = 1
    while len(Q) > 0:
        y, x = Q.popleft()
        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= ny < 2**N and 0 <= nx < 2**N and arr[ny][nx] > 0 and visited[ny][nx] == False:
                visited[ny][nx] = True
                Q.append([ny, nx])
                cnt += 1
    return cnt



for p in process:
    temp = [[0] * (2 ** N) for _ in range(2 ** N)]
    for sy in range(0, 2**N, 2**p):
        for sx in range(0, 2**N, 2**p):
            Rotate(p, sy, sx, sy + 2**p - 1, sx + 2**p - 1)
    arr = [x[:] for x in temp]
    Melt()

visited = [[False]*(2**N) for _ in range(2**N)]
ans = 0
s = 0
for y in range(2**N):
    s += sum(arr[y])
    for x in range(2**N):
        if arr[y][x] > 0 and visited[y][x] == False:
            a = bfs(y, x)
            ans = max(a, ans)
print(s)
print(ans)