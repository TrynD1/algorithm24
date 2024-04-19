# [3.2 알고리즘]
def sequential_search(A, key): # 입력 A는 리스트, key는 탐색 키
    for i in range(len(A)):
        if A[i] == key: # 탐색 성공하면 (비교 연산)
             return i # 인덱스 반환
    return -1 # 탐색 실패 시, -1 반환

a = [0,1,4,3,4,5,6]
key = 4
result = sequential_search(a, key)
print("찾고자하는", key, "값은 리스트의", result,"번째 위치에 있습니다.")