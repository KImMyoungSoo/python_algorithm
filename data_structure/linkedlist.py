class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 맨 뒤에 노드 추가
    def append(self, data):
        temp_node = Node(data)
        if self.head == None :
            self.head = temp_node
        else :
            index_node = self.head
            while index_node.next != None :
                index_node = index_node.next
            index_node.next = temp_node                

    # 맨 앞에 노드 추가
    def prepend(self, data):
        temp_node = Node(data)
        if self.head == None :
            self.head = temp_node
        else :
            index_node = self.head
            temp_node.next = index_node
            self.head = temp_node

    # 특정 값 삭제
    def delete(self, data):
        if self.head == None :
            return
        index_node = self.head
        if self.head.data == data :
            self.head = index_node.next
        else :
            node2 = index_node.next
            while node2 != None :
                if node2.data == data :
                    node3 = node2.next
                    if node3 == None :
                        index_node.next = None
                    else :
                        index_node.next = node3
                        node2.next = None
                    break
                index_node = index_node.next
                node2 = node2.next
            if node2 == None :
                print("삭제할 값이 리스트에 없습니다.")
                return

    # 리스트 출력
    def print_list(self):
        if self.head == None :
            print("빈 리스트")
        else :
            index_node = self.head
            print('Head',end='  Head -> ')
            while index_node != None :
                print(index_node.data, end=' -> ')
                index_node = index_node.next
            print('None')

    # 길이 반환
    def size(self):
        index_node = self.head
        count = 0
        while index_node != None:
            count = count + 1
            index_node = index_node.next
        return count

    # 값 검색
    def search(self, data):
        Index_node = self.head
        while Index_node != None :
            if Index_node.data == data :
                return True
            Index_node = Index_node.next
        return False


# 테스트 코드
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.print_list()