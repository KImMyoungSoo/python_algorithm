def solution(n, left, right):
    answer = []
    for i in range(left,right+1) :
        quo = i // n + 1
        remain = i % n + 1
        num = max(quo,remain)
        answer.append(num)
    return answer

n = 3
left = 2
right = 5
print(solution(n,left,right))