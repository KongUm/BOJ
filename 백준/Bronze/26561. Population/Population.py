n = int(input())

for _ in range(n):
    a, t = map(int, input().split())
    p = t // 4
    q = t // 7

    print(a + p - q)