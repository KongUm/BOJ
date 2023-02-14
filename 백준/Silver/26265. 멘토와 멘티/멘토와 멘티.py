import sys
N = int(input())
A = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
A.sort(reverse = True)
A.sort(key = lambda x : x[0])
for a, b in A:
    print(a, b)