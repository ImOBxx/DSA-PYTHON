class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBalanced(root):

    if root is None:
        return True
    
    lh = isBalanced(root.left)

    if lh == -1:
        return -1
    
    rh = isBalanced(root.right)
    if rh == -1:
        return -1
    
    else:
        return max(lh, rh) + 1
    
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(30)
    root.right.left = Node(15)
    root.right.right = Node(20)
    if (isBalanced(root) == -1):
        print("Not Balanced")
    else:
        print("Balanced")

