from math import gcd
N, S = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in A:
    B.append(abs(S - i))

a = B[0]
for i in B[1:]:
    a = gcd(a, i)
print(a)
