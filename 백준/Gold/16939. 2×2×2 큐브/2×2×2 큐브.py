color = list(map(int, input().split()))

idx = [[[5,1],[7,3],[9,5],[11,7],[24,9],[22,11],[1,24],[3,22]],[[6,2],[8,4],[10,6],[12,8],[23,10],[21,12],[2,23],[4,21]],[[15,7],[16,8],[7,19],[8,20],[19,23],[20,24],[24,16],[23,15]],[[13,5],[14,6],[5,17],[6,18],[17,21],[18,22],[22,14],[21,13]],[[3,17],[4,19],[17,10],[19,9],[10,16],[9,14],[14,4],[16,3]],[[1,18],[2,20],[18,12],[20,11],[12,15],[11,13],[15,1],[13,2]]]


def all(arr):
    for i in range(0,24, 4):
        if arr[i] != arr[i+1] or arr[i+1] != arr[i+2] or arr[i+2] != arr[i+1] or arr[i+2] != arr[i+3]:
            return False
    print(1)
    exit()
    

for i in range(6):
    temp = color[:]
    for a,b in idx[i]:
        temp[a-1] = color[b-1]
    all(temp)

for i in range(6):
    temp = color[:]
    for a,b in idx[i]:
        temp[b-1] = color[a-1]
    all(temp)
print(0)
