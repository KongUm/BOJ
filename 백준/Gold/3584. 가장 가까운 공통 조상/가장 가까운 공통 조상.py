import sys
sys.setrecursionlimit(10**5)
T = int(input())

def dfs(node, level):
    info[node] = level
    for i in graph[node]:
        if info[i] == -1:
            dfs(i, level + 1)

for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    parent = [0]*(N + 1)
    info = [-1] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        parent[b] = a

    A, B = map(int, input().split())

    for i in range(1, N + 1):
        if parent[i] == 0:
            dfs(i, 0)
            break

    while info[A] != info[B]:
        if info[A] > info[B]:
            A = parent[A]
        else:
            B = parent[B]

    while A != B:
        A = parent[A]; B = parent[B]
    print(A)