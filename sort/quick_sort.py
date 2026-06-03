def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = [arr[0]]
    small = []
    big = []
    for i in range(1,len(arr)):
        if arr[i] < pivot[0] :
            small.append(arr[i])
        elif arr[i] == pivot[0] :
            pivot.append(arr[i])
        else :
            big.append(arr[i])
    return quick_sort(small) + pivot + quick_sort(big)

# 테스트 1
nums = [64, 25, 12, 22, 11]
print("Test1:", quick_sort(nums))

# 테스트 2
nums = [1, 2, 3, 4, 5]
print("Test2:", quick_sort(nums))

# 테스트 3
nums = [5, 4, 3, 2, 1]
print("Test3:", quick_sort(nums))

# 테스트 4 (중복값)
nums = [3, 1, 3, 2, 3]
print("Test4:", quick_sort(nums))

# 테스트 5 (원소 1개)
nums = [42]
print("Test5:", quick_sort(nums))

# 테스트 6 (빈 리스트)
nums = []
print("Test6:", quick_sort(nums))

# 최종 보스
nums = [8, 3, 5, 1, 9, 2, 7, 4, 6]
print("Boss :", quick_sort(nums))