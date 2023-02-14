from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    #N = 문서의 개수, M = 출력할 문서의 위치 (0부터 센다)
    queue = deque(map(int, input().split()))
    count = 0
    
    while len(queue) != 0:
        if queue[0] >= max(queue):
            if M == 0:
                print(count+1)
                break
            queue.popleft()
            M -= 1
            count += 1
            
        else:
            queue.append(queue.popleft())
            if M == 0:
                M = len(queue)-1
            else:
                M -= 1            