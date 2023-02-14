H, W = map(int, input().split())
block = list(map(int, input().split()))

ans = 0
for h in range(H):
    checker = False
    count = 0
    stack = []
    for w in range(W):
        if block[w] > h:
            checker = True
            if len(stack) > 0 and stack[-1] != -1:
                count += stack.pop()
            stack.append(-1)
        else:
            if checker == True:
                if len(stack) > 0 and stack[-1] != -1:
                    stack.append(stack.pop()+1)
                else:
                    stack.append(1)
    
    ans += count
print(ans)                