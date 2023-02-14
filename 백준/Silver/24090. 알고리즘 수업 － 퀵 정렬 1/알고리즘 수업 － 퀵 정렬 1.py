import sys
sys.setrecursionlimit(100000)
N,K = map(int,input().split())
A = list(map(int,input().split()))
count = 0
ans = ""
def quick_sort(arr):
        def sort(low, high): #시작 인덱스(low)와 끝 인덱스(high)를 인자로 받음
                if high <= low: 
                        return
                
                mid = partition(low,high) #분활기준점 mid
                
                sort(low, mid -1)  #분활기준점을 기준으로 나눠서 정렬
                sort(mid+1, high)
        
        def partition(low, high):
                global count
                pivot = arr[high] #분활 범위의 중간 값을 pivot으로 설정
                i = low - 1
                for j in range(low,high):
                        if A[j] <= pivot:
                                i = i + 1
                                A[i],A[j] = A[j],A[i]
                                count = count + 1
                                if count == K:
                                        print(A[i],A[j])
                                
                if i+1 != high:
                        A[i+1],A[high] = A[high],A[i+1]
                        count = count + 1
                        if count == K:
                                print(A[i+1],A[high])
                        
                return i+1
        return sort(0,len(arr)-1) #맨 처음 quick_sort가 실행 되었을때 리스트 전체를 분활 범위로 가지는 sort로 반환 됨
quick_sort(A)

if count < K:
        print(-1)
