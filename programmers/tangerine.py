def solution(k, tangerine):
    count_t = {}
    for i in tangerine :
        if i in count_t :
            count_t[i] += 1
        else :
            count_t[i] = 1

    arr = sorted(count_t.values(), reverse=True)
    answer = 0
    num = 0
    for i in arr :
        num = num + i
        answer += 1
        if num >= k :
            break
    return answer

tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 6
print(solution(k,tangerine))