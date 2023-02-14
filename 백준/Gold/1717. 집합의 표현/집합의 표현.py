import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])
    return parent[x]

def Union(a, b):
    a = Find(a)
    b = Find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    type, p, q = map(int, sys.stdin.readline().split())
    if type == 0:
        Union(p, q)
    else:
        p = Find(p)
        q = Find(q)
        if p == q:
            print("YES")
        else:
            print("NO")

