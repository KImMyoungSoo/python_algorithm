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

def heap_sort(arr):
    n = len(arr)

    # 1. 최대 힙 만들기
    for i in range(n//2-1,-1,-1):
        heapify(arr, n, i)

    # 2. 하나씩 뒤로 보내면서 정렬
    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# 테스트 코드
tests = [
    [3, 8, 6, 4, 1, 2],
    [9, 4, 7, 1, 3, 6],
    [10, 5, 8, 2, 1],
    [1],
    [],
    [5, 5, 5, 5],
]

for arr in tests:
    print("-" * 30)
    print("Before:", arr)

    heap_sort(arr)

    print("After :", arr)