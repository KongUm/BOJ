m = int(input())
A = [tuple(map(int, input().split())) for _ in range(m)]
res = 0
div = int(1e9) + 7

for n, s in A:
    res += (s % div) * pow(n, div - 2, div)
    res %= div
print(res)