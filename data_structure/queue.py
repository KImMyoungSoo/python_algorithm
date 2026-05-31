class Queue:
    def __init__(self):
        # 큐를 저장할 공간 생성
        self.item = []

    def enqueue(self, data):
        # 큐의 뒤쪽에 데이터를 추가
        # 반환값 없음
        self.item.append(data)

    def dequeue(self):
        # 큐의 앞쪽 데이터를 제거하고 반환
        # 큐가 비어있으면
        # "빈 큐입니다." 출력 후 None 반환
        if self.is_empty() :
            print("빈 큐입니다.")
            return None
        return self.item.pop(0)

    def peek(self):
        # 큐의 가장 앞쪽 데이터를 반환
        # 데이터는 제거하지 않음
        # 큐가 비어있으면
        # "빈 큐입니다." 출력 후 None 반환
        if self.is_empty() :
            print("빈 큐입니다.")
            return None
        return self.item[0]

    def is_empty(self):
        # 큐가 비어있는지 확인
        # 비어있으면 True
        # 아니면 False 반환
        if not self.item :
            return True
        else :
            return False

    def size(self):
        # 현재 큐에 들어있는 데이터 개수 반환
        return len(self.item)

    def display(self):
        # 큐 전체 내용을 출력
        # 예시:
        # [10, 20, 30]
        print(self.item)


# 테스트 코드
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()

print(queue.peek())      # 10 예상

print(queue.dequeue())   # 10 예상
print(queue.dequeue())   # 20 예상

print(queue.is_empty())  # False 예상

print(queue.dequeue())   # 30 예상
print(queue.dequeue())   # "빈 큐입니다." + None 예상

print(queue.is_empty())  # True 예상