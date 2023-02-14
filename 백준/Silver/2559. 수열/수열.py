N, K = map(int,input().split())
# N = 온도를 측정한 전체 날짜의 수
# K = 온도를 구하기 위한 연속적인 날짜의 수

A = list(map(int,input().split()))
sum_A = [0]
for i in range(N):
    sum_A.append(sum_A[-1]+A[i])
#print(sum_A)
maxi = -100000000

if N == K:
    maxi = sum_A[-1]
    
else:
    for i in range(K,N+1):
        a = sum_A[i] - sum_A[i-K]
        if a > maxi:
            maxi = a
print(maxi)
    
