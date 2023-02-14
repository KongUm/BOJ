import sys
import math
arr = list(map(int, input().split()))
stack = []
cnt = 0
r = 2**(-0.5)
dx = [0,r,1,r,0,-r,-1,-r]
dy = [1,r,0,-r,-1,-r,0,r]

def CCW():
    global cnt
    checker = True
    for p in range(8):
        a,b,c = stack[p-2], stack[p-1], stack[p]
        ax, ay = arr[a]*dx[p-2], arr[a]*dy[p-2]
        bx, by = arr[b]*dx[p-1], arr[b]*dy[p-1]
        cx, cy = arr[c]*dx[p], arr[c]*dy[p]
        
        x1,x2,y1,y2 = bx-ax, cx-bx, by-ay, cy-by
        
        if math.fabs(x2*y1 - x1*y2) > sys.float_info.epsilon:  
            if x2*y1 < x1*y2:
                checker = False
                break
    if checker == True:
        cnt += 1
    return        
    
def BT(n):
    if n == 8:
        CCW()
        return
    else:
        for i in range(8):
            if i in set(stack):
                continue
            stack.append(i)
            BT(n+1)
            stack.pop()
BT(0)
print(cnt)            
