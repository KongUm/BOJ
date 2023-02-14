import sys
T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())
    if (n % 2 == 0):
        print("No")
        continue

    N = n * 2
    A = []
    
    for i in range(N - (n // 2) + 1, N + (n // 2 - 1) + 3):
        A.append(i)
    A.remove(N + 1)
    ans = []
 
    for i in range(1, n // 2 + 1):
        ans.append((i * 2, A[i - 1] - i * 2))
        ans.append((i * 2  + 1, A[i + (n // 2) - 1] - (i * 2 + 1)))
    ans.append((1, N))
    print("Yes")
    for a, b in ans:
        print(a, b)