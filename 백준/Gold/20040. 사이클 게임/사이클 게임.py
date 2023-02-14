import sys
N, M = map(int, input().split())
parent = [i for i in range(N)]
cnt = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a
    else:
        return True
    return False
    
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    cnt += 1
    if union(a, b):
        print(cnt)
        exit()
print(0)
    