p = int(input())
c = int(input())

res = p * 50 - c * 10
if p > c:
    res += 500
print(res)