import sys
from collections import deque
N = int(input())
Q = deque()
while True:
   
    c = int(sys.stdin.readline())
    if c < 0:
        break
    elif c > 0:
        if len(Q) < N:
            Q.append(c)
    else:
        Q.popleft()
        
if len(Q) == 0:
    print("empty")
else:
    for i in range(len(Q)):
        print(Q.popleft(), end = " ")
    