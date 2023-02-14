import sys

N = int(input())
D = {}
D['ChongChong'] = 0
parent = [0]
query = []
for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    if a not in D:
        parent.append(parent[-1] + 1)
        D[a] = parent[-1]
    if b not in D:
        parent.append(parent[-1] + 1)
        D[b] = parent[-1]
    query.append((a, b))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(D[a])
    b = find(D[b])
    if a != 0 and b != 0:
        return 
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(N):
    a, b = query[i]
    union(a, b)

cnt = 0

for i in range(len(parent)):
    if parent[i] == 0:
        cnt += 1
print(cnt)