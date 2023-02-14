import sys

sys.setrecursionlimit(100000)
N = int(input()) # N = 컴퓨터의 수 (node)
M = int(input()) # M = 네트워크 상에서 연결되어 있는 컴퓨터 쌍의 수 (edge)

graph = [[] for _ in range(N+1)]
# graph[i] = 노드 i와 연결되어 있는 노드의 번호들이 들어있는 리스트
visited = [False]*(N+1)
# visited[i] = False : 노드 i를 방문하지 않았음
# visited[i] = True : 노드 i를 이미 방문했음


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(R): # R = 시작노드
    visited[R] = True
    for v in graph[R]:
        if visited[v] == False:
            dfs(v)
dfs(1)         
count = 0            
for i in range(1,N+1):
    if visited[i] == True:
        count += 1
print(count-1)
    