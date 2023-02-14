from collections import deque

M, N = map(int, input().split()) # M = 가로, N = 세로

arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
for x in range(M):
    for y in range(N):
        if arr[y][x] == 1:
            arr[y][x] = -1
            Q.append([x,y,1])
loc = [[0,1],[1,0],[-1,0],[0,-1]]

while len(Q) != 0:
    u = Q.popleft()
    for v in loc:
        dx = u[0] + v[0]
        dy = u[1] + v[1]
        if 0 <= dx < M and 0 <= dy < N:
            if arr[dy][dx] == 0:
                arr[dy][dx] = u[2]
                Q.append([dx, dy, u[2]+1])

maxi = 0
checker = True                
for x in range(M):
    for y in range(N):
        if arr[y][x] == 0:
            maxi = -1
            checker = False
            break
        elif arr[y][x] > maxi:
            maxi = arr[y][x]
    if checker == False:
        break

print(maxi)
            
        