N,K = map(int,input().split())

def fac(n):
        if n > 1:
                return n*fac(n-1)
        else:
                return 1

print(fac(N)//(fac(K)*fac(N-K)))