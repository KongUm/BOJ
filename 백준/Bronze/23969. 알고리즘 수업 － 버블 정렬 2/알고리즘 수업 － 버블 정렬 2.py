N,K = map(int,input().split())
A = list(map(int,input().split()))
count = 0

def bubble_sort(A): #버블 소트
        global count
        for i in range(len(A)): #리스트 원소 선택 (0번부터 ~)
                for j in range(len(A)-i-1): #이미 정렬된 원소 예외 처리
                        if A[j] > A[j+1]:
                                temp = A[j]
                                A[j] = A[j+1]
                                A[j+1] = temp
                                count = count + 1
                                if count == K:
                                        for i in range(len(A)):
                                                print(A[i],end = ' ')
                                        break
bubble_sort(A)
if count < K:
        print(-1)