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
    if b1 <= a2 and a1 <= b2:
        return True
    return False

def lineCross(a1, a2, b1, b2):
    c1 = ccw(a1, a2, b1)
    c2 = ccw(a1, a2, b2)
    c3 = ccw(b1, b2, a1)
    c4 = ccw(b1, b2, a2)
    if c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0:
        if checkOverlap(a1, a2, b1, b2):
            return 1
    elif c1 * c2 <= 0 and c3 * c4 <= 0:
        return 1
    return 0
    
 
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A = [(x1, y1), (x2, y2)]; A.sort()
B = [(x3, y3), (x4, y4)]; B.sort()
print(lineCross(A[0], A[1], B[0], B[1]))
