class Node:
    def __init__(self, key):
        self.key = key
        self.next = None 

def delfirst(head):
    if head == None:
        return None
    else:
        return head.next
    


def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = delfirst(head)

printlist(head)