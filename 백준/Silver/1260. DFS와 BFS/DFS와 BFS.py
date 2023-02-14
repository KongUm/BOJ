import sys
from collections import deque
sys.setrecursionlimit(100000)
N, M, V = map(int, input().split())
# N = node의 개수, M = edge의 개수, V = 시작 node

graph = [[] for _ in range(N+1)]
# graph[i] = 노드 i와 연결되어 있는 노드의 번호들이 들어있는 리스트

dfs_visited = [False]*(N+1)
bfs_visited = [False]*(N+1)
# visited[i] = False : 노드 i를 방문하지 않았음
# visited[i] = True : 노드 i를 이미 방문했음
ans_dfs = []
ans_bfs = []
Q = deque()

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()
    
def dfs(R): # R = 시작노드
    dfs_visited[R] = True
    ans_dfs.append(R)
    for v in graph[R]:
        if dfs_visited[v] == False:
            dfs(v)
 
def bfs(R): 
    bfs_visited[R] = True
    ans_bfs.append(R)
    Q.append(R)
    while len(Q) != 0:
        u = Q.popleft()
        for v in graph[u]:
            if bfs_visited[v] == False:
                bfs_visited[v] = True
                ans_bfs.append(v)
                Q.append(v)
           
dfs(V)
bfs(V)        

for i in range(len(ans_dfs)):
    if i == len(ans_dfs)-1:
        print(ans_dfs[i])
    else:
        print(ans_dfs[i], end = " ")

for i in range(len(ans_bfs)):
    if i == len(ans_bfs)-1:
        print(ans_bfs[i])
    else:
        print(ans_bfs[i], end = " ")
    