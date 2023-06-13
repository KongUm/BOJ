import math
n = int(input())
A = list(map(int, input().split()))
B = sorted(A[:])

for i in range(n):
    a = A[i] * B[i]
    
    if int(math.isqrt(A[i] * B[i])) ** 2 != A[i] *B[i]:
        print("NO")
        exit()
print("YES")