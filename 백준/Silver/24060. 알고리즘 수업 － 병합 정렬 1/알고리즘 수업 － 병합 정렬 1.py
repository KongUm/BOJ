def merge_sort(L):
    if len(L) == 1:
        return L

    mid = (len(L) + 1) // 2

    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])

    a, b = 0, 0
    L2 = []
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            L2.append(left[a])
            ans.append(left[a])
            a += 1
        else:
            L2.append(right[b])
            ans.append(right[b])
            b += 1
    while a < len(left):
        L2.append(left[a])
        ans.append(left[a])
        a += 1
    while b < len(right):
        L2.append(right[b])
        ans.append(right[b])
        b += 1
    return L2

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = []
merge_sort(a)

if len(ans) >= k:
    print(ans[k - 1])
else:
    print(-1)