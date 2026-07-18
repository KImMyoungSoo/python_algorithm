def solution(n, words):
    answer = [words[0]]
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    arr = arr * (len(words)//n)
    for i in range(1,len(words)) :
        if words[i] not in answer and answer[-1][-1] == words[i][0]: 
            answer.append(words[i])
        else :
            return [arr[i],i//n+1]
        # print(i,n)
        # print(answer)
    else :
        return [0,0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n,words))