from node import Node, LinkedList

n = 10
data = LinkedList(n)

ptr = data.head
l   = 0
while ptr is not None:
    ptr = ptr.next
    l = l+1

print("Solution: %d" % l)
