class Stack:
    def __init__(self):
        # 스택을 저장할 공간 생성
        self.item = []

    def push(self, data):
        self.item.append(data)
        pass

    def pop(self):
        # 스택이 비어있는지 확인
        # 비어있다면 메시지 출력 후 None 반환
        # 아니라면 가장 위의 데이터 제거 후 반환
        if self.is_empty() :
            print("빈 스택입니다. ")
            return None
        else :
            return self.item.pop()

    def peek(self):
        # 가장 위의 데이터 반환
        # 제거하지는 않음
        if self.is_empty() :
            print("빈 스택입니다.")
            return None
        else :
            return self.item[-1]

    def is_empty(self):
        # 스택이 비어있는지 확인
        if not self.item :
            return True
        else :
            return False

    # 현재 스택의 크기 반환
    def size(self):
        return len(self.item)

    # 스택의 전체 내용을 출력하는 함수
    def display(self):
        print(self.item)

# 테스트 코드
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())      # 30 예상

print(stack.pop())       # 30 예상
print(stack.pop())       # 20 예상

print(stack.is_empty())  # False 예상

print(stack.pop())       # 10 예상
print(stack.pop())       # 스택이 비어있습니다 + None 예상

print(stack.is_empty())  # True 예상
print(stack.size())
stack.display()