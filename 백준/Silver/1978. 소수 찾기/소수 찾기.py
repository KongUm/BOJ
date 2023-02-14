N = int(input())
A = list(map(int,input().split()))

def prime(n):
    checker_list = [True]*(n+1)
    checker_list[0] = False
    checker_list[1] = False
    m = n//2

    for i in range(2,m+1):
        if checker_list[i] == True:
            for j in range(i*2,n+1,i):
                checker_list[j] = False
    return checker_list
ans = 0
B = prime(max(A))
for i in A:
    if B[i] == True:
        ans = ans + 1
print(ans)






