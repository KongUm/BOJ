import bisect
N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0

for i in range(N):
    for j in range(i,N):
        if i != j:
            sum = A[i] + A[j]
            left = bisect.bisect_left(A, -sum)
            
            if 0 <= left < N and A[left] == -sum:
                right = bisect.bisect_right(A, -sum)-1               
                ans += right - left + 1
                
                if left <= i <= right:
                    ans -= 1
                if left <= j <= right:
                    ans -= 1
print(ans//3)              