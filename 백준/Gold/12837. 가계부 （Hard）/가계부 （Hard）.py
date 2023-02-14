import sys

N, Q = map(int, input().split())

tree = [0] * ((N + 1) * 4)

def update(start, end, node, value, target):
    if target < start or target > end:
        return
    tree[node] += value
    if start == end:
        return 
    mid = (start + end) // 2
    update(start, mid, node * 2, value, target)
    update(mid + 1, end, node * 2 + 1, value, target)

def find(start, end, node, fl, fr):
    if fr < start or fl > end:
        return 0
    if fl <= start and fr >= end:
        return tree[node]
    mid = (start + end) // 2
    return find(start, mid, node * 2, fl, fr) + find(mid + 1, end, node * 2 + 1, fl, fr)

for _ in range(Q):
    q = list(map(int, sys.stdin.readline().split()))
    if q[0] == 1:
        update(0, N, 1, q[2], q[1])
    else:
        print(find(0, N, 1, q[1], q[2]))