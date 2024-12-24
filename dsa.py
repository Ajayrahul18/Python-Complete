####           Array
## Fixed size array -> arr = [0]*5
## E.g
arr = [1,2,3,4]

### transversial
def tranvercial(lst):
    for i in range(len(lst)):
        print(lst[i], end=" ")


###    Insertion
def insertation(lst, pos, num):
    lst.insert(pos, num)
    return lst

###    Deletion
def deletion(lst, pos):
    if pos in lst:
        lst.remove(pos)
    return lst




####           Linked List
## Node -> Data
## Pointer -> Points next data
## E.g 
class Node:
    def __init__(self, data):
        self.data = data
        self.point = None

### transversial 
def transervisal(head):
    current = head

    while current is not None:
        print(current.data)

        current =data.next

        print()


### Searching 
def serching(head, target):
    curr = head
    while curr is not None:
        if curr.data ==target:
            return True
        curr = curr.next
    return False

### Find Length

def length(head):
    curr = head

    leng = 0
    while curr is not None:
        leng += 1
        curr = curr.next
    return leng 

### Insertion -> At the beginning

def insertionAtStart(head, value):
    new_node = Node(value)
    new_node.next = head

    head = new_node

    return head

### Insertion -> At the end

def insertionAtEnd(head, value):
    new_node = Node(value)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node

    return head

### Insertion -> At a Sepecific position

def inserPosition(head, value, pos):
    new_node = Node(value)
    curr = head

    if pos == 1:
        new_node.next = head
        head = new_node
        return head
    
### Delection at the start

def deletStart(head):
    temp = head

    head = head.next
    temp = None
    return head

### Delection at the end

def deleAtEnd(head):
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

### Delection at Sepecific Location

def delAtSepfic(head, pos):
    if pos < 1:
        return("Invalid")
    elif pos == 1:
        temp = head
        head = head.next
        temp = None


####    Double Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

### transversial -> Forward
def forwardtrans(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

### Length of Doubly Linked List
def length(head):
    curr = head
    count = 0

    while curr is not None:
        count += 1
        curr = curr.next
    print(count)

###  Insertation at Begning
def InsertAtFront(head, value):
    new_node = Node(value)

    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

### Insertation at End
def insertaDablLstEnd(head, value):
    new_node = Node(value)

    if head is None:
        return new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

        return head

def deleteDoubleLinkAtStart(head):
    if head is None:
        return None
    
    head = head.next
    head.prev = None
    return head

def deleDblLinkAtEnd(head):
    curr = head
    while curr.next is not None:
        curr = curr.next
    
    curr = curr.prev
    curr.next = None
    return head


def printDoubList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":


    head = Node(10)
    head.next= Node(20)
    head.next.prev = head
    head.next.next = Node(30)
    head.next.next.prev = head.next

    head = (deleDblLinkAtEnd(head))
    printDoubList(head)

