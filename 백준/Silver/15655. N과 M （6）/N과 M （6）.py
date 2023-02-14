N,M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

stack = [] #스택

def dfs(): 
    if len(stack) == M: # 만약 모든 조건을 만족한다면 출력하고 함수를 끝낸다
            print(" ".join(map(str, stack)))
            return
    for i in arr: 
        if len(stack) != 0: 
            if i <= stack[-1]: # 수열이 오름차순이 아니라면 건너뛴다
                continue
        stack.append(i)
        dfs()
        stack.pop()
dfs()