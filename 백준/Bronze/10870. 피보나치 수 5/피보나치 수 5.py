n = int(input())
a = 0
b = 1

def fibo(n,a,b):
    if n == 0:
        print(a)
        return
    b = a+b
    a = b - a
    n = n - 1
    
    fibo(n,a,b)

fibo(n,a,b)
