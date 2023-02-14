import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()

mini = int(1e10)
ans = []
for i in range(N):
    target = A[i]
    l = bisect.bisect_left(A, -target)
    
    for j in range(-1, 2):
        if 0 <= l+j < N and i != l+j:
            a = abs(A[l+j] + target)
            if a < mini:
                ans = [A[l+j], target]
                mini = a
ans.sort()
print(ans[0], ans[1])
    
