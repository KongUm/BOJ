T = int(input())

for _ in range(T):
    S = input()
    if len(S) % 2 != 0:
        cnt = 0
        for i in S:
            if i == '?':
                cnt += 1
        print(2**cnt)
    else:
        A, B = S[: len(S)//2], S[len(S)//2:]
        cnt, checker, q = 0, True, 0
        for i in range(len(A)):
            if A[i] == '?':
                cnt += 1
            if B[i] == '?':
                cnt += 1
            if A[i] == '?' and B[i] == '?':
                q += 1
            elif A[i] != B[i] and A[i] != '?' and B[i] != '?':
                checker = False
        ans = 2 ** cnt

        if checker:
            ans -= 2**q
        print(ans%1000000007)

