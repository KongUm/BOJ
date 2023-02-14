from collections import deque
N = int(input())
Q = deque()
count = 0

def bfs():
    global count
    for i in range(1,10):
        Q.append(str(i))
    count += 9
    
    while True:
        if len(Q) == 0:
            return -1 
        u = Q.popleft()
        for i in range(10): # 0 ~ 10
            if i < int(u[-1]):
                num = u + str(i)
                Q.append(num)
                count += 1
            
                if int(num) > 9876543210:
                    return -1
                if count == N:
                    return int(num)                  
                    
if N < 10:
    print(N)
else:
    print(bfs())