from collections import deque

isprime = [False, False] + [True]*(10**5-1)

for i in range(2, 100001):
    if isprime[i]:
        for j in range(2*i, 100001, i):
            isprime[j] = False

def bfs(N, A, B):
    visited = [False]*1000001
    Q = deque()
    visited[N] = True
    Q.append([N, 0])

    while len(Q) > 0:
        u, cnt = Q.popleft()
        if A <= u <= B and isprime[u]:
            return cnt
        for i in range(-1, 2, 2):
            if 0 <= u + i <= 1000000 and visited[u + i] == False:
                Q.append([u + i, cnt + 1])
                visited[u + i] = True
        for i in range(2, 4):
            if 0 <= u // i <= 1000000 and visited[u // i] == False:
                Q.append([u // i, cnt + 1])
                visited[u // i] = True
    return -1

T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    print(bfs(N, A, B))

