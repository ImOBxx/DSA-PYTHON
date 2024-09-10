class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k

def height(root):
    if root == None:
        return 0
    else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh, rh) + 1
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
height(root)

tree_height = height(root)
print("Height Of The Root: ", tree_height)