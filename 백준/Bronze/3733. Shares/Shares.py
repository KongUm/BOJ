while True:
    try:
        N, S = map(int, input().split())
        x = S // (N + 1)
        print(x)
    except EOFError:
        break
