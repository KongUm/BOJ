from collections import deque

H, W = map(int, input().split())

arr = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(sy, sx, island_num):
    Q = deque()
    arr[sy][sx] = island_num
    Q.append((sy, sx))
    
    while len(Q) > 0:
        y, x = Q.popleft()
        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= ny < H and 0 <= nx < W and arr[ny][nx] == -1:
                arr[ny][nx] = island_num
                Q.append((ny, nx))
    
for i in range(H):
    S = list(map(int, input().split()))
    for j in range(W):
        if S[j] == 1:
            S[j] = -1
    arr.append(S)

island_cnt = 1
for i in range(H):
    for j in range(W):
        if arr[i][j] == -1:
            bfs(i, j, island_cnt)
            island_cnt += 1
            
edge = []

for i in range(H):
    for j in range(W):
        island = arr[i][j]
        if island > 0:
            for left in range(j-1, -1, -1):
                if arr[i][left] == island:
                    break
                elif arr[i][left] > 0:
                    edge.append((j-left-1, island, arr[i][left]))
                    break
            
            for right in range(j+1, W):
                if arr[i][right] == island:
                    break
                elif arr[i][right] > 0:
                    edge.append((right-j-1, island, arr[i][right]))
                    break
            
            for up in range(i-1, -1, -1):
                if arr[up][j] == island:
                    break
                elif arr[up][j] > 0:
                    edge.append((i-up-1, island, arr[up][j]))
                    break
            
            for down in range(i+1, H):
                if arr[down][j] == island:
                    break
                elif arr[down][j] > 0:
                    edge.append((down-i-1, island, arr[down][j]))
                    break
edge.sort()
parent = [i for i in range(island_cnt)]
total = 0

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
        
for i in range(len(edge)):
    w, a, b = edge[i]
    if w > 1 and find(a) != find(b):
        union(a, b)
        total += w


for i in range(1, island_cnt):
    if find(i) != 1:
        print(-1)
        exit()
print(total)