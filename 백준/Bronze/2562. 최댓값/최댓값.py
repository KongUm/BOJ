import sys
i = 0

a = [int(sys.stdin.readline().strip()) for i in range(9)]

print(max(a))

while a[i] != max(a):
    i = i + 1

print(i+1)