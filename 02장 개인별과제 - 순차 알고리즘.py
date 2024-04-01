#팩토리얼 함수의 순환 알고리즘 구현
def factorial(n):
    # 기본 조건
    if n == 0:
        return 1
    # 순환 호출
    else:
        return n * factorial(n-1)
# 함수 사용 예
print(factorial(5))  # 120

#피보나치 수열을 생성하는 순환 알고리즘
def fibonacci(n):
    # 기본 조건
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # 순환 호출
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# 함수 사용 예
print(fibonacci(10))  # 55

""" 
이 코드는 주어진 숫자 n에 대해 피보나치 수를 계산합니다. fibonacci 함수는 자신을 두 번 호출하며, 한 번은 n−1에 대해, 
다른 한 번은 n−2에 대해 호출합니다. 이 두 호출의 결과를 합하여 반환합니다. 이 과정은 n이 0이나 1에 도달할 때까지 반복됩니다.

이 순환 알고리즘은 비효율적일 수 있습니다. n이 커질수록 같은 계산을 여러 번 반복하기 때문입니다.
"""