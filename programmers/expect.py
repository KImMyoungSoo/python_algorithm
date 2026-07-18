def solution(n,a,b):
    answer = 0
    seq = ['x']*n
    seq[a-1] = 'a'
    seq[b-1] = 'b'
    while True :
        answer += 1
        arr = []
        for i in range(0,len(seq),2) :
            temp = seq[i] + seq[i+1]
            arr.append(temp)
        if 'ab' in arr :
            break
        else :   
            for idx, j in enumerate(arr) :
                if 'a' in j :
                    arr[idx] = 'a'
                elif 'b' in j :
                    arr[idx] = 'b'
                else :
                    arr[idx] = 'x'
            seq = arr
    return answer

n = 8
a = 4
b = 7
print(solution(n,a,b))