N,M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

stack = []

def dfs(): 
    if len(stack) == M: # 만약 모든 조건을 만족한다면 출력하고 함수를 끝낸다
            print(" ".join(map(str, stack)))
            return
    for i in arr: 
        
        stack.append(i)
        dfs()
        stack.pop()
dfs()