class Node:
    def __init__(self, data):
        # 데이터 저장
        self.data = data
        # 왼쪽 자식
        self.left = None
        # 오른쪽 자식
        self.right = None

def dfs(node) :
    if node is None :
        return
    print(node.data)
    dfs(node.left)
    dfs(node.right)

root = Node("A")

root.left = Node("B")
root.right = Node("C")

# print(root.data)
# print(root.left.data)
# print(root.right.data)
root.left.left = Node("D")
root.left.right = Node("E")
# print(root.left.left.data)
# print(root.left.right.data)

dfs(root)