def solution(n):
    answer = 0
    cnt = 1
    while cnt <= n :
        sum = 0
        for i in range(cnt,n+1) :
            sum = sum + i
            if sum < n :
                continue
            elif sum == n :
                answer += 1
            else :
                break
        cnt += 1
    return answer

s = 15
print(solution(s))