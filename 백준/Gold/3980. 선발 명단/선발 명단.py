T = int(input())

def BT(n):
    global ans
    if n == 11:
        ans = max(ans, sum(stack))
        return

    for i in range(11):
        if i not in used and info[i][n] > 0:
            stack.append(info[i][n])
            used.add(i)
            BT(n + 1)
            stack.pop()
            used.remove(i)
    return

for _ in range(T):
    info = [list(map(int, input().split())) for _ in range(11)]
    stack = []
    used = set()
    ans = 0
    BT(0)
    print(ans)