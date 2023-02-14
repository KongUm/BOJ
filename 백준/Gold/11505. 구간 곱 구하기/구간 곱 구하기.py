import sys

div = 1000000007
N, M, K = map(int, input().split())
# N = 수의 개수, M = 수의 변경이 일어 나는 횟수, K = 구간의 곱을 구하는 횟수

num = [int(sys.stdin.readline()) for _ in range(N)]
segment_tree = [0]* (N * 4)

def init(left, right, node):
    if left == right:
        segment_tree[node] = num[left - 1]
        return segment_tree[node]

    mid = (left + right) // 2
    segment_tree[node] = init(left, mid, node * 2) * init(mid + 1, right, node * 2 + 1) % div
    return segment_tree[node]

def find(start, end, node, fl, fr):
    if fr < start or fl > end:
        return 1

    if fl <= start and fr >= end:
        return segment_tree[node]

    mid = (start + end) // 2
    sub_multi = find(start, mid, node * 2, fl, fr) * find(mid + 1, end, node * 2 + 1, fl, fr) % div
    return sub_multi

def update(start, end, node, target, value):
    if start > target or end < target:
        return

    if start == end:
        segment_tree[node] = value
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, target, value)
    update(mid + 1, end, node * 2 + 1, target, value)

    segment_tree[node] = segment_tree[node * 2] * segment_tree[node * 2 + 1] % div
    
init(1, N, 1)

for i in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, N, 1, b, c)
        num[b - 1] = c
    elif a == 2:
        print(find(1, N, 1, b, c))