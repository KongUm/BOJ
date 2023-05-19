s = int(input())

maxi = 0
for i in range(1, int(1e7)):
    tmp = i * (i + 1) // 2
    if tmp <= s:
        maxi = max(i, maxi)
print(maxi)
        