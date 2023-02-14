from collections import deque
T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    queue = deque()  
    arr = input()
    arr = arr.replace("[", "").replace("]", "").replace(",", " ").split()
    for i in range(len(arr)):
        queue.append(int(arr[i]))
        
        
    checker = True
    # True = 정방향, False = 역방향
    error = False
    
    for F in p:
        if F == "R":
            if checker == True:
                checker = False
            else:
                checker = True
                
        else:
            if len(queue) == 0:
                print("error")
                error = True
                break
            else:
                if checker == True:
                    queue.popleft()
                else:
                    queue.pop()
                    
    if error == False:
        if len(queue) == 0:
            print("[]", end = "\n")
        elif len(queue) == 1:
            print("[", end = "")
            print(queue[0], end = "]\n")
        elif checker == True:
            print("[", end = "")
            for i in range(len(queue)):
                if i == len(queue)-1:
                    print(queue[i], end = "]\n")
                else:
                    print(queue[i], end = ",")
                
        else:
            print("[", end = "")
            for i in range(len(queue)-1, -1, -1):
                if i == 0:
                    print(queue[i], end = "]\n")
                else:
                    print(queue[i], end = ",")
