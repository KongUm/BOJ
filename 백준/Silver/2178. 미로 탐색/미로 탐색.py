from collections import deque
N, M = map(int, input().split())
# N = 세로, M = 가로
maze = []
maze.append([0]*(M+2))
for i in range(1,N+1):
    a = input()
    maze.append([0])
    for j in range(M):
        maze[i].append(int(a[j]))
    maze[i].append(0)
maze.append([0]*(M+2))
Q = deque() # 큐
xy = [[0,1],[1,0],[-1,0],[0,-1]]

def bfs(x,y):
    Q.append([[x,y]])
    count = -1
    edge = 0
    maze[y][x] = count
    
    while len(Q) != 0:
        u = Q.popleft()
        count -= 1
        qq = []
        for i in u:   
            for v in xy:
                if i[1]+v[1] == N and i[0]+v[0] == M:
                    maze[N][M] = count
                    return
                elif maze[i[1]+v[1]][i[0]+v[0]] == 1:
                    maze[i[1]+v[1]][i[0]+v[0]] = count
                    qq.append([i[0]+v[0],i[1]+v[1]])
        Q.append(qq)
bfs(1,1)
print(maze[N][M]*(-1))