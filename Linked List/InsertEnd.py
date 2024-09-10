class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def insertEnd(head, key):
    if head is None:
        return Node(key)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = Node(key)
    return head

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()

# Initially, head is None (empty list)
head = None

# Insert elements at the end
head = insertEnd(head, 10)
head = insertEnd(head, 20)
#head = insertEnd(head, 30)
head = insertEnd(head, 40)

# Print the list
printlist(head)
