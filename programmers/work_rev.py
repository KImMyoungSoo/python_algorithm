def solution(n, words):
    answer = {words[0]}
    for i in range(1,len(words)) :
        if words[i] not in answer and words[i-1][-1] == words[i][0]: 
            answer.add(words[i])
        else :
            return [(i%n)+1,(i//n)+1]
    else :
        return [0,0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n,words))