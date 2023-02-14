white = [[0]*100 for _ in range(100)]

n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    for y in range(b, b+10):
        for x in range(a, a+10):
            white[y][x] = 1
cnt = 0
for y in range(100):
    for x in range(100):
        cnt += white[y][x]
print(cnt)
            
            