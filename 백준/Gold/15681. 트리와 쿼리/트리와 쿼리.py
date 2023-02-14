import sys
sys.setrecursionlimit(10**6)

V, R, Q = map(int, input().split())
tree = [[] for _ in range(V+1)]
child = [[] for _ in range(V+1)]
parent = [-1]*(V+1)
size = [0]*(V+1)

def makeTree(cur, par): # cur = 현재 노드, par = 현재 노트의 부모 노드
    for node in tree[cur]:
        # 현재 노드와 연결된 모든 노드를 돌림 (부모노드, 자식노드 둘다)
        if node != par: # 부모노드가 아니라면 (현재노드의 자식노드라면)
            child[cur].append(node) # 현재 노드의 child table에 자식 노드를 추가
            parent[node] = cur # cur의 자식노드의 parent table의 값을 cur로 변경
            makeTree(node, cur) # 자식노드 탐색
            
def countPoint(cur):
    size[cur] = 1
    for node in child[cur]:
        countPoint(node)
        size[cur] += size[node]
    
for _ in range(V-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    
makeTree(R, -1) # 루트를 R로 설정 후 트리의 각 노드의 child, parent table을 채움
countPoint(R)
# 루트가 R일때 각 노드를 루트로 하는 서브트리에 속한 정점의 수를 size table에 저장

for i in range(Q):
    print(size[int(sys.stdin.readline())])
       
            