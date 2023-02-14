import sys

T = int(input())

def init(left, right, node):
    if left == right:
        segment_tree[node] = [num[left]] * 2
        return segment_tree[node]

    mid = (left + right) // 2
    a, b = init(left, mid, node * 2), init(mid + 1, right, node * 2 + 1)
    segment_tree[node] = [min(a[0], b[0]), max(a[1], b[1])]

    return segment_tree[node]

def find(start, end, node, fl, fr):
    if fr < start or fl > end:
        return [int(1e10), 0]

    if start >= fl and end <= fr:
        return segment_tree[node]

    mid = (start + end) // 2
    a, b = find(start, mid, node * 2, fl, fr), find(mid + 1, end, node * 2 + 1, fl, fr)
    return [min(a[0], b[0]), max(a[1], b[1])]

def update(start, end, node, target, value):
    if start > target or end < target:
        return

    if start == end:
        segment_tree[node][0] = value
        segment_tree[node][1] = value
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, target, value)
    update(mid + 1, end, node * 2 + 1, target, value)

    segment_tree[node][0] = min(segment_tree[node * 2][0], segment_tree[node * 2 + 1][0])
    segment_tree[node][1] = max(segment_tree[node * 2][1], segment_tree[node * 2 + 1][1])


for _ in range(T):
    N, K = map(int, input().split()) # DVD 번호 : 0 ~ N - 1
    segment_tree = [[0, 0] for _ in range(4 * N)] # idx 0 = 합, idx 1 = 최소, idx 2 = 최대
    num = [i for i in range(N)] # 즉 세그 트리 ) 0 ~ N-1
    init(0, N-1, 1)

    for _ in range(K):
        q, a, b = map(int, sys.stdin.readline().split())

        if q == 0:
            temp = num[a]
            num[a] = num[b]
            num[b] = temp
            update(0, N-1, 1, a, num[a])
            update(0, N-1, 1, b, num[b])

        else:
            info = find(0, N-1, 1, a, b)
            if info[0] == a and info[1] == b:
                print("YES")
            else:
                print("NO")