class Node:
    def __init__(self, k):
        self.data = k 
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()

def removeDups(head):
    curr = head
    while curr != None and curr.next != None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

head = Node(10)
head.next = Node(10)
head.next.next = Node(20)

printList(head)
removeDups(head)
printList(head)