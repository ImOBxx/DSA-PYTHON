from collections import deque

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k 

def printLevel(root):
    if root is None:
        return 
    q = deque()
    q.append(root)
    q.append(None)
    while len(q) > 1:
        curr = q.popleft()
        if curr == None:
            print()
            q.append(None)
            continue
        print(curr.key, end = " ")
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

printLevel(root)

