N = int(input())
building = list(map(int,input().split()))
slope_list = []

for i in range(N):
    s_list = []
    for j in range(N):
        if i == j:
            s_list.append(-10000000000000)
        elif j > i:
            x = i-j
            y = building[i] - building[j]
            s_list.append(y/x)
        else:
            x = j-i
            y = building[i] - building[j]
            s_list.append(y/x)
    slope_list.append(s_list)

for i in range(N): # i번째 건물 선택
    if i-1 != N: #가장 오른쪽 건물 예외 처리
        right_sm = -10000000000000
        for j in range(i+1,N):
            if slope_list[i][j] > right_sm:
                right_sm = slope_list[i][j]
            else:
                slope_list[i][j] = -10000000000000

    if i-1 != N: #가장 왼쪽 건물 예외 처리
        left_sm = -10000000000000
        for j in reversed(range(i)):
            if slope_list[i][j] > left_sm:
                left_sm = slope_list[i][j]
            else:
                slope_list[i][j] = -10000000000000

seeable = [0]*N

for i in range(N):
    for j in range(N):
        if slope_list[i][j] != -10000000000000:
            seeable[i] = seeable[i] + 1

print(max(seeable))