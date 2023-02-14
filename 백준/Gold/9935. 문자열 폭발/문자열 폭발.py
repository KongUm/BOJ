S = input()
explosion = input()
le = len(explosion)

stack = []

def Check():
    for i in range(le):
        if stack[len(stack)-le+i] != explosion[i]:
            return 
    Explode()
    return 
 
def Explode():
    for _ in range(le):
        stack.pop()
    if len(stack) >= le:
        Check()
    else:
        return
    

for i in range(len(S)):
    stack.append(S[i])
    if len(stack) >= le:
        Check()
        
if len(stack) == 0:
    print("FRULA")
else:
    for i in stack:
        print(i, end = "")