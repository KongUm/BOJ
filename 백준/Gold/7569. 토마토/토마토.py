from collections import deque

M, N, H = map(int, input().split())

arr = []
for _ in range(H):
    arr.append([list(map(int, input().split())) for _ in range(N)])
# arr[h][y][x]
    
Q = deque()
for x in range(M):
    for y in range(N):
        for h in range(H):
            if arr[h][y][x] == 1:
                arr[h][y][x] = -1
                Q.append([x,y,h,1])
         
loc = [[0,1,0],[1,0,0],[-1,0,0],[0,-1,0],[0,0,1],[0,0,-1]]

while len(Q) != 0:
    u = Q.popleft()
    for v in loc:
        dx = u[0] + v[0]
        dy = u[1] + v[1]
        dh = u[2] + v[2]
        if 0 <= dx < M and 0 <= dy < N and 0 <= dh < H:
            if arr[dh][dy][dx] == 0:
                arr[dh][dy][dx] = u[3]
                Q.append([dx, dy, dh, u[3]+1])
maxi = 0
checker = True
for x in range(M):
    for y in range(N):
        for h in range(H):
            if arr[h][y][x] == 0:
                maxi = -1
                checker = False
                break
            elif arr[h][y][x] > maxi:
                maxi = arr[h][y][x]
        if checker == False:
            break
    if checker == False:
        break                 
print(maxi)
