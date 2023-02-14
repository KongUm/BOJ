from collections import deque
MAX, flag = 1000010, True

def push_Q():
    for i in range(MAX - 1, -1, -1):
        if ty[i] == 0:
            Q.append(i)
    

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
ty = [0] * (MAX)

for i in A:
    ty[i] = 1

Q = deque()
push_Q()

for i in range(N):
    u = A[i]
    while (len(Q) > 0 and (Q[0] >= u or ty[Q[0]] != 0)): Q.popleft()
    if (len(Q) == 0 or u - Q[0] > M):
        flag = False
        break
    tmp = Q.popleft()
    ty[tmp] = 2

Q = deque()
push_Q()

for i in range(N):
    u = A[i]
    while (len(Q) > 0 and (Q[0] >= u or ty[Q[0]] != 0)): Q.popleft()
    if (len(Q) == 0):
        flag = False
        break
    tmp = Q.popleft()
    ty[tmp] = 2
if flag:
    print("success")
else:
    print("fail")