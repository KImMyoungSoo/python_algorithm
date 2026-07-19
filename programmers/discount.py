def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        temp_want = want.copy()
        temp_num = number.copy()
        for j in range(i,10+i):
            if discount[j] in temp_want :
                idx = temp_want.index(discount[j])
                temp_num[idx] -= 1
                if temp_num[idx] == 0 :
                    temp_num.pop(idx)
                    temp_want.pop(idx)
        if not temp_num :
            answer += 1
    return answer




want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want,number,discount))