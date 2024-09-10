class Node:
    def __init__(self, key):
        self.key = key
        self.next = None 

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()

def delGNode(ptr):
    if ptr is None or ptr.next is None:
        return  # Cannot delete the node if it is the last node or if ptr is None
    temp = ptr.next 
    ptr.key = temp.key 
    ptr.next = temp.next 

# Initialize the linked list
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)

# Print the list before deletion
print("Before deletion:")
printlist(head)

# Delete the given node
delGNode(head)

# Print the list after deletion
print("After deletion:")
printlist(head)

