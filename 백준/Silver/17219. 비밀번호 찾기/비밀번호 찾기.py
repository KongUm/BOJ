import sys
N, M = map(int, input().split())
dict = dict()
for i in range(N):
    s, k = sys.stdin.readline().split()
    dict[s] = k
    
for i in range(M):
    url = sys.stdin.readline().rstrip()
    print(dict.get(url)) 