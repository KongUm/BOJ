S = input()
stack = []
std = ""
count = 0
for i in range(len(S)):
        if i > 0:
                std = S[i-1]
        if S[i] == ")" and std == "(":
                stack.pop()
                stack.append(1)
                #print(stack,i)
        elif S[i] == "(":
                stack.append("(")
                #print(stack,i)
        else:
                lazer_counter = 0
                #print(stack,i,"loop start")
                        
                while True:
                        if stack[-1] == "(":
                                stack.pop()
                                #print(stack,i)
                                break
                        else:
                                lazer_counter = lazer_counter + stack.pop()
                                
                count = count + lazer_counter + 1
                
                stack.append(lazer_counter)                               
print(count)
                
        