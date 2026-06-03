def insertion_sort(arr):
    # 여기 구현
    for i in range(1, len(arr)):
        for j in range(i, 0, -1): 
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

print(insertion_sort([5, 3, 4, 1]))
# [1, 3, 4, 5]

print(insertion_sort([10, 2, 7, 6, 1]))
# [1, 2, 6, 7, 10]

print(insertion_sort([1, 2, 3, 4]))
# 이미 정렬된 경우도 테스트