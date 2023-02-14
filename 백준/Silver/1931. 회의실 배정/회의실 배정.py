import sys
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
A.sort()

count = 0
last = 0

for i in A:
    if i[0] >= last:
        count += 1
        last = i[1]
    elif i[1] < last:
        last = i[1]
print(count)