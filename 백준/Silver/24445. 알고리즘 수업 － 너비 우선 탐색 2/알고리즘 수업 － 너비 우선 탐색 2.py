import sys
from collections import deque

sys.setrecursionlimit(100000)
N, M, R = map(int, input().split())
Q = deque()
graph = [[] for _ in range(N+1)]
# graph[i] = 노드 i와 연결되어 있는 노드의 번호들이 들어있는 리스트
visited = [0]*(N+1)
# visited[i] = 0 : 노드 i를 방문하지 않았음
# visited[i] = n : 노드 i를 n번째에 방문했음
count = 1

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,N+1):
    graph[i].sort(reverse = True)
    
def bfs(R): # R = 시작 정점
    global count
    
    visited[R] = count # 시작지점 노드에 방문표시
    Q.append(R) # 시작 지점의 
    
    while len(Q) != 0:
        u = Q.popleft() 
        for v in graph[u]:
            if visited[v] == 0:
                count += 1
                visited[v] = count
                Q.append(v)
bfs(R)
             
for i in range(1,N+1):
    print(visited[i])