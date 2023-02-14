# 크루스칼 (Kruskal) 알고리즘
import sys
V, E = map(int, input().split())

parent = [0] + [i for i in range(1, V+1)] # 부모테이블 초기화

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
      
edge = []
total = 0

for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    edge.append((w, a, b))
    
edge.sort() # 가중치가 내림차순이 되도록 정렬

for i in range(E):
    w, a, b = edge[i]
    if find(a) != find(b):
        # 만약 a와 b가 같은 집합에 속해있지 않다면 (연결되어 있지 않다면)
        union(a, b) 
        total += w 
print(total)