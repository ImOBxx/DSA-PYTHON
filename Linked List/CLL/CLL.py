class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printCir(head):
    if head is None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

# Create the circular linked list
head = Node(10)
head.next = Node(5)
head.next.next = Node(20)
head.next.next.next = Node(15)
head.next.next.next.next = head

# Print the circular linked list
printCir(head)

