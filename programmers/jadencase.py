s = "3people  unFollowed me"

def solution(s):
    answer = ''
    for i in range(len(s)) :
        # i = 0
        if i == 0 :
            # 알파벳일 경우
            if s[i].isalpha() :
                answer = answer + s[i].upper()
                continue
            # 공백이나 숫자일 경우a
            else :
                answer = answer + s[i]
                continue
        # 공백일 경우
        if s[i] == ' ':
            answer = answer + ' '
        
        # 알파벳일경우
        elif s[i].isalpha() :
            if s[i-1] == ' ':
                answer = answer + s[i].upper()
            elif s[i-1].isalpha() or s[i-1].isdigit() :
                answer = answer + s[i].lower()
        
        # 숫자일 경우
        else :
            answer = answer + s[i]
        
    return answer

print(solution(s))