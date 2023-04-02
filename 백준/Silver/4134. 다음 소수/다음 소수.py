from math import sqrt

def isPrime(x):
    if 0 <= x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

T = int(input())
for i in range(T):
    a = int(input())
    while True:
        if isPrime(a):
            print(a)
            break
        else:
            a += 1