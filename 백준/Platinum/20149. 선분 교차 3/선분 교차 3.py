from decimal import Decimal as d
INF = int(1e10)
ansx, ansy = d(INF), d(INF)

def ccw(a, b, c):
    # a -> b -> c 의 회전 방향을 나타냄
    res = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
    
    if res < 0: # 시계 방향
        return -1
    elif res > 0: # 반시계 방향
        return 1
    else: # 일직선 상
        return 0
        
def checkOverlap(a1, a2, b1, b2):
    t1, t2 = [a1, a2], [b1, b2]
    global ansx, ansy
    if b1 <= a2 and a1 <= b2:
        if a1 == b2:
            ansx, ansy = a1[0], a1[1]
        elif a2 == b1:
            ansx, ansy = a2[0], a2[1]
        return True
    return False

def get(a1, a2, b1, b2):
    global ansx, ansy
    x1, y1 = a1
    x2, y2 = a2
    x3, y3 = b1
    x4, y4 = b2
    
    if d(x2) - d(x1) == 0:
        s2 = (d(y4) - d(y3)) / (d(x4) - d(x3))
        a2 = d(y3) - d(s2) * d(x3)
        ansx = x1
  
        ansy = s2 * x1 + a2
        return
    
    if d(x4) - d(x3) == 0:
        s1 = (d(y2) - d(y1)) / (d(x2) - d(x1))
        a1 = d(y1) - d(s1) * d(x1)
        ansx = x3
        ansy = s1 * x3 + a1
        return
        
    s1 = (d(y2) - d(y1)) / (d(x2) - d(x1))
    a1 = d(y1) - d(s1) * d(x1)
     
    s2 = (d(y4) - d(y3)) / (d(x4) - d(x3))
    a2 = d(y3) - d(s2) * d(x3)
    
    ansx = (d(a2) - d(a1)) / (d(s1) - d(s2)) # 노상관
    ansy = d(ansx) * d(s1) + d(a1)
    
def lineCross(a1, a2, b1, b2):
    c1 = ccw(a1, a2, b1)
    c2 = ccw(a1, a2, b2)
    c3 = ccw(b1, b2, a1)
    c4 = ccw(b1, b2, a2)
    if c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0:
        if checkOverlap(a1, a2, b1, b2):
            return 1
    elif c1 * c2 <= 0 and c3 * c4 <= 0:
        get(a1, a2, b1, b2)
        return 1
    return 0
    
 
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A = [(x1, y1), (x2, y2)]; A.sort()
B = [(x3, y3), (x4, y4)]; B.sort()
ans = lineCross(A[0], A[1], B[0], B[1])
print(ans)

if ans == 1 and ansx != INF and ansy != INF:
    print(ansx, ansy)