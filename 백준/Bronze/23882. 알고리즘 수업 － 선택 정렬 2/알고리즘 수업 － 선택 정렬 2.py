N,K = map(int,input().split())
A = list(map(int,input().split()))
count = 0
def selection_sort_min(A):
        for i in range(N-1): 
                min_index = i #정렬된 원소 다음 원소를 기준으로 설정 
                for j in range(i+1,N): #기준 원소 다음부터 탐색
                        if A[j] < A[min_index]: 
                                min_index = j
                A[i],A[min_index] = A[min_index],A[i] #가장 작은 원소와 기준 원소를 swap

def selection_sort_max(A):
        global count
        for i in range(N-1,0,-1):
                max_index = i
                for j in range(i-1,-1,-1):
                        if A[j] > A[max_index]:
                                max_index = j
                if A[i] < A[max_index]:
                        count = count + 1
                        A[i],A[max_index] = A[max_index],A[i]
                        if count == K:
                                for p in range(N):
                                        print(A[p],end = " ")
 
selection_sort_max(A)
if count < K:
        print(-1)