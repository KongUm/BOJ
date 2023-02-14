import sys
N = int(input())

D = {}

for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    b = int(b)
    if a not in D:
        D[a] = 0
    D[a] += b
for i in D.keys():
    if D[i] == 5:
        print("YES")
        exit()
print("NO")