N = int(input())

isprime = [False]*2 + [True]*(N-1)
prime = []

for i in range(2,N+1):
    if isprime[i]:
        prime.append(i)
        for j in range(i*2, N+1, i):
            isprime[j] = False

sum = 0
count = 0
right = 0

for left in range(len(prime)):
    while right < len(prime) and sum < N:
        sum += prime[right]
        right += 1
    if sum == N:
        count += 1
    sum -= prime[left]
print(count)