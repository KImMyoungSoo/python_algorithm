def solution(n):
    arr = []

    for i in range(0, n):
        if i == 0 :
            arr.append(1)
        elif i == 1 :
            arr.append(2)
        else :
            arr.append(arr[i-1] + arr[i-2])

    
    return arr[n-1] % 1234567

n = 4
print(solution(n))