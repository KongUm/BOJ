import sys
sys.setrecursionlimit(100000)
N, M, R = map(int, input().split())

E = [[] for _ in range(N+1)]
# 간선집합 E[i] = vertex i와 연결되어 있는 vertex들이 오름차순으로 정렬 되어 있는 리스트 
V = set() #정점 집합
visited = [False]*(N+1)
count = [0]*(N+1)
cnt = 0

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    V.add(a)
    V.add(b)
    E[a].append(b)
    E[b].append(a)
    
for i in range(1,N+1):
    E[i].sort(reverse = True)
 
def dfs(V, E, R):
    global cnt
    cnt += 1
    visited[R] = True
    count[R] = cnt
    #print(E[R])
    for x in E[R]:
        #print(visited[x])
        if visited[x] == False:
            dfs(V, E, x)
dfs(V,E,R)
for i in range(1,N+1):
    print(count[i])