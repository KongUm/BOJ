from collections import deque


def bfs(sn, sy, sx):
    global mini, min_node
    Q = deque()
    visited = [[0]*N for _ in range(N)]
    visited[sy][sx] = 1
    Q.append((sy, sx, 0))
    
    while len(Q) > 0:
        y, x, cnt = Q.popleft()
        
        if arr[y][x] == 'K' or arr[y][x] == 'S':
            a = D[str(y)+'-'+str(x)]
            if a != sn:
                edge.append((cnt, sn, a))
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if arr[ny][nx] != '1' and visited[ny][nx] == 0:
                Q.append((ny, nx, cnt + 1))
                visited[ny][nx] = 1
    

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
edge = []
D = {}
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
cnt = 1
mini = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'K':
            D[str(i)+'-'+str(j)] = cnt
            cnt += 1
        elif arr[i][j] == 'S':
            D[str(i)+'-'+str(j)] = 0
 
for y in range(N):
    for x in range(N):
        if arr[y][x] == 'K' or arr[y][x] == 'S':
            sn = D[str(y)+'-'+str(x)]
            bfs(sn, y, x)


parent = [0] + [i for i in range(1, M+1)]

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
      
edge.sort(key = lambda x : x[0])

for i in range(len(edge)):
    w, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        mini += w
        
for i in range(M + 1):
    if find(i) != 0:
        print(-1)
        exit()
print(mini)

