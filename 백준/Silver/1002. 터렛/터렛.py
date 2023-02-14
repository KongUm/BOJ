T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (y2 - y1)**2 + (x2 - x1)**2
    r = (r1 + r2) **2
    R = (r2 - r1) ** 2
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    
    elif r == d or R == d:
        print(1)
    elif R < d < r:
        print(2)
    else:
        print(0)