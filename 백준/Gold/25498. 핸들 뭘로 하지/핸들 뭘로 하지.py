import sys
from collections import deque

N = int(input())
S = "." + input()
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    A = list(map(int, sys.stdin.readline().split())) 
    graph[A[1]].append(A[0])
    graph[A[0]].append(A[1])


handle = []
Q = deque()
visited = [False]*(N+1)
def bfs():
    Q.append([1,0]) # 0 = node번호, 1 = level (0부터 시작)
    handle.append(ord(S[1])-96)
    visited[1] = True
    while len(Q) != 0: 
        u = Q.popleft()
        for v in graph[u[0]]:
            if visited[v] == True:
                continue
            visited[v] = True
            if u[1] != 0 and ord(S[u[0]])-96 != handle[u[1]]:
                break
            if len(handle) == u[1]+1:
                handle.append(ord(S[v])-96)
            else:
                handle[u[1]+1] = max(handle[-1], ord(S[v])-96)
            Q.append([v,u[1]+1]) 
            #print(Q)
        
bfs()
for i in range(len(handle)):
    print(chr(handle[i]+96), end = "")
