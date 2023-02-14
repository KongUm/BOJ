from collections import deque
from itertools import combinations

H, W = map(int, input().split())
arr = []
empty = []
virus = []
empty_cnt = -3

for y in range(H):
    S = list(map(int, input().split()))
    arr.append(S[:])
    for x in range(W):
        if S[x] == 0:
            empty.append([y, x])
            empty_cnt += 1
        elif S[x] == 2:
            virus.append([y, x])
            
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
           
def bfs(wall):
    Q = deque()
    visited = [x[:] for x in arr]
    infection = 0
    
    for i in virus:
        Q.append([i[0], i[1]])
    for i in wall:
        visited[i[0]][i[1]] = 1
        
    while len(Q) > 0:
        u = Q.popleft()
        for i in range(4):
            ny, nx = u[0] + dy[i], u[1] + dx[i]
            
            if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == 0:
                visited[ny][nx] = 2
                Q.append([ny, nx])
                infection += 1
    return infection  
         
ans = 0 
for w in combinations(empty, 3):
    infect = bfs(w)
    ans = max(ans, empty_cnt - infect)
print(ans)