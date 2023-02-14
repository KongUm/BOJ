while True:
    S = input() 
    if len(S) > 0:
        if S[0] == '#':
            exit()
        
    stack = []
    checker = False
    tag_ending = False
    type = 0 
    tag = ""
    for i in range(len(S)):
        if S[i] == '<':
            checker = True
            tag_ending = False
            tag = ""
                
        elif S[i] == '>':
            checker = False
            if S[i-1] == '/' and S[i-2] == " ":
                continue 
            elif tag[0] == '/':
                stack.append([tag[1:], 1])
            else:
                stack.append([tag, 0])    
             
        elif checker == True:
            if S[i] == " ":
                tag_ending = True             
            elif tag_ending == False:
                tag = tag + S[i]
    ans = True
    
    A = []
    for i in stack:
      
        tag, stat = i[0], i[1]
        if len(A) > 0:
            if A[-1][0] == tag and A[-1][1] == 0 and stat == 1:
                A.pop()
                continue
        A.append(i[:])
    if len(A) == 0:
        print("legal")
    else:
        print("illegal")