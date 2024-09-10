class Node:
    def __init__(self, data):
        self.key = data
        self.next = None

def insertBeg(head, x):
    temp = Node(x)
    if head is None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next 
        head.next = temp 
        head.key, temp.key = temp.key, head.key
        return head

def printCir(head):
    if head is None:
        return
    print(head.key, end=" ")
    curr = head.next 
    while curr != head:
        print(curr.key, end=" ")
        curr = curr.next
    print()

# Create the circular linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head 

# Print the circular linked list
printCir(head)

# Insert a new node at the beginning
head = insertBeg(head, 5)

# Print the circular linked list again
printCir(head)
