def uniuqe_elements(A): # 리스트 A 입력
    n = len(A) #입력의 크기 = 리스트의 크기
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] == A[j]: # 기본 연산
                return False # 같은 항목이 있으면 False 반환
    return True # 같은 항목이 없으면 True 반환