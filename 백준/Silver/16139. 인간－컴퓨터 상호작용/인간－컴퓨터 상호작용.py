S = input()
leng = len(S)
sum_S = [[0]*leng for _ in range(26)]

for i in range(leng):
    alp = ord(S[i])-97
    # alp --> a = 0 ... z = 25
    if i == 0:
        sum_S[alp][0] = 1
    else:
        for j in range(0,26):
            if alp == j:
                sum_S[alp][i] = sum_S[alp][i-1] + 1
            else:
                sum_S[j][i] = sum_S[j][i-1]
q = int(input())

for _ in range(q):
    a,start,end = input().split()
    start = int(start)
    end = int(end)
    
    alp = ord(a)-97
    if start != 0:
        print(sum_S[alp][end]-sum_S[alp][start-1])
    else:
        print(sum_S[alp][end])