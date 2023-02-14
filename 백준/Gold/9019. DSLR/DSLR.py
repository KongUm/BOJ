from collections import deque

T = int(input())

def bfs(A, B):
    visited = [""]*10001
    dp = [-1]*10001
    Q = deque()
    visited[A] = "A"
    Q.append([A, 0])
    
    while len(Q) > 0:
        u = Q.popleft()
        if u[0] == B:
            return u[1], visited, dp
        if visited[u[0]*2 %10000] == "":
            Q.append([u[0]*2 %10000, u[1]+1])
            visited[u[0]*2 %10000] = "D"
            dp[u[0]*2 %10000] = u[0]
        
        if u[0] == 0:
            a = 9999
        else:
            a = u[0]-1
        if visited[a] == "":
            Q.append([a, u[1]+1])
            visited[a] = "S"
            dp[a] = u[0]
        
        d = "0"*(4-len(str(u[0]))) + str(u[0])
        ld = int(d[1:4] + d[0])
        rd = int(d[3] + d[:3])
        
        if visited[ld] == "":
            Q.append([ld, u[1]+1])
            visited[ld] = "L"
            dp[ld] = u[0]
            
        if visited[rd] == "":
            Q.append([rd, u[1]+1])
            visited[rd] = "R"
            dp[rd] = u[0]
    
for _ in range(T):
    A, B = map(int, input().split())
    cnt, visited, dp = bfs(A, B)
    path = []
    n = B
    for i in range(cnt):
        path.append(visited[n])
        n = dp[n]
    for i in range(cnt):
        print(path.pop(), end = "")
    print()