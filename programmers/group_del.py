def solution(s):
    stk = []
    for i in s :
        if not stk :
            stk.append(i)
        else :
            if stk[-1] == i :
                stk.pop(-1)
            else :
                stk.append(i) 
    if not stk :
        return 1
    else :
        return 0

s = 'cbcb'
print(solution(s))