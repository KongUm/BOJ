import sys
sys.setrecursionlimit(110000)
N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

idx = [0]*(N+1)
for i in range(N):
    idx[inorder[i]] = i

stack = []
def preorder(il, ir, pl, pr):
    root = postorder[pr]
    a = idx[root] - il
    
    stack.append(root)
    
    if il <= il+a-1 or pl <= pl+a-1:
        preorder(il, il+a-1, pl, pl+a-1)
          
    if idx[root]+1 <= ir or pl+a <= pr-1:
        preorder(idx[root]+1, ir, pl+a, pr-1)
    
preorder(0, N-1, 0, N-1)

for i in stack:
    print(i, end = " ")