n = int(input())

f = [0,1,1]
re_checker = 0
dp_checker = 0

def re_fib(n):
    global re_checker 
    if n == 1 or n == 2:
        re_checker = re_checker + 1
        return 1 #code 1
    else:
        return re_fib(n-1) + re_fib(n-2)

def dp_fib(n):
    global dp_checker
    if n>2:
        for i in range(3,n+1):
            dp_checker = dp_checker + 1
            f.append(f[i-1] + f[i-2]) #code 2
        return f[n]
    else:
        return 1

re_fib(n)
dp_fib(n)
print(re_checker, dp_checker)