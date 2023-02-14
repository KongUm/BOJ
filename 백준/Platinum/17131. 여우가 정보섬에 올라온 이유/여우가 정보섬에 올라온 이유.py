def update(index, value): # index = 갱신할 인덱스, value 더할 값
    while index < len(tree):
        tree[index] += value
        index += (index & -index)

def find(index): 
    res = 0
    while index > 0:
        res += tree[index]
        index -= (index & -index)
        
    return res

import sys
N = int(input())
S = [[] for _ in range(400001)]
ans, div = 0, 1000000007
tree = [0]*400002

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x += 200001; y += 200000
    S[y].append(x)

for y in range(400000-1, -1, -1):
    for i in S[y + 1]:
        update(i, 1)
        
    for x in S[y]:
        left = find(x - 1)
        right = find(400001) - find(x)
        ans = (ans%div + (left*right)%div)%div
print(ans%div)