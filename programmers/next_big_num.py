def solution(n):
    arr = list(map(int,bin(n)[2:]))
    count_one = 0
    idx = len(arr)
    print(arr)
    for i in range(len(arr)-1,0,-1):
        idx = idx -1
        if arr[i] == 1 and arr[i-1] == 0 :
            print(i)
            arr[i] = 0
            arr[i-1] = 1
            print(idx)
            print(count_one)
            break
        if arr[i] == 1:
            count_one += 1
        arr[i] = 0
    else :
        arr[0] = 0
        arr.insert(0,1)

    for i in range(len(arr)-1,len(arr)-count_one-1,-1):
        arr[i] = 1

    answer = int("".join(map(str, arr)),2)
    

    return answer


n = 15
print(solution(n))
