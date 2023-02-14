import itertools

N,M = map(int,input().split())
card = list(map(int,input().split()))

com_list = list(itertools.combinations(card,3))
min = M
for i in range(len(com_list)):
    if 0 <= M-sum(com_list[i]) < min:
        min = M-sum(com_list[i])

print(M-min)