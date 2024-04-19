def selection_sort(arr):
    n =len(arr)
    for i in range(n):
        # i 위치에 들어갈 최소값 찾기
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 찾은 최소값을 i 위치로 이동
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # 현재 단계에서의 배열 상태 출력
        print(f"Step {i+1}: {arr}")
# 주어진 배열
a = [7, 4, 9, 6, 3, 8, 7, 5]
print("a 리스트:", a)
selection_sort(a)
print("리스트 a 오름차순 정렬:", a)