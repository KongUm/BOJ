import sys
import math
sys.setrecursionlimit(300000)

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [i for i in range(N + 1)]
used = [-1] * (N + 1)
cnt = [0] * (N + 1)
info = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n, p):
    for node in graph[n]:
        if node != p:
            info[node] = n
            dfs(node, n)


def find(target):
    if target == parent[target]:
        return target

    # 경로 압축 최적화
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b


dfs(1, 0)
Q = int(input())
for _ in range(Q):
    k, *A = map(int, sys.stdin.readline().split())
    temp = []
    ans = 0

    for i in A:
        used[i] = 0

    for i in A:
        if used[info[i]] == 0:
            union(i, info[i])

    for i in A:
        cnt[find(i)] += 1

    for i in A:
        ans += cnt[i] * (cnt[i] - 1) // 2
        parent[i] = i
        used[i] = -1
        cnt[i] = 0
    print(ans)








