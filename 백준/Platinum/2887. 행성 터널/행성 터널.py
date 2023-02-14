import sys
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
        
xp = []
yp = []
zp = []
total = 0

for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    xp.append((x, i))
    yp.append((y, i))
    zp.append((z, i))
xp.sort()
yp.sort()
zp.sort()

edge = []
for i in range(1,N):
    edge.append((abs(xp[i][0] - xp[i-1][0]), xp[i-1][1], xp[i][1]))
    edge.append((abs(yp[i][0] - yp[i-1][0]), yp[i-1][1], yp[i][1]))
    edge.append((abs(zp[i][0] - zp[i-1][0]), zp[i-1][1], zp[i][1]))
edge.sort()

for i in range(len(edge)):
    w, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        total += w
print(total)        

    
    
    
    