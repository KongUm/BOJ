T = int(input())
cnt = 0

def isSame(now, end):
    nw, ed = str(bin(now)), str(bin(end))
    if len(nw) > len(ed):
        return False
    
    for i in range(len(nw)):
        if nw[i] != ed[i]:
            return False
    return True

def save(now):
    global cnt
    for i in range(20):
        if now + i not in D:
            D[now + i] = cnt + i + 1
        D[now + i] = min(cnt + i + 1, D[now + i])
    cnt = D[now]
        

for _ in range(T):
    cnt = -1
    now, end = map(int, input().split())
    D = {}
    save(now)

    while isSame(now, end) == False:
        if (now % 2 == 1):
            now += 1
            save(now)
            if isSame(now, end):
                break
        now //= 2
        save(now)
        
    while (now != end):
        nw, ed = str(bin(now)), str(bin(end))
        now *= 2
        save(now)
        nw, ed = str(bin(now)), str(bin(end))
        
        if nw[-1] != ed[len(nw) - 1]:
            now += 1
            save(now)
    print(cnt)