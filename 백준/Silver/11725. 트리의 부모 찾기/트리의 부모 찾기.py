import sys
from collections import deque

N = int(input())

tree = [[] for _ in range(N+1)]
used = set()

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

Q = deque()
Q.append(1)

d = [0]*(N+1)

while len(Q) > 0:
    u = Q.popleft()
    for i in tree[u]:
        if d[i] == 0:
            d[i] = u
            Q.append(i)
for i in range(2, N+1):
    print(d[i])