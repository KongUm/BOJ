from collections import deque
from itertools import combinations

N, M = map(int, input().split())
arr = []
virus = []
empty_cnt = 0
virus_cnt = 0

for y in range(N):
    S = list(map(int, input().split()))
    arr.append(S[:])
    for x in range(N):
        if S[x] == 0:
            empty_cnt += 1
        elif S[x] == 2:
            virus_cnt += 1
            virus.append([y, x])
            arr[y][x] = 3
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(virus):
    Q = deque()
    visited = [x[:] for x in arr]
    
    for i in virus:
        visited[i[0]][i[1]] = 2
        Q.append([i[0], i[1], 0])
    maxi = 0
    emp = empty_cnt
        
    while len(Q) > 0 and empty_cnt > 0:
        u = Q.popleft()
        for i in range(4):
            ny, nx = u[0] + dy[i], u[1] + dx[i]
            
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 2
                    Q.append([ny, nx, u[2]+1])
                    maxi = max(u[2]+1, maxi)
                    emp -= 1
                elif visited[ny][nx] == 3:
                    visited[ny][nx] = 2
                    Q.append([ny, nx, u[2]+1])
                    
                
    return maxi,emp
          
time = int(1e9)

for v in combinations(virus, M):
    a, b = bfs(v)
    #print(a, b)
    if b == 0:
        time = min(time, a)
if time == int(1e9):
    print(-1)
else:
    print(time)        
              
