import math
n, k = map(int, input().split())

fac = [1] * 4000001
div = 10 ** 9 + 7

for i in range(2, n + 1):
    fac[i] = ((fac[i - 1] % div) * (i % div)) % div

a = fac[n]
b = (fac[k] * fac[n - k]) % div

ans = (a % div) * pow(b, div - 2, div) 
print(ans % div)