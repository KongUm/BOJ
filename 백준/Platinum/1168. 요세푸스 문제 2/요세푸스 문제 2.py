N, K = map(int, input().split())

tree = [0] * (4 * N)
arr = []

def init(start, end, node):
    if start == end:
        tree[node] = 1
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

def find(start, end, node, remain, sub_sum):
    tree[node] -= 1

    if start == end:
        return [end, sub_sum]

    mid = (start + end) // 2
    if tree[node * 2] >= remain:
        return find(start, mid, node * 2, remain, sub_sum)
    else:
        return find(mid + 1, end, node * 2 + 1, remain - tree[node * 2], sub_sum + tree[node * 2])


init(1, N, 1)
ans, sl = find(1, N, 1, K, 0)
sr = (N-1) - sl
arr.append(ans)


for r in range(N-1, 0, -1):
    if r < K:
        sub_K = K % r
    else:
        sub_K = K
    if sub_K == 0:
        sub_K = r

    if sr >= sub_K:
        ans, sl = find(1, N, 1, sl + sub_K, 0)
    else:
        ans, sl = find(1, N, 1, sub_K - sr, 0)
    sr = (r-1) - sl
    arr.append(ans)


print("<", end="")
for i in range(N-1):
    print(str(arr[i]), end=", ")
print(str(arr[-1]) + ">", end="")






