import random

def mk_answer():
    answer = random.sample(range(1,10),6)
    print(answer)
    return answer

def user_answer():
    user_input = input("정답을 입력하세요 : ")
    numbers = list(map(int,user_input))
    # print(numbers)
    # print(numbers[0].is_integer())
    return numbers     


def count_bs(cr_answer, numbers):
    count_s = 0
    count_b = 0
    for i in range(0,len(cr_answer)):
        if cr_answer[i] == numbers[i] :
            count_s += 1
    
    for i in numbers :
        if i in cr_answer:
            count_b += 1
    
    count_b = count_b - count_s

    print(f"Strike : {count_s} Ball : {count_b}")
    return count_s

while True :
    cr_answer = mk_answer()

    count = 0
    count_s = 0

    while not (count_s == 6) :
        count = count + 1
        numbers = user_answer()
        count_s = count_bs(cr_answer,numbers)
        

    print(f"{count}번 만에 승리하였습니다!!")
    is_stop = input("계속 하시겠습니까?(y/n) : ")
    if is_stop == 'n' :
        break