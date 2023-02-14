N = int(input())


parent = [i for i in range(N)]

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
        
vert = []
edge = []
total = 0

for _ in range(N):
    x, y = map(float, input().split())
    vert.append([x, y])

for i in range(N):
    for j in range(N):
        if i != j:
            dx = vert[i][0] - vert[j][0]
            dy = vert[i][1] - vert[j][1]
            c = (dx**2 + dy**2)**0.5
            edge.append([c, i, j])           
edge.sort()

for i in range(len(edge)):
    w, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        total += w
print(total)