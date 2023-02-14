N,M = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
C = A-B
D = B-A
print(len(C.union(D)))
