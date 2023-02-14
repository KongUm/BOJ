from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(arr,sz,sy,sx, end):
    Q = deque()
    Q.append([sz, sy, sx, 0])
    arr[sz][sy][sx] = -2
    
    while len(Q) > 0:
        u = Q.popleft()
        
        for i in range(6):
            nz, ny, nx = u[0] + dz[i], u[1] + dy[i], u[2] + dx[i]
            if 0 <= nz < len(arr) and 0 <= ny < len(arr[sz]) and 0 <= nx < len(arr[sz][sy]):
                if arr[nz][ny][nx] == 0:
                    arr[nz][ny][nx] = u[3]+1
                    Q.append([nz, ny, nx, u[3]+1])
                    
    return  arr[end[0]][end[1]][end[2]]
    
while True:
    F, H, W = map(int, input().split())
    
    if F+H+W == 0:
        exit()
    
    arr = []
    start = []
    end = []
    for f in range(F):
        arr.append([])
        for i in range(H):
            temp = []
            a = input()
            for j in range(W):
                if a[j] == 'S':
                    start = [f,i,j]
                if a[j] == 'E':
                    end = [f, i, j]
                if a[j] == '#':
                    temp.append(-1)
                else:
                    temp.append(0)
            arr[f].append(temp)
        l = input()
    dest = bfs(arr, start[0], start[1], start[2], end)
    
    if dest > 0:
        print("Escaped in " + str(dest) + " minute(s).")
    else:
        print("Trapped!")
        
                    
   
