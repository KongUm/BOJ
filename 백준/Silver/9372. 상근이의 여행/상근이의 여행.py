T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    for i in range(E):
        a, b = map(int, input().split())
    print(V-1) # 트리는 항상 V - 1개의 간선을 가진다