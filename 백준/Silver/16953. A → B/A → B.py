from collections import deque

A, B = map(int, input().split())

Q = deque()

count = 1

def bfs():

    global count

    Q.append([A,count])

    while len(Q) != 0:

        u = Q.popleft()

 

        p = u[0]*2

        q = int(str(u[0])+'1')

  

        if p == B or q == B:

            return u[1]+1

        if p < B:

            Q.append([p,u[1]+1])

        if q < B:

            Q.append([q,u[1]+1])

        

    return -1

print(bfs())

            

        

    