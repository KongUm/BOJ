import sys
from collections import deque
N = int(input())
deque = deque()

for _ in range(N):
    A = sys.stdin.readline().split()
    if A[0] == "push_front":
        deque.appendleft(int(A[1]))     
    elif A[0] == "push_back":
        deque.append(int(A[1]))
        
    elif A[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif A[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
        
    elif A[0] == "size":
        print(len(deque))
        
    elif A[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif A[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    else:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
        