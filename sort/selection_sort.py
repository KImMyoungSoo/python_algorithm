def selection_sort(arr):
    # 구현
    for i in range(0,len(arr)):
        print(arr)
        min_index = i
        for j in range(i,len(arr)):
            # print(arr[j], arr[min_index])
            if arr[j] < arr[min_index] :
                min_index = j
                # print("hi")
                # print(min_index)
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # print(arr)
        # print('----------')
    return arr

nums = [64, 25, 12, 22, 11]
selection_sort(nums)
print(nums)