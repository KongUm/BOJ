from collections import deque
N, K = map(int, input().split())
queue = deque(i for i in range(1,N+1))
ans = []
while len(queue) != 0:
    for i in range(1,K+1):
        if i == K:
            ans.append(queue.popleft())
        else:
            queue.append(queue.popleft())

print("<", end = "")
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end = ">")
    else:
        print(ans[i], end = ", ")