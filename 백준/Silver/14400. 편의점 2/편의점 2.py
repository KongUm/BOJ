import sys
n = int(input())

x, y = [], []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a); y.append(b)

x.sort(); y.sort()
mx, my = x[n // 2], y[n // 2]

res = 0
for i in range(n):
    res += abs(x[i] - mx) + abs(y[i] - my)
print(res)