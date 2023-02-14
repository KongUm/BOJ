import sys
N = int(input())
Flower = []
day = [0,0,31,59,90,120,151,181,212,243,273,304,334]
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    start = day[a[0]] + a[1]
    end = day[a[2]] + a[3]
    Flower.append([start, end])
Flower.sort()

empty_last = 60 # 비어있는 부분의 처음
current_max = -1
count = 0
checker = False
for i in range(N):
    if Flower[i][0] <= empty_last:
        current_max = max(Flower[i][1], current_max)
        
    else:
        count += 1
        if current_max > 334: # 334 = 11월 30일
            checker = True
            break
            
        empty_last = current_max
        
        current_max = -1
        if Flower[i][0] <= empty_last:
            current_max = max(Flower[i][1], current_max)

if checker == True:
    print(count)
elif current_max <= 334:
    print(0)
else:
    print(count + 1)

