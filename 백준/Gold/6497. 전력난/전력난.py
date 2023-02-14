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
        
while True:
    V, E = map(int, input().split())
    if V + E == 0:
        exit()
    
    edge, total, all = [], 0, 0
    parent = [0] + [i for i in range(1, V + 1)]
    
    for _ in range(E):
        a, b, w = map(int, input().split())
        edge.append((w, a, b)); all += w
    edge.sort()
    
    for i in range(E):
        w, a, b = edge[i]
        if find(a) != find(b):
            union(a, b)
            total += w
    print(all - total)