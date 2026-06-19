def solution(brown, yellow):
    arr = []
    answer = []
    for i in range(1,yellow+1) :
        if yellow % i == 0:
            arr.append(i)
    if len(arr) % 2 == 1:
        idx = int(len(arr)/2)
        arr.insert(idx,arr[idx])
    print(arr)
    for j in range(int(len(arr)/2)) :
        print((arr[-j-1]*2) + (arr[j]+2)*2)
        print(brown)
        if ((arr[-j-1]*2) + (arr[j]+2)*2) == brown :
            answer.append(arr[-j-1]+2)
            answer.append(arr[j]+2)
            break
    return answer

brown = 16
yello = 9
print(solution(brown,yello))