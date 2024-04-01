# 피보나치 수열의 n번째 항을 계산하는 반복 알고리즘
def fibonacci_iterative(n):
    # 첫 번째와 두 번째 피보나치 수를 초기화
    a, b = 0, 1

    # n번 반복하여 피보나치 수 계산
    for _ in range(n):
        # 다음 피보나치 수를 계산하고, (a, b)를 업데이트
        a, b = b, a + b

    # n번째 피보나치 수 반환
    return a


# 함수 사용 예
print(fibonacci_iterative(10))  # 55
