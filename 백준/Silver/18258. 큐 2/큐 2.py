from collections import deque
import sys

N = int(input())
queue = deque()

for i in range(N):
    A  = sys.stdin.readline().split()
    
    if A[0] == "push":
        queue.append(A[1])
    
    elif A[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
        
    elif A[0] == "size":
        print(len(queue))
        
    elif A[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif A[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
        