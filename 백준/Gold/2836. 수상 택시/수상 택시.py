import sys
N, M = map(int, input().split())

def Sweeping():
    line.sort()
    now, total = line[0][0], 0
    for a, b in line:
        if a <= now:
            diff = b - now
            if diff > 0:
                now = b; total += diff
        else:
            now = b; total += b - a
    return total
            
line = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        line.append((b, a))

ans = M        
if len(line) > 0:
    ans += Sweeping()*2
print(ans)