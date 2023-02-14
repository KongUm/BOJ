N = int(input())
A = list(map(int, input().split()))
num = [0]*N
arr = []
for i in range(N):
    arr.append((A[i], i + 1))
arr.sort()

segment_tree = [0]*(4*N)

def init(left, right, node):
    if left == right:
        segment_tree[node] = num[left - 1]
        return segment_tree[node]

    mid = (left + right) // 2
    segment_tree[node] = init(left, mid, node * 2) + init(mid + 1, right, node * 2 + 1)
    return segment_tree[node]

def find(start, end, node, fl, fr):
    if fr < start or fl > end:
        return 0

    if fl <= start and fr >= end:
        return segment_tree[node]

    mid = (start + end) // 2
    sub_sum = find(start, mid, node * 2, fl, fr) + find(mid + 1, end, node * 2 + 1, fl, fr)
    return sub_sum

def update(start, end, node, target, value):
    if target < start or target > end:
        return

    segment_tree[node] += value

    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, target, value)
    update(mid + 1, end, node * 2 + 1, target, value)

init(1, N, 1)
ans = 0

for i in range(N):
    v, idx = arr[i]
    f = find(1, N, 1, idx + 1, N)
    update(1, N, 1, idx, 1)
    ans += f

print(ans)