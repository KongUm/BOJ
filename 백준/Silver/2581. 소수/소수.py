M = int(input())
N = int(input())

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

checker = prime(N)
sum = 0
first_check = True
for i in range(1,M):
    checker[i] = False
for i in range(M-1,N+1):
    if checker[i] == True:
        sum = sum + i
        if first_check == True:
            first_prime = i
            first_check = False

if sum == 0:
    print(-1)
else:
    print(sum)
if first_check == False:
    print(first_prime)