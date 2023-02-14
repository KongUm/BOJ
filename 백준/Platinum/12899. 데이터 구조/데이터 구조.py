import sys

seg_tree = [0] * 8000000
a = 2000000
ans = 0


def update(start, end, node, target, diff):
    if target < start or target > end:
        return

    seg_tree[node] += diff

    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, target, diff)
    update(mid + 1, end, node * 2 + 1, target, diff)


def find(start, end, node, target, checker):
    mid = (start + end) // 2
    
    seg_tree[node] -= 1
    
    if start == end:
        return start
    
    if seg_tree[node * 2] >= target:
        return find(start, mid, node * 2, target, checker)
    else:
        return find(mid + 1, end, node * 2 + 1, target - seg_tree[node * 2], checker)

N = int(input())
for _ in range(N):
    q, x = map(int, sys.stdin.readline().split())
    if q == 1:
        update(1, a, 1, x, 1)
    else:
        e = find(1, a, 1, x, False)
        print(e)
