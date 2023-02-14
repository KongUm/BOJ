from collections import deque
T = int(input())

a = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]

def bfs(x,y,cnt):
    Q = deque()
    arr[y][x] = -1 # 시작지점 방문 표시
    Q.append([x,y,cnt]) #큐에 시작지점 좌표 담음
    
    while len(Q) != 0:
        u = Q.popleft()
        for v in a:
            dx = u[0]+v[0]
            dy = u[1]+v[1]
            if 0 <= dx < I and 0 <= dy < I:
                if dx == end[0] and dy == end[1]:
                    arr[dy][dx] = u[2]+1
                    return u[2]+1
                elif arr[dy][dx] == 0:
                    arr[dy][dx] = u[2]+1
                    Q.append([dx,dy,u[2]+1])

for _ in range(T):
    I = int(input())
    arr = [[0]*I for _ in range(I)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    if start == end:
        print(0)
    else:
        print(bfs(start[0], start[1],0))