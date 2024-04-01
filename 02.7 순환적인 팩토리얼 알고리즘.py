def factorial(n): # 순환적으로 구현한 factorial 함수
    if n == 1: # 종료 조건
        return 1 # 순환을 멈추는 부분
    else:
        return n * factorial(n-1) # 자기 자신을 순환적으로 호출