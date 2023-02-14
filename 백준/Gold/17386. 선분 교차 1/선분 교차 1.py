def ccw(a, b, c):
    # a -> b -> c 의 회전 방향을 나타냄
    res = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
    
    if res < 0: # 시계 방향
        return -1
    elif res > 0: # 반시계 방향
        return 1
    else: # 일직선 상
        return 0

def lineCross(p1, p2, p3, p4):
    c1 = ccw(p1, p2, p3)
    c2 = ccw(p1, p2, p4)
    c3 = ccw(p3, p4, p1)
    c4 = ccw(p3, p4, p2)
    if c1 * c2 < 0 and c3 * c4 < 0:
        return 1
    return 0
    
 
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(lineCross(A[:2], A[2:], B[:2], B[2:]))