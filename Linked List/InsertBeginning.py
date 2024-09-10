class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def insertBegin(head, key):
    temp = Node(key)
    temp.next = head
    return temp

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()

# Initially, head is None (empty list)
head = None

# Insert elements at the beginning
head = insertBegin(head, 10)
head = insertBegin(head, 20)
head = insertBegin(head, 30)

# Print the list
printlist(head)





