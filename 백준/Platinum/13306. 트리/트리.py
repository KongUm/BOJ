import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    if find(a) != find(b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


N, Q = map(int, input().split())
info = [0, 1]
for _ in range(N - 1):
    info.append(int(sys.stdin.readline()))
parent = [i for i in range(N + 1)]

query = []
for _ in range(Q + N - 1):
    query.append(list(map(int, sys.stdin.readline().split())))

stack = []
for i in range(Q + N - 1):
    q = query.pop()
    if q[0] == 0:
        a = q[1]
        union(a, info[a])
    else:
        b, c = q[1], q[2]
        if find(b) == find(c):
            stack.append("YES")
        else:
            stack.append("NO")
for i in range(Q):
    print(stack.pop())




