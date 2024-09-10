class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def reversedList(head):
    if head is None or head.next is None:
        return head

    rest_head = reversedList(head.next)
    head.next.next = head
    head.next = None

    return rest_head

def printList(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next 
    print()

# Create the linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Print the original list
print("Original list:")
printList(head)

# Reverse the linked list
head = reversedList(head)

# Print the reversed list
print("Reversed list:")
printList(head)
