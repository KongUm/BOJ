import sys
N = int(input())
A = list(map(int, input().split()))
tree = [0] * (4 * N)

def update(start, end, node, ul, ur, value):
    if ur < start or ul > end:
        return
    if ul <= start and ur >= end:
        tree[node] += value
        return
    
    mid = (start + end) // 2
    update(start, mid, node * 2, ul, ur, value)
    update(mid + 1, end, node * 2 + 1, ul, ur, value)
    
def find(start, end, node, target):
    if target < start or target > end:
        return 0
    if start == end:
        return tree[node]
        
    mid = (start + end) // 2
    sub_sum = find(start, mid, node * 2, target) + find(mid + 1, end, node * 2 + 1, target) + tree[node]
    return sub_sum

M = int(input())

for _ in range(M):
    q = list(map(int, sys.stdin.readline().split()))
    if q[0] == 1:
        update(1, N, 1, q[1], q[2], q[3])
    else:
        sub_sum = find(1, N, 1, q[1])
        print(sub_sum + A[q[1] - 1])        
    
     