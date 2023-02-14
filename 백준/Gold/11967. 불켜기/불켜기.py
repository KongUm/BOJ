from collections import deque
N, M = map(int, input().split())

graph = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
visited = [[-1]*(N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y, a, b = map(int, input().split())
    graph[y][x].append((b, a))

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]



def light(sy, sx):
    for ay, ax in graph[sy][sx]:
        if visited[ay][ax] == -1:
            visited[ay][ax] = 0
            for i in range(4):
                ny, nx = ay + dy[i], ax + dx[i]
                if 1 <= ny <= N and 1 <= nx <= N and visited[ny][nx] == 1:
                    visited[ay][ax] = 1
                    Q.append((ay, ax))
                    break

Q = deque()
Q.append((1, 1))
visited[1][1] = True

while len(Q) > 0:
    y, x = Q.popleft()
    light(y, x)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 1 <= ny <= N and 1 <= nx <= N and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            Q.append((ny, nx))

cnt = 0
for y in range(1, N + 1):
    for x in range(1, N + 1):
        if visited[y][x] != -1:
            cnt += 1
print(cnt)
