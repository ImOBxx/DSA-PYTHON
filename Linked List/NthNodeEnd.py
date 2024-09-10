class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def printList(head):
    curr = head  # Assign curr to head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def printNthNodeFromEnd(head, n):
    if head is None:
        return
    first = head
    for i in range(n):
        if first is None:
            return
        first = first.next
    second = head
    while first is not None:
        second = second.next
        first = first.next
    print(second.data)

# Create the linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Print the list
printList(head)

# Print the nth node from the end
printNthNodeFromEnd(head, 1)
