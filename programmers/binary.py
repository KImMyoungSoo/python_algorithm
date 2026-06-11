def solution(s):
    answer = []
    cnt = 0
    cnt_0 = 0
    
    while not (len(s) == 1) :
        arr = []
        for i in range(len(s)) :
            if s[i] == '0' :
                cnt_0 += 1
            else :
                arr.append('1')
        c = len(arr)
        s = bin(c)[2:]
        cnt += 1

    answer.append(cnt)
    answer.append(cnt_0)

    return answer

s = "110010101001"
print(solution(s))