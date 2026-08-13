'''
def solution(clothes):
    answer = 1
    dict = {}
    for elem in clothes :
        dict[elem[0]] = elem[1]

    dicval = dict.values()

    typecount = {}

    for i in dicval:
        print(i)
        if typecount.get(i,None) == None :
            typecount[i] = 2
        else :
            typecount[i] += 1

    typecount_val = typecount.values()

    for i in typecount_val :
        answer *= i
    
    return answer - 1

'''

def solution(clothes) :
    answer = 1
    count = {}

    for key, val in clothes :
        if val not in count :
            count[val] = 2
        else :
            count[val] += 1
    
    for i in count.values() :
        answer *= i

    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))


