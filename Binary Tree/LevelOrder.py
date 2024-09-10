from collections import deque

class Node:
    def __init__(self, k):
        self.right = None
        self.left = None
        self.key = k


def printlevelOrder(root):
    if root is None:
        return 
    
    q = deque()
    q.append(root)

    while len(q) > 0:
        node = q.popleft()
        print(node.key)


    if node.left is not None:
        q.append(node.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.right.left = Node(50)
root.right.right = Node(60)
root.right.left.left = Node(70)
root.right.left.right = Node(80)

printlevelOrder(root)