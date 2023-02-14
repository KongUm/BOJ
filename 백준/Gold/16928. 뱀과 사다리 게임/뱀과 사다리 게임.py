from collections import deque

N, M = map(int, input().split())
graph = [0]*101

for _ in range(M+N):
    a, b = map(int, input().split())
    graph[a] = b

arr = [0]*101
Q = deque()

def bfs(N):
    arr[0] = -1
    Q.append([N,1])
    
    while len(Q) != 0:
        u = Q.popleft()
        for v in range(1,6+1):
            x = u[0] + v
            if 0 < x < 101:
                if arr[x] == 0:
                    if x == 100:
                        return u[1]
                    else:
                        if graph[x] > 0:
                            arr[graph[x]] = u[1]
                            arr[x] = u[1]
                            Q.append([graph[x], u[1]+1])
                        else:
                            arr[x] = u[1]
                            Q.append([x, u[1]+1])
print(bfs(1))