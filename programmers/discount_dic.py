from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)) :
        dic[want[i]] = number[i]
    print(dic)
    cnt = Counter(discount[0:10])

    for i in range(len(discount)-9) :
        if i == 0:
            pass
        else :
            print(f"i : {i}")
            print(f"before cnt : {cnt}")
            cnt[discount[i-1]] -= 1
            cnt[discount[i+9]] += 1
            print(f"after cnt : {cnt}")
        for key, val in dic.items() :
            temp = cnt[key]
            if temp < val :
                break
        else :
            answer += 1
        print(f"answer : {answer}")
    return answer




want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

# want = ["apple"]
# number = [10]
# discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

print(solution(want,number,discount))