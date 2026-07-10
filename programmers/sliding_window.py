def solution(elements):
    arr = elements + elements
    answer = set()
    n = len(elements)

    for length in range(1, n + 1):

        current_sum = sum(arr[:length])
        answer.add(current_sum)

        for start in range(1, n):
            current_sum = current_sum - arr[start - 1] + arr[start + length - 1]
            answer.add(current_sum)

    return len(answer)

n = [7,9,1,1,4]
print(solution(n))