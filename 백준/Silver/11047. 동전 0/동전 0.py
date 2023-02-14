N, K = map(int, input().split())

coin = []
for i in range(N):
    coin.append(int(input()))
coin.sort(reverse = True)

count = 0
for i in coin:
    count += K//i
    K -= i*(K//i)
print(count)