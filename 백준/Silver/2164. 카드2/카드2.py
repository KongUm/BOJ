from collections import deque
import sys

N = int(input())
queue = deque(i for i in range(1,N+1))

#print(queue)
if N > 1:
    while True:
        queue.popleft()
        if len(queue) == 1:
            print(queue[0])
            break
        queue.append(queue.popleft())
else:
    print(1)