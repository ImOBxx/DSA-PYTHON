class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def delLast(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()

# Initialize the linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Delete the last node
head = delLast(head)

# Print the list
printlist(head)
