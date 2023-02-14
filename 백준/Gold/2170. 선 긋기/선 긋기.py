import sys
N = int(input())
line = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    line.append((min(a, b), max(a, b)))

line.sort()
now = line[0][0]
total = 0

for i in range(N):
    s, e = line[i]
    if s <= now:
        diff = e - now
        if diff > 0:
            now = e; total += diff
    else:
        total += e - s
        now = e
print(total)