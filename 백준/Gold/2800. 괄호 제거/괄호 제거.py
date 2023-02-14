S = input()
type = [0]*len(S)
cnt = 0
st = []
for i in range(len(S)):
    if S[i] == '(':
        cnt += 1
        st.append([cnt, i])
    elif S[i] == ')':
        p = st.pop()
        type[p[1]] = p[0]
        type[i] = p[0]
    
stack = []
comb = []
def BT():
    if len(stack) == cnt:
        return
    s = 1
    if len(stack) > 0:
        s = stack[-1] + 1
  
    for i in range(s, cnt+1):
        stack.append(i)
        BT()
        stack.pop()
    comb.append(stack[:])
    
BT()
ans = []
for c in comb:
    temp = ""
    for i in range(len(S)):
        if type[i] != 0 and type[i] not in c:
            continue
        else:
            temp += S[i]
    if temp not in ans:
        ans.append(temp)

ans.sort()
for i in ans:
    print(i)
    