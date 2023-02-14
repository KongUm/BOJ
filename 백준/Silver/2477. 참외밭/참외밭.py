K = int(input())

A = [list(map(int, input().split())) for _ in range(6)]
A.append(A[0])

c = [[1, 3], [4, 1], [2, 4], [3, 2]]
B = [[], []]
t = 0
for i in range(6):
    for a, b in c:
        if A[i][0] == a and A[i + 1][0] == b:
            t = A[i][1] * A[i + 1][1]
            break
    if t != 0: break
for i in range(6):
    if A[i][0] <= 2:
        B[0].append(A[i][1])
    else: B[1].append(A[i][1])
ans = max(B[0]) * max(B[1]) - t
print(ans * K)