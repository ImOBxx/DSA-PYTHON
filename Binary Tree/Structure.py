class Node:
    def __init__(self, k):
        self.right = None
        self.left = None
        self.key = k

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.right = Node(40)


