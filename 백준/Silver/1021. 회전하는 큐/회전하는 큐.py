from collections import deque
N, M = map(int, input().split())
# N = 큐의 크기 M = 뽑아내려고 하는 수의 개수

A = list(map(int, input().split()))
D = deque(i for i in range(1,N+1))
count = 0

for target in A:
    while True:
        if D[0] == target:
            D.popleft()
            break
        elif D.index(target) <= len(D)//2:
            D.append(D.popleft())
            count += 1
        else:
            D.appendleft(D.pop())
            count += 1
        
print(count)