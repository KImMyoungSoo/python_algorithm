def heapify(arr, n, i):
    # 현재 노드
    largest = i

    # 왼쪽 자식
    left = 2 * i + 1

    # 오른쪽 자식
    right = 2 * i + 2

    # 왼쪽 자식과 비교
    if left < n and arr[left] > arr[largest] :
        largest = left

    # 오른쪽 자식과 비교
    if right < n and arr[right] > arr[largest] :
        largest = right

    # 가장 큰 값이 현재 노드가 아니라면
    if i != largest :
        # 교환
        arr[i], arr[largest] = arr[largest], arr[i]
        # 재귀 호출
        heapify(arr,n,largest)


# 테스트
arr = [3, 8, 6, 4, 1, 2]

print("Before:", arr)

heapify(arr, len(arr), 0)

print("After :", arr)

# 예상 결과
# [8, 4, 6, 3, 1, 2]

tests = [
    [3, 8, 6, 4, 1, 2],
    [1, 9, 8, 7, 6, 5],
    [5, 10, 8, 4, 3, 2],
]

for arr in tests:
    print("-" * 30)
    print("Before:", arr)

    heapify(arr, len(arr), 0)

    print("After :", arr)