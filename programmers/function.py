import math

def solution(progresses, speeds):
    answer = []
    times = []
    for p,s in zip(progresses,speeds) :
        days = math.ceil((100-p)/s)
        times.append(days)

    current = times[0]
    cnt = 1

    for i in range(1, len(times)) :
        if times[i] <= current :
            cnt += 1
        else :
            answer.append(cnt)

            current = times[i]
            cnt = 1
    answer.append(cnt)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses,speeds))