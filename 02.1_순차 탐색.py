def sequential_search(A, key): # 순차 탐색, A는 리스트, key는 탐색키
    for i in range(len(A)): # i : 0, 1, ... len(A)-1
        if A[i] == key: # 탐색 성공하면 (비교 연산, 기본 연산임)
            return i # 인덱스 반환
        return -1 # 탐색에 실패하면 -1 반환