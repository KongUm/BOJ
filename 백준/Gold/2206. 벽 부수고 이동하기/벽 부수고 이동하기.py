import copy
from collections import deque
N, M = map(int, input().split())
# N = 세로, M = 가로
arr = [[-2]*(M+2)]
for _ in range(N):
    a = []
    S = input()
    a.append(-2)
    for i in range(M):
        if int(S[i]) == 1:
            a.append(-1)
        else:
            a.append(0)
    a.append(-2)
    arr.append(a)
arr.append([-2]*(M+2))
arr2 = copy.deepcopy(arr)
visited = [arr, arr2]


# 지나갈 수 있는길 = 0, 벽 = -1, 공간밖 = -2
# visited[z][y][x] -> z = 0 : 벽을 통과하지 않은 경로, z = 1 벽을 통과한 경로 
 
Q = deque() #Queue
loca = [[0,1],[1,0],[-1,0],[0,-1]]

def bfs(x,y):
    visited[0][y][x] = 1
    visited[1][y][x] = 1 # 벽 통과 여부에 상관없이 시작지점은 항상 통과
    Q.append([x,y,0,1])
 
    while len(Q) != 0:
        u = Q.popleft()
        for v in loca:
            dx = u[0] + v[0]
            dy = u[1] + v[1]
            
            if dx == M and dy == N:
                visited[u[2]][dy][dx] = u[3]+1
                return u[3]+1
                
            if u[2] == 0: #벽통과 0번
                if visited[0][dy][dx] == 0:
                    visited[0][dy][dx] = u[3]+1             
                    visited[1][dy][dx] = u[3]+1       
                    Q.append([dx,dy,0,u[3]+1])
                    
                elif visited[0][dy][dx] == -1:               
                    #벽을 통과할 수 있는 상황에서 벽을 만났을때
                          
                        visited[1][dy][dx] = u[3]+1
                     
                        Q.append([dx,dy,1,u[3]+1])

                    
            elif u[2] == 1: # 이미 벽통과를 한상태
                if visited[1][dy][dx] == 0: 
                    
                    visited[1][dy][dx] = u[3]+1
                    Q.append([dx,dy,1,u[3]+1])
t = arr[1][1]
ans = bfs(1,1)

if N == 1 and M == 1 and t == 0:
    print(1)
elif ans == None:
    print(-1)
else:
    print(ans)
#print(visited)

           
                
            
        
       
