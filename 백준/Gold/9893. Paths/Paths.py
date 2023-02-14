from collections import deque

V, E = map(int, input().split())

graph = [[] for _ in range(V)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

visited = [False]*V

Q = deque()
Q.append([0, 0, 0]) # 현재 노드, 거리, 비용
visited[0] = True

checker = False
short = int(1e9)
ans = int(1e9)

while len(Q) > 0:
    u = Q.popleft()
    
    if checker == True and u[1] > short:
        print(ans)
        exit()
        
    for i in graph[u[0]]:
        if i[0] == 1:
            if checker == False:
                checker = True
                short = u[1] + 1
                ans = min(ans, u[2] + i[1])
            elif short == u[1] + 1:
                ans = min(ans, u[2] + i[1])
            
        elif visited[i[0]] == False:
            Q.append([i[0], u[1]+1, u[2]+i[1]])
    
print(ans)
