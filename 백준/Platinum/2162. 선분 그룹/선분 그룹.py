import sys

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


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

N = int(input())
seg = []
parent = [i for i in range(N)]
maxi = [0] * N
cnt = 0

for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    tmp = [(a, b), (c, d)]
    tmp.sort()
    seg.append(tmp)
    
for i in range(N):
    for j in range(N):
        if i != j and lineCross(seg[i][0], seg[i][1], seg[j][0], seg[j][1]) == 1:
            union(i, j)

for i in range(N):
    find(i)
for i in range(N):
    if maxi[parent[i]] == 0:
        cnt += 1
    maxi[parent[i]] += 1

print(cnt)
print(max(maxi))
            
            