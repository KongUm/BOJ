A = list(int(input())%42 for _ in range(10))
N = list()

for i in range(10):
    if N.count(str(A[i])) == 0:
        N.append(str(A[i]))
print(len(N))