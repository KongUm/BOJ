import sys
sys.setrecursionlimit(100000)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

def postorder(l, r):
    root = preorder[l]
    
    idx = r+1
    for i in range(l+1,r+1):
        if preorder[i] > root:
            idx = i
            break
    if l+1 <= idx-1:
        postorder(l+1,idx-1)
    if idx <= r:
        postorder(idx, r)
    print(root)
postorder(0,len(preorder)-1)