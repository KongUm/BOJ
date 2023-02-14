from collections import deque
N, w, L = map(int, input().split())
A = list(map(int, input().split()))

Q = deque()
for i in range(w):
    Q.append(0)
now_weight = 0
cnt = 0

for i in range(N):
    checker = False
    while now_weight + A[i] > L:
        now_weight -= Q.popleft()
        Q.append(0)
        cnt += 1
        checker = True
    if checker:
        Q.pop()
        Q.append(A[i])
        now_weight += A[i]
    else:
        now_weight -= Q.popleft()
        Q.append(A[i])
        now_weight += A[i]
        cnt += 1
while now_weight != 0:
    now_weight -= Q.popleft()
    cnt += 1
print(cnt)


