from node import Node, LinkedList

data = LinkedList(5)

ptr = data.head # incrementer
prev = None
curr = None
next = None
while ptr is not None:
    curr = ptr
    ptr  = ptr.next

    curr.next = prev  # reverse linked list

    prev = curr       # memorize current location for next iteration
    data.head = curr  # move this along with pointer



print(data.tostring())
