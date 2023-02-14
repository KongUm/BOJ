N = int(input())

tree = {}
for _ in range(N):
    m, l, r, = map(str, input().split())
    tree[m] = [l, r]

def preorder(root): # 전위 순회
    if root != '.': # 만약 노드가 존재한다면
        print(root, end = "") # 자기자신 출력
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right

def inorder(root): # 중위 순회
    if root != '.': # 만약 노드가 존재한다면
        inorder(tree[root][0]) # left
        print(root, end = "") # 자기자신
        inorder(tree[root][1]) # right
        
def postorder(root): # 후위 순회
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = "")

preorder('A')
print()
inorder('A')
print()
postorder('A')
        
        
    
