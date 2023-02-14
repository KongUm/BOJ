N, M = map(int, input().split())
A = input()
B = input()

one = [[0,0] for _ in range(M)]
idx = 0
for i in range(N+M):
    if A[i] == '1':
        one[idx][0] = i
        idx += 1
idx = 0
for i in range(N+M):
    if B[i] == '1':
        one[idx][1] = i
        idx += 1

cnt = 0
for i in range(M):
    cnt += abs(one[i][0] - one[i][1])

a = cnt // 2
b = cnt - a
print(a**2 + b**2)

