A = list(int(input()) for _ in range(3))
N = A[0]*A[1]*A[2]

for i in range(10):
    print(str(N).count(str(i)))