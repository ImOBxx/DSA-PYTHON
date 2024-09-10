class Node:
    def __init__(self, k):
        self.right = None
        self.left = None
        self.key = k

def printKDist(root, k):
    if root is None:
        return 
    if k == 0:
        print(root.key, end = " ")
    else:
        printKDist(root.left, k - 1)
        printKDist(root.right, k - 1)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.right = Node(50)
root.left.left = Node(40)
root.right.right = Node(70)
root.right.right.right = Node(80)

k = 2
printKDist(root, k)











