import sys
from collections import deque

T = int(input())

def bfs(visited):
    Q = deque()
    for i in range(1,V+1):
        if visited[i] == 0:
            start = i
            visited[start] = 1 # 첫 시작 노드는 검은색
            Q.append([start,1])
      
            while len(Q) != 0:
                u = Q.popleft()
                for v in graph[u[0]]:
                    if u[1] == 1:
                        color = 2
                    else:
                        color = 1
                    
                    if visited[v] == 0: # 방문하지 않았다면
                        visited[v] = color
                        Q.append([v, color])
                    elif visited[v] != color: # 연속된다면
                        return "NO"
    return "YES"

for _ in range(T):
    V, E = map(int, input().split())
    # V = 정점의 개수, E = 간선의 개수 (1부터 시작)
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    # visited: 0 = 방문 안함, 1 = 검은색, 2 = 빨간색
    for i in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    print(bfs(visited))