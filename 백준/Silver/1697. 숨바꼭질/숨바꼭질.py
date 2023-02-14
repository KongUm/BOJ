from collections import deque
N, K = map(int, input().split())
# N = 수빈이가 있는 위치, K = 동생이 있는 위치
arr = [0]*(10**5+10)
Q = deque()

def bfs(N):
    
    arr[N] = -1
    Q.append([N])
    count = 1
    while len(Q) != 0:
        u = Q.popleft()
        qq = []
        for p in u:
            a = []
            if p*2 < 10**5+1:
                a.append(p*2)
            if p+1 < 10**5+1:
                a.append(p+1)
            if p-1 >= 0:
                a.append(p-1)
            for i in a:
                if i == K:
                    return count
                #print(i)
                if arr[i] == 0:
                    arr[i] = count
                    qq.append(i)
        Q.append(qq)
        count += 1
if N == K:
    print(0)
else:
    print(bfs(N))
#print(arr)


    
