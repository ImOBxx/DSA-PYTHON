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
    print()

def insertEnd(head, x):
    temp = Node(x)

    if head is None:
        temp.next = temp 
        return temp 
    else:
        temp.next = head.next
        head.next = temp 

        temp.data, head.data = head.data, temp.data
        return temp
    

# Create the circular linked list
head = Node(10)
head.next = Node(20)
head.next.next = head

# Print the circular linked list
printCir(head)

# Insert a new node at the end
head = insertEnd(head, 30)

# Print the circular linked list again
printCir(head)
