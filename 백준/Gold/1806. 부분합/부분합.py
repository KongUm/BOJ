N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
mini_len = 1000000
right = 0

for left in range(N):
    while right < N and sum < M:
        sum += A[right]
        right += 1
    if sum >= M:
        mini_len = min(mini_len, right - left)
    sum -= A[left]
    
if mini_len == 1000000:
    print(0)
else:
    print(mini_len)