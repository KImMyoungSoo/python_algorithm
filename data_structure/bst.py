class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # 루트 노드 저장
        self.root = None

    # def insert(self, data):
    #     # 데이터를 BST 규칙에 맞게 삽입
    #     self.root = self._insert(self.root, data)

    # def _insert(self, node, data):
    #     if node is None :
    #         return Node(data)
        
    #     if data < node.data:
    #         node.left = self._insert(node.left, data)
    #     else:
    #         node.right = self._insert(node.right, data)

    #     return node

    def insert(self,data):
        # 데이터를 BST 규칙에 맞게 삽입
        if self.root is None :
            self.root = Node(data)
            return

        cur = self.root

        while True :
            if data < cur.data :
                if cur.left is None :
                    cur.left = Node(data)
                    return
                else :
                    cur = cur.left
            else :
                if cur.right is None :
                    cur.right = Node(data)
                    return
                else :
                    cur = cur.right

    def search(self, data):
        # 데이터가 존재하면 True
        # 없으면 False 반환
        cur = self.root
        
        while True :
            if cur.data == data :
                return True
            if data < cur.data :
                if cur.left is None :
                    return False
                cur = cur.left
            else :
                if cur.right is None :
                    return False
                cur = cur.right

            

bst = BST()

bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

print(bst.search(40))
# True

print(bst.search(100))
# False