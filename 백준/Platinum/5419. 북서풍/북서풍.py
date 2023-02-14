def update(index, value): # index = 갱신할 인덱스, value 더할 값
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
    N = int(input())
    land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    land.sort(key = lambda x : (-x[0], x[1]))
    
    sy = set()
    
    for x, y in land:
        sy.add(y)
        
    sy = sorted(list(sy))
    Dy = {sy[i] : (i + 1) for i in range(len(sy))} # 1 ~ 
    
    for i in range(N):
        land[i][1] = Dy[land[i][1]]
    
    l = len(Dy)
    tree = [0] * (l + 1)
    ans = 0
    
    for x, y in land:
        ans += find(y)
        update(y, 1)
    print(ans)