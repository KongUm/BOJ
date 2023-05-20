n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ia, ib = [0] * (n + 1), [0] * (n + 1)
for i in range(n):
    ia[A[i]] = i
    ib[B[i]] = i

p = B[ib[A[-1]] + 1:] + B[:ib[A[-1]] + 1]
q = B[ib[A[0]] + 1:] + B[:ib[A[0]] + 1]

if p == A or q[::-1] == A:
    print("good puzzle")
else:
    print("bad puzzle")
    