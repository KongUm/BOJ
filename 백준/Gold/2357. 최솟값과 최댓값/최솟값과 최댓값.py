import sys

N, M = map(int, input().split())

num = [int(sys.stdin.readline()) for _ in range(N)]
segment_tree = [[0, 0] for _ in range(4 * N)]
# index 0 = 최솟값, index 1 = 최댓값

def init(left, right, node):
    if left == right:
        segment_tree[node] = [num[left - 1], num[left - 1]]
        return segment_tree[node]

    mid = (left + right) // 2
    A, B = init(left, mid, node * 2), init(mid + 1, right, node * 2 + 1)
    segment_tree[node] = [min(A[0], B[0]), max(A[1], B[1])]
    return segment_tree[node]


def find(start, end, node, fl, fr):
    if fr < start or fl > end:
        return [int(1e10), 0]

    if fl <= start and fr >= end:
        return segment_tree[node]

    mid = (start + end) // 2
    A, B = find(start, mid, node * 2, fl, fr), find(mid + 1, end, node * 2 + 1, fl, fr)
    return [min(A[0], B[0]), max(A[1], B[1])]

init(1, N, 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ans = find(1, N, 1, a, b)
    print(ans[0], ans[1])