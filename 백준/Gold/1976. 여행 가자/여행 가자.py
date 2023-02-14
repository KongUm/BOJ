import sys
sys.setrecursionlimit(100000)
N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

def Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])
    return parent[x]

def Union(a, b):
    if parent[a] == parent[b]:
        return
    a = Find(a)
    b = Find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(N):
    command = list(map(int, input().split()))
    for j in range(N):
        if command[j] == 1:
            Union(i+1, j+1)
S = list(map(int, input().split()))

start = parent[S[0]]
for i in range(len(S)):
    a = Find(S[i-1])
    if a != start:
        print("NO")
        exit()
print("YES")
