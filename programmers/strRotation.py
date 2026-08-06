def solution(s):
    answer = 0
    for i in range(len(s)) :
        temp = s
        arr1 = temp[:i]
        arr2 = temp[i:]
        temp = arr2 + arr1
        if iscorrect(temp) :
            answer += 1
    return answer

def iscorrect(s) :
    pair = {')' : '(', '}' : '{', ']' : '['}
    arr = []
    for i in s :
        if i in ")}]" and not arr :
            return False
        if i in "([{" :
            arr.append(i)
        else :
            x = pair[i]
            y = arr[-1]
            if x == y :
                arr.pop()
            else :
                return False
    return not arr

s = "[](){}"
print(solution(s))