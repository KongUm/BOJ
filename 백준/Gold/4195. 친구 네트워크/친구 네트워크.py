import sys
T = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        if parent[b] != a:
            count_arr[a] += count_arr[b]
            parent[b] = a 
    else:
        if parent[a] != b:
            count_arr[b] += count_arr[a] 
            parent[a] = b
        

        

for _ in range(T):
    N = int(input())
    d = {}
    used = set()
    friend = []
    parent = []
    count_arr = []
    cnt = 0
    for i in range(N):
        a, b = map(str, sys.stdin.readline().split())
        
        if a not in used:
            used.add(a)
            d[a] = cnt
            parent.append(cnt)
            count_arr.append(1)
            cnt += 1
        if b not in used:
            used.add(b)
            d[b] = cnt
            parent.append(cnt)
            count_arr.append(1)
            cnt += 1
        union(d[a],d[b])
        print(count_arr[find(d[b])])