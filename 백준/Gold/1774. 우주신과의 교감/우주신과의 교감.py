V, E = map(int, input().split())

parent = [i for i in range(V+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

vert = [[0,0]] + [list(map(int, input().split())) for _ in range(V)]
edge = []
total = 0

for i in range(E):
    a, b = map(int, input().split())
    edge.append((0, a, b))

for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j:
            dx = vert[i][0] - vert[j][0]
            dy = vert[i][1] - vert[j][1]
            c = (dy**2 + dx**2)**0.5
            edge.append((c, i, j))
edge.sort()

for i in range(len(edge)):
    w, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        total += w
print('%0.2f' %total)