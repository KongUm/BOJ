N = int(input())
A = list(map(int, input().split()))
A.sort()
if N%2 == 0:
    print(A[0]*A[-1])
else:
    print(A[N//2]**2)