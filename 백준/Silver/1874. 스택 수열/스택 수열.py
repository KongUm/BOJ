import sys
n = int(input())
stack = []
ans = []
checker = True
last_push = 0

for _ in range(n):
        target = int(sys.stdin.readline().rstrip())
        if last_push < target:
                for i in range(last_push+1,target+1):
                        stack.append(i)
                        last_push = i
                        ans.append("+")
        elif stack[-1] > target:
                checker = False
                print("NO")
                break
        stack.pop()
        ans.append("-")
        
if checker == True:
        for an in ans:
                print(an)