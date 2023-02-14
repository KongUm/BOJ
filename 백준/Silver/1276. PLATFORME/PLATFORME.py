N = int(input()) # N = 플랫폼 수

plat = []
alt = [0]*10001
pillar = 0
for i in range(N):
    plat.append(list(map(int, input().split())))
plat.sort()

for i in range(N):
    al, lo, hi = plat[i][0], plat[i][1], plat[i][2]-1
    pillar += al - alt[lo] # 왼쪽 기둥의 길이
    pillar += al - alt[hi] # 오른쪽 기둥의 길이
    for j in range(lo,hi+1):
        alt[j] = al   
        
print(pillar)