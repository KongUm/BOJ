import sys
N, M = map(int, input().split())

num = [0] * (N + 1)
seg_tree = [0]*(N * 4)

def modify(start, end, node, target, diff):
    if target < start or target > end:
        return
        
    seg_tree[node] += diff
    
    if start == end:
        return
    
    mid = (start + end) // 2
    modify(start, mid, node * 2, target, diff)
    modify(mid + 1, end, node * 2 + 1, target, diff)
    
def find(start, end, node, fl, fr):
    if fr < start or fl > end:
        return 0
    
    if fl <= start and fr >= end:
        return seg_tree[node]
    
    mid = (start + end) // 2
    sub_sum = find(start, mid, node * 2, fl, fr) + find(mid + 1, end, node * 2 + 1, fl, fr)
    return sub_sum

for _ in range(M):
    q, a, b = map(int, sys.stdin.readline().split())
    if q == 0:
        c = min(a, b)
        d = max(a, b)
        print(find(1, N, 1, c, d))
    else:
        diff = b - num[a]
        modify(1, N, 1, a, diff)
        num[a] = b
    
     
        
