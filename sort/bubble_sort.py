def bubble_sort(arr):
    for i in range(0,len(arr)):
        count = 0
        for j in range(0,len(arr)-1-i):
            if arr[j+1] < arr[j] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count = count + 1
            print(arr)
        if count == 0 :
            break
    return arr

nums = [64, 25, 12, 22, 11]
bubble_sort(nums)
print(nums)