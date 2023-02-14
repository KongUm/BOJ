import sys
N = int(input())
X = list(map(int,input().split()))

SX = [0]*N
for i in range(N):
        SX[i] = X[i]
SX.sort()
CX = [SX[0]]

cur = SX[0]

def binary_search(arr, target, start, end):
        if start > end:
                return
        mid = (start + end)//2 #start ~ end (범위) 의 중간을 중간점 mid로 설정
        
        if arr[mid] == target: #원하는 값 찾은 경우 인덱스 반환
                return mid
        elif arr[mid] > target:
                return binary_search(arr, target, start, mid-1)
                #중간점 mid보다 target이 작은경우 mid의 왼쪽부분 확인
        else:
                return binary_search(arr, target, mid+1, end)
                #중간점 mid보다 target이 작은경우 mid의 왼쪽부분 확인
for i in range(N):
        if SX[i] != cur:
                CX.append(SX[i])
                cur = SX[i]
                
for i in range(N):
        sys.stdout.write(str(binary_search(CX,X[i],0,len(CX)-1))+" ")