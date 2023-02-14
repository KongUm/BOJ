N = int(input())
arr = [[" "]*(N*2-1) for _ in range(N)]
mid = N-1

for i in range(N):
        for j in range(mid-i,mid+i+1):
                arr[i][j] = "*"

def piramid(N,mid,y):
        if N == 3:
                arr[y+1][mid] = " "
                return     
        else:
                for i in range(N//2): ##y좌표 설정 + 줄어드는 수 구현
                        for j in range(mid-N//2+1+i,mid+N//2-i):
                                arr[y+N//2+i][j] = " "
        piramid(N//2,mid,y)
        piramid(N//2,mid-N//2,y+N//2)
        piramid(N//2,mid+N//2,y+N//2)
        return

piramid(N,mid,0)

for i in range(N):
    ans = "".join(arr[i])
    print(ans)