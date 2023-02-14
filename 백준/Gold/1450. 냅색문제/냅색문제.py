from itertools import combinations
import bisect

N, C = map(int, input().split())
item = list(map(int, input().split()))

A = []
B = []

if N%2 == 0:
    a = N // 2
else:
    a = N // 2 + 1

for i in range(a + 1):
    for j in combinations(item[:a],i):
        A.append(sum(j))
        
for i in range(a + 1):
    for j in combinations(item[a:],i):
        B.append(sum(j))
A.sort()
B.sort()

ans = 0
for i in range(len(A)):
    t = C - A[i]
    idx = bisect.bisect_right(B, t)
    ans += idx
print(ans)