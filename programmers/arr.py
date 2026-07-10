def solution(elements):
    arr = elements + elements
    answer = []

    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            temp = sum(arr[j:j+i])
            answer.append(temp)

    answer = list(set(answer))
    print(answer)
    
    count = len(answer)
    return count

n = [7,9,1,1,4]
print(solution(n))