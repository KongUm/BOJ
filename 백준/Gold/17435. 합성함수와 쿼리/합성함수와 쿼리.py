import sys

M = int(input())
A = list(map(int, input().split()))
table = [[0]*(M + 1) for _ in range(20)]

for i in range(1, M + 1):
    table[0][i] = A[i - 1]

for i in range(1, 20):
    for j in range(1, M + 1):
        table[i][j] = table[i - 1][table[i - 1][j]]

Q = int(input())

for _ in range(Q):
    n, a = map(int, sys.stdin.readline().split())
    for j in range(19, -1, -1):
        if n >= 1 << j:
            n -= 1 << j
            a = table[j][a]
    print(a)