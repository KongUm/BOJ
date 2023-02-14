import sys
T = int(input())

for i in range(T):
        S = input()
        stack = []
        checker = True
        for j in range(len(S)):
                if S[j] == "(":
                        stack.append("(")
                else:
                        try:
                                stack.pop()
                        except:
                                checker = False
                                break
        if len(stack) != 0 or checker == False:
                print("NO")
        else:
                print("YES")