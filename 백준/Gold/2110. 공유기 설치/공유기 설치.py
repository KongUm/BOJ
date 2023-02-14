import sys

N, C = map(int, input().split())
house = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
house.sort()


def upper_bound(left, right):  # left <= 범위 < right
    while left < right:  # 범위가 1이 될 때 까지 탐색
        mid = (left + right) // 2

        if checker(mid) >= C:
            left = mid + 1
        else:
            right = mid
    return left


def checker(min_distance):
    lo = 0 # index
    wifi_count = 1
    for i in range(1,N):
        if house[i] - house[lo] >= min_distance:
            wifi_count += 1
            lo = i

    return wifi_count

print(upper_bound(1, house[-1]-house[0]+1)-1)



