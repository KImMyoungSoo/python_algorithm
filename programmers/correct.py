def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    print(A)
    print(B)

    answer = 0

    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

A = [1,4,2]
B = [5,4,4]
print(solution(A,B))