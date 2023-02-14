N = int(input())
arr = list(map(int, input().split()))
arr.sort()

stack = []
checker = False
target = -1
for i in range(len(arr)):
    if checker == False or target == arr[i]:
        if len(stack) == 0 or stack[-1]+1 != arr[i]:
            stack.append(arr[i])
        else:
            stack.append(arr[i])
            checker = True
            target = arr[i]
    else:
        checker = False
        t = []
        while len(stack) > 0  and stack[-1] == target:
            t.append(stack.pop())
        stack.append(arr[i])
        for i in t:
            stack.append(i)

t = []
a = -1
b = []
if checker == True:
    for i in range(N):
        if stack[-1] != target:
            a = stack[-1]
            break
        t.append(stack.pop())
   
    for i in range(len(stack)):
        if len(stack) == 0 or stack[-1] != a:
            break
        b.append(stack.pop())
   
    for i in t:
        stack.append(i)
    for i in b:
        stack.append(i)

for i in stack:
    print(i, end = " ")