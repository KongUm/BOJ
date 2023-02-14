while True:
        S = input()
        if S == ".":
                break
        stack = []
        checker = True
        for i in range(len(S)-1):
                if S[i] == "(" or S[i] == "[":
                        stack.append(S[i])
                elif S[i] == ")":
                        try:
                                if stack.pop() != "(":
                                        checker = False
                                        break
                        except:
                                checker = False
                                break
                elif S[i] == "]":
                        try:
                                if stack.pop() != "[":
                                        checker = False
                                        break
                        except:
                                checker = False
                                break             
        if checker == False or len(stack) != 0:
                print("no")
        else:
                print("yes")