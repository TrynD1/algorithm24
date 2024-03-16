# 다음은 배열에서 가장 가까운 두 항목을 찾아 거리를 찾아(?) 반환하는 알고리즘이다.
# 이 알고리즘을 개선하는 방법을 생각해 보라. 알고리즘을 완전히 바꾸어도 좋다.
# 작성자 : 송재찬

def closest_distance(arr):
    arr.sort()  # 배열을 정렬합니다.
    min_diff = float('inf')  # 최소 거리를 무한대로 초기화합니다.

    for i in range(1, len(arr)):
        # 인접한 두 항목 간의 거리를 계산하고, 최소 거리를 갱신합니다.
        diff = abs(arr[i] - arr[i - 1])
        min_diff = min(min_diff, diff)

    return min_diff  # 최소 거리를 반환합니다.

# 입력을 받습니다. 여러 숫자를 공백으로 구분하여 입력할 수 있습니다.
arr = [int(x) for x in input().split()]

# 최소 거리를 계산하고 출력합니다.
print(closest_distance(arr))
