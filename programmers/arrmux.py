def solution(arr1, arr2):
    answer = []

    for _ in range(len(arr1)):
        answer.append([])

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            total = 0

            for k in range(len(arr2)):
                total += arr1[i][k] * arr2[k][j]

            answer[i].append(total)

    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))