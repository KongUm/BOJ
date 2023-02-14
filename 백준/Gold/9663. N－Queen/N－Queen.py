N = int(input())
stack = []
ans = 0

def dfs(a): # a = 현재 Queen을 놓을 가로 인덱스
    global ans
    if a == N:
        ans += 1
        return
    else:
        for i in range(N): # i = Queen을 놓을 세로 인덱스
            if i in stack:
                continue
            checker = True
            up = 1
            down = 1
            while 0 <= a-up <= N-1 and 0 <= i+up <= N-1: # 좌측 위로 탐색
                if stack[a-up] == i + up: # 이미 Queen이 있다면
                    checker = False
                    break
                up += 1
            if checker == False:
                continue
            while 0 <= a-down <= N-1 and 0 <= i-down <= N-1: # 좌측 아래로 탐색
                if stack[a-down] == i - down: # 이미 Queen이 있다면
                    checker = False
                    break
                down += 1
            if checker == False:
                continue
            stack.append(i)
            dfs(a+1)
            stack.pop()
dfs(0)
print(ans) 