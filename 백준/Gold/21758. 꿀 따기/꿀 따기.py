N = int(input())
A = list(map(int, input().split()))

prefix = [A[0]]
ans = 0

for i in range(1, N):
    prefix.append(prefix[-1] + A[i])

for i in range(1, N-1):
    temp = prefix[N-1] - prefix[0] - A[i]
    temp += prefix[N-1] - prefix[i]
    temp2 = prefix[i-1] + prefix[N-2] - A[i]
    temp3 = prefix[i] - A[0] + prefix[N-1] - prefix[i-1] - A[N-1]
    ans = max(ans, temp, temp2, temp3)
print(ans)
