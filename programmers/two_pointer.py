def solution(arr, k):
    answer = 0

    left = 0
    right = 0
    total = arr[0]

    while True:
        if total < k:
            right += 1
            if right == len(arr):
                break
            total += arr[right]
        elif total > k:
            total -= arr[left]
            left += 1
        else:
            answer += 1
            total -= arr[left]
            left += 1

    return answer


# 테스트 케이스 1
arr = [1, 2, 3, 2, 5]
k = 5
print(solution(arr, k))  # 3

# 테스트 케이스 2
arr = [1, 1, 1, 1, 1]
k = 2
print(solution(arr, k))  # 4

# 테스트 케이스 3
arr = [1, 2, 1, 3, 1]
k = 3
print(solution(arr, k))  # 3

# 테스트 케이스 4
arr = [5]
k = 5
print(solution(arr, k))  # 1

# 테스트 케이스 5
arr = [1, 2, 3, 4, 5]
k = 100
print(solution(arr, k))  # 0

# 테스트 케이스 6
arr = [2, 2, 2, 2, 2]
k = 4
print(solution(arr, k))  # 4

# 테스트 케이스 7
arr = [1, 3, 2, 1, 1, 2]
k = 4
print(solution(arr, k))  # 3