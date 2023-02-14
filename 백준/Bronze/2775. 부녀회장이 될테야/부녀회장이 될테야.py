T = int(input())
memo = list([0]*15 for _ in range(15))

def res(F,a):
    global memo
    if memo[F][a] != 0:
        return memo[F][a]
    if F == 0:
        return a
    elif F == 1:
        return ((a+1)/2)*a
    else:
        sum = 0
        for i in range(1, a+1):
            sum = sum + res(F-1,i)
        return sum


for i in range(T):
    k = int(input())
    n = int(input())
    print(int(res(k,n)))
