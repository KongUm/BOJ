import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
stack = []
ans = [0]*N

for i in range(1,N+1):
    x = arr.pop()
    while len(stack) > 0:
        if x >= stack[-1][0]:
            a = stack.pop()
            ans[a[1]] = N-i+1
        else:
            break
    stack.append([x,N-i])
for i in ans:
    print(i, end = " ")
            