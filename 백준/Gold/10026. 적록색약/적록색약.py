from collections import deque
N = int(input())

A = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == 'R':
            B[i].append('G')
        else:
            B[i].append(S[j])
        A[i].append(S[j])

Q = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs_A(x,y):
    if A[y][x] == 'V':
        return False
    color = A[y][x]
    A[y][x] = 'V'
    Q.append([x,y]) 
    while len(Q) != 0:
        u = Q.popleft()
       
        for i in range(4):
            cx = u[0]+dx[i]
            cy = u[1]+dy[i]
            if 0 <= cx < N and 0 <= cy < N and A[cy][cx] == color:
                A[cy][cx] = 'V'
                Q.append([cx, cy])
    return True

def bfs_B(x,y):
    if B[y][x] == 'V':
        return False
    color = B[y][x]
    B[y][x] = 'V'
    Q.append([x,y]) 
    while len(Q) != 0:
        u = Q.popleft()
        
        for i in range(4):
            cx = u[0]+dx[i]
            cy = u[1]+dy[i]
            if 0 <= cx < N and 0 <= cy < N and B[cy][cx] == color:
                B[cy][cx] = 'V'
                Q.append([cx, cy])
    return True
acnt = 0
bcnt = 0
for y in range(N):
    for x in range(N):
        if bfs_A(x,y) == True:
            acnt += 1
        if bfs_B(x,y) == True:
            bcnt += 1
print(acnt,bcnt)
    
    
    
    