def update(index, value): 
    while index < len(tree):
        tree[index] += value
        index += (index & -index)

def find(index): 
    res = 0
    while index > 0:
        res += tree[index]
        index -= (index & -index)
        
    return res

import sys
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    C = [[] for _ in range(10**5 + 2)] # Y =  0 ~ 100001
    P = [[] for _ in range(10**5 + 2)] 
    tree = [0]*(10**5 + 2) # X = 0 ~ 100001
    
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        C[y].append(x + 1) # 1 ~ 100001
        
    for _ in range(M):
        x1, x2, y1, y2 = map(int, sys.stdin.readline().split())
        # 직사각형의 왼쪽 아래 좌표 (x1, y1), 오른쪽 위 좌표 (x2, y2)
        P[y1].append((0, x1 + 1, x2 + 1)) # x : 1 ~ 100001
        P[y2 + 1].append((1, x1 + 1, x2 + 1))
        # sum(0) - sum(1) # 내림차순으로 봐야함
    
    A, B = 0, 0
    for y in range(10**5 + 1, -1, -1): # Y : 100001 ~ 0
        for x in C[y]:
            update(x, 1)
           
            
        for q, x1, x2 in P[y]:
           # print(q, x1, x2, y)
            if q == 0:
                A += find(x2) - find(x1 - 1)
            else:
                B += find(x2) - find(x1 - 1)
        
    print(A - B)