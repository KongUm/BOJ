import sys
N = int(input())
stack = []

for i in range(N):
        C = sys.stdin.readline().split()
        if "top" == C[0]:
                if len(stack) == 0:
                        print(-1)
                else:
                        print(stack[-1])
                
        elif "pop" == C[0]:
                if len(stack) == 0:
                        print(-1)
                else:
                        print(stack.pop())
        elif "size" == C[0]:
                print(len(stack))
        elif "empty" == C[0]:
                if len(stack) == 0:
                        print(1)
                else:
                        print(0)
        elif "push" == C[0]:
                X = int(C[1])
                stack.append(X)