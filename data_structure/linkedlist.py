class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 맨 뒤에 노드 추가
    def append(self, data):
        pass

    # 맨 앞에 노드 추가
    def prepend(self, data):
        pass

    # 특정 값 삭제
    def delete(self, data):
        pass

    # 리스트 출력
    def print_list(self):
        pass

    # 길이 반환
    def size(self):
        pass

    # 값 검색
    def search(self, data):
        pass


# 테스트 코드
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.print_list()