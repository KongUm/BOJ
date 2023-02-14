import sys

V, E = map(int, input().split())
edge = []
for _ in range(E):
    edge.append(list(map(int, sys.stdin.readline().split())))
INF = int(1e9)
D = [INF]*(V+1)
    
def BF(start):
    D[start] = 0
    for c in range(V):
        for i in range(E):
            a, b, w = edge[i][0], edge[i][1], edge[i][2]       
            
            if D[a] != INF and D[a] + w < D[b]:
                D[b] = D[a] + w
                
                if c == V-1:
                    return True
    return False
    
negative_cycle = BF(1)

if negative_cycle == True:
    print(-1)
else:
    for i in range(2,V+1):
        if D[i] == INF:
            print(-1)
        else:
            print(D[i])