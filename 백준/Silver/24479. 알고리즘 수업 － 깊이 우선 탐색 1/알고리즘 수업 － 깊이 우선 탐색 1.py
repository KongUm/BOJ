#공부용 코드
import sys
sys.setrecursionlimit(100000)
N, M, R = map(int, input().split())

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
    graph[i].sort()
    
def dfs(R): # R = 시작 노드
    global count
    visited[R] = count # 방문한 노드에 방문처리를 해준다
    #graph[R].sort()
    for x in graph[R]:
        if visited[x] == 0: # 아직 방문하지 않은 노드가 존재한다면
            count += 1
            dfs(x) # 더 깊이 들어가 탐색한다
     
dfs(R)
for i in range(1,N+1):
    print(visited[i])
